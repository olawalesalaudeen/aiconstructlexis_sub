# Paraphrase identification
**Type:** Behavior  
**Referenced in:** 15 papers  
**Also known as:** Semantic equivalence judgment  

## State of the Field

Across the provided literature, paraphrase identification is most commonly defined as the task of determining whether two given sentences have the same meaning. Some papers offer slight variations, such as specifying that the meaning should be the same "despite differences in wording," while a less frequent framing defines it as judging "semantic equivalence" through mutual entailment. This behavior is consistently operationalized and measured using a set of established benchmarks. The most frequently cited instruments include MRPC and QQP, which are often used as part of the GLUE benchmark suite to evaluate natural language understanding. The PAWS dataset is also used for this purpose. Additionally, PAWS-X is employed as a "cross-lingual adversarial dataset for paraphrase identification," with one study noting its use for evaluating the task in Spanish. The task is generally situated as a common natural language understanding capability, studied alongside tasks like question answering and coreference resolution.

## Sources

**[Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf)**
> The task of determining whether two given sentences have the same meaning.

**[BeSimulator: A Large Language Model Powered Text-based Behavior Simulator](https://aclanthology.org/2025.emnlp-main.238.pdf) (as "Semantic equivalence judgment")**
> Determining whether two responses are semantically equivalent by mutual entailment.

**[Primus: A Pioneering Collection of Open-Source Datasets for CybersecurityLLMTraining](https://aclanthology.org/2025.emnlp-main.528.pdf) (as "Paraphrase detection")**
> Identifying whether two sentences express the same meaning despite differences in wording.

## Relationships

### Paraphrase identification →
- **PAWS** (measurements) — *measured_by*
  - [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](https://aclanthology.org/2025.acl-long.1155.pdf)
- **MRPC** (measurements) — *measured_by*
  > We employ eight datasets across various NLP tasks to evaluate the impact of bit-flip errors on model performance: MRPC (paraphrase detection) (Dolan and Brockett, 2005)... (Section 5.1)
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
- **QQP** (measurements) — *measured_by*
  > (5) Paraphrase Identification (QQP): determine if two questions are “equivalent” or “not equivalent” (Section 4.6)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
- **PAWS-X** (measurements) — *measured_by*
  > We perform zero-shot evaluation on six tasks that test the LLMs ability on reasoning (Xstorycloze, Xcopa) (Ponti et al., 2020), coreference resolution (Xwinograd) (Muennighoff et al., 2023), reading comprehension (Lambada) (Paperno et al., 2016), natural language understanding (XNLI) (Conneau et al., 2018), and paraphrasing (PAWS-X) (Yang et al., 2019). (Section 4)
  - [Simple Yet Effective: An Information-Theoretic Approach to Multi-LLMUncertainty Quantification](https://aclanthology.org/2025.emnlp-main.1552.pdf)
