# Multiple-choice question answering
**Type:** Behavior  
**Referenced in:** 294 papers  
**Also known as:** Multi-choice question answering, Multiple-choice answering, Yes/no question answering, Binary preference selection, Single-choice question answering, Multiple-selection question answering, Binary question answering, True/False question answering, True/false question answering, Multiple Choice Question  

## State of the Field

Across the surveyed literature, multiple-choice question answering is predominantly defined as the observable task of selecting one or more correct answers from a discrete set of options in response to a question. The most common operationalization involves presenting a model with a question and several candidate answers, often labeled with letters such as "A", "B", "C", and "D", and requiring it to output the identifier for the correct choice. While the prevailing format requires selecting a single correct option, some work describes "multiple-selection" variants, and a recurring sub-type is binary question answering, which includes "Yes/No" and "True/False" formats. This behavior is widely used as an evaluation method, with performance typically measured by accuracy or exact match, though some approaches calculate the likelihood of each option. It is operationalized through numerous benchmarks—including MMLU, TruthfulQA, ARC, and StrategyQA—to assess a wide array of model capabilities. These capabilities range from commonsense reasoning and factual knowledge to specialized expertise in domains like science, medicine, and finance. The task is applied in both text-only and multimodal settings that incorporate visual inputs. As one study notes, it is viewed as a "simple but good proxy to evaluate the abilities of LLMs" ("Towards Understanding Factual Knowledge of Large Language Models").

## Sources

**[Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)**
> The observable task of selecting the correct answer from a set of discrete options (e.g., A/B/C/D) in response to a given question.

**[Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Multi-choice question answering")**
> The task of selecting the single correct option from a set of four choices in response to a question about a given grid, code, or programming concept.

**[IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf) (as "Multiple-choice answering")**
> Selecting the correct option from a set of choices based on provided context and question.

**[SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25n/chen25n.pdf) (as "Yes/no question answering")**
> Responding to a question with either 'Yes' or 'No' based on whether a provided statement is correct.

**[Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf) (as "Binary preference selection")**
> The task of comparing a pair of model-generated responses and choosing the one that is better according to some criteria.

**[Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLMCollaboration](https://aclanthology.org/2025.emnlp-main.1222.pdf) (as "Single-choice question answering")**
> The observable task of selecting the single correct option from a list of choices in response to a question, often within a structured format.

**[PerspectiveMod: A Perspectivist Resource for Deliberative Moderation](https://aclanthology.org/2025.emnlp-main.1734.pdf) (as "Multiple-selection question answering")**
> Selecting all correct responses from a set of options for each sub-question in a multi-step instruction chain, where distractors increase complexity and test robustness.

**[Regularized Best-of-N Sampling with MinimumBayes Risk Objective for Language Model Alignment](https://aclanthology.org/2025.naacl-long.473.pdf) (as "Binary question answering")**
> Generating 'Yes' or 'No' answers to comprehension questions about sentence meaning, particularly after garden path disambiguation.

**[Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf) (as "True/False question answering")**
> The task of determining whether a given statement is true or false based on provided context.

**[Unveiling the Tapestry of Consistency in Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f094ba0f5ce1720466342f78031bdb-Paper-Conference.pdf) (as "True/false question answering")**
> A specific question answering task where the model must respond with 'yes' or 'no' or an equivalent binary choice.

**[CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25t/wang25t.pdf) (as "Multiple Choice Question")**
> A benchmark task in which the model selects the correct API invocation from four candidate invocations with one correct option and three distractors.

## Relationships

### Multiple-choice question answering →
- **MMLU** (measurements) — *measured_by*
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [Answer, Assemble, Ace: Understanding How LMs Answer Multiple Choice Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c248154176c08147e82c0b30961604f7-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  - [Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/688006b3d1df8be5bb2a2a31a407180c-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **MedQA** (measurements) — *measured_by*
  - [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.246.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **MedMCQA** (measurements) — *measured_by*
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  > Given that most commonsense reasoning datasets are structured in a multiple-choice question (MCQ) format (Talmor et al., 2019; Mihaylov et al., 2018; Geva et al., 2021), we designed a three-stage process inspired by human problem-solving strategies. (Section 1)
  - [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.503.pdf)
- **RACE** (measurements) — *measured_by*
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  - [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf)
- **OBQA** (measurements) — *measured_by*
  - [P](https://aclanthology.org/2025.acl-long.722.pdf)
- **COPA** (measurements) — *measured_by*
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **StoryCloze** (measurements) — *measured_by*
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Belebele** (measurements) — *measured_by*
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **MMMLU** (measurements) — *measured_by*
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  - [TheUD-NewsCrawl Treebank: Reflections and Challenges from a Large-scaleTagalog Syntactic Annotation Project](https://aclanthology.org/2025.acl-long.358.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  - [Language Models Predict Empathy Gaps Between Social In-groups and Out-groups](https://aclanthology.org/2025.naacl-long.612.pdf)
- **WMDP** (measurements) — *measured_by*
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
- **JAMA Clinical Challenge** (measurements) — *measured_by*
  - [Ihquin tlahtouah in Tetelahtzincocah: An annotated, multi-purpose audio and text corpus of Western SierraPueblaNahuatl](https://aclanthology.org/2025.naacl-long.182.pdf)
- **Medbullets** (measurements) — *measured_by*
  - [Ihquin tlahtouah in Tetelahtzincocah: An annotated, multi-purpose audio and text corpus of Western SierraPueblaNahuatl](https://aclanthology.org/2025.naacl-long.182.pdf)
- **OLMES** (measurements) — *measured_by*
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
- **SinhalaMMLU** (measurements) — *measured_by*
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1673.pdf)
- **EDUADAPT** (measurements) — *measured_by*
  - [CodeSSM: Towards State Space Models for Code Understanding](https://aclanthology.org/2025.emnlp-main.1736.pdf)

### → Multiple-choice question answering
- **MMLU** (measurements) — *measured_by*
  - [You Only Read Once (YORO): Learning to Internalize Database Knowledge for Text-to-SQL](https://aclanthology.org/2025.naacl-long.95.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [AlgoPuzzleVQA: Diagnosing Multimodal Reasoning Challenges of Language Models with Algorithmic Multimodal Puzzles](https://aclanthology.org/2025.naacl-long.487.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)

### Associated with
- **Knowledge forgetting** (constructs)
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs)
  - [Reinforcement Learning for Large Language Models via Group Preference Reward Shaping](https://aclanthology.org/2025.emnlp-main.1086.pdf)
- **MMLU** (measurements)
  - [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)
- **Referring expression understanding** (behaviors tasks)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instruction following** (constructs)
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **Selection bias** (constructs)
  - [NESTFUL: A Benchmark for EvaluatingLLMs on Nested Sequences ofAPICalls](https://aclanthology.org/2025.emnlp-main.1703.pdf)
- **Emergent abilities** (constructs)
  - [U-shaped and Inverted-U Scaling behind Emergent Abilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f696200311b445af686c3ebd87ade1d7-Paper-Conference.pdf)
- **CommonsenseQA** (measurements)
  - [Taming Overconfidence in LLMs: Reward Calibration in RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/29fb6e1456b3d8b57ede5c45aa2c6537-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks)
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)
- **Decision-making** (constructs)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
- **Knowledge acquisition** (constructs)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
