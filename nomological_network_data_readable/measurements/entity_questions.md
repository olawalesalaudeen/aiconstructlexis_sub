# Entity Questions
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** ENTITYQUESTIONS  

## State of the Field

Across the provided literature, Entity Questions is consistently described as a question answering dataset used to measure the behavior of closed-book question answering (CBQA). The dataset is characterized as being "CBQA-specific" and containing "knowledge across 24 topics extracted from Wikipedia." A complementary description frames it as a "fact-seeking question answering dataset" with a focus on "entity-related factual knowledge." In practice, researchers use it to construct training and testing sets for experiments. One study also reports its use for evaluating non-factuality prediction, and it is sometimes used alongside other QA datasets such as PopQA and Natural Questions.

## Sources

**[MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.25.pdf) (as "ENTITYQUESTIONS")**
> A dataset for closed-book question answering containing knowledge across 24 topics extracted from Wikipedia, used to construct training and testing sets.

**[Procedural Environment Generation for Tool-Use Agents](https://aclanthology.org/2025.emnlp-main.937.pdf)**
> Fact-seeking question answering dataset focusing on entity-related factual knowledge, used to evaluate non-factuality prediction.

## Relationships

### → Entity Questions
- **Closed-book question answering** (behaviors tasks) — *measured_by*
  > we use the ENTITYQUESTIONS (Sciavolino et al., 2021) to construct the training and testing datasets for our experiments, which is a CBQA-specific dataset containing knowledge across 24 topics extracted from Wikipedia (Section 3.1).
  - [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.25.pdf)
