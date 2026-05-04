# OpenBookQA
**Type:** Measurement  
**Referenced in:** 151 papers  
**Also known as:** OpenbookQA, Obqa, openBookQA, OpenBook QA, Openbook QA  

## State of the Field

Across the surveyed literature, OpenBookQA is consistently characterized as a multiple-choice question-answering benchmark modeled after open-book exams, focusing on elementary-level science questions. The prevailing usage frames it as a task requiring reasoning over a provided set of science facts, often in a zero-shot evaluation context. A recurring theme in its definition is the need to combine these provided facts with external commonsense knowledge; as one paper specifies, it focuses on the challenge of "combining a corpus of provided science facts (open book) with external common knowledge" (Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study). Papers most frequently use OpenBookQA to operationalize and measure `commonsense understanding` and `question answering`. It is also widely employed to assess a range of other constructs, including `language understanding`, `text generation`, `reading comprehension`, and `scientific reasoning`. Additionally, some studies use it to evaluate model `generalization`, for instance, as a held-out test set or to assess applicability beyond a specific domain. The benchmark is commonly evaluated alongside other commonsense reasoning datasets like ARC, HellaSwag, and PIQA, with accuracy being the standard reported metric.

## Sources

**[Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf)**
> A zero-shot multiple-choice question answering benchmark based on open-book science questions.

**[Efficient Streaming Language Models with Attention Sinks](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e5fd18f863cbe6d8ae392a93fd271c9-Paper-Conference.pdf) (as "OpenbookQA")**
> A question-answering dataset modeled after open book exams, requiring reasoning over a set of elementary science facts.

**[Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf) (as "openBookQA")**
> A question-answering dataset that requires combining a corpus of provided science facts with external common knowledge to assess understanding and reasoning.

**[Efficient Learning with Sine-Activated Low-Rank Matrices](https://proceedings.iclr.cc/paper_files/paper/2025/file/112d8e0c7563de6e3408b49a09b4d8a3-Paper-Conference.pdf) (as "OBQA")**
> OpenBookQA, a benchmark for answering elementary science questions requiring commonsense and open-book knowledge.

**[Scaling up Masked Diffusion Models on Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1c1ff5d94079dea348a2317a889281-Paper-Conference.pdf) (as "Obqa")**
> The OpenBookQA dataset, a commonsense question-answering benchmark that requires reasoning with a small set of common knowledge facts.

**[u-$\mu$P: The Unit-Scaled Maximal Update Parametrization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e3130a164f5c724e37271b93bc76dd28-Paper-Conference.pdf) (as "OpenBook QA")**
> A benchmark requiring open-book question answering based on provided facts.

**[SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf) (as "Openbook QA")**
> A question answering dataset modeled after open-book exams, requiring reasoning with a given set of elementary-level science facts.

## Relationships

### OpenBookQA →
- **Question answering** (behaviors tasks) — *measured_by*
  > The OpenBookQA dataset is a question-answering dataset designed to test deep understanding through multi-step reasoning, common knowledge, and text comprehension, similar to open-book exams. (Section 4.1)
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)

### → OpenBookQA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e6c2e85db1f1039177c4495ccd399ac4-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > “we evaluate the proposed MoEQuant on various reasoning tasks, including MMLU (Hendrycks et al., 2020), BoolQ (Clark et al., 2019), HellaSwag (Zellers et al., 2019), Openbookqa (Mihaylov et al., 2018), and MathQA (Amini et al., 2019).”
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > We have selected three datasets that measure common sense reasoning and language understanding to evaluate the possible performance loss after altering the model: OpenBookQA (OBQA) (Mihaylov et al., 2018)... (Section 2.5)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > In this section, we investigate whether our method is generally applicable beyond the medical domain. We use two general domain datasets, CommonsenseQA (CSQA) (Talmor et al., 2018) and OpenbookQA (OBQA) (Mihaylov et al., 2018)... (Section 4.5)
  - [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
- **Commonsense question answering** (behaviors tasks) — *measured_by*
  - [Path Drift in Large Reasoning Models: How First-Person Commitments Override Safety](https://aclanthology.org/2025.emnlp-main.991.pdf)
- **Zero-shot classification** (behaviors tasks) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > we use seven commonsense reasoning tasks from the popular framework Harness (Gao et al., 2024), including four reading comprehension tasks (ARC-e, ARC-c (Clark et al., 2018), OBQA (Mihaylov et al., 2018), and BoolQ (Clark et al., 2019))... (Section 4.1)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **Factuality** (constructs) — *measured_by*
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > These tasks assess the model performance on logical reasoning, language understanding, commonsense reasoning, and knowledge utilization. (Section 4.1)
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **Scientific reasoning** (constructs) — *measured_by*
  > OpenBookQA (Mihaylov et al., 2018) for fact reasoning (Section 3.1)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
- **Scientific question answering** (behaviors tasks) — *measured_by*
  - [Debiasing the Fine-Grained Classification Task inLLMs with Bias-AwarePEFT](https://aclanthology.org/2025.acl-long.718.pdf)
