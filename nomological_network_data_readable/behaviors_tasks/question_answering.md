# Question answering
**Type:** Behavior  
**Referenced in:** 331 papers  
**Also known as:** Retain query answering  

## State of the Field

Across the surveyed literature, question answering (QA) is consistently defined as the observable behavior of a model producing answers to natural language questions. The prevailing usage frames this task in a context-dependent manner, where models generate answers based on provided information such as Wikipedia articles, structured tables, or retrieved documents. A smaller but common line of work treats QA as a test of a model's internal general knowledge, evaluating its ability to answer factual questions without a given context. The expected answer format varies widely, from direct, short-form responses and span extraction to multiple-choice selections and, as one paper specifies, "Yes/No/Don’t Know" answers ("Teaching Models to Balance Resisting and Accepting Persuasion").

This behavior is operationalized and measured using a vast array of benchmarks. Among the most frequently cited instruments are TriviaQA and Natural Questions for open-domain knowledge, SQuAD for reading comprehension from a given passage, HotpotQA for multi-hop reasoning, and MMLU for assessing knowledge across a massive set of tasks. Papers also evaluate QA in specialized domains like medicine and law, and in both standard and adversarial settings. Question answering is commonly studied alongside hallucination, where the factuality of generated answers is a primary concern, and is also frequently associated with complex reasoning and long-context processing.

## Sources

**[A Survey ofNLPProgress inSino-Tibetan Low-Resource Languages](https://aclanthology.org/2025.naacl-long.397.pdf)**
> Producing answers to natural language questions, evaluated in both standard and adversarial settings.

**[HS-STaR: Hierarchical Sampling for Self-Taught Reasoners via Difficulty Estimation and Budget Reallocation](https://aclanthology.org/2025.emnlp-main.283.pdf) (as "Retain query answering")**
> The model's observable ability to correctly answer questions about information it was instructed to retain, even when those questions appear alongside forget queries.

## Relationships

### Question answering →
- **TriviaQA** (measurements) — *measured_by*
  > “• TRIVIAQA (Joshi et al., 2017): Assesses the model’s question-answering capability.”
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  > The questions used for constructing our training data are sourced from the ASQA (Stelmakh et al., 2022), WebQuestions (Berant et al., 2013), and Natural Questions (Kwiatkowski et al., 2019) training splits. (Section 4.1.1)
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  > We apply our evaluation method to the Stanford Question Answering Dataset (SQuAD) 1.1 (Rajpurkar et al., 2016), which comprises context paragraphs extracted from Wikipedia articles, along with manually crafted questions and their corresponding correct answers.
  - [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  > “Complex Reasoning (HotpotQA (Yang et al., 2018)) is a multi-turn QA dataset.”
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU** (measurements) — *measured_by*
  > We then evaluate it on question answering tasks: MMLU, ARC-Easy and ARC-Challenge. (Section 3.2)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  > “we evaluate the proposed MoEQuant on various reasoning tasks, including MMLU (Hendrycks et al., 2020), BoolQ (Clark et al., 2019), HellaSwag (Zellers et al., 2019), Openbookqa (Mihaylov et al., 2018), and MathQA (Amini et al., 2019).”
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  > “we evaluate the proposed MoEQuant on various reasoning tasks, including MMLU (Hendrycks et al., 2020), BoolQ (Clark et al., 2019), HellaSwag (Zellers et al., 2019), Openbookqa (Mihaylov et al., 2018), and MathQA (Amini et al., 2019).”
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > For short-form Q&A scenarios evaluation, we adopt the open-ended generation task of TruthfulQA (Lin et al., 2022), Entity Questions (Sciavolino et al., 2021), SciQ(Welbl et al., 2017) and StrategyQA (Geva et al., 2021). (Section 4.1)
  - [On the Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/c48dcd605cfb17d5b4f94ce106a915f7-Paper-Conference.pdf)
- **NarrativeQA** (measurements) — *measured_by*
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **Qasper** (measurements) — *measured_by*
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
- **zs-RE** (measurements) — *measured_by*
  > "ZsRE is a closed-book question answering (QA) dataset derived from zero-shot relation extraction."
  - [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  > We employ Web Questions (WebQA) (Berant et al., 2013; Chang et al., 2021), MultiModalQA (Talmor et al.), ManyModalQA (Hannan et al., 2020) and StrategyQA (Geva et al., 2021a) dataset for experiments. (Section 5.1)
  - [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb113910e9c3f6242541c1652e30dfd6-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  > "We evaluate our proposed method on several question-answering benchmarks, including ScienceQA (Lu et al., 2022), CommonsenseQA (Talmor et al., 2019), OpenBookQA (Mihaylov et al., 2018) and SIQA (Sap et al., 2019)."
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  > We then evaluate it on question answering tasks: MMLU, ARC-Easy and ARC-Challenge. (Section 3.2)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
- **PopQA** (measurements) — *measured_by*
  > We demonstrate ADACAD’s effectiveness on a diverse range of tasks, covering question-answering (QA) and summarization, with six QA datasets (Natural Question (NQ; Kwiatkowski et al., 2019), NQ-SWAP (Longpre et al., 2021), TriviaQA (Joshi et al., 2017), PopQA (Mallen et al., 2023), HotpotQA (Yang et al., 2018), TabMWP (Lu et al., 2023)) (Section 1).
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
- **QASC** (measurements) — *measured_by*
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  > We evaluate each method on a wide range of reasoning tasks. These tasks include [...] ARC (ARCe for the easier dataset and ARCc for the challenging dataset) for multiple-choice science QA [...] (Section 4.1)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
- **WikiQA** (measurements) — *measured_by*
  - [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf)
- **2WikiMultihopQA** (measurements) — *measured_by*
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **MuSiQue** (measurements) — *measured_by*
  > We measure all the methods on four different QA datasets, including multi-hop Wikipedia reasoning datasets: (1) MuSiQue (Trivedi et al., 2022)... (Section 4.1)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **SQuAD v2.0** (measurements) — *measured_by*
  - [Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf)
- **CoQA** (measurements) — *measured_by*
  > “for the Independent setting, where the questions are not related to each other, we use the CoQA (Reddy et al., 2019)”
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Mixture of Tokens: Continuous MoE through Cross-Example Aggregation](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc427eb348789b190e3ea050cceff8a3-Paper-Conference.pdf)
- **BioASQ** (measurements) — *measured_by*
  > We evaluate RAG performance across three datasets spanning different reasoning complexities and domain-specificity... BioASQ (Task 11B) (Krithara et al., 2023): PubMed-based biomedical QA for specialized domains. (Section 3.3)
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  - [Calibrating Expressions of Certainty](https://proceedings.iclr.cc/paper_files/paper/2025/file/66b35d2e8d524706f39cc21f5337b002-Paper-Conference.pdf)
- **SQuAD 1.1** (measurements) — *measured_by*
  > We used SQuAD v1.1 (Rajpurkar et al., 2016) for QA tasks (Section 4.1)
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
- **TyDiQA** (measurements) — *measured_by*
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **DROP** (measurements) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
- **ScienceQA** (measurements) — *measured_by*
  > “we follow the datasets and tuning orders of the CoIN benchmark ... including ScienceQA”
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
- **TyDi QA** (measurements) — *measured_by*
  > For example, multilingual datasets like TyDi QA (Clark et al., 2020), which includes only Swahili from Africa, AfriQA (Ogundepo et al., 2023), NaijaRC (Aremu et al., 2024), and AfriMed-QA (Nimo et al., 2025). (Section 4.3)
  - [LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf)
- **BBQ** (measurements) — *measured_by*
  - [Prompting Fairness: Integrating Causality to Debias Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f26a2d143a227376dff99a279f93f99-Paper-Conference.pdf)
- **SIQA** (measurements) — *measured_by*
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
- **RULER** (measurements) — *measured_by*
  - [MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/13f972adf12bdf886583d48cd528002f-Paper-Conference.pdf)
- **ELI5** (measurements) — *measured_by*
  > We run experiments on two question- answering datasets, namely NQ-Open and ELI5. (Section 3.1)
  - [Investigating Human Values in Online Communities](https://aclanthology.org/2025.naacl-long.78.pdf)
- **SQuAD 2.0** (measurements) — *measured_by*
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
- **ZeroSCROLLS** (measurements) — *measured_by*
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **PubMedQA** (measurements) — *measured_by*
  - [Shh, don't say that! Domain Certification in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/27befed4547edcb4bdeacef9472cadee-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  > We finetune the pretrained RoBERTa-base model (Liu et al., 2019) on the GLUE benchmark, a widely used suite for evaluating NLP models across various tasks, including sentiment analysis and question answering (Wang et al., 2019). (Section 4.2)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.71.pdf)
- **BBH** (measurements) — *measured_by*
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
- **MedMCQA** (measurements) — *measured_by*
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
- **ArXivQA** (measurements) — *measured_by*
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **ToolQA** (measurements) — *measured_by*
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **MedQA-USMLE** (measurements) — *measured_by*
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
- **LogiQA** (measurements) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Diff-eRank: A Novel Rank-Based Metric for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/45cc967d7899616f51993b7b363d35b5-Paper-Conference.pdf)
- **MS MARCO** (measurements) — *measured_by*
  - [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf)
- **Bamboogle** (measurements) — *measured_by*
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **SAMSum** (measurements) — *measured_by*
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **Spec-Bench** (measurements) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **WebQuestions** (measurements) — *measured_by*
  > The questions used for constructing our training data are sourced from the ASQA (Stelmakh et al., 2022), WebQuestions (Berant et al., 2013), and Natural Questions (Kwiatkowski et al., 2019) training splits. (Section 4.1.1)
  - [KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.459.pdf)
- **NewsQA** (measurements) — *measured_by*
  - [Evaluating Copyright Takedown Methods for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/faed4276b52ef762879db4142655c699-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SocialIQA** (measurements) — *measured_by*
  > OLMo-30M models trained on various pre-training token budgets are fine-tuned on downstream tasks using fixed hyperparameters: math (GSM8k), code (Starcoder-Python), and QA (SIQA). (Figure 4)
  - [Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
- **MM-Hal-Bench** (measurements) — *measured_by*
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **LoCoMo** (measurements) — *measured_by*
  - [SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf)
- **ECQA** (measurements) — *measured_by*
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
- **EVOUNA** (measurements) — *measured_by*
  - [MetaMetrics: Calibrating Metrics for Generation Tasks Using Human Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1b248453bca182b6138b8c14a75340d-Paper-Conference.pdf)
- **SST-2** (measurements) — *measured_by*
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
- **Arena-Hard** (measurements) — *measured_by*
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **WildBench** (measurements) — *measured_by*
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **ASQA** (measurements) — *measured_by*
  > The questions used for constructing our training data are sourced from the ASQA (Stelmakh et al., 2022), WebQuestions (Berant et al., 2013), and Natural Questions (Kwiatkowski et al., 2019) training splits. (Section 4.1.1)
  - [KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.459.pdf)
- **XQuAD** (measurements) — *measured_by*
  > “Question Answering: We focus on 3 QA datasets 1) XQUAD (Artetxe et al., 2019)” (Section 4.1)
  - [Has this Fact been Edited? Detecting Knowledge Edits in Language Models](https://aclanthology.org/2025.naacl-long.493.pdf)
- **MLQA** (measurements) — *measured_by*
  > “For the question-answering task, we fine-tune Qwen2.5-1.5B... We evaluate LMTransplant on five established benchmarks: • MLQA ... A question-answering benchmark”
  - [iTool: Reinforced Fine-Tuning with Dynamic Deficiency Calibration for Advanced Tool Use](https://aclanthology.org/2025.emnlp-main.702.pdf)
- **NQ-Swap** (measurements) — *measured_by*
  - [Ethical Concern Identification inNLP: A Corpus ofACLAnthology Ethics Statements](https://aclanthology.org/2025.naacl-long.581.pdf)
- **IIRC** (measurements) — *measured_by*
  - [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
- **TabMWP** (measurements) — *measured_by*
  > "Lastly, we also test on a popular tabular question-answering dataset, TabMWP (Lu et al., 2023), that requires LLMs to use reasoning skills over tabular contexts."
  - [Ethical Concern Identification inNLP: A Corpus ofACLAnthology Ethics Statements](https://aclanthology.org/2025.naacl-long.581.pdf)
- **Belebele** (measurements) — *measured_by*
  > "We use the following datasets: ARC challenge (Clark et al., 2018), HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2020), CommonSense QA (Talmor et al., 2018) and Belebele (Bandarkar et al., 2023)."
  - [Neutral residues: revisiting adapters for model extension](https://raw.githubusercontent.com/mlresearch/v267/main/assets/talla25a/talla25a.pdf)
- **ParaRel** (measurements) — *measured_by*
  - [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf)
- **CosmosQA** (measurements) — *measured_by*
  - [Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Nectar** (measurements) — *measured_by*
  > We began our experiments using the Nectar (Zhu et al., 2023) dataset, which includes human-labeled responses categorized into seven distinct rankings. (Section 4.2)
  - [Through the Valley: Path to Effective LongCoTTraining for Small Language Models](https://aclanthology.org/2025.emnlp-main.252.pdf)
- **QNLI** (measurements) — *measured_by*
  - [The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology](https://aclanthology.org/2025.emnlp-main.1769.pdf)
- **EDUADAPT** (measurements) — *measured_by*
  > Paper title: "EduAdapt: A Question Answer Benchmark Dataset for Evaluating Grade-Level Adaptability in LLMs"
  - [2025.emnlp-main.1736.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1736.checklist.pdf)

### → Question answering
- **Information retrieval** (behaviors tasks) — *causes*
  - [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  > The OpenBookQA dataset is a question-answering dataset designed to test deep understanding through multi-step reasoning, common knowledge, and text comprehension, similar to open-book exams. (Section 4.1)
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)
- **MMLU** (measurements) — *measured_by*
  > We evaluate the impact of data contamination using a mix of seven different benchmarks: ARC-Easy (Clark et al., 2018), Social-I-QA (Sap et al., 2019), WinoGrande (Sakaguchi et al., 2021), PiQA (Bisk et al., 2020), BoolQ (Clark et al., 2019), MMLU (Hendrycks et al., 2021), and HellaSwag (Zellers et al., 2019).
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)
- **Coreference resolution** (behaviors tasks) — *causes*
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **Retention** (constructs) — *measured_by*
  - [Self-Updatable Large Language Models by Integrating Context into Model Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b0c4fc1bd52329279c51ad2ddec9ace-Paper-Conference.pdf)
- **Knowledge conflict resolution** (constructs) — *causes*
  - [Measuring Data Diversity for Instruction Tuning: A Systematic Analysis and A Reliable Metric](https://aclanthology.org/2025.acl-long.909.pdf)

### Associated with
- **Complex reasoning** (behaviors tasks)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Long-context understanding** (constructs)
  > ...achieving substantial progress on tasks such as summarization and question answering that emphasize the effective utilization and understanding of long inputs.
  - [SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  > This paper focuses on fundamental research of ambiguity-caused hallucination in question answering.
  - [2025.emnlp-main.365.checklist](https://aclanthology.org/attachments/2025.emnlp-main.365.checklist.pdf)
- **Reasoning** (constructs)
  - [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Relevance** (constructs)
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **Verbosity** (constructs)
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **Completeness** (constructs)
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **World knowledge** (constructs)
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Federated In-Context Learning: Iterative Refinement for Improved Answer Quality](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25db/wang25db.pdf)
- **Hallucination detection** (behaviors tasks)
  > We demonstrate that the influence of negated text on hallucination detection extends across multiple tasks, including question answering (QA), dialogue, summarization, and completion, indicating its task-agnostic.
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **Prompt engineering** (behaviors tasks)
  - [Characterizing the Role of Similarity in the Property Inferences of Language Models](https://aclanthology.org/2025.naacl-long.575.pdf)
- **Ranking** (behaviors tasks)
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **Entity disambiguation** (behaviors tasks)
  - [Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models](https://aclanthology.org/2025.naacl-long.268.pdf)
- **Dialogue state tracking** (behaviors tasks)
  - [CAST: Corpus-Aware Self-similarity Enhanced Topic modelling](https://aclanthology.org/2025.naacl-long.387.pdf)
