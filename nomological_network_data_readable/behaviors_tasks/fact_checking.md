# Fact checking
**Type:** Behavior  
**Referenced in:** 28 papers  
**Also known as:** Fact verification, Fact-checking, Truthfulness prediction, Statement verification, Statement validation  

## State of the Field

Across the provided literature, fact checking is most commonly defined as the task of judging whether a given claim is supported or contradicted by available knowledge or evidence. While many papers frame this as a binary true/false or supported/unsupported determination, a notable variation treats it as a three-way classification that includes a 'not enough information' category. The process of verification is operationalized against various evidence sources, including provided documents, knowledge graphs, and tables. To measure this behavior, researchers employ several benchmarks, with the provided data citing the use of LongBench, SciFact, and PubHealth. Other datasets frequently mentioned in the context of fact checking tasks include FEVER, Creak, Counterfact, FactKG, HoVer, and VitaminC. Some work also frames fact checking as an entailment task or focuses on specific domains, such as verifying medical statements. The behavior is studied alongside the construct of Faithfulness and is frequently discussed in the context of retrieval-augmented language models and as a method for evaluating the veracity of individual claims within longer model generations.

## Sources

**[BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)**
> Judging whether a claim is supported or contradicted by available knowledge.

**[Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf) (as "Fact verification")**
> The task of determining whether a given textual claim is true or false based on evidence.

**[Logical Consistency of Large Language Models in Fact-Checking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3209cf3312b2cbb68e33644362ddc2bd-Paper-Conference.pdf) (as "Fact-checking")**
> The observable task of verifying a queried fact against a provided knowledge base, such as a knowledge graph, and producing a binary response indicating its validity.

**[GameArena: Evaluating LLM Reasoning through Live Computer Games](https://proceedings.iclr.cc/paper_files/paper/2025/file/520416e27d3b0cef3cd70a083e2991c7-Paper-Conference.pdf) (as "Truthfulness prediction")**
> Predicting whether a human statement is true or false after questioning.

**[Reliable and Diverse Evaluation of LLM Medical Knowledge Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/91a5bb5e5939cb075f5f2464d7b8bbf0-Paper-Conference.pdf) (as "Statement verification")**
> The task of determining whether a given textual statement is true or false based on underlying factual knowledge.

**[Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf) (as "Statement validation")**
> Determining whether a given medical statement is true or false, requiring precise discrimination of knowledge without the aid of multiple-choice options.

## Relationships

### Fact checking →
- **FEVER** (measurements) — *measured_by*
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
- **SciFact** (measurements) — *measured_by*
  - [CanLLMs Ground when they (Don’t) Know: A Study on Direct and Loaded Political Questions](https://aclanthology.org/2025.acl-long.729.pdf)
- **LongBench** (measurements) — *measured_by*
  > LongBench (Bai et al., 2024): Focused on medium-context tasks (10K tokens), it assesses summarization, QA, and fact-checking across multiple domains...
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **PubHealth** (measurements) — *measured_by*
  - [CanLLMs Ground when they (Don’t) Know: A Study on Direct and Loaded Political Questions](https://aclanthology.org/2025.acl-long.729.pdf)
- **Climate-FEVER** (measurements) — *measured_by*
  - [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [CanLLMs Ground when they (Don’t) Know: A Study on Direct and Loaded Political Questions](https://aclanthology.org/2025.acl-long.729.pdf)
- **CounterFact** (measurements)
  - [The Validation Gap: A Mechanistic Analysis of How Language Models Compute Arithmetic but Fail to Validate It](https://aclanthology.org/2025.emnlp-main.1496.pdf)
