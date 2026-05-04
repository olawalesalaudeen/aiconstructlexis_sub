# Logical reasoning
**Type:** Construct  
**Referenced in:** 242 papers  
**Also known as:** Logical Thinking, Logical deduction, Logic inference, Logical capabilities, Logic reasoning, Logic, Syllogistic reasoning, Logical awareness, Deduction, Deductive reasoning, Deductive generalization, Logicality, Reasoning coherence, Reasoning logic, Coherence & reasoning, First-order logic reasoning, Logical inference, Reasoning comprehensiveness, Multi-step deduction, Logical step generation, Multi-hop deduction, Propositional inference, Logical problem solving, Deductive question answering, Multi-domain deductive reasoning, Non-rulebreaker acceptance, Boolean expression evaluation, Conclusion generation, Logical puzzle solving, Disjunctive reasoning  

## State of the Field

Across the provided literature, logical reasoning is most commonly defined as the ability to deduce conclusions from a set of premises using formal rules of logic. A smaller set of papers offers more specific framings, such as the capacity to recognize abstract patterns beyond co-occurrence, maintain internal consistency, or perform particular types of inference like syllogistic or first-order logic reasoning. The construct is operationalized and measured through a wide array of benchmarks, with FOLIO, LogiQA, ProofWriter, and ReClor appearing as frequently used instruments for evaluation. Specific observable behaviors, such as multi-step deduction and logical puzzle solving, are also used to assess this ability; one paper highlights a particular failure of logical deduction it terms the "Reversal Curse," where models trained on “A is B” fail to infer “B is A” ("The Reversal Curse: LLMs trained on ‘A is B’ fail to learn ‘B is A’"). Logical reasoning is frequently studied alongside mathematical reasoning, with some sources noting that math tasks challenge logical deduction. It is also associated with commonsense knowledge, inductive reasoning, and abductive reasoning. Some papers report that this ability influences downstream tasks like decision-making, while prompting techniques like Chain-of-Thought are frequently cited as a method to enhance it. Throughout the sources, logical reasoning is often presented as a challenging area for language models, with many studies aiming to evaluate or improve what are described as "inherent shortcomings" in this capacity.

## Sources

**[AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)**
> The ability to deduce conclusions from a set of premises using formal rules of logic.

**[The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://proceedings.iclr.cc/paper_files/paper/2024/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf) (as "Logical deduction")**
> The latent ability to infer logically equivalent statements from given premises, such as deriving 'B is A' from 'A is B' based on the symmetry of identity.

**[FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf) (as "Logical Thinking")**
> The latent ability to apply reasoning, critical thinking, and deductive skills to process and respond to instructions in a logically sound, robust, and efficient manner.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Logic inference")**
> The ability to reason from legal facts and rules to derive correct conclusions through deductive or multi-step inference.

**[Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf) (as "Logical capabilities")**
> The model's capacity for logical reasoning and related problem-solving reflected in benchmark performance.

**[From Unstructured Data to In-Context Learning: Exploring What Tasks Can Be Learned and When](https://proceedings.neurips.cc/paper_files/paper/2024/file/1da38b872e19f1f4a3c2846720e8f64a-Paper-Conference.pdf) (as "Logic reasoning")**
> The capacity to recognize abstract token patterns that do not rely on simple co-occurrence and to generalize them to novel tokens or sequences.

**[SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf) (as "Logic")**
> The ability of a model to reason soundly and produce text that is internally consistent and follows logical principles.

**[ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf) (as "Syllogistic reasoning")**
> A form of logical reasoning that joins two or more premises to arrive at a conclusion.

**[Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf) (as "Logical awareness")**
> The model's latent awareness of logical relationships between time series data and language prompts, ensuring semantic coherence.

**[ADIFF: Explaining audio difference using natural language](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e337afbbb9fc2de993b88df0db6161e-Paper-Conference.pdf) (as "Deductive reasoning")**
> The ability to draw logical conclusions by interpreting and comparing features from provided inputs.

**[Strategist: Self-improvement of LLM Decision Making via Bi-Level Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/439dbffb7a044ee4b636babff57d4994-Paper-Conference.pdf) (as "Deduction")**
> The ability to infer hidden information, such as other players' identities or roles, from observable actions and communication.

**[Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf) (as "Deductive generalization")**
> The tendency for reasoning learned from broader causal relations to transfer to a more specific relation that was not directly demonstrated.

**[FoldMoE: Efficient Long SequenceMoETraining via Attention-MoEPipelining](https://aclanthology.org/2025.acl-long.187.pdf) (as "Logicality")**
> The extent to which a model's response is internally consistent and free from logical errors or contradictions.

**[JI2S: JointInfluence‐Aware Instruction Data Selection for EfficientFine‐Tuning](https://aclanthology.org/2025.emnlp-main.27.pdf) (as "Reasoning coherence")**
> The degree to which a model's reasoning process maintains logical consistency and structural integrity across long-form outputs, especially when generating spoken responses.

**[Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.915.pdf) (as "Reasoning logic")**
> The degree to which the model produces reliable, coherent, and logically structured reasoning rather than inconsistent or incoherent chains.

**[REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf) (as "Coherence & reasoning")**
> The latent ability of a model to generate logically consistent, well-structured responses that demonstrate sound reasoning across multiple steps or ideas.

**[Recontextualizing Revitalization: A Mixed Media Approach to Reviving the Nüshu Language](https://aclanthology.org/2025.emnlp-main.628.pdf) (as "First-order logic reasoning")**
> The ability to perform logical deductions and manipulations within the formal system of first-order logic, involving quantifiers, predicates, and logical connectives.

**[What are Foundation Models Cooking in the Post-Soviet World?](https://aclanthology.org/2025.emnlp-main.1045.pdf) (as "Logical inference")**
> The latent ability of LLMs to derive conclusions from premises through inductive, abductive, or deductive reasoning processes, reflecting underlying cognitive-style reasoning mechanisms.

**[MovieCORE:COgnitiveREasoning in Movies](https://aclanthology.org/2025.emnlp-main.67.pdf) (as "Reasoning comprehensiveness")**
> The latent ability of a model to include all relevant, potentially contradictory information from a document in its reasoning process, reflecting the breadth and thoroughness of its analysis.

**[Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf) (as "Multi-step deduction")**
> The observable task of generating a sequence of logical steps to derive a given hypothesis from a set of provided facts.

**[Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf) (as "Logical step generation")**
> The observable task of producing intermediate reasoning steps that connect facts to a conclusion.

**[Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf) (as "Multi-hop deduction")**
> The observable task of solving a problem that requires chaining together multiple steps of inference or information retrieval from a given context.

**[Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e2dd37e10bb18ed9d6d488f63094631-Paper-Conference.pdf) (as "Propositional inference")**
> Deriving all propositions that follow from a set of rules and known facts.

**[Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf) (as "Logical problem solving")**
> The observable task of answering a question or solving a problem that requires logical deduction.

**[LLM-based Typed Hyperresolution for Commonsense Reasoning with Knowledge Bases](https://proceedings.iclr.cc/paper_files/paper/2025/file/67496dfa96afddab795530cc7c69b57a-Paper-Conference.pdf) (as "Multi-domain deductive reasoning")**
> Deriving conclusions from axioms and facts across multiple domains such as biological entities, foods, and vehicles.

**[Improving Reasoning Performance in Large Language Models via Representation Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e73c39cc428c7d264d9820319f31e79-Paper-Conference.pdf) (as "Deductive question answering")**
> Answering a question based on a provided passage of text, requiring logical deduction from the given facts.

**[The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf) (as "Boolean expression evaluation")**
> The task of computing the truth value of a given logical boolean expression.

**[RULEBREAKERS: Challenging LLMs at the Crossroads between Formal Logic and Human-like Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25a/chan25a.pdf) (as "Conclusion generation")**
> Producing a conclusion from given premises rather than only deciding whether a proposed conclusion should be accepted.

**[RULEBREAKERS: Challenging LLMs at the Crossroads between Formal Logic and Human-like Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25a/chan25a.pdf) (as "Non-rulebreaker acceptance")**
> The observable behavior of accepting a conclusion that is both logically valid and factually consistent with the premises.

**[Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.727.pdf) (as "Logical puzzle solving")**
> The act of determining the identities of characters in Knights & Knaves logic puzzles based on their statements.

**[SelfRACG: EnablingLLMs to Self-Express and Retrieve for Code Generation](https://aclanthology.org/2025.emnlp-main.542.pdf) (as "Disjunctive reasoning")**
> Handling questions where the correct answer depends on an 'or' relation, including cases where only one of multiple clauses needs to be true.

## Relationships

### Logical reasoning →
- **FOLIO** (measurements) — *measured_by*
  > To evaluate the efficacy of our approach, we use GSM8K (Cobbe et al., 2021), Big-Bench-Hard (BBH) (Suzgun et al., 2022), and FOLIO (Han et al., 2022) benchmark datasets for diverse reasoning tasks in mathematics, commonsense, and logical reasoning. (Section 5.1)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **LogiQA** (measurements) — *measured_by*
  > We investigate two open-source LLMs Mistral 7B instruct (Jiang et al., 2023) and LLaMA3 8B instruct (Touvron et al., 2023) and Qwen 2-7B-Instruct (Bai et al., 2023) on two logical benchmarks (LogiQA, BBH) and two mathematics benchmarks (GSM8K and MATH). (Section 4.1)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **PrOntoQA** (measurements) — *measured_by*
  > For logical reasoning, we evaluate the PrOntoQA (Saparov & He, 2022) dataset for logical deduction in a 5-shot setting (Section 4).
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
- **ProofWriter** (measurements) — *measured_by*
  > We evaluate CLOVER on seven logical reasoning tasks: AR-LSAT (Zhong et al., 2022), ZebraLogic (Lin et al., 2025), Logic grid puzzle (Puzzle), Symbol interpretation (Symbol), and Logical deduction (Deduction) from the BigBench collaborative benchmark (Srivastava et al., 2022), FOLIO (Han et al., 2022), and ProofWriter (Tafjord et al., 2021). (Section 4.1)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **ReClor** (measurements) — *measured_by*
  > In the experiment, we employ five logical reasoning datasets: (1) ReClor (Yu et al., 2020), which is collected from standardized test logical reasoning questions, including the Law School Admission Test (LSAT) and the Graduate Management Admission Test (GMAT) (Section 4.1).
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
- **MMStar** (measurements) — *measured_by*
  > The evaluation dataset is MMStar. (Figure 1 Caption)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **RuleTaker** (measurements) — *measured_by*
  > The RuleTaker (Clark et al., 2021) and ProofWriter (Tafjord et al., 2021) datasets proposed a modern approach to evaluating logical reasoning
  - [Self-calibration for Language Model Quantization and Pruning](https://aclanthology.org/2025.naacl-long.510.pdf)
- **ZebraLogic** (measurements) — *measured_by*
  > we introduce ZebraLogic, a comprehensive evaluation framework for assessing LLM reasoning performance on logic grid puzzles derived from constraint satisfaction problems (CSPs). (Abstract)
  - [English-based acoustic models perform well in the forced alignment of twoEnglish-based Pacific Creoles](https://aclanthology.org/2025.acl-long.1506.pdf)
- **Information extraction** (behaviors tasks) — *causes*
  - [A Decision-Language Model (DLM) for Dynamic Restless Multi-Armed Bandit Tasks in Public Health](https://proceedings.neurips.cc/paper_files/paper/2024/file/074f42212be2c8ee651db00f17965ec4-Paper-Conference.pdf)
- **LogiQA2** (measurements) — *measured_by*
  - [Self-playing Adversarial Language Game Enhances LLM Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4be7e9867ef163563f4a5e90cec478f-Paper-Conference.pdf)
- **LogicNLI** (measurements) — *measured_by*
  > We evaluate our framework on five multi-step logical reasoning datasets: RobustLR (Sanyal et al., 2022), PrOntoQA-OOD (Saparov et al., 2023), ProofWriter (Tafjord et al., 2020), ParaRules (Clark et al., 2020), LogicNLI (Tian et al., 2021) (Section 4.1).
  - [MAPS: Motivation-Aware Personalized Search viaLLM-Driven Consultation Alignment](https://aclanthology.org/2025.acl-long.153.pdf)
- **MMLU** (measurements) — *measured_by*
  > MMLU (Hendrycks et al., 2021) provides a comprehensive set of logical reasoning assessments across diverse subjects and difficulties, utilizing multiple-option questions to measure general world knowledge and logical inference capabilities.
  - [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  > Reasoning: The model’s capacity for commonsense and logical reasoning is measured using Winogrande (Sakaguchi et al., 2021) and ARC (easy and challenge subsets) (Clark et al., 2018). (Section 4.1)
  - [MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs](https://aclanthology.org/2025.emnlp-main.718.pdf)
- **AgentBench** (measurements) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
- **Consistency** (constructs) — *causes*
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
- **bAbI** (measurements) — *measured_by*
  > bAbI comprises various reasoning tasks, one related to deductive reasoning of which there are 2, 000 examples. (Section 3.1)
  - [Improving Reasoning Performance in Large Language Models via Representation Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e73c39cc428c7d264d9820319f31e79-Paper-Conference.pdf)
- **CLUTRR** (measurements) — *measured_by*
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **Decision-making** (constructs) — *causes*
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  > These tasks assess the model performance on logical reasoning, language understanding, commonsense reasoning, and knowledge utilization. (Section 4.1)
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Flexibility** (constructs) — *causes*
  > The grounding knowledge and principled reasoning procedure enable R2-Guard to be effective, robust against jailbreak attacks, and flexible given new safety categories. (Abstract)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > Notably, Figure 8 shows significant gains in categories like MBPP (programming) and PIQA (physical commonsense reasoning), reflecting enhanced logical reasoning and problem-solving skills. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **Date Understanding** (measurements) — *measured_by*
  > Logical Reasoning: Date Understanding (bench authors, 2023). (Section 4)
  - [Substance Beats Style: Why Beginning Students Fail to Code withLLMs](https://aclanthology.org/2025.naacl-long.434.pdf)
- **Logical deduction** (measurements) — *measured_by*
  > We evaluate CLOVER on seven logical reasoning tasks: AR-LSAT (Zhong et al., 2022), ZebraLogic (Lin et al., 2025), Logic grid puzzle (Puzzle), Symbol interpretation (Symbol), and Logical deduction (Deduction) from the BigBench collaborative benchmark (Srivastava et al., 2022), FOLIO (Han et al., 2022), and ProofWriter (Tafjord et al., 2021). (Section 4.1)
  - [Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e592c571de69a43d7a870ea89c7e33a-Paper-Conference.pdf)
- **MMMU** (measurements) — *measured_by*
  > MMMU (Yue et al., 2024), which tests multimodal models on large-scale multidisciplinary tasks requiring advanced subject matter knowledge and reasoning skills. (Section 3.1)
  - [TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types](https://proceedings.iclr.cc/paper_files/paper/2025/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf)
- **ContextHub** (measurements) — *measured_by*
  > We use a new propositional logic benchmark Contexthub (Hua et al., 2024) for evaluation. (Section 4.5)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **MBPP** (measurements) — *measured_by*
  > Notably, Figure 8 shows significant gains in categories like MBPP (programming) and PIQA (physical commonsense reasoning), reflecting enhanced logical reasoning and problem-solving skills. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  > “The tasks are categorized into five domains: • Knowledge: CommonsenseQA ... BoolQ ...”
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **Word unscrambling** (behaviors tasks) — *measured_by*
  - [Beyond Surface Structure: A Causal Assessment of LLMs' Comprehension ability](https://proceedings.iclr.cc/paper_files/paper/2025/file/88139fdcc82fc597090620d77b023282-Paper-Conference.pdf)
- **e-SNLI** (measurements) — *measured_by*
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  > For logical reasoning, we evaluate the PrOntoQA (Saparov & He, 2022) dataset for logical deduction in a 5-shot setting and the GPQA (Rein et al., 2023) dataset for graduate-level multiple-choice questions in a 0-shot setting (Section 4).
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
- **Time series forecasting** (behaviors tasks) — *causes*
  > FSCA can be flexibly and repeatedly integrated into various layers of pre-trained LLMs to improve awareness of logic and structure, thereby enhancing performance.
  - [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf)
- **RACE** (measurements) — *measured_by*
  > This suggests that the state space architecture effectively enhances logical reasoning capabilities without compromising long-text processing efficiency. (Section 4.5)
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)
- **LogicBench** (measurements) — *measured_by*
  > Logic LogicBench (Parmar et al., 2024) comprises various logic questions in both binary classification and multiple-choice formats. We sample 100 binary and 100 multiple-choice questions, collecting 200 samples in total. (Section 2.1)
  - [Efficiently Identifying Watermarked Segments in Mixed-Source Texts](https://aclanthology.org/2025.acl-long.317.pdf)
- **Game of 24** (measurements) — *measured_by*
  > the performance comparison on the Game of 24 validates the effectiveness of the FoT in the mathematical and logical reasoning task. (Section 4.6)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)
- **Safety alignment** (constructs) — *causes*
  > To tackle these challenges, we propose SHIELDAGENT, the first guardrail agent designed to enforce explicit safety policy compliance for the action trajectory of other protected agents through logical reasoning. (Section 1)
  - [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ae/chen25ae.pdf)
- **TTT-Bench** (measurements) — *measured_by*
  > In this work, we introduce TTT-Bench, a new benchmark that is designed to evaluate basic strategic, spatial, and logical reasoning abilities in LRMs through a suite of four two-player Tic-Tac-Toe-style games that humans can effortlessly solve from a young age. (Abstract)
  - [MultiMatch: Multihead Consistency Regularization Matching for Semi-Supervised Text Classification](https://aclanthology.org/2025.emnlp-main.140.pdf)

### → Logical reasoning
- **In-context learning** (constructs) — *causes*
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
- **MR-Ben** (measurements) — *measured_by*
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **MuSR** (measurements) — *measured_by*
  > These datasets require the application of logical rules to reach the answer... (MuSR Murder Mysteries)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **Fine-grained perception** (constructs) — *causes*
  > This suggests that fusing raw image and text embeddings in a single transformer is beneficial for fine-grained perception and subsequently enhances image-based logical reasoning. (Section 4.3)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  > “LLMs frequently fail to solve discrete mathematics problems and often make logical missteps, highlighting significant challenges in mathematical reasoning and problem-solving for LLMs.”
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Abductive reasoning** (constructs)
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Natural language inference** (behaviors tasks)
  > “what is required is not the capability of logical reasoning ... However, understanding implicit toxic language needs inferences that draw on nonlogical, subjective social experiences, conventional knowledge, and contextual awareness. ... Such reasoning from context, intention, and signs is named ‘pragmatic inference’”
  - [Merger-as-a-Stealer: Stealing TargetedPIIfrom AlignedLLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.296.pdf)
- **Inductive reasoning** (constructs)
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Consistency** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Constrained text generation** (behaviors tasks)
  > We posit that one direction is incorporating logical and compositional challenges via constrained text generation.
  - [COLLIE: Systematic Construction of Constrained Text Generation Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/a77eadda332b6d4a9ae1e0e4024555f2-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  > “Another failure mode multi-branch reasoning, i.e. in keeping track of multiple reasoning traces that could lead to valid solutions.”
  - [Understanding Chain-of-Thought in LLMs through Information Theory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ton25a/ton25a.pdf)
- **In-context learning** (constructs)
  - [From Unstructured Data to In-Context Learning: Exploring What Tasks Can Be Learned and When](https://proceedings.neurips.cc/paper_files/paper/2024/file/1da38b872e19f1f4a3c2846720e8f64a-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [K-Level Reasoning: Establishing Higher Order Beliefs in Large Language Models for Strategic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf)
- **Natural language understanding** (constructs)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Data analysis** (behaviors tasks)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Code reasoning** (constructs)
  > Code reasoning encompasses a category of tasks that demonstrate logical reasoning through code
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
- **Pattern recognition** (constructs)
  - [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  > “Given the evidence and reasoning rules, LLM must decide if the queried clause is true, false, or unknown.”
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Knowledge manipulation** (constructs)
  > Knowledge manipulation is arguably a simplest form of logical reasoning. (Section 1)
  - [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf)
- **Abstract reasoning** (constructs)
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Tabular reasoning** (constructs)
  > Tabular reasoning presents an inherently challenging problem, requiring logical, mathematical, and textual reasoning over unstructured queries and structured tables
  - [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Long-context processing** (constructs)
  - [CAMIEval: EnhancingNLGEvaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.439.pdf)
- **Reasoning faithfulness** (constructs)
  - [Self-calibration for Language Model Quantization and Pruning](https://aclanthology.org/2025.naacl-long.510.pdf)
- **Multi-agent debate** (behaviors tasks)
  > Inspired by Du et al., we build multi-agent debate tasks on several mathematical or logical reasoning datasets. (Section 4.2.1)
  - [PRISM: Efficient Long-Range Reasoning With Short-ContextLLMs](https://aclanthology.org/2025.emnlp-main.518.pdf)
- **Embodied question answering** (behaviors tasks)
  > Evaluating the resulting EQA trajectories necessitates a nuanced assessment of the agent’s reasoning coherence, action appropriateness, and how well language is grounded within the environment. (Section 1)
  - [Parallel Continuous Chain-of-Thought with Jacobi Iteration](https://aclanthology.org/2025.emnlp-main.48.pdf)
- **Legal reasoning** (constructs)
  - [Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.915.pdf)
- **Reasoning rigor** (constructs)
  > Current LLM-based methods for logical reasoning still struggle to perform structured exploration while ensuring logical coherence and rigor in complex, multi-step reasoning tasks (Section 2.2).
  - [SOLAR: Towards Characterizing Subjectivity of Individuals through Modeling Value Conflicts and Trade-offs](https://aclanthology.org/2025.emnlp-main.1054.pdf)
