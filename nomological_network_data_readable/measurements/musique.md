# MuSiQue
**Type:** Measurement  
**Referenced in:** 73 papers  
**Also known as:** MUSIQUE, Musique, MusiQue, musique, MuSiQue-Ans  

## State of the Field

Across the surveyed literature, MuSiQue is consistently defined and utilized as a benchmark for multi-hop question answering. The prevailing description is that of a challenging dataset requiring models to connect information across multiple paragraphs or documents to answer complex questions, which are often constructed from composable pairs of single-hop questions. A recurring design feature mentioned in the definitions is its construction to prevent models from using "reasoning shortcuts," thereby testing for what some papers call "true compositional reasoning." Consequently, MuSiQue is prevalently used to operationalize and measure both `multi-hop question answering` and the broader construct of `complex reasoning`. Some studies also use it to evaluate `chain-of-thought reasoning` performance. The dataset's questions vary in difficulty, with papers specifically mentioning the use of its 2-hop, 3-hop, and 4-hop subsets for evaluation; as one study notes, this allows researchers to "diversify from HotpotQA where most of the data is 2-hop" (AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios). A smaller line of work employs MuSiQue in out-of-domain settings to test model `generalization`. In practice, it is frequently evaluated alongside other multi-hop QA datasets like HotpotQA and 2WikiMultihopQA and is also identified as a component of the LongBench benchmark.

## Sources

**[KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf)**
> MuSiQue is a challenging multi-hop question answering dataset where questions are constructed from composable pairs of single-hop questions, requiring models to connect multiple pieces of information.

**[SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf) (as "MUSIQUE")**
> A multi-hop question answering dataset that requires reasoning over multiple paragraphs to answer questions, featuring adversarially-written paragraphs to challenge models.

**[MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://proceedings.iclr.cc/paper_files/paper/2025/file/e01c431bbb83153632c0dcfaf8ccda0a-Paper-Conference.pdf) (as "Musique")**
> A benchmark for multi-hop question answering, where a model must connect multiple pieces of information to arrive at the correct answer.

**[AnaScore: Understanding Semantic Parallelism in Proportional Analogies](https://aclanthology.org/2025.naacl-long.55.pdf) (as "musique")**
> Multi-hop question answering dataset constructed to prevent reasoning shortcuts, with complex questions derived from single-hop questions linked by bridge entities, used for evaluating decomposition and downstream QA performance.

**[ImgTrojan: Jailbreaking Vision-Language Models withONEImage](https://aclanthology.org/2025.naacl-long.361.pdf) (as "MusiQue")**
> Multi-hop question answering dataset requiring reasoning over diverse domains with minimal lexical overlap, designed to test true compositional reasoning.

**[Static Word Embeddings for Sentence Semantic Representation](https://aclanthology.org/2025.emnlp-main.317.pdf) (as "MuSiQue-Ans")**
> A benchmark dataset for multi-hop question answering featuring complex, multi-step questions, also referred to as MuSiQue.

## Relationships

### → MuSiQue
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  > We select four typical complex multi-hop question-answering datasets, i.e., HotpotQA (Yang et al., 2018), 2Wiki-MultihopQA (Ho et al., 2020), MusiQue (Trivedi et al., 2022), and StrategyQA (Geva et al., 2021). (Section 5.1)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We measure all the methods on four different QA datasets, including multi-hop Wikipedia reasoning datasets: (1) MuSiQue (Trivedi et al., 2022)... (Section 4.1)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022)... These datasets test the model’s generalization ability beyond the training domain. (Section 4.2.1)
  - [ViClaim: A Multilingual Multilabel Dataset for Automatic Claim Detection in Videos](https://aclanthology.org/2025.emnlp-main.22.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  > HotpotQA (Yang et al., 2018), 2WikiMultihopQA (Ho et al., 2020), and MuSiQue (Trivedi et al., 2021) can be applied to evaluate the multi-step reasoning performance of LLMs. (Section 2)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Long-context reasoning** (constructs) — *measured_by*
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)

### Associated with
- **LongBench** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
