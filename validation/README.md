# Validation data

Human-expert validation data used in §3.1 (Quality Control) of the paper.
Expert identities are anonymized as **E1..E6** consistent with the paper.

## Contents

- `expert_reviews/` — per-expert workbooks for **concept extraction** review.
  Each expert independently extracted constructs, behaviors, and measurement
  instruments from a sample of 20 papers. Used to compute the precision and
  recall numbers in Figure 6 of the paper.
- `characterization_ratings/` — per-expert workbooks for **characterization**
  review. Six experts independently rated the LLM-synthesized usage
  characterizations of the top-20 canonical entities (10 constructs, 10
  behaviors) on a 5-point Likert scale (Strongly agree → Strongly disagree).
  Used to produce Figure 7 and the agreement statistics in the paper.
- `precision_recall_summary.csv` — aggregated precision/recall numbers used
  in Figure 6.
- `review_assignments_20papers.csv` — which papers were assigned to which
  reviewer.
