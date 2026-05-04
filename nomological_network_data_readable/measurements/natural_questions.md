# Natural Questions
**Type:** Measurement  
**Referenced in:** 151 papers  
**Also known as:** NQ, NQ-Open, NaturalQuestion, NaturalQuestions, NQ dataset, Nature Questions, NaturalQuestions (NQ-Open), NQ Open, Natural Questions (NQ), NATURAL QUESTIONS (NQ)  

## State of the Field

Across the surveyed literature, Natural Questions (NQ) is a widely used benchmark for evaluating question answering, consistently described as a dataset derived from real user queries to a search engine, often Google, with answers sourced from Wikipedia articles. The prevailing use of this instrument is to measure behaviors such as open-domain question answering, information retrieval, and factual recall. Papers operationalize it in several distinct settings; it is frequently used in retrieval-augmented generation (RAG) contexts, but also appears in "closed-book" evaluations to assess a model's stored knowledge, as one study notes, to "measure the factual knowledge in the model" (Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning). The dataset is often characterized as a "single-hop" QA benchmark requiring direct fact-based answers. Evaluation is commonly performed in few-shot settings, with papers mentioning 3-shot, 5-shot, and 32-shot configurations, and performance is typically scored using metrics like exact match or F1 score. Beyond core QA, Natural Questions is also employed to evaluate broader capabilities like text generation, generalization, and the performance of RAG systems under varying conditions. A smaller set of studies uses its questions for more specific tasks, such as evaluating locality in knowledge editing or for hallucination detection.

## Sources

**[INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf)**
> Natural Questions (NQ) is a closed-book question answering dataset derived from real user queries, used for evaluation.

**[Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf) (as "NaturalQA")**
> A question answering benchmark included in the expanded evaluation set.

**[Making Retrieval-Augmented Language Models Robust to Irrelevant Context](https://proceedings.iclr.cc/paper_files/paper/2024/file/8011b23e1dc3f57e1b6211ccad498919-Paper-Conference.pdf) (as "NQ")**
> Natural Questions benchmark, a real-world question answering dataset requiring retrieval and comprehension of factual information, evaluated in a 32-shot setting.

**[From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf) (as "NQ-Open")**
> An open-domain question-answering benchmark derived from the Natural Questions dataset, where questions are real user queries to a search engine.

**[Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/26d3c9a66836ded8f34a944f2bfe868e-Paper-Conference.pdf) (as "NaturalQuestions")**
> A question-answering dataset derived from real user queries to the Google search engine, cited as an example of a world knowledge benchmark.

**[Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbb10d319d44f8c3b4720873e4177c65-Paper-Conference.pdf) (as "NaturalQuestion")**
> A question-answering corpus of queries issued to the Google search engine.

**[MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf) (as "NQ dataset")**
> A dataset used to source text questions for evaluating locality in knowledge editing.

**[SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf) (as "Nature Questions")**
> A question answering dataset used to evaluate QA behavior under dynamic input streams.

**[Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf) (as "NaturalQuestions (NQ-Open)")**
> A question answering dataset of Google search queries with annotated answers from Wikipedia and multiple annotators.

**[Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf) (as "NQ Open")**
> Open-domain version of the Natural Questions dataset, used for evaluating question answering and hallucination detection in realistic settings.

**[Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf) (as "Natural Questions (NQ)")**
> A question answering dataset used to evaluate RAG system performance by varying the number of retrieved passages.

**[SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf) (as "NATURAL QUESTIONS (NQ)")**
> A question answering dataset consisting of real user questions posed to Google search and corresponding answers found in Wikipedia articles.

## Relationships

### Natural Questions →
- **Text generation** (behaviors tasks) — *measured_by*
  > "Experiments are conducted based on LLaMA-2-7B on Natural Question dataset."
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)

### → Natural Questions
- **Question answering** (behaviors tasks) — *measured_by*
  > The questions used for constructing our training data are sourced from the ASQA (Stelmakh et al., 2022), WebQuestions (Berant et al., 2013), and Natural Questions (Kwiatkowski et al., 2019) training splits. (Section 4.1.1)
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  > To thoroughly evaluate model performance across both in-domain (ID) and out-of-domain (OOD) settings, we construct a diverse benchmark suite spanning a range of open-domain QA challenges. For in-domain evaluation, we include the dev sets of NQ... (Section 4.2.1)
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > "We benchmark the current LLM’s ability to perform situated faithful reasoning on several question-answering tasks, including ... NaturalQA"
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **Factuality** (constructs) — *measured_by*
  - [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > The evaluation leverages three datasets: NaturalQuestions (NQ) (Kwiatkowski et al., 2019), TriviaQA (TQA) (Joshi et al., 2017) and WebQA (WebQ) (Berant et al., 2013), and a specilized task KV Retrieval (Liu et al., 2024). (Section 5.1)
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  - [Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **Locality** (constructs) — *measured_by*
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **Factual knowledge** (constructs) — *measured_by*
  - [On Synthetic Data Strategies for Domain-Specific Generative Retrieval](https://aclanthology.org/2025.acl-long.393.pdf)
- **Factual recall** (behaviors tasks) — *measured_by*
  > We consider nine varied downstream tasks: ... (f) fact recall (WebQuestions (Berant et al., 2013), Natural Questions (Kwiatkowski et al., 2019))
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
- **Open-ended question answering** (behaviors tasks) — *measured_by*
  - [LongReward: Improving Long-context Large Language Models withAIFeedback](https://aclanthology.org/2025.acl-long.188.pdf)
- **Memorization** (constructs) — *measured_by*
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **Knowledge transferability** (constructs) — *measured_by*
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Factual question answering** (behaviors tasks) — *measured_by*
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
- **Fact-seeking question answering** (behaviors tasks) — *measured_by*
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Deliberation in Latent Space via Differentiable Cache Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bc/liu25bc.pdf)
- **Text-based question answering** (behaviors tasks) — *measured_by*
  > we apply this intervention to ... two QA tasks, Natural Questions (NQ) and HotpotQA... By contrast, on the QA tasks, masking RH leads to a substantial performance decrease. These results confirm that ... retrieval heads play a more pivotal role in text-based QA. (Section 5.2)
  - [Please Translate Again: Two Simple Experiments on Whether Human-Like Reasoning Helps Translation](https://aclanthology.org/2025.emnlp-main.1032.pdf)

### Associated with
- **HELMET** (measurements)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
