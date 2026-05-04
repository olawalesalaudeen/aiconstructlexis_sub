#!/usr/bin/env bash
set -euo pipefail

# ============================================================================
# End-to-end nomological network extraction and harmonization pipeline.
#
# Usage:
#   ./run_pipeline.sh <papers_json> <output_dir> [--max-papers N]
#
# Example:
#   ./run_pipeline.sh paper_list/neurips_2024_papers_LLM_papers.json network_data/neurips24
#
# Required env vars: TOGETHER_API_KEY, GOOGLE_API_KEY, OPENAI_API_KEY
#
# Extraction models: Gemini 2.5 Pro + GPT-5.4 Mini + Qwen 3.5-397B (majority vote)
# Harmonization model: Gemini 2.5 Pro
# Characterization model: Gemini 2.5 Pro
# ============================================================================

PAPERS="${1:?Usage: ./run_pipeline.sh <papers_json> <output_dir> [--max-papers N]}"
OUTDIR="${2:?Usage: ./run_pipeline.sh <papers_json> <output_dir> [--max-papers N]}"
shift 2

MAX_PAPERS=0
WORKERS=5
TEMPERATURE=0
HARM_PROVIDER="google"
HARM_MODEL="gemini-2.5-pro"
CHAR_PROVIDER="google"
CHAR_MODEL="gemini-2.5-pro"
BATCH_SIZE=100
# Optional seed mapping so harmonization can reuse canonical names from a
# prior run (e.g. NeurIPS 2024 → ICLR 2025) — applied deterministically first,
# then the LLM only processes new/unmapped names.
NAME_MAPPING=""

# Resolve python — prefer .venv if available
if [[ -x ".venv/bin/python" ]]; then
    PYTHON=".venv/bin/python"
elif command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "ERROR: No python found. Install Python or create .venv/"
    exit 1
fi

while [[ $# -gt 0 ]]; do
    case "$1" in
        --max-papers)   MAX_PAPERS="$2"; shift 2 ;;
        --workers)      WORKERS="$2"; shift 2 ;;
        --temperature)  TEMPERATURE="$2"; shift 2 ;;
        --harm-provider) HARM_PROVIDER="$2"; shift 2 ;;
        --harm-model)    HARM_MODEL="$2"; shift 2 ;;
        --char-provider) CHAR_PROVIDER="$2"; shift 2 ;;
        --char-model)    CHAR_MODEL="$2"; shift 2 ;;
        --batch-size)    BATCH_SIZE="$2"; shift 2 ;;
        --name-mapping)  NAME_MAPPING="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

mkdir -p "$OUTDIR"

echo "========================================"
echo " Pipeline: $PAPERS -> $OUTDIR"
echo " Python:   $PYTHON"
echo " Models:   Gemini 2.5 Pro + GPT-5.4 Mini + Qwen 3.5-397B"
echo " Voting:   Majority vote (2/3)"
echo "========================================"

# Step 1 — Multi-model extraction (Gemini 2.5 Pro + GPT-5.4 Mini + Qwen 3.5-397B)
echo ""
echo "[Step 1/4] Multi-model extraction..."
EXTRACT_ARGS=(
    --papers_url "$PAPERS"
    --sandbox "$OUTDIR"
    --temperature "$TEMPERATURE"
    --workers "$WORKERS"
)
if [[ "$MAX_PAPERS" -gt 0 ]]; then
    EXTRACT_ARGS+=(--max_papers "$MAX_PAPERS")
fi
$PYTHON scripts/multi_model_mv.py "${EXTRACT_ARGS[@]}"

EXTRACTION_JSON="$OUTDIR/inputs/extraction_multi_model_mv3.json"
if [[ ! -f "$EXTRACTION_JSON" ]]; then
    echo "ERROR: Expected extraction output not found: $EXTRACTION_JSON"
    exit 1
fi

# Step 2 — Simplify extracted results
echo ""
echo "[Step 2/4] Simplify..."
SIMPLIFIED_JSON="$OUTDIR/inputs/simplified_multi_model_mv3.json"
$PYTHON scripts/simplify_extracted_results.py \
    --input "$EXTRACTION_JSON" \
    --output "$SIMPLIFIED_JSON"

# Step 3 — Harmonize (LLM-based semantic grouping + relationship aggregation)
echo ""
echo "[Step 3/4] Harmonize..."
HARMONIZED_JSON="$OUTDIR/harmonized_network.json"
HARM_ARGS=(
    --input "$SIMPLIFIED_JSON"
    --output "$HARMONIZED_JSON"
    --provider "$HARM_PROVIDER"
    --model "$HARM_MODEL"
    --batch-size "$BATCH_SIZE"
)
if [[ -n "$NAME_MAPPING" ]]; then
    HARM_ARGS+=(--name-mapping "$NAME_MAPPING")
    echo "  Using seed name mapping: $NAME_MAPPING"
fi
$PYTHON scripts/llm_aggregator.py "${HARM_ARGS[@]}"

# Step 4 — Characterize entities (synthesize definitions) via Google batch API.
# Production used the BATCH version (synthesize_definitions_batch.py); the older
# synchronous synthesize_definitions.py has been moved to DEP/.
# Production parameters: --model gemini-2.5-pro, --min-papers 3.
echo ""
echo "[Step 4/4] Characterize..."
CHARACTERIZED_JSON="$OUTDIR/harmonized_network_characterized.json"
VENUE_LABEL="$(basename "$OUTDIR")"
$PYTHON scripts/synthesize_definitions_batch.py \
    --input "$HARMONIZED_JSON" \
    --output "$CHARACTERIZED_JSON" \
    --model "$CHAR_MODEL" \
    --min-papers 3 \
    --description "characterize-${VENUE_LABEL}"

echo ""
echo "========================================"
echo " Pipeline complete!"
echo " Outputs in: $OUTDIR"
echo "   - Extraction:     $EXTRACTION_JSON"
echo "   - Simplified:     $SIMPLIFIED_JSON"
echo "   - Harmonized:     $HARMONIZED_JSON"
echo "   - Characterized:  $CHARACTERIZED_JSON"
echo "   - Logs:           logs/"
echo "========================================"
# NOTE: Per-conf site export and readable-Markdown generation are NOT part of
# the per-conf pipeline in production. Those steps run on the JOINT network
# only (see scripts/export_to_existing_site.py and generate_readable_configs.py),
# typically driven by update_joint_network.sh + the joint post-processing.
