# Complex reasoning
**Type:** Behavior  
**Referenced in:** 93 papers  
**Also known as:** Multi-hop reasoning, Two-hop relational question answering, Multi-hop tracing, Subtask execution, Composite task solving, Multi-step inference, Sequential inference, Iterative reasoning, Multi-step reasoning, Multi-turn reasoning, Multi-step problem solving, Complex reasoning task performance  

## State of the Field

Across the provided literature, complex reasoning is predominantly characterized as an observable behavior involving a multi-step, sequential, or iterative process. The most common framing is "multi-hop reasoning," defined as inferring an answer by "chaining together multiple intermediate facts or relations across more than one step." Other definitions describe it as "multi-step inference," which requires deriving intermediate conclusions, or as "composite task solving," which involves the sequential execution of subtasks. A smaller set of papers defines it as an interactive process of refining answers through follow-up questions or reprocessing inputs. This behavior is operationalized and measured through performance on a wide array of benchmarks, with HotpotQA, MuSiQue, GSM8k, 2WikiMultihopQA, BBH, and MATH appearing as frequently used evaluation instruments. Complex reasoning is often studied alongside mathematical reasoning, question answering, and chain-of-thought reasoning. Some papers also report that behaviors such as planning, tool use, and self-correction can enable or cause complex reasoning.

## Sources

**[LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf) (as "Multi-hop reasoning")**
> Inferring an answer by chaining together multiple intermediate facts or relations across more than one step.

**[SEAL: Structure and Element Aware Learning Improves Long Structured Document Retrieval](https://aclanthology.org/2025.emnlp-main.430.pdf) (as "Multi-hop tracing")**
> The task of following a chain of reasoning or references across multiple steps within a text to answer a question.

**[DocReRank: Single-Page Hard Negative Query Generation for Training Multi-ModalRAGRerankers](https://aclanthology.org/2025.emnlp-main.437.pdf) (as "Two-hop relational question answering")**
> The task of answering a question that requires composing two distinct relational facts from a provided context to find the correct entity.

**[Understanding Subword Compositionality of Large Language Models](https://aclanthology.org/2025.emnlp-main.1147.pdf) (as "Composite task solving")**
> Producing correct outputs for tasks that require two sequential subtask applications, such as retrieving knowledge and then transforming it, without explicit intermediate steps in the input.

**[2025.emnlp-main.1147.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1147.checklist.pdf) (as "Subtask execution")**
> The observable generation or processing of intermediate steps in a reasoning task, such as solving a part of a multi-step problem.

**[Image Difference Captioning via Adversarial Preference Optimization](https://aclanthology.org/2025.emnlp-main.1714.pdf) (as "Sequential inference")**
> The observable process of generating a sequence of conclusions or actions based on a set of facts to solve a problem.

**[2025.emnlp-main.1714.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1714.checklist.pdf) (as "Multi-step inference")**
> Producing an output that depends on correctly deriving intermediate conclusions from a chain of premises, where each step relies on the previous one.

**[RESF: Regularized-Entropy-Sensitive Fingerprinting for Black-Box Tamper Detection of Large Language Models](https://aclanthology.org/2025.emnlp-main.248.pdf) (as "Iterative reasoning")**
> Generating follow-up explanations or justifications for an initial answer by reprocessing the original question augmented with the prior response and a prompting prefix.

**[Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf) (as "Multi-step reasoning")**
> Engaging in iterative, step-by-step reasoning to refine answers by decomposing queries, generating follow-up questions, and progressively improving response quality.

**[MAVL: A Multilingual Audio-Video Lyrics Dataset for Animated Song Translation](https://aclanthology.org/2025.emnlp-main.690.pdf) (as "Multi-turn reasoning")**
> Engaging in a sequential reasoning process where the model generates partial outputs across multiple turns, each conditioned on prior truncated responses and intervention prompts.

**[Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)**
> Answering multimodal questions that require higher-level inference beyond simple recognition or description.

**[AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark](https://aclanthology.org/2025.acl-long.983.pdf) (as "Multi-step problem solving")**
> The observable task of solving a complex mathematical problem that requires integrating multiple knowledge concepts in a sequential reasoning process.

**[Personality Alignment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/25203d1cc8c58381eab578f4fcf9c4f8-Paper-Conference.pdf) (as "Complex reasoning task performance")**
> The observable behavior of solving structured problems that require multi-step logical, mathematical, or commonsense reasoning, as measured by performance on specific benchmarks.

## Relationships

### Complex reasoning →
- **HotpotQA** (measurements) — *measured_by*
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)
- **MuSiQue** (measurements) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [ExtendingLLMContext Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.29.pdf)
- **2WikiMultihopQA** (measurements) — *measured_by*
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
- **WebQSP** (measurements) — *measured_by*
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  > Finally, we select four text-only benchmarks to evaluate text-based performance: ...BBH for complex reasoning (Suzgun et al., 2023)... (Section 4.1)
  - [Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf)
- **MATH** (measurements) — *measured_by*
  - [Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf)
- **RULER** (measurements) — *measured_by*
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **GrailQA** (measurements) — *measured_by*
  - [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf)
- **MQUAKE** (measurements) — *measured_by*
  - [From Capabilities to Performance: Evaluating Key Functional Properties ofLLMArchitectures in Penetration Testing](https://aclanthology.org/2025.emnlp-main.803.pdf)
- **LLaVA-Bench** (measurements) — *measured_by*
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  > Additionally, we evaluate generative performance on complex reasoning tasks, such as GSM8K (Cobbe et al., 2021) with 5-shot prompting and MMLU-Pro Engineering/Law (Wang et al., 2024a) with zero-shot chain-of-thought.
  - [Lexico: Extreme KV Cache Compression via Sparse Coding over Universal Dictionaries](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25ae/kim25ae.pdf)
- **CWQ** (measurements) — *measured_by*
  - [Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf)
- **TACT** (measurements) — *measured_by*
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **CLUTRR** (measurements) — *measured_by*
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **Omni-MATH** (measurements) — *measured_by*
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
- **OBQA** (measurements) — *measured_by*
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
- **CLEVR** (measurements) — *measured_by*
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.192.pdf)
- **Claim verification** (behaviors tasks) — *causes*
  - [Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models](https://aclanthology.org/2025.naacl-long.268.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [pFedGPT: Hierarchically OptimizingLoRAAggregation Weights for Personalized FederatedGPTModels](https://aclanthology.org/2025.emnlp-main.240.pdf)
- **SQA** (measurements) — *measured_by*
  - [Instance-Selection-Inspired Undersampling Strategies for Bias Reduction in Small and Large Language Models for Binary Text Classification](https://aclanthology.org/2025.acl-long.459.pdf)
- **FOLIO** (measurements) — *measured_by*
  - [Morpheme Induction for Emergent Language](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **MultiHopRAG** (measurements) — *measured_by*
  - [MadaKV: Adaptive Modality-PerceptionKVCache Eviction for Efficient Multimodal Long-Context Inference](https://aclanthology.org/2025.acl-long.653.pdf)
- **ComplexWebQuestions** (measurements) — *measured_by*
  - [Beyond One-Size-Fits-All: Tailored Benchmarks for Efficient Evaluation](https://aclanthology.org/2025.acl-long.760.pdf)
- **WebQuestions** (measurements) — *measured_by*
  - [Beyond One-Size-Fits-All: Tailored Benchmarks for Efficient Evaluation](https://aclanthology.org/2025.acl-long.760.pdf)
- **Code navigation** (behaviors tasks) — *causes*
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)
- **Iterative refinement** (behaviors tasks) — *causes*
  - [Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wan25g/wan25g.pdf)
- **LLaVA-Bench-in-the-Wild** (measurements) — *measured_by*
  > LLaVA-Bench-in-the-Wild (Liu et al., 2024), which examines the helpfulness of VLMs in aspects like instruction following and complex reasoning (Section 5.2)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
- **GPQA** (measurements) — *measured_by*
  - [Resource-Rational Noisy-Channel Language Processing: Testing the Effect of Algorithmic Constraints on Inferences](https://aclanthology.org/2025.emnlp-main.1208.pdf)
- **ProofWriter** (measurements) — *measured_by*
  - [Morpheme Induction for Emergent Language](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **GPQA-Diamond** (measurements) — *measured_by*
  - [Morpheme Induction for Emergent Language](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **HybridQA** (measurements) — *measured_by*
  - [Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions](https://aclanthology.org/2025.emnlp-main.710.pdf)
- **AndroidWorld** (measurements) — *measured_by*
  - [Phi: Preference Hijacking in Multi-modal Large Language Models at Inference Time](https://aclanthology.org/2025.emnlp-main.902.pdf)
- **MBPP** (measurements) — *measured_by*
  - [pFedGPT: Hierarchically OptimizingLoRAAggregation Weights for Personalized FederatedGPTModels](https://aclanthology.org/2025.emnlp-main.240.pdf)
- **ViDoSeek** (measurements) — *measured_by*
  - [ComplexTempQA: A 100m Dataset for Complex Temporal Question Answering](https://aclanthology.org/2025.emnlp-main.464.pdf)
- **LongMemEval** (measurements) — *measured_by*
  - [Easy asPIE? Identifying Multi-Word Expressions withLLMs](https://aclanthology.org/2025.emnlp-main.1214.pdf)

### → Complex reasoning
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf)
- **Abstract reasoning** (constructs) — *causes*
  - [THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS](https://proceedings.iclr.cc/paper_files/paper/2024/file/2dae7d1ccf1edf76f8ce7c282bdf4730-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *causes*
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Planning** (constructs) — *causes*
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.192.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Adaptive Self-improvement LLM Agentic System for ML Library Development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25at/zhang25at.pdf)
- **Multi-step planning** (behaviors tasks) — *causes*
  > Our detailed analysis demonstrates how planning trajectories improves complex reasoning capabilities, showing that PLAN-TUNING is an effective strategy for improving task-specific performance of smaller LLMs. (Abstract)
  - [zFLoRA: Zero-Latency Fused Low-Rank Adapters](https://aclanthology.org/2025.emnlp-main.1087.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  > Complex reasoning has been an intriguing ability of large language models (LLMs), with application in for example mathematical problem-solving (Section 1).
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf)
- **Task decomposition** (behaviors tasks)
  - [Towards Robust Multi-Modal Reasoning via Model Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c78ae0c1140902bf3a430b1725bcc4e-Paper-Conference.pdf)
- **Question answering** (behaviors tasks)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf)
- **Implicit reasoning** (constructs)
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
- **Table reasoning** (constructs)
  - [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Hallucination** (behaviors tasks)
  - [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf)
- **Contextual understanding** (constructs)
  - [Towards Robust Multi-Modal Reasoning via Model Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c78ae0c1140902bf3a430b1725bcc4e-Paper-Conference.pdf)
- **Multi-hop question answering** (behaviors tasks)
  - [Delving into Multilingual Ethical Bias: TheMSQADwith Statistical Hypothesis Tests for Large Language Models](https://aclanthology.org/2025.acl-long.16.pdf)
- **Critique** (behaviors tasks)
  - [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
- **Tool use** (behaviors tasks)
  - [TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Claim verification** (behaviors tasks)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Planning** (constructs)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
- **Portability** (constructs)
  - [From Capabilities to Performance: Evaluating Key Functional Properties ofLLMArchitectures in Penetration Testing](https://aclanthology.org/2025.emnlp-main.803.pdf)
- **Knowledge transfer** (constructs)
  - [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf)
- **Textual reasoning** (behaviors tasks)
  - [JiuZhang3.0: Efficiently Improving Mathematical Reasoning by Training Small Data Synthesis Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0356216f73660e15670510f5e42b5fa6-Paper-Conference.pdf)
- **Compositional reasoning** (constructs)
  - [Limits of Deep Learning: Sequence Modeling through the Lens of Complexity Theory](https://proceedings.iclr.cc/paper_files/paper/2025/file/62868cc2fc1eb5cdf321d05b4b88510c-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  - [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf)
- **Long-context reasoning** (constructs)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks)
  - [Pay More Attention to Images: Numerous Images-Oriented Multimodal Summarization](https://aclanthology.org/2025.naacl-long.475.pdf)
- **Sequential reasoning** (constructs)
  - [Exploring Safety-Utility Trade-Offs in Personalized Language Models](https://aclanthology.org/2025.naacl-long.566.pdf)
- **Entity disambiguation** (behaviors tasks)
  - [Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models](https://aclanthology.org/2025.naacl-long.268.pdf)
- **Long-context understanding** (constructs)
  - [LLM-Guided Co-Training for Text Classification](https://aclanthology.org/2025.emnlp-main.1584.pdf)
- **Long-context processing** (constructs)
  - [SpeculatingLLMs’Chinese Training Data Pollution from Their Tokens](https://aclanthology.org/2025.emnlp-main.1328.pdf)
- **Associative reasoning** (constructs)
  - [Static Word Embeddings for Sentence Semantic Representation](https://aclanthology.org/2025.emnlp-main.317.pdf)
