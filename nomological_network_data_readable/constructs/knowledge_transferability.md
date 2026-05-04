# Knowledge transferability
**Type:** Construct  
**Referenced in:** 72 papers  
**Also known as:** Cross-lingual transfer, Cross-lingual propagation, Cross-lingual transferability, Cross-lingual knowledge transfer, Domain transferability, Self-transfer learning, Content transfer and synthesis, Generalization to unseen tasks, Competence transfer, Hyperparameter transfer, Prompt transferability, Super transferability, Transferability, Zero-shot transferability  

## State of the Field

Knowledge transferability is most commonly framed as a model's ability to apply knowledge or capabilities learned in one language to other languages, a concept variously termed cross-lingual transfer, propagation, or transferability. This is often described as being enabled by “shared representations in a multilingual space” (MolErr2Fix: BenchmarkingLLMTrustworthiness in Chemistry via Modular Error Detection, Localization, Explanation, and Correction). Beyond the cross-lingual context, the construct is also defined as the generalization of knowledge across different task domains, levels of complexity, or from previously learned tasks to new ones. A smaller set of studies conceptualizes transferability in more specific contexts, such as applying optimal hyperparameters from small to large models (hyperparameter transfer), the effectiveness of an adversarial attack across models and tasks (super transferability), or a system's capacity to learn from its own past interactions (self-transfer learning). The operationalization of this construct is varied, with researchers measuring it through performance on a wide array of benchmarks and tasks. These measurement approaches include multilingual understanding benchmarks like XNLI, question-answering datasets such as TruthfulQA, TriviaQA, and Natural Questions, and reasoning tasks like GSM8k. Other papers assess it via performance on machine translation, text classification, and general instruction-following benchmarks like MT-Bench and Arena-Hard. In the provided literature, knowledge transferability is reported to influence several other properties, including generalization, training efficiency, and in-context learning. The construct is also frequently studied in relation to continual learning, multilingual ability, and semantic understanding, and is sometimes positioned as being driven by factors like cross-lingual alignment and language proficiency.

## Sources

**[Language Imbalance Driven Rewarding for Multilingual Self-improving](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cdee7247c410907b32fcbc12a605823-Paper-Conference.pdf) (as "Cross-lingual transfer")**
> The latent ability for improvements learned in one language to generalize to other languages, including unseen ones.

**[FLRC: Fine-grained Low-Rank Compressor for EfficientLLMInference](https://aclanthology.org/2025.emnlp-main.756.pdf)**
> The ability of a multilingual model to consistently access and apply the same factual knowledge across different languages, indicating that the knowledge is not tied to a single linguistic representation.

**[From Capabilities to Performance: Evaluating Key Functional Properties ofLLMArchitectures in Penetration Testing](https://aclanthology.org/2025.emnlp-main.803.pdf) (as "Cross-lingual propagation")**
> The extent to which a factual edit made in one source language successfully transfers to semantically equivalent queries in other target languages.

**[MolErr2Fix: BenchmarkingLLMTrustworthiness in Chemistry via Modular Error Detection, Localization, Explanation, and Correction](https://aclanthology.org/2025.emnlp-main.978.pdf) (as "Cross-lingual transferability")**
> The capability of a multilingual model to apply knowledge learned from one language to another, enabled by shared representations in a multilingual space.

**[Are Checklists Really Useful for Automatic Evaluation of Generative Tasks?](https://aclanthology.org/2025.emnlp-main.539.pdf) (as "Cross-lingual knowledge transfer")**
> The model's ability to apply knowledge acquired in one language to perform tasks accurately in another language, reflecting robust multilingual understanding.

**[When People are Floods: Analyzing Dehumanizing Metaphors in Immigration Discourse with Large Language Models](https://aclanthology.org/2025.acl-long.399.pdf) (as "Domain transferability")**
> The extent to which optimized safety checks and learned risk patterns generalize from one task domain to another without performance degradation.

**[Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf) (as "Knowledge transfer")**
> The ability of a model to leverage knowledge from previously learned tasks to improve learning of new tasks (forward transfer) or to enhance performance on old tasks using knowledge from new ones (backward transfer).

**[MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gaven25a/gaven25a.pdf) (as "Competence transfer")**
> The phenomenon where practicing one goal improves performance on other semantically related goals, captured dynamically through learned representations rather than predefined groupings.

**[Can RLHF be More Efficient with Imperfect Reward Models? A Policy Coverage Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25o/huang25o.pdf) (as "Self-transfer learning")**
> The latent ability of a learning system to improve future policy updates by distilling knowledge from its own past online interactions, forming a self-improving loop.

**[$\mathrmμ$nit Scaling: Simple and Scalable FP8 LLM Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/narayan25b/narayan25b.pdf) (as "Hyperparameter transfer")**
> The property of a training methodology that allows optimal hyperparameters found on small models to be successfully applied to larger models without re-tuning.

**[Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf) (as "Content transfer and synthesis")**
> The ability to generate output by integrating original and modified elements from memory, such as copying, rephrasing, or synthesizing information across context segments.

**[Learngene Tells You How to Customize: Task-Aware Parameter Initialization at Flexible Scales](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25af/xu25af.pdf) (as "Generalization to unseen tasks")**
> The ability of a parameter initialization method to produce effective model parameters for tasks not seen during training.

**[LaMAGIC2: Advanced Circuit Formulations for Language Model-Based Analog Topology Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25b/chang25b.pdf) (as "Transferability")**
> The model's ability to generalize its performance from training on simpler circuits to generating more complex circuits with a larger number of components.

**[X-Transfer Attacks: Towards Super Transferable Adversarial Attacks on CLIP](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25h/huang25h.pdf) (as "Super transferability")**
> A property of an adversarial attack where a single perturbation is effective across different data samples, domains, models, and tasks simultaneously.

**[LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/niu25e/niu25e.pdf) (as "Zero-shot transferability")**
> The ability of the pre-trained model to perform forecasting in unseen domains without task-specific fine-tuning.

**[Efficient and Privacy-Preserving Soft Prompt Transfer for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ds/wang25ds.pdf) (as "Prompt transferability")**
> The latent ability of a soft prompt tuned on one language model to maintain high performance when applied to a different, larger language model.

## Relationships

### Knowledge transferability →
- **XNLI** (measurements) — *measured_by*
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Alignment** (constructs) — *causes*
  - [Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion](https://aclanthology.org/2025.naacl-long.88.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  - [Mutual-Taught](https://aclanthology.org/2025.acl-long.795.pdf)
- **Machine reading comprehension** (behaviors tasks) — *measured_by*
  - [Mutual-Taught](https://aclanthology.org/2025.acl-long.795.pdf)
- **Machine translation** (behaviors tasks) — *measured_by*
  - [Mutual-Taught](https://aclanthology.org/2025.acl-long.795.pdf)
- **Traffic** (measurements) — *measured_by*
  - [LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/niu25e/niu25e.pdf)
- **HaluEval** (measurements) — *measured_by*
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Data efficiency** (constructs) — *causes*
  - [Can RLHF be More Efficient with Imperfect Reward Models? A Policy Coverage Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25o/huang25o.pdf)
- **Training efficiency** (constructs) — *causes*
  - [$\mathrmμ$nit Scaling: Simple and Scalable FP8 LLM Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/narayan25b/narayan25b.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [LingGym: How Far AreLLMs from Thinking Like Field Linguists?](https://aclanthology.org/2025.emnlp-main.70.pdf)
- **Arena-Hard** (measurements) — *measured_by*
  - [LingGym: How Far AreLLMs from Thinking Like Field Linguists?](https://aclanthology.org/2025.emnlp-main.70.pdf)
- **Linguistic similarity** (constructs) — *correlates*
  - [FoREST: Frame of Reference Evaluation in Spatial Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf)

### → Knowledge transferability
- **Knowledge retrieval** (behaviors tasks) — *causes*
  - [CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf)
- **In-context reasoning** (constructs) — *correlates*
  - [CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf)
- **Language proficiency** (constructs) — *causes*
  - [CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf)

### Associated with
- **Generalization** (constructs)
  - [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [Improving Handshape Representations for Sign Language Processing: A Graph Neural Network Approach](https://aclanthology.org/2025.emnlp-main.1484.pdf)
- **Multilingual ability** (constructs)
  - [FoREST: Frame of Reference Evaluation in Spatial Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf)
- **Translation capability** (constructs)
  - [Assessing Reliability and Political Bias InLLMs’ Judgements of Formal and Material Inferences With Partisan Conclusions](https://aclanthology.org/2025.acl-long.1451.pdf)
- **Definition generation** (behaviors tasks)
  - [Jigsaw-Puzzles: From Seeing to Understanding to Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1321.pdf)
- **LASER** (measurements)
  - [PrimeX: A Dataset of Worldview, Opinion, and Explanation](https://aclanthology.org/2025.emnlp-main.1257.pdf)
- **Semantic understanding** (constructs)
  - [Leveraging Loanword Constraints for Improving Machine Translation in a Low-Resource Multilingual Context](https://aclanthology.org/2025.emnlp-main.1407.pdf)
