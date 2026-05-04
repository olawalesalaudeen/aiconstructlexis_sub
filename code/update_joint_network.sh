#!/usr/bin/env bash
# ============================================================================
# Update the joint nomological network when a new conference's papers arrive.
#
# Usage:
#   ./update_joint_network.sh \
#       --new-conf icml25 \
#       --new-papers paper_list/icml_2025_papers_LLM_papers.json \
#       --joint-dir network_data/joint_neurips24_iclr25_icml25 \
#       --confs neurips24 iclr25 icml25
#
# Steps:
#   1. Export the existing joint name_mapping (from the last joint network)
#      as a seed for the new conference's harmonization.
#   2. Run the full per-conf pipeline (extract → harmonize → vote →
#      characterize) on the new conference, using the joint mapping as seed
#      so canonical names align with prior conferences.
#   3. Build the new joint network across ALL listed conferences (including
#      the new one).
#   4. Run the LLM cross-conference merge to catch any new semantic dups
#      introduced by the new conference's vocabulary.
#   5. Apply joint canonical-MV across all conferences for entities.
#      Relationships are aggregated deterministically (no vote).
#
# Outputs:
#   network_data/<new_conf>/                 # full per-conf artifacts
#   $JOINT_DIR/joint_network_merged.json     # final joint network
#   outputs/<joint_label>_name_mapping.json  # exported mapping for next run
# ============================================================================
set -euo pipefail

# ── Args ────────────────────────────────────────────────────────────────────
NEW_CONF=""
NEW_PAPERS=""
JOINT_DIR=""
CONFS=()
PRIOR_MAPPING="${PRIOR_MAPPING:-}"     # optional override for seed mapping
MODELS=("gemini25pro" "gpt54mini" "qwen35_397b")
HARM_MODEL="gemini-2.5-pro"
BATCH_SIZE=1500   # llm_aggregator batch size for new-conf harmonization
THRESHOLD=2        # canonical-MV threshold (≥k of 3 models per paper)

while [[ $# -gt 0 ]]; do
    case "$1" in
        --new-conf)     NEW_CONF="$2"; shift 2 ;;
        --new-papers)   NEW_PAPERS="$2"; shift 2 ;;
        --joint-dir)    JOINT_DIR="$2"; shift 2 ;;
        --confs)        shift; while [[ $# -gt 0 && "$1" != --* ]]; do CONFS+=("$1"); shift; done ;;
        --prior-mapping) PRIOR_MAPPING="$2"; shift 2 ;;
        --models)       shift; MODELS=(); while [[ $# -gt 0 && "$1" != --* ]]; do MODELS+=("$1"); shift; done ;;
        --batch-size)   BATCH_SIZE="$2"; shift 2 ;;
        --threshold)    THRESHOLD="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

if [[ -z "$NEW_CONF" || -z "$NEW_PAPERS" || -z "$JOINT_DIR" || ${#CONFS[@]} -eq 0 ]]; then
    echo "Usage: $0 --new-conf LABEL --new-papers PAPERS_JSON --joint-dir DIR --confs C1 C2 ..."
    exit 1
fi

PYTHON=".venv/bin/python"
[[ -x "$PYTHON" ]] || PYTHON="python3"

mkdir -p "$JOINT_DIR" outputs

echo "========================================"
echo " Adding $NEW_CONF to joint network"
echo " Joint dir:   $JOINT_DIR"
echo " Conferences: ${CONFS[*]}"
echo "========================================"

# ── Step 1: Seed mapping for new-conf harmonization ─────────────────────────
SEED_MAPPING="$PRIOR_MAPPING"
if [[ -z "$SEED_MAPPING" ]]; then
    # Derive seed from the most recent joint mapping (or fall back to the
    # union of per-conf mappings)
    SEED_MAPPING="outputs/${NEW_CONF}_seed_name_mapping.json"
    echo "[1/6] Building seed name mapping from existing conferences..."
    $PYTHON - <<PYEOF
import json
from pathlib import Path
out = {}
for conf in [c for c in [${CONFS[@]/#/\"} ] if c != "$NEW_CONF"]:
    p = Path(f"network_data/{conf}/harmonized_network_characterized.json")
    if not p.is_file(): continue
    with open(p) as f: net = json.load(f)
    for et in ("constructs","measurements","behaviors"):
        for g in net.get(et, []) or []:
            c = g.get("canonical_name","").strip()
            if not c: continue
            out[c] = c
            for orig in g.get("original_names",[]) or []:
                if orig: out[orig] = c
    for orig, canon in (net.get("name_mapping") or {}).items():
        if orig and canon: out.setdefault(orig, canon)
with open("$SEED_MAPPING","w") as f: json.dump(out, f, indent=2)
print(f"  wrote {len(out)} mappings -> $SEED_MAPPING")
PYEOF
fi
echo "  Using seed mapping: $SEED_MAPPING"

# ── Step 2: Per-conf pipeline (extraction → harmonization → vote → characterization) ─
# The per-conf canonical majority vote is performed inside run_pipeline.sh
# (between harmonization and characterization), so no separate per-conf vote
# pass is needed here.
echo "[2/5] Running per-conference pipeline on $NEW_CONF..."
./run_pipeline.sh "$NEW_PAPERS" "network_data/$NEW_CONF" --name-mapping "$SEED_MAPPING" \
    --batch-size "$BATCH_SIZE"

# ── Step 3: Build joint network across all conferences ──────────────────────
echo "[3/5] Building joint network across all conferences..."
INPUTS=()
for conf in "${CONFS[@]}"; do
    INPUTS+=("$conf:network_data/$conf/harmonized_network_characterized.json")
done
$PYTHON scripts/build_joint_network.py \
    --inputs "${INPUTS[@]}" \
    --output "$JOINT_DIR/joint_network.json"

# ── Step 4: LLM cross-conference merge ──────────────────────────────────────
echo "[4/5] Running LLM cross-conference merge..."
$PYTHON scripts/joint_llm_merge.py \
    --input "$JOINT_DIR/joint_network.json" \
    --output "$JOINT_DIR/joint_network_merged.json" \
    --provider google --model "$HARM_MODEL" --batch-size 500

# ── Step 5: Joint canonical-MV (entities only) ──────────────────────────────
# Relationships are aggregated deterministically by canonical (src, tgt, type)
# in earlier steps; no separate vote pass is applied to edges.
echo "[5/5] Applying joint canonical-MV..."
TRIALS_ARGS=()
for conf in "${CONFS[@]}"; do
    TRIALS_ARGS+=("$conf:network_data/$conf/trials")
done
$PYTHON scripts/joint_canonical_mv.py \
    --joint "$JOINT_DIR/joint_network_merged.json" \
    --confs "${TRIALS_ARGS[@]}" \
    --models "${MODELS[@]}" --threshold "$THRESHOLD"

# ── Export the new joint mapping for future runs ────────────────────────────
JOINT_LABEL="$(IFS=_; echo "${CONFS[*]}")"
JOINT_MAPPING="outputs/${JOINT_LABEL}_name_mapping.json"
$PYTHON - <<PYEOF
import json
with open("$JOINT_DIR/joint_network_merged.json") as f: net = json.load(f)
out = {}
for et in ("constructs","measurements","behaviors"):
    for g in net.get(et, []) or []:
        c = g.get("canonical_name","").strip()
        if not c: continue
        out[c] = c
        for orig in g.get("original_names",[]) or []:
            if orig: out[orig] = c
for orig, canon in (net.get("name_mapping") or {}).items():
    if orig and canon: out.setdefault(orig, canon)
with open("$JOINT_MAPPING","w") as f: json.dump(out, f, indent=2)
print(f"Exported {len(out)} canonical mappings -> $JOINT_MAPPING")
PYEOF

echo ""
echo "========================================"
echo " ✓ Joint network updated."
echo " Output:  $JOINT_DIR/joint_network_merged.json"
echo " Mapping: $JOINT_MAPPING (use --prior-mapping for next run)"
echo "========================================"
