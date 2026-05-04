# Natural language understanding
**Type:** Construct  
**Referenced in:** 369 papers  
**Also known as:** Language understanding, Natural Language Understanding, Language comprehension, Natural language comprehension, Linguistic understanding, Multilingual language understanding, Semantic analysis, General language understanding, Machine reading comprehension, Linguistic comprehension, Text comprehension, Intent recognition, Dialogue understanding, Document parsing, File reading, Paper reading, Multiple-choice reading comprehension, Legal contract analysis, Contract understanding, Document comprehension, Legal document interpretation, Legal element recognition, Legal fact verification, Legal reading comprehension, Legal relation extraction, Legal cause prediction, Legal article prediction, Legal penalty prediction, Legal multi-hop reasoning, Legal calculation, Similar case identification, Legal document proofreading, Judicial analysis generation, Long structured data understanding  

## State of the Field

Across the surveyed literature, the most prevalent framing of natural language understanding is a model's general ability to comprehend and interpret human language across a diverse range of tasks, with terms like "language understanding" and "language comprehension" used frequently. This construct is most commonly operationalized through performance on the General Language Understanding Evaluation (GLUE) benchmark, which is widely cited for assessing performance on tasks such as sentence classification, textual entailment, and semantic similarity. A broad array of other benchmarks are also used to measure this capability, with the Massive Multitask Language Understanding (MMLU) benchmark frequently employed to evaluate general and multitask understanding, alongside other instruments like SuperGLUE, ARC, and HellaSwag. The general construct is often specified for particular domains or modalities, giving rise to more focused concepts such as "multilingual language understanding," "document understanding," and various forms of "legal reading comprehension," which are measured by specialized datasets like INCLUDE, DocVQA, and LexEval, respectively. Natural language understanding is consistently studied alongside text generation as a foundational model capability and is often described as a prerequisite for tasks involving reasoning and world knowledge. While most definitions treat it as a latent capacity, a smaller set of papers defines it more directly as the observable performance on these evaluation tasks. The concept also encompasses more granular abilities, with some work defining it through specific behaviors like "intent recognition" or "discourse understanding."

## Sources

**[Fast-ELECTRA for Efficient Pre-training](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e5f58d98523298cba093f658cfdf2d6-Paper-Conference.pdf)**
> The ability of a model to comprehend and interpret human language across a range of tasks.

**[Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf) (as "Language understanding")**
> The general capability of a model to comprehend and process textual information, which is a prerequisite for interpreting puzzle rules and states.

**[SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf) (as "Natural Language Understanding")**
> The latent capacity to comprehend and interpret natural language text and instructions.

**[DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50e9ad960ae78b741a6b4fea533f2eaf-Paper-Conference.pdf) (as "Language comprehension")**
> The fundamental ability to process and interpret the meaning of written or spoken language.

**[EditRoom: LLM-parameterized Graph Diffusion for Composable 3D Room Layout Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/d807e7678ba3afd3a904f4af52819e77-Paper-Conference.pdf) (as "Natural language comprehension")**
> The ability to interpret open-ended user commands and convert them into actionable internal representations for downstream execution.

**[Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf) (as "Linguistic understanding")**
> The model's ability to comprehend and interpret the meaning, intent, and nuances of natural language questions and contexts.

**[Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf) (as "Multitask language understanding")**
> The ability to perform a wide variety of language tasks across different knowledge domains without task-specific training.

**[To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf) (as "Reading comprehension")**
> The latent ability to interpret provided context and extract relevant factual information needed to answer questions accurately.

**[INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf) (as "Multilingual language understanding")**
> The latent ability of an LLM to comprehend and answer questions accurately across multiple languages rather than only in one dominant language.

**[Did Translation Models Get More Robust Without AnyoneEven Noticing?](https://aclanthology.org/2025.acl-long.123.pdf) (as "General language understanding")**
> The latent ability of a language model to comprehend and perform well across a diverse range of natural language tasks involving reasoning, comprehension, and knowledge recall.

**[Comparing Moral Values inWesternEnglish-speaking societies andLLMs with Word Associations](https://aclanthology.org/2025.acl-long.178.pdf) (as "Semantic analysis")**
> The latent capacity to interpret the meaning of classical Chinese texts by combining word-level sense selection with sentence-level translation and contextual reasoning.

**[Discriminative Policy Optimization for Token-Level Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ca/chen25ca.pdf) (as "Machine reading comprehension")**
> The ability to understand a given text and answer questions based on it, evaluated on dimensions such as relevance, factuality, and completeness.

**[ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://proceedings.iclr.cc/paper_files/paper/2024/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf) (as "Text understanding")**
> The model's ability to comprehend the meaning, context, and nuances of written language.

**[Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.262.pdf) (as "Linguistic comprehension")**
> The model’s ability to understand spoken language content well enough to answer questions correctly.

**[Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf) (as "Text comprehension")**
> The ability to process textual information, understand its meaning, and extract relevant details to answer questions or perform tasks.

**[An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf) (as "Dialogue understanding")**
> Processing conversational context and responding to dialogue-based inputs over long contexts.

**[Understanding and Enhancing the Transferability of Jailbreaking Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/db988b089d8d97d0f159c15ed0be6a71-Paper-Conference.pdf) (as "Intent recognition")**
> Identifying the underlying intent of an input sentence from token-level cues.

**[Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf) (as "Document parsing")**
> The task of extracting structured information or transcribing content from document images, which often contain dense text and layouts.

**[CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf) (as "Multiple-choice reading comprehension")**
> The observable task of answering questions about a given text by selecting the correct option from a predefined set of choices.

**[ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf) (as "Paper reading")**
> Aggregating information from papers to form a researcher profile or condensed understanding of research materials.

**[Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf) (as "File reading")**
> Reading and extracting information from files or documents to answer a query.

**[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf) (as "Discourse understanding")**
> The task of interpreting and reasoning over lengthy and complex narratives to answer questions that require a cohesive understanding of the entire text.

**[Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf) (as "Contract understanding")**
> The task of processing and interpreting legal contracts to extract specific information or answer questions about their content.

**[Position: AI Scaling: From Up to Down and Out](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25fh/wang25fh.pdf) (as "Legal contract analysis")**
> Extracting, interpreting, or evaluating clauses and terms in legal documents using AI.

**[MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf) (as "Document understanding")**
> The task of extracting and interpreting information from document images, which may include text, tables, and figures.

**[Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf) (as "Document comprehension")**
> The observable task of understanding and answering questions about the content of a document image.

**[SaulLM-54B & SaulLM-141B: Scaling Up Domain Adaptation for the Legal Domain](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea3f85a33f9ba072058e3df233cf6cca-Paper-Conference.pdf) (as "Legal document interpretation")**
> Interpreting legal texts and extracting their meaning, issues, or implications from prompts about legal documents.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal element recognition")**
> Identifying the legal elements contained in a legal text from answer options.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal fact verification")**
> Selecting facts that can be logically inferred from evidence in a legal case.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal reading comprehension")**
> Answering questions that require understanding and extracting information from a provided legal text.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal relation extraction")**
> Identifying and extracting specific types of legal relationship triples from a given legal text.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal cause prediction")**
> Inferring the likely legal cause or case type based on a given case description and background information.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal article prediction")**
> Inferring the relevant legal articles that apply to a given case description.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal penalty prediction")**
> Predicting the likely penalties a defendant may face based on a case description.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal multi-hop reasoning")**
> Performing multiple logical inference steps to solve a problem based on given contextual information from a legal scenario.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal calculation")**
> Computing legally relevant time periods, monetary amounts, or other quantifiable values from legal rules and facts.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Similar case identification")**
> Determining the most relevant case to a given query case from a list of candidates.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal document proofreading")**
> Identifying and correcting errors within a given legal text.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Judicial analysis generation")**
> Producing formatted judicial analysis paragraphs that discuss facts, legal issues, grounds, logic, and outcomes.

**[CanLLMs Generate and Solve Linguistic Olympiad Puzzles?](https://aclanthology.org/2025.emnlp-main.970.pdf) (as "Long structured data understanding")**
> The task of parsing, interpreting, and reasoning about information presented in long, structured formats like tables or JSON.

## Relationships

### Natural language understanding →
- **GLUE** (measurements) — *measured_by*
  > We compare our approach with LoRA and other parameter-efficient adaptation methods on the natural language understanding (GLUE) and natural language generation (E2E) benchmarks... (Section 1)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
- **CoLA** (measurements) — *measured_by*
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > "multi-task language understanding (MMLU (Hendrycks et al., 2020))"
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  > For short-context evaluation, we employ MMLU (Hendrycks et al., 2021), ARC-C (Clark et al., 2018), Hellaswag (Zellers et al., 2019) and Winogrande (Sakaguchi et al., 2019) for assessing the general language understanding and reasoning capabilities...
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **SuperGLUE** (measurements) — *measured_by*
  > "We benchmark FIRE as well as other positional encoding approaches on a wide range of real-world language modeling (C4, arXiv, and Github), long text benchmark (SCROLLS), zero-shot long-context question answering (NarrativeQA), and natural language understanding benchmarks (GLUE/SuperGLUE)."
  - [A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
- **MNLI** (measurements) — *measured_by*
  > These datasets encompass various typical language understanding tasks such as natural language inference. (Section 5.1)
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **QNLI** (measurements) — *measured_by*
  > These datasets encompass various typical language understanding tasks such as natural language inference. (Section 5.1)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **RTE** (measurements) — *measured_by*
  > For NLU tasks, we compare baselines on five datasets, including CoLA (Warstadt et al., 2018), MRPC (Dolan & Brockett, 2005), RTE (Wang et al., 2019), SST-2 (Socher et al., 2013), and WNLI (Wang et al., 2019).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **MRPC** (measurements) — *measured_by*
  > For NLU tasks, we compare baselines on five datasets, including CoLA (Warstadt et al., 2018), MRPC (Dolan & Brockett, 2005), RTE (Wang et al., 2019), SST-2 (Socher et al., 2013), and WNLI (Wang et al., 2019).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > For short-context evaluation, we employ MMLU (Hendrycks et al., 2021), ARC-C (Clark et al., 2018), Hellaswag (Zellers et al., 2019) and Winogrande (Sakaguchi et al., 2019) for assessing the general language understanding and reasoning capabilities...
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > We use 12 natural language understanding benchmarks for evaluation: CMNLI (Xu et al., 2020), HellaSwag(HeSw) (Zellers et al., 2019), PIQA (Bisk et al., 2020),CHID (Zheng et al., 2019), WSC (Levesque et al., 2012),CommonSenseQA(CoQA) (Talmor et al., 2018), BoolQ (Clark et al., 2019),MMLU (Hendrycks et al., 2020), CMMLU (Li et al., 2023),Race-High/Middle (Lai et al., 2017), C3 (Sun et al., 2020). (Section 4.2)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  > we evaluate unsupervised ICL on the GSM8K dataset that requires reasoning capabilities and on the MMLU(-Pro) dataset that covers broad knowledge of different disciplines. (Section 5.1)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **SST-2** (measurements) — *measured_by*
  > Together, these benchmarks provide a well-rounded evaluation of language understanding, covering reasoning, sentiment, social context, and word meaning.
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
- **SNLI** (measurements) — *measured_by*
  > Experimental results demonstrate that our ReFusion framework can significantly improve models’ understanding capability, achieving superior and robust performance. (Section 1)
  - [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf)
- **GLUE-X** (measurements) — *measured_by*
  > We conduct experiments on both zero-shot and few-shot settings of natural language understanding and question answering (QA). SuperContext is validated on a comprehensive OOD benchmarks GLUE-X (Yang et al., 2022), and a QA dataset, SQuAD 2.0 (Rajpurkar et al., 2018). (Section 2)
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  > "We evaluate the distilled students on LAMBADA (Paperno et al., 2016) ... We find that SDTT preserves the natural language understanding performance of the teacher."
  - [Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  > "including four reading comprehension tasks (ARC-e, ARC-c (Clark et al., 2018), OBQA (Mihaylov et al., 2018), and BoolQ (Clark et al., 2019))"
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  > ...language understanding (HellaSwag (Zellers et al., 2019), BoolQ (Clark et al., 2019), OpenbookQA (Mihaylov et al., 2018), SQuAD (Rajpurkar et al., 2016), MMLU (Hendrycks et al., 2021), MMLU-Pro (Wang et al., 2024), GPQA(Rein et al., 2023)) (Section 3).
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
- **DocVQA** (measurements) — *measured_by*
  > DocVQA (Mathew et al., 2021) focuses on reading comprehension tasks over document images. (Section 4.1)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  > we use seven commonsense reasoning tasks from the popular framework Harness (Gao et al., 2024), including four reading comprehension tasks (ARC-e, ARC-c (Clark et al., 2018), OBQA (Mihaylov et al., 2018), and BoolQ (Clark et al., 2019))... (Section 4.1)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **INCLUDE** (measurements) — *measured_by*
  - [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf)
- **SWAG** (measurements) — *measured_by*
  > To evaluate multitask performance, we test on several NLP benchmarks, including MMLU (Hendrycks et al., 2020), MMLU-Pro (Wang et al., 2024), ARC-Easy, ARC-Challenge (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), SWAG (Zellers et al., 2018), and CommonsenseQA (Talmor et al., 2018). These benchmarks consist of multiple-choice questions, assessing various aspects of the model's natural language understanding.
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **LiveBench** (measurements) — *measured_by*
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  > "In Table 3, we provide results across the InfiniteBench tasks" and the table includes "Dialogue" tasks under InfiniteBench
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **20 Newsgroups** (measurements) — *measured_by*
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > “Language Comprehension: Connections word puzzles, a typo-fixing task, and a movie synopsis unscrambling task”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Chronological ordering** (behaviors tasks) — *measured_by*
  > “Language Comprehension: Connections word puzzles, a typo-fixing task, and a movie synopsis unscrambling task”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **MLQA** (measurements) — *measured_by*
  > We evaluate our methods on unlearning math-solving, Python-coding, and comprehension skills across seven different languages with GSM8K, MBPP, and MLQA datasets respectively. (Section 6)
  - [Model Surgery: ModulatingLLM’s Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.322.pdf)
- **Natural language inference** (behaviors tasks) — *measured_by*
  > In the recent past, a popular way of evaluating natural language understanding (NLU), was to consider a model’s ability to perform natural language inference (NLI) tasks. (Abstract)
  - [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.466.pdf)
- **CUAD** (measurements) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **ALFWorld** (measurements) — *measured_by*
  > ALFWorld (Shridhar et al., 2020) provides a text-based household task environment that for natural language understanding and embodied reasoning. (Section 5.1)
  - [BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation](https://aclanthology.org/2025.emnlp-main.152.pdf)
- **Direct prompting** (measurements) — *measured_by*
  - [Topic Coverage-based Demonstration Retrieval for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1008.pdf)
- **Chain-of-thought prompting** (measurements) — *measured_by*
  - [Topic Coverage-based Demonstration Retrieval for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1008.pdf)

### → Natural language understanding
- **Data analysis** (behaviors tasks) — *correlates*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)

### Associated with
- **Text generation** (behaviors tasks)
  > Large language models (LLMs) are transforming various domains by enabling sophisticated natural language understanding and generation (Zhao et al., 2023).
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Understanding** (constructs)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Logical reasoning** (constructs)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Critique** (behaviors tasks)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text understanding** (constructs)
  - [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [Iterative Multilingual Spectral Attribute Erasure](https://aclanthology.org/2025.emnlp-main.1489.pdf)
- **Dialogue state tracking** (behaviors tasks)
  - [CAST: Corpus-Aware Self-similarity Enhanced Topic modelling](https://aclanthology.org/2025.naacl-long.387.pdf)
- **Contextual reasoning** (constructs)
  > Recent advances in Large Language Models (LLMs) have demonstrated strong capabilities in natural language understanding and contextual reasoning, opening new avenues for complex tasks. (Section 1)
  - [Improving the Quality of Web-mined Parallel Corpora of Low-Resource Languages using Debiasing Heuristics](https://aclanthology.org/2025.emnlp-main.1436.pdf)
- **Knowledge graph question answering** (behaviors tasks)
  > KGQA poses challenges to existing approaches, as it requires a deep understanding of natural language questions and the ability to perform complex reasoning over KGs. (Section 1)
  - [Evaluating Large Language Models for Detecting Antisemitism](https://aclanthology.org/2025.emnlp-main.1793.pdf)
