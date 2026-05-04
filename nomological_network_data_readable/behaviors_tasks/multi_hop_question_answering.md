# Multi-hop question answering
**Type:** Behavior  
**Referenced in:** 79 papers  
**Also known as:** Multi-hop QA, Multihop question answering  

## State of the Field

Across the provided literature, multi-hop question answering is predominantly defined as the task of answering a complex question that requires finding, combining, and reasoning over multiple pieces of information scattered across different documents or sources. Several papers describe this process as involving sequential steps, with one study noting it requires models to "generate intermediate questions and answers until arriving at the final answer" (Making Retrieval-Augmented Language Models Robust to Irrelevant Context). While the core idea of integrating information is consistent, a few papers offer slightly different framings, such as producing answers through "relational reasoning" over multiple facts. The field operationalizes and measures this behavior using a set of established benchmarks. The most frequently cited datasets for evaluating multi-hop question answering are HotpotQA, MuSiQue, and 2WikiMultihopQA. Other datasets, such as StrategyQA, Bamboogle, and WebQuestions, are also used to measure this behavior, though less commonly in this set of papers. This task is positioned as a way to assess a model's capacity for complex, multi-step reasoning and, as one paper suggests, to measure its "associativity by requiring the model to connect multiple pieces of information" (From RAG to Memory: Non-Parametric Continual Learning for Large Language Models).

## Sources

**[DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)**
> The task of answering a question that requires finding and combining multiple pieces of information, often by generating and answering a series of intermediate questions.

**[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf) (as "Multi-hop QA")**
> Producing answers that require integrating information from multiple passages or facts through relational reasoning.

**[From Complex to Atomic: Enhancing Augmented Generation via Knowledge-Aware Dual Rewriting and Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ac/wang25ac.pdf) (as "Multihop question answering")**
> Generating answers to questions that require retrieving and synthesizing information from multiple sources or documents.

## Relationships

### Multi-hop question answering →
- **HotpotQA** (measurements) — *measured_by*
  > Reasoning, including ... multi-hop question answering (HotpotQA)... (Section 2.2)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
- **MuSiQue** (measurements) — *measured_by*
  > We select four typical complex multi-hop question-answering datasets, i.e., HotpotQA (Yang et al., 2018), 2Wiki-MultihopQA (Ho et al., 2020), MusiQue (Trivedi et al., 2022), and StrategyQA (Geva et al., 2021). (Section 5.1)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **2WikiMultihopQA** (measurements) — *measured_by*
  - [ImgTrojan: Jailbreaking Vision-Language Models withONEImage](https://aclanthology.org/2025.naacl-long.361.pdf)
- **StrategyQA** (measurements) — *measured_by*
  > We select four typical complex multi-hop question-answering datasets, i.e., HotpotQA (Yang et al., 2018), 2Wiki-MultihopQA (Ho et al., 2020), MusiQue (Trivedi et al., 2022), and StrategyQA (Geva et al., 2021). (Section 5.1)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Bamboogle** (measurements) — *measured_by*
  > We conduct experiments on five multi-hop QA datasets: HotPotQA (Yang et al., 2018), 2WikiMultiHopQA (2Wiki) (Ho et al., 2020), MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2023) and WebQuestions (WebQA) (Berant et al., 2013). (Section 4.1)
  - [Evaluating Sequence Labeling on the basis of Information Theory](https://aclanthology.org/2025.acl-long.1352.pdf)
- **MultiHop-RAG** (measurements) — *measured_by*
  > We evaluate BELLE on four multi-hop QA datasets, including MultiHop-RAG (Tang and Yang, 2024), 2WikiMultiHopQA (Ho et al., 2020), HotPotQA (Yang et al., 2018), and MuSiQue (Trivedi et al., 2022). (Section 1)
  - [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf)
- **MQUAKE** (measurements) — *measured_by*
  - [MQuAKE-Remastered: Multi-Hop Knowledge Editing Can Only Be Advanced with Reliable Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/f782860c2a5d8f675b0066522b8c2cf2-Paper-Conference.pdf)
- **WebQSP** (measurements) — *measured_by*
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
- **RULER** (measurements) — *measured_by*
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
- **WebQuestions** (measurements) — *measured_by*
  > We conduct experiments on five multi-hop QA datasets: HotPotQA (Yang et al., 2018), 2WikiMultiHopQA (2Wiki) (Ho et al., 2020), MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2023) and WebQuestions (WebQA) (Berant et al., 2013). (Section 4.1)
  - [LoGU: Long-form Generation with Uncertainty Expressions](https://aclanthology.org/2025.acl-long.929.pdf)
- **COMPLEXTEMPQA** (measurements) — *measured_by*
  > “Questions in COMPLEXTEMPQA require advanced reasoning skills, including event/entity matching, multi-hop inference, cross-time comparisons, and temporal ordering.”
  - [Predicate-Guided Generation for Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.463.pdf)

### Associated with
- **Complex reasoning** (behaviors tasks)
  - [Delving into Multilingual Ethical Bias: TheMSQADwith Statistical Hypothesis Tests for Large Language Models](https://aclanthology.org/2025.acl-long.16.pdf)
- **Knowledge integration** (constructs)
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)
