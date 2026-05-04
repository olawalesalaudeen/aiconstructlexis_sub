# MMLU
**Type:** Measurement  
**Referenced in:** 612 papers  
**Also known as:** MMLU auxiliary training set  

## State of the Field

Across the surveyed literature, MMLU (Massive Multitask Language Understanding) is consistently characterized as a large-scale, multitask benchmark composed of multiple-choice questions. It covers 57 diverse subjects, including STEM, humanities, and social sciences, with questions ranging in difficulty from elementary to professional levels. The benchmark is most frequently used to measure a model's `world knowledge` and `problem-solving ability`, with papers also widely using it to operationalize constructs like `reasoning`, `general capabilities`, and `language understanding`. Models are typically evaluated on their accuracy in a 5-shot setting, although zero-shot and other few-shot configurations are also common. Beyond these general assessments, a smaller set of studies uses MMLU to evaluate more specific behaviors such as `instruction following`, `knowledge retention` after fine-tuning, or to check for `catastrophic forgetting`. While its use is widespread, some work characterizes it as primarily testing `parametric knowledge` and factual recall, as noted in one paper that states it "largely depend[s] on recalling factual information learned during training" (Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks). MMLU is frequently situated within broader evaluation suites, often appearing alongside benchmarks like ARC, HellaSwag, and GSM8K as part of the Open LLM Leaderboard.

## Sources

**[AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf)**
> A massive multitask benchmark, fully named Massive Multitask Language Understanding, consisting of multiple-choice questions covering 57 diverse subjects to measure world knowledge and problem-solving ability.

**[Training on the Test Task Confounds Evaluation and Emergence](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab8c971c2ccd12bac0ab249f75e2c16d-Paper-Conference.pdf) (as "MMLU auxiliary training set")**
> The auxiliary training set accompanying the HF MMLU repository, used as task-specific data for fine-tuning before evaluation.

**[Streamlining Redundant Layers to Compress Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4b00a351b41358965613c118e87dc28c-Paper-Conference.pdf) (as "CMMLU")**
> A comprehensive benchmark for evaluating the knowledge and reasoning abilities of LLMs in a Chinese context.

## Relationships

### MMLU →
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [You Only Read Once (YORO): Learning to Internalize Database Knowledge for Text-to-SQL](https://aclanthology.org/2025.naacl-long.95.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We evaluate the impact of data contamination using a mix of seven different benchmarks: ARC-Easy (Clark et al., 2018), Social-I-QA (Sap et al., 2019), WinoGrande (Sakaguchi et al., 2021), PiQA (Bisk et al., 2020), BoolQ (Clark et al., 2019), MMLU (Hendrycks et al., 2021), and HellaSwag (Zellers et al., 2019).
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)

### → MMLU
- **Faithfulness** (constructs) — *measured_by*
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > We have selected three datasets that measure common sense reasoning and language understanding to evaluate the possible performance loss after altering the model: ... Massive Multitask Language Understanding (MMLU) (Hendrycks et al., 2021)... (Section 2.5)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > Multi-task Language Understanding: MMLU (Hendrycks et al.), C-Eval (Huang et al., 2023); (Section 3.1)
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  > "MMLU (Hendrycks et al., 2021a) to determine factuality, BBH (Suzgun et al., 2022) to check reasoning abilities"
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We then evaluate it on question answering tasks: MMLU, ARC-Easy and ARC-Challenge. (Section 3.2)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  > We also evaluate on the massive multitask language understanding (MMLU) (Hendrycks et al., 2020) benchmark. The results are summarized in Table 4. We found that compared to the base model, our model has improved zero-shot performance... on MMLU. (Section 3.4)
  - [MUFFIN: Curating Multi-Faceted Instructions for Improving Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d1a0188e18c1d74a0f8d6eb5ecede4f-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  > To assess general ability, we evaluate both the MMLU score of the edited model and the Loc-FactScore for unrelated questions. (Section 5.1)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Instance-adaptive Zero-shot Chain-of-Thought Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/e304e04a6f455dd82f8a85a0a3679493-Paper-Conference.pdf)
- **Knowledge** (constructs) — *measured_by*
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **Factual knowledge** (constructs) — *measured_by*
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > Besides, we also employ another two tasks MMLU (Hendrycks et al., 2021), and BBH (Suzgun et al., 2022) from Harness to evaluate the problem-solving capabilities for further clarify of our effectiveness. (Section 4.1)
  - [Automated Design of Agentic Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > “we evaluate the quantized models on zero-shot commonsense reasoning (CSR) ability... Besides common sense abilities, we also evaluate multi-task generalization ability with five-shot setting (in-context learning) on MMLU”
  - [LQ-LoRA: Low-rank plus Quantized Matrix Decomposition for Efficient Language Model Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/d97a16cb83d74195b76e0bf1e85bf072-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > "multi-task language understanding (MMLU (Hendrycks et al., 2020))"
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Domain knowledge** (constructs) — *measured_by*
  > We measure this knowledge reservoir using the Massive Multitask Language Understanding dataset (MMLU) (Hendrycks et al., 2021). (Section 4.1)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
- **Task generalization** (constructs) — *measured_by*
  > We further evaluate the LLMs before and after M2MS instruction tuning on the MMLU evaluation dataset (Hendrycks et al., 2021). The MMLU dataset covers 57 tasks including elementary mathematics, US history, computer science, law, etc, and is designed to evaluate models’ world knowledge and problem-solving ability. (Section 6)
  - [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf)
- **Short-context capability** (constructs) — *measured_by*
  > For short-context evaluation, we followed Llama2 to test on MMLU (Hendrycks et al., 2020), Math (Hendrycks et al., 2021), and BigBenchHard(BBH) (Suzgun et al., 2022). (Section 4.1)
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
- **Domain-specific knowledge** (constructs) — *measured_by*
  > MMLU (Hendrycks et al., 2021) and GAOKAO (Zhong et al., 2023) for comprehensive knowledge evaluation. (Section 3.2)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf)
- **Knowledge retention** (constructs) — *measured_by*
  - [Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf)
- **Knowledge reasoning** (constructs) — *measured_by*
  - [Discovering Sparsity Allocation for  Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **Parametric knowledge** (constructs) — *measured_by*
  > MMLU primarily assesses a model’s parametric knowledge and requires minimal reasoning, thus offering limited benefits from CoT reasoning. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > MMLU (Hendrycks et al., 2021) provides a comprehensive set of logical reasoning assessments across diverse subjects and difficulties, utilizing multiple-option questions to measure general world knowledge and logical inference capabilities.
  - [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs) — *measured_by*
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
- **Medical question answering** (behaviors tasks) — *measured_by*
  > we use Google Translate to translate the questions and answers from the medical-clinical section of the MMLU dataset (Section 3.1.2).
  - [Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1551c01d7a3d0bf21e2518331e9f7074-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > We also assess the helpfulness of the targeted LLMs... To do this, we select 500 examples from three sources: ...MMLU (knowledge tests)... (Section 4.1)
  - [A-TASC:AsianTED-Based Automatic Subtitling Corpus](https://aclanthology.org/2025.acl-long.158.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > These tasks assess the model performance on logical reasoning, language understanding, commonsense reasoning, and knowledge utilization. (Section 4.1)
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **Factuality** (constructs) — *measured_by*
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **STEM problem solving** (behaviors tasks) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > and 2 knowledge-intensive tasks (NQ (Kwiatkowski et al., 2019), MMLU (Hendrycks et al., 2021)). (Section 5.1)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **Knowledge-intensive reasoning** (constructs) — *measured_by*
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  > For a fair comparison, we evaluate the models on MMLU (23), Arc Challenge (6), and OpenBookQA (35) zero-shot tasks implemented in Language Model Evaluation Harness (18).
  - [SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3504a4fa45685d668ce92797fbbf1895-Paper-Conference.pdf)
- **Few-shot learning** (measurements) — *measured_by*
  - [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)
- **BABILong** (measurements) — *correlates*
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Linguistic capability** (constructs) — *measured_by*
  > However, the high-quality data used in SFT significantly improved the language ability, effectively mitigating the disadvantages introduced during the pre-training phase. (Section 5.2)
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
- **Knowledge awareness** (constructs) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *measured_by*
  > The fine-tuned models under MDS are evaluated on the general tasks including MMLU (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), and PIQA (Bisk et al., 2020) to measure the catastrophic forgetting of the PEFT approaches. (Section 4.1)
  - [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.246.pdf)
- **Multitask language understanding** (constructs) — *measured_by*
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  > To examine how retrieval heads effect reasoning tasks, we test Mistrial-7B-Instruct-v0.2 on MMLU (Hendrycks et al., 2020), MuSiQue and GSM8K (Cobbe et al., 2021), with and without chain-of-thought (CoT) reasoning. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  > “We track the progress of IFT based on the performance on four standard benchmarks: GSM8k (Cobbe et al., 2021) (math), MMLU (Hendrycks et al., 2021) (general fact recall), SQuAD (Rajpurkar et al., 2016) (reading comprehension), and ARC-Challenge (Clark et al., 2018) (reasoning).”
  - [Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa27ac7aca4e462da1439b43ceebc04c-Paper-Conference.pdf)
- **Understanding** (constructs) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Stability** (constructs) — *measured_by*
  - [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > “We also compare the models’ general knowledge and reasoning capabilities by measuring accuracy across 57 diverse academic subjects using the MMLU benchmark (Hendrycks et al., 2020).”
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  > In Table 2, we present the text classification results of different dataset pruning methods on the MMLU benchmark. (Section 4.2.2)
  - [Exploring Learning Complexity for Efficient Downstream Dataset Pruning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7e4aab3786a1f8e39e0f9b8dd9fa105-Paper-Conference.pdf)
- **Knowledge editing** (behaviors tasks) — *measured_by*
  > Using the MMLU Pro (Wang et al., 2024) benchmark taxonomy, which divides question-answer sets into 14 distinct domains, we investigated the effects of domain-specific knowledge unlearning on MMLU (Hendrycks et al., 2021).
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [RouteLLM: Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
- **Knowledge-based question answering** (behaviors tasks) — *measured_by*
  - [CanLLMs Convert Graphs to Text-Attributed Graphs?](https://aclanthology.org/2025.naacl-long.66.pdf)
- **Memorization** (constructs) — *measured_by*
  > Memorization was evaluated using a subset of the MMLU benchmark focused on factual knowledge domains
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **Conversational ability** (constructs) — *measured_by*
  > "Traditional benchmarks, such as MMLU (Hendrycks et al., 2021) and HumanEval (Chen et al., 2021), play an important role in assessing specific capabilities of LLMs."
  - [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf)
- **Factual recall** (behaviors tasks) — *measured_by*
  - [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.618.pdf)
- **Knowledge storage** (constructs) — *measured_by*
  > "For our QA evals, we used Massive Multitask Language Understanding (MMLU) (Hendrycks et al., 2020), a common world-knowledge and problem solving benchmark"
  - [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf)
- **Emergent abilities** (constructs) — *measured_by*
  > "the MMLU benchmark ... evaluated using 56 LLMs" and "Fig. 1a–3a show the scaling trend of accuracy on the MMLU" (Fig. 1 caption; Sec. 2.3)
  - [U-shaped and Inverted-U Scaling behind Emergent Abilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f696200311b445af686c3ebd87ade1d7-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences inLLMReasoning](https://aclanthology.org/2025.emnlp-main.1046.pdf)
- **Alignment** (constructs) — *measured_by*
  - [Puzzle: Distillation-Based NAS for Inference-Optimized LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bercovich25a/bercovich25a.pdf)
- **Iterative refinement** (behaviors tasks) — *measured_by*
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **Financial question answering** (behaviors tasks) — *measured_by*
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
- **Overfitting** (constructs) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **Contextual understanding** (constructs) — *measured_by*
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **Multi-Agent Debate** (measurements) — *measured_by*
  - [Communicating Activations Between Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ramesh25a/ramesh25a.pdf)
- **Error handling** (constructs) — *measured_by*
  > We evaluate our method on LLMs and show significant perplexity improvements over baselines. This is particularly noteworthy at high sparsity levels, maintaining robust improvements even as high as 70% sparsity. Benchmark results. In Table 3, we evaluate the performance of our method on several benchmark datasets.
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
- **Multilingual reasoning** (constructs) — *measured_by*
  > Beyond English textual reasoning, we include two additional evaluation tracks: a multilingual experiment using MMLU and its professionally translated variant MMMLU (Hendrycks et al., 2021)...
  - [NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-TurnLLMJailbreaks](https://aclanthology.org/2025.emnlp-main.1236.pdf)
- **Locality** (constructs) — *measured_by*
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf)

### Associated with
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM Evaluation Harness** (measurements)
  > Besides, we also employ another two tasks MMLU (Hendrycks et al., 2021), and BBH (Suzgun et al., 2022) from Harness to evaluate the problem-solving capabilities... (Section 4.1)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)
- **FLASK** (measurements)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **OpenLLM Leaderboard** (measurements)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **MR-Ben** (measurements)
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **Knowledge retrieval** (behaviors tasks)
  - [Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25af/huang25af.pdf)
