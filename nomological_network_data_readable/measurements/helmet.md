# HELMET
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, HELMET is consistently characterized as a comprehensive benchmark for evaluating the performance of large language models on long-context tasks. It is described as a composite instrument, with one paper noting that it "includes portions from popular long-text benchmarks such as RULER... and ∞Bench" (MorphMark: Flexible Adaptive Watermarking for Large Language Models). Papers use HELMET to assess a diverse set of capabilities, though the exact scope varies slightly across descriptions; one source states its evaluation spans five task types including synthetic recall, retrieval-augmented generation, and long-document QA, while another mentions it covers seven categories. Broadly, HELMET is used to measure constructs and behaviors such as long-context understanding, information retrieval, memorization, and length generalization. In terms of its operationalization, HELMET is reported to curate versions of existing datasets like HotpotQA, Natural Questions, and TriviaQA for its own long-context evaluations. Researchers commonly employ it in experiments to demonstrate enhancements in a model's long-context processing and memory abilities.

## Sources

**[MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.241.pdf)**
> A long-context benchmark that includes portions from RULER and ∞Bench, used to assess model performance on extended text processing tasks.

## Relationships

### → HELMET
- **Long-context understanding** (constructs) — *measured_by*
  - [Enhancing Transformers for Generalizable First-Order Logical Entailment](https://aclanthology.org/2025.acl-long.275.pdf)
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Ranking** (behaviors tasks) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  > The evaluation spans five task types from the HELMET benchmark: synthetic recall, retrieval-augmented generation (RAG), many-shot in-context learning (ICL), passage re-ranking, and long-document QA, covering a total of 17 sub-tasks. (Section 4.1. Evaluation)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Synthetic recall** (behaviors tasks) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Long-range dependency modeling** (constructs) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Memorization** (constructs) — *measured_by*
  - [ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **Length generalization** (constructs) — *measured_by*
  - [ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf)

### Associated with
- **HotpotQA** (measurements)
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **Natural Questions** (measurements)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **TriviaQA** (measurements)
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
