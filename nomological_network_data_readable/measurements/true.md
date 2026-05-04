# TRUE
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, TRUE is consistently described as a Natural Language Inference (NLI) model that functions as an automated evaluator. It is specified as a T5-11B model fine-tuned on a collection of NLI datasets. The model's primary role is to judge the entailment between a premise, such as a source document, and a hypothesis, like a generated claim. As one study notes, its output can be represented as a binary value indicating whether "the premise p entails the hypothesis h." The most prevalent application for TRUE in this set of papers is to measure `Citation quality`, where it is used to verify if a claim is fully supported by cited documents. It is also documented as a tool for assessing the related construct of `Faithfulness`, specifically for evaluating factual consistency between summaries and their references. In all cases, it serves as a component within evaluation frameworks to assess the factual grounding of generated text.

## Sources

**[KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.459.pdf)**
> A fine-tuned T5-11B model used as the Natural Language Inference (NLI) component within evaluation frameworks to judge the entailment between a source passage and a generated claim.

## Relationships

### → TRUE
- **Citation quality** (constructs) — *measured_by*
  > We use TRUE3, a fine-tuned T5-11B (Raffel et al., 2020) model as the NLI model for the judgement of entailment in citation quality. (Section 4)
  - [PeerQA: A Scientific Question Answering Dataset from Peer Reviews](https://aclanthology.org/2025.naacl-long.23.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [POINTS-Reader: Distillation-Free Adaptation of Vision-Language Models for Document Conversion](https://aclanthology.org/2025.emnlp-main.83.pdf)
