# MLQA
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, MLQA is consistently described as the Multilingual Question Answering dataset, a benchmark used for evaluation. It is most frequently used to measure `Multilingual question answering` and general `Question answering`, with some work also using it to evaluate broader `Natural language understanding` and comprehension skills. More specifically, papers state that the benchmark evaluates "cross-lingual reading comprehension and answer extraction" and "extractive question answering capabilities in multiple languages." The dataset is characterized as consisting of "extractive question-answer instances" presented in the SQuAD format. One source specifies it contains "over 5K" instances across seven languages: English, Arabic, German, Spanish, Hindi, Vietnamese, and Simplified Chinese. A noted feature of its design is its "aligned dataset structure, where each question-answer pair is present in multiple languages," which facilitates cross-lingual evaluation. Beyond standard evaluation, MLQA is also mentioned as a source for the MLNeedle test and as a benchmark in a "language skill unlearning task."

## Sources

**[Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding inVLMs](https://aclanthology.org/2025.naacl-long.489.pdf)**
> The Multilingual Question Answering dataset, which consists of extractive question-answer instances across seven languages in the SQuAD format, used as the source for the MLNeedle test.

## Relationships

### → MLQA
- **Multilingual question answering** (behaviors tasks) — *measured_by*
  > However, efforts such as MLQA (Lewis et al., 2020) and XQuAD (Artetxe et al., 2019) have introduced datasets supporting multiple languages, facilitating cross-lingual evaluation of QA systems. (Section 5)
  - [On the Vulnerability of Text Sanitization](https://aclanthology.org/2025.naacl-long.267.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > “For the question-answering task, we fine-tune Qwen2.5-1.5B... We evaluate LMTransplant on five established benchmarks: • MLQA ... A question-answering benchmark”
  - [iTool: Reinforced Fine-Tuning with Dynamic Deficiency Calibration for Advanced Tool Use](https://aclanthology.org/2025.emnlp-main.702.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > We evaluate our methods on unlearning math-solving, Python-coding, and comprehension skills across seven different languages with GSM8K, MBPP, and MLQA datasets respectively. (Section 6)
  - [Model Surgery: ModulatingLLM’s Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.322.pdf)
