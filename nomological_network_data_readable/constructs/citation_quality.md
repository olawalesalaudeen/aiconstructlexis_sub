# Citation quality
**Type:** Construct  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, citation quality is consistently framed as a model's latent ability to correctly identify and reference source passages that support its generated claims, reflecting concepts like grounding, traceability, and faithfulness. The goal is to enable a model to "cite documents related to the claim correctly and to avoid citing irrelevant documents," as one paper puts it. This construct is commonly operationalized using recall and precision-based metrics, such as Recall@k, MAP@k, and citation recall and precision calculated at the level of atomic claims. Some work also introduces more specific metrics like the Coefficient of Variation of Citation Positions. A prevalent evaluation strategy involves using a Natural Language Inference (NLI) model to assess the relationship between claims and cited sources. Specifically, multiple papers report using the TRUE model for "the judgement of entailment in citation quality." One paper also proposes that the Best-of-N method influences this construct.

## Sources

**[KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.459.pdf)**
> The latent ability of a model to correctly identify and reference relevant source passages when generating a response, reflecting its grounding and traceability.

## Relationships

### Citation quality →
- **TRUE** (measurements) — *measured_by*
  > We use TRUE3, a fine-tuned T5-11B (Raffel et al., 2020) model as the NLI model for the judgement of entailment in citation quality. (Section 4)
  - [PeerQA: A Scientific Question Answering Dataset from Peer Reviews](https://aclanthology.org/2025.naacl-long.23.pdf)

### → Citation quality
- **Best-of-N** (measurements) — *causes*
  - [SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25a/chuang25a.pdf)
