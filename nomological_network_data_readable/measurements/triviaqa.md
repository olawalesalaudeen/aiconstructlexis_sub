# TriviaQA
**Type:** Measurement  
**Referenced in:** 178 papers  
**Also known as:** TRIVIAQA, TrivialQA, Trivia-QA  

## State of the Field

Across the surveyed literature, TriviaQA is a widely used benchmark for evaluating question answering capabilities. There is a notable variation in how it is operationalized: it is most frequently described as a "closed-book" question answering dataset with short, factual answers, used to assess a model's internal knowledge recall. However, a substantial number of papers also frame it as a "reading comprehension" or "open-domain" QA task, where models are expected to find answers within provided evidence documents. The questions are consistently characterized as being authored by trivia enthusiasts and are described as "knowledge-intensive." The most prevalent use of TriviaQA is to measure `question answering`, `open-domain question answering`, and `fact-seeking question answering`. It is also commonly employed to evaluate `text generation` within retrieval-augmented systems, as well as a model's `generalization` and `factual recall`. A smaller set of studies uses it to assess more specific behaviors like `information retrieval` and `spoken question answering`. Evaluation is often conducted in few-shot settings, with one paper noting they "conduct 5-shot evaluations on TriviaQA... using the exact match metric" (MiCEval: Unveiling Multimodal Chain of Thought’s Quality via Image Description and Reasoning Steps).

## Sources

**[BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)**
> TriviaQA is a closed-book question answering dataset used for evaluation, featuring questions with short, factual answers.

**[SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf) (as "TRIVIAQA")**
> A reading comprehension dataset containing question-answer pairs authored by trivia enthusiasts, used for evaluating question answering systems.

**[SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf) (as "TrivialQA")**
> A question answering dataset where questions are authored by people without seeing the evidence documents, reflecting a more natural information-seeking process.

**[Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf) (as "Trivia-QA")**
> A reading comprehension dataset containing question-answer pairs authored by trivia enthusiasts, used to assess a model's ability to find answers in provided documents.

## Relationships

### → TriviaQA
- **Question answering** (behaviors tasks) — *measured_by*
  > “• TRIVIAQA (Joshi et al., 2017): Assesses the model’s question-answering capability.”
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  > Finally, we apply our method to open-domain QA using the TriviaQA (Joshi et al., 2017) dataset.
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > Moreover, the choice of the four datasets, which include short- and long-form generation, question answering, summarization, and multi-hop reasoning, demonstrates the generalizability of the Sparse RAG approach. (Section 1)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > Performance comparison on eight LongBench datasets evaluating single/multi-document QA, summarization, and retrieval tasks... (Table 3)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Factuality** (constructs) — *measured_by*
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > The evaluation leverages three datasets: NaturalQuestions (NQ) (Kwiatkowski et al., 2019), TriviaQA (TQA) (Joshi et al., 2017) and WebQA (WebQ) (Berant et al., 2013), and a specilized task KV Retrieval (Liu et al., 2024). (Section 5.1)
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Open-ended question answering** (behaviors tasks) — *measured_by*
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Factual recall** (behaviors tasks) — *measured_by*
  > “We plot the accuracy versus sparsity for the OPT-13B, OPT-30B, LLaMA-13B, and LLaMA-33B models on TriviaQA dataset for fact recall evaluation (left)”
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Spoken question answering** (behaviors tasks) — *measured_by*
  > Spoken Question Answering ... We evaluate our model on 3 datasets in D´efossez et al. (2024): Web Questions (Berant et al., 2013), Llama Questions (Nachmani et al., 2024), and TriviaQA (Joshi et al., 2017).
  - [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)
- **Factual question answering** (behaviors tasks) — *measured_by*
  - [Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
- **Factual knowledge** (constructs) — *measured_by*
  - [On Synthetic Data Strategies for Domain-Specific Generative Retrieval](https://aclanthology.org/2025.acl-long.393.pdf)
- **Knowledge** (constructs) — *measured_by*
  - [Benchmarking and Improving Generator-Validator Consistency of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfcb583d225b1db8d3ca2331f6785774-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  - [The Cost of Scaling Down Large Language Models: Reducing Model Size Affects Memory before In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb68f698772f14b6d8eaef4529fb9176-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Benign question answering** (behaviors tasks) — *measured_by*
  - [Protecting Your LLMs with Information Bottleneck](https://proceedings.neurips.cc/paper_files/paper/2024/file/34a1fc7890141f1ada3d8bc6199cce07-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
- **Document understanding** (constructs) — *measured_by*
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  - [AISees YourLocation—But With A Bias Toward The Wealthy World](https://aclanthology.org/2025.emnlp-main.911.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Deliberation in Latent Space via Differentiable Cache Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bc/liu25bc.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **Knowledge transferability** (constructs) — *measured_by*
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > “We tested the models on the following benchmarks: • TRIVIAQA (Joshi et al., 2017): Assesses the model’s question-answering capability.”
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
- **Knowledge-intensive reasoning** (constructs) — *measured_by*
  > • TriviaQA (Joshi et al., 2017): A large-scale dataset containing knowledge-intensive questions sourced from Wikipedia. (Section 4.1)
  - [CoMet: Metaphor-Driven Covert Communication for Multi-Agent Language Games](https://aclanthology.org/2025.acl-long.390.pdf)
- **Fact-seeking question answering** (behaviors tasks) — *measured_by*
  > TriviaQA (5-shot) (Joshi et al., 2017), a factual question-answering dataset compiled by trivia enthusiasts to test retrieval of world knowledge. (Section 4.1)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)

### Associated with
- **HELMET** (measurements)
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
