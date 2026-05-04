# XCOMET
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** xCOMET  

## State of the Field

Across the provided literature, XCOMET is consistently characterized as a neural metric for evaluating machine translation. The most prevalent definition describes it as a quality estimation metric that scores a translation based on a source text and a generated hypothesis, often operating without a reference text. A smaller set of papers adds that it is trained on human judgments, can be used for both reference-based and reference-free estimation, and is fine-tuned to identify error spans with severity labels in addition to providing scores. In practice, XCOMET is used to measure constructs such as `Translation quality` and `Faithfulness`. It is frequently employed as a "main evaluation metric" or a "baseline," with its selection justified by its high correlation with human judgments, as noted in one paper. Described as a "popular" and one of the "strongest open-source MT metrics," it appears in various sizes like XCOMET-XL and XCOMET-XXL. While widely applied, one study notes that its effectiveness on specialized domains like "literary texts" remains "untested."

## Sources

**[Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.548.pdf)**
> A neural quality estimation metric that scores the quality of a translation based on source and hypothesis, used here to assess translatability, meaning preservation, and overall translation quality without reference texts.

**[A Case Against Implicit Standards: Homophone Normalization in Machine Translation for Languages that use theGe’ez Script.](https://aclanthology.org/2025.emnlp-main.524.pdf) (as "xCOMET")**
> Neural metric for machine translation evaluation trained on human judgments, used as a baseline for reference-based and reference-free quality estimation.

## Relationships

### → XCOMET
- **Meaning preservation** (constructs) — *measured_by*
  - [KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)
- **Translation quality** (constructs) — *measured_by*
  > We additionally report the combined evaluation metric, XCOMET(s′, t′, r) to take into account of the trade-off between the two above metrics, and METRICX(t′, r) which also assesses translation quality of the rewrite but is not informed by the updated source s′. (§3.2)
  - [KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)
