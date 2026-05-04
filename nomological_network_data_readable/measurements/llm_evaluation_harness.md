# LLM Evaluation Harness
**Type:** Measurement  
**Referenced in:** 214 papers  
**Also known as:** lm-eval, LM-Eval, LM-EVAL, Language Model Evaluation Harness, language model evaluation harness, LM Eval Harness, lm-eval-harness, LM-Eval-Harness, LM Evaluation Harness, LM-evaluation harnesses, lm-evaluation-harness, LM-Evaluation-Harness, LM-evaluation-harness, LM-EVALUATION-HARNESS, LM Harness, lm-harness, lm-eval framework, LM-Eval framework, Harness, llm-evaluation-harness, LLMs Evaluation Harness, Evaluation Harness, EleutherAI LM Harness, Harness-Eval framework, LLM-evaluation suite, Eleuther Harness, Eleuther AI Language Model Evaluation Harness, EleutherAI LM-Eval-Harness, llm-eval-harness, Eleuther AI eval-harness, Open LLM Leaderboard Harness, EleutherAI Language Model Evaluation Harness, HuggingFace Open LLM harness, EleutherAI evaluation harness, Harness framework, eleuther-AI evaluation harness, lm eval framework, Eleuther LM eval harness, eleuther AI eval harness  

## State of the Field

Across the surveyed literature, the LLM Evaluation Harness is consistently defined as a standardized, open-source framework or software suite for evaluating language models to ensure reproducible and comparable results. It is widely used to measure a broad range of model capabilities, with the most frequently assessed being zero-shot task performance, commonsense understanding, language modeling, and mathematical reasoning. Other reported applications include evaluating language understanding, text generation, problem-solving, and helpfulness. The prevailing usage of the harness is for zero-shot evaluations, though some papers also mention its use in few-shot or in-context learning settings. The framework operationalizes these assessments by running models on a diverse set of downstream tasks and benchmarks, and is frequently studied alongside or used to run evaluations on MMLU, HellaSwag, PIQA, ARC, and WinoGrande. Some papers specify its evaluation methodology, with one noting its technique of "investigating output logits over a constrained set of potential responses," while another describes its use of tools like `sympy` to verify mathematical correctness. The tool, often attributed to EleutherAI, appears under numerous names including "lm-evaluation-harness," "LM-Eval," and simply "Harness."

## Sources

**[Differential Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/00b67df24009747e8bbed4c2c6f9c825-Paper-Conference.pdf) (as "LM Eval Harness")**
> A standardized evaluation suite comprising multiple downstream tasks like ARC, BoolQ, and HellaSwag to assess general language model performance.

**[SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf) (as "lm-evaluation-harness")**
> An open-source framework used to standardize the evaluation of language models on various benchmarks, ensuring reproducible and comparable results.

**[Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf) (as "LM Evaluation Harness")**
> A standardized evaluation harness used to run language-model benchmarks and multiple-choice tasks.

**[Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf) (as "LM-Evaluation-Harness")**
> A unified software framework for evaluating language models on a wide range of tasks in a zero-shot setting.

**[Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf) (as "Language Model Evaluation Harness")**
> A unified framework for running standardized evaluations of generative language models on a large number of diverse tasks.

**[Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf) (as "LM Harness")**
> Eleuther's LM Harness, a standardized evaluation framework used to run the paper's text-only task suite.

**[Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf) (as "lm-harness")**
> An evaluation framework (lm-evaluation-harness) that provides a standardized way to benchmark language models on a wide range of tasks.

**[RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf) (as "lm-eval-harness")**
> An evaluation framework for language models used to score performance on various downstream tasks.

**[Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf) (as "language model evaluation harness")**
> An evaluation suite providing a standardized framework for assessing performance on various downstream tasks.

**[Forgetting Transformer: Softmax Attention with a Forget Gate](https://proceedings.iclr.cc/paper_files/paper/2025/file/add3d389197ad2267f660ad060ef61f4-Paper-Conference.pdf) (as "LM-evaluation-harness")**
> A standardized evaluation harness used to run zero-shot short-context language-model benchmarks such as Wikitext, LAMBADA, PIQA, HellaSwag, and others.

**[Adaptive Rank Allocation: Speeding Up Modern Transformers with RaNA Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/bdb0596d13cfccf2db6f0cc5280d2a3f-Paper-Conference.pdf) (as "LM-evaluation harnesses")**
> A software suite used to run downstream-task performance evaluations in zero-shot or few-shot settings.

**[On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf) (as "lm-eval")**
> An evaluation harness (lm-evaluation-harness) used to assess model performance on a wide range of zero-shot tasks, in this case to measure helpfulness.

**[$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf) (as "LM-Eval")**
> LM-Eval is an evaluation benchmark suite used here for generation tasks assessing commonsense and math reasoning.

**[STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf) (as "LM-Eval-Harness")**
> A standardized framework for evaluating language models on a wide range of downstream tasks.

**[Hymba: A Hybrid-head Architecture for Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f32def07618040e540e0a6182e290562-Paper-Conference.pdf) (as "LM-EVALUATION-HARNESS")**
> LM Evaluation Harness, a standardized evaluation framework used to run language-model benchmarks across multiple tasks and settings.

**[Quamba: A Post-Training Quantization Recipe for Selective State Space Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb4b2fb2434f7cce5cb5ab50271296ee-Paper-Conference.pdf) (as "LM-EVAL")**
> LM-EVAL is an evaluation harness used to run zero-shot language-model benchmarks across multiple common-sense tasks.

**[Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf) (as "Harness")**
> An evaluation framework (also known as lm-evaluation-harness) used to assess the generic performance of LLMs across a diverse set of tasks.

**[Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf) (as "llm-evaluation-harness")**
> The llm-evaluation-harness repository, used to run standardized evaluations on reasoning benchmarks.

**[Improving Reasoning Performance in Large Language Models via Representation Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e73c39cc428c7d264d9820319f31e79-Paper-Conference.pdf) (as "lm-eval framework")**
> An evaluation suite for language models, referenced in the paper for its method of benchmarking performance by investigating output logits over a constrained set of potential responses.

**[RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf) (as "LLMs Evaluation Harness")**
> An evaluation framework used to assess mathematical reasoning performance, which can use tools like sympy to verify the correctness of generated solutions.

**[HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf) (as "LM-Eval framework")**
> A software framework used to conduct zero-shot inference evaluations on language models.

**[Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf) (as "Evaluation Harness")**
> The Evaluation Harness framework, a standardized benchmark evaluation procedure used to run general capability tests.

**[Mixture Compressor for Mixture-of-Experts LLMs Gains More](https://proceedings.iclr.cc/paper_files/paper/2025/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf) (as "EleutherAI LM Harness")**
> An evaluation framework used to test language models on a wide range of benchmarks in a standardized way.

**[INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf) (as "Harness-Eval framework")**
> An evaluation framework used to standardize the assessment of language models, which was used to validate the results on the INCLUDE benchmark.

**[Towards Scalable Exact Machine Unlearning Using Parameter-Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/d33b741600f100b31256c70a46f66ec9-Paper-Conference.pdf) (as "LLM-evaluation suite")**
> LLM Evaluation Suite, a standardized evaluation suite used to report zero-shot performance on multiple language-model benchmarks.

**[Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf) (as "EleutherAI Language Model Evaluation Harness")**
> A standardized evaluation suite that assesses language models across a variety of zero-shot benchmarks covering reasoning, knowledge, and comprehension tasks.

**[any4: Learned 4-bit Numeric Representation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/elhoushi25a/elhoushi25a.pdf) (as "Eleuther Harness")**
> The EleutherAI Language Model Evaluation Harness, a framework for standardized evaluation of language models on a wide range of natural language tasks.

**[MoH: Multi-Head Attention as Mixture-of-Head Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25l/jin25l.pdf) (as "Eleuther AI Language Model Evaluation Harness")**
> A unified software framework, also known as lm-evaluation-harness, for standardized evaluation of generative language models across a wide range of benchmarks.

**[PROXSPARSE: REGULARIZED LEARNING OF SEMI-STRUCTURED SPARSITY MASKS FOR PRETRAINED LLMS](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bi/liu25bi.pdf) (as "EleutherAI LM-Eval-Harness")**
> EleutherAI LM-Eval-Harness is an evaluation harness used to run standardized zero-shot language reasoning tasks on LLMs.

**[DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf) (as "llm-eval-harness")**
> A framework for few-shot language model evaluation used to assess the performance of compressed models on zero-shot tasks.

**[Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf) (as "Eleuther AI eval-harness")**
> A standardized framework and software library for evaluating language models on a wide range of benchmarks.

**[Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)**
> A standardized framework for few-shot evaluation of language models across a diverse set of benchmarks.

**[Fairness Beyond Performance: Revealing Reliability Disparities Across Groups in LegalNLP](https://aclanthology.org/2025.acl-long.1189.pdf) (as "Open LLM Leaderboard Harness")**
> A standardized framework and software tool used to provide a consistent methodology for evaluating the performance of large language models.

**[𝛿-Stance: A Large-Scale Real World Dataset of Stances in Legal Argumentation](https://aclanthology.org/2025.acl-long.1518.pdf) (as "HuggingFace Open LLM harness")**
> Standard evaluation suite for assessing foundational language understanding and reasoning abilities of LLMs using a collection of short-text benchmarks such as MMLU, Winogrande, and Hellaswag.

**[SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bbf38332580c1bed99fa99bc9ee53229-Paper-Conference.pdf) (as "EleutherAI evaluation harness")**
> A software framework for standardized evaluation of large language models across a wide range of benchmarks.

**[Detecting Legal Citations inUnitedKingdom Court Judgments](https://aclanthology.org/2025.emnlp-main.1362.pdf) (as "Harness framework")**
> The lm-eval-harness evaluation framework used to run benchmark evaluations under default settings.

**[Leveraging Text-to-Text Transformers as Classifier Chain for Few-Shot Multi-Label Classification](https://aclanthology.org/2025.emnlp-main.1369.pdf) (as "eleuther-AI evaluation harness")**
> Standardized framework for zero-shot evaluation of LLMs across a wide range of benchmarks, used here to ensure consistent scoring across multilingual tasks.

**[Add-One-In: Incremental Sample Selection for Large Language Models via a Choice-Based Greedy Paradigm](https://aclanthology.org/2025.emnlp-main.271.pdf) (as "lm eval framework")**
> The lm-eval framework, a standardized evaluation suite used to run benchmark tasks such as PIQA, ARC, HellaSwag, and WinoGrande.

**[RECALL:REpresentation-aligned Catastrophic-forgettingALLeviation via Hierarchical Model Merging](https://aclanthology.org/2025.emnlp-main.830.pdf) (as "Eleuther LM eval harness")**
> The Eleuther LM Eval Harness, a standardized evaluation framework used to run benchmark tasks in the same setting for models not on the leaderboard.

**[2025.emnlp-main.1170.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1170.checklist.pdf) (as "eleuther AI eval harness")**
> Evaluation framework developed by EleutherAI for standardized assessment of language models across a variety of benchmarks and tasks.

## Relationships

### LLM Evaluation Harness →
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  - [SliceGPT: Compress Large Language Models by Deleting Rows and Columns](https://proceedings.iclr.cc/paper_files/paper/2024/file/316648eb8b4ffb6010f531b07848c300-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [PICLe: Pseudo-annotations for In-Context Learning in Low-Resource Named Entity Detection](https://aclanthology.org/2025.naacl-long.519.pdf)
- **MATH** (measurements) — *measured_by*
  - [PICLe: Pseudo-annotations for In-Context Learning in Low-Resource Named Entity Detection](https://aclanthology.org/2025.naacl-long.519.pdf)

### → LLM Evaluation Harness
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  > zero-shot tasks implemented in Language Model Evaluation Harness (18)
  - [A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > “for several other zero-shot tasks, we use the open-source tool lm-evaluation-harness (version 0.4.4) (Gao et al., 2024) for assessment.”
  - [Test-Time Training on Nearest Neighbors for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f02f1185b97518ab5bd7ebde466992d3-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > We evaluate the pretrained models on language model tasks and multiple-choice tasks from LM evaluation Harness (Gao et al., 2023). (Section 5.3)
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  > “Table 1 reports the zero-shot results on the LM Eval Harness benchmark (Gao et al., 2023).”
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
- **Zero-shot learning** (constructs) — *measured_by*
  - [MoDeGPT: Modular Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb7214d2fdfd84165b08539d59c92e07-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > “We use LM Evaluation Harness framework (Gao et al., 2024) to assess model performance on HellaSwag ... as well as ARC-Easy and ARC-Challenge”
  - [Domain2Vec: Vectorizing Datasets to Find the Optimal Data Mixture without Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bu/zhang25bu.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > we evaluate the impact of safety heads ablation on helpfulness. We use lm-eval (Gao et al., 2024) to assess model performance after ablating safety heads of Llama-2-7b-chat on zero-shot tasks... (Section 5.3)
  - [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  - [Discovering Sparsity Allocation for  Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > "including four reading comprehension tasks (ARC-e, ARC-c (Clark et al., 2018), OBQA (Mihaylov et al., 2018), and BoolQ (Clark et al., 2019))"
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Knowledge awareness** (constructs) — *measured_by*
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf)
- **Natural language inference** (behaviors tasks) — *measured_by*
  > All the tasks except for MT are classification tasks, where we use the lm-evaluation-harness (Gao et al., 2024) evaluation tool and report accuracy. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > it can be inferred through diverse abilities such as commonsense and problem-solving, with evaluation tools like Harness (Gao et al., 2024). (Section 2.1)
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Fairness through Difference Awareness: MeasuringDesiredGroup Discrimination inLLMs](https://aclanthology.org/2025.acl-long.342.pdf)

### Associated with
- **MMLU** (measurements)
  > Besides, we also employ another two tasks MMLU (Hendrycks et al., 2021), and BBH (Suzgun et al., 2022) from Harness to evaluate the problem-solving capabilities... (Section 4.1)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **PIQA** (measurements)
  > Therefore, we only test on tasks (ARC-easy, Hellaswag, PIQA, SciQ, LAMBADA) in lm-evaluation-harness. (Section 4.1)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **WinoGrande** (measurements)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **HellaSwag** (measurements)
  > We evaluate LLMs on these benchmarks using the LM-Evaluation-Harness framework (Gao et al., 2024), and all evaluations are conducted in a zero-shot setting. (Section 6)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **BoolQ** (measurements)
  > We utilize the LM Eval Harness (Gao et al., 2023) for standardized performance evaluation. (Section 4.1)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **SciQ** (measurements)
  > Therefore, we only test on tasks (ARC-easy, Hellaswag, PIQA, SciQ, LAMBADA) in lm-evaluation-harness. (Section 4.1)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **ARC-Easy** (measurements)
  > We utilize the LM Eval Harness (Gao et al., 2023) for standardized performance evaluation. (Section 4.1)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **ARC-Challenge** (measurements)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **LAMBADA** (measurements)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **WikiText-2** (measurements)
  > We use lm-evaluation-harness to report results on Wikitext2 (Merity et al., 2016), ARC (challenge) (Clark et al., 2018), BoolQ (Clark et al., 2019), CommonSenseQA (Talmor et al., 2019), Winogrande (Sakaguchi et al., 2019), MMLU (Hendrycks et al., 2021), and BigBench-Hard (Suzgun et al., 2022).
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **ARC** (measurements)
  > We evaluate LLMs on these benchmarks using the LM-Evaluation-Harness framework (Gao et al., 2024), and all evaluations are conducted in a zero-shot setting. (Section 6)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **BBH** (measurements)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **GSM8k** (measurements)
  - [Training-Free Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)
- **CommonsenseQA** (measurements)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **LogiQA2** (measurements)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
