#!/usr/bin/env bash
# Re-runnable anonymity audit. Greps the entire submission for any string
# that could de-anonymize the authors. Run from the repo root.
#
#   bash code/scripts/anonymity_audit.sh
#
# Edit the IDENTIFIERS array to add author last names, emails, handles.

set -u
ROOT=$(cd "$(dirname "$0")"/../.. && pwd)
cd "$ROOT"

# === Author identifiers to scrub ==========================================
IDENTIFIERS=(
  "Olawale" "Salaudeen"
  "olawalesalaudeen.com"
  "@mit.edu" "@stanford.edu" "@cornell.edu" "@huggingface" "@meta.com"
  "olawale@" "salaudeen@"
)

# === Files to skip (research data with legitimate citations) ==============
SKIP_PATHS='/(network_data|lexis_artifact|nomological_network_data|nomological_network_data_readable|paper_list|data)/'

fail=0
echo "== Anonymity audit =="
for id in "${IDENTIFIERS[@]}"; do
  hits=$(grep -rEnIi --color=never "$id" . 2>/dev/null \
         | grep -vE "$SKIP_PATHS" \
         | grep -v "^./.git/" \
         | grep -v "anonymity_audit.sh")
  if [ -n "$hits" ]; then
    fail=1
    echo
    echo "[FAIL] '$id' found in:"
    echo "$hits" | head -20
  fi
done

# Catch-all for contact links anywhere in the deploy
hits=$(grep -rEnI "mailto:|substack\.com|twitter\.com|linkedin\.com|orcid\.org" . 2>/dev/null \
       | grep -vE "$SKIP_PATHS" \
       | grep -v "^./.git/" \
       | grep -v "anonymity_audit.sh")
if [ -n "$hits" ]; then
  fail=1
  echo
  echo "[FAIL] contact / social links found:"
  echo "$hits"
fi

# Catch-all for analytics scripts
hits=$(grep -rEnI "google-analytics|gtag\(|fbq\(|hotjar|plausible\.io|cloudflare-insights" . 2>/dev/null \
       | grep -v "^./.git/" \
       | grep -v "anonymity_audit.sh")
if [ -n "$hits" ]; then
  fail=1
  echo
  echo "[FAIL] analytics / tracking found:"
  echo "$hits"
fi

if [ $fail -eq 0 ]; then
  echo "PASS — no identifying strings found."
  exit 0
else
  echo
  echo "AUDIT FAILED. Fix the hits above before publishing."
  exit 1
fi
