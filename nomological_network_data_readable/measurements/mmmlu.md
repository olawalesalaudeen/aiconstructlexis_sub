# MMMLU
**Type:** Measurement  
**Referenced in:** 11 papers  

## State of the Field

Across the provided literature, MMMLU is consistently characterized as a multilingual, human-translated version of the MMLU benchmark. Its most frequently stated purpose is to assess "general language understanding" across various languages and subjects. Papers also use it to measure more specific constructs, including "multilingual reasoning," "reasoning performance," and "knowledge comprehension." Operationally, MMMLU is used to evaluate the behavior of text generation, specifically in the context of five-shot, multiple-choice question answering. One paper specifies that the benchmark functions by extracting answers from a model's generated outputs rather than from token probabilities. Another source notes that the test sets can be divided by difficulty into "easy" and "hard" evaluations. Several papers associate this benchmark with OpenAI.

## Sources

**[Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf)**
> A human-translated version of the MMLU benchmark, used to test general language understanding across multiple languages and subjects.

## Relationships

### → MMMLU
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **Multilingual reasoning** (constructs) — *measured_by*
  > Beyond English textual reasoning, we include two additional evaluation tracks: a multilingual experiment using MMLU and its professionally translated variant MMMLU (Hendrycks et al., 2021)...
  - [NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-TurnLLMJailbreaks](https://aclanthology.org/2025.emnlp-main.1236.pdf)
