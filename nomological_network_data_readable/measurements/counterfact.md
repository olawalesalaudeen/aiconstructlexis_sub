# CounterFact
**Type:** Measurement  
**Referenced in:** 38 papers  
**Also known as:** COUNTERFACT, Counterfact  

## State of the Field

Across the surveyed literature, CounterFact is a widely used dataset for evaluating large language models, with two prevalent applications: assessing knowledge editing interventions and measuring factual knowledge. It is most commonly described as a question-answering dataset structured around `(subject, relation, answer)` tuples, often including paraphrased prompts for each query. A defining feature highlighted in multiple papers is its use of "counterfactual statements" or "false facts" to test a model's ability to adopt new information that may contradict its stored knowledge. In the context of model editing, CounterFact is used to measure constructs such as `Knowledge editing`, `Generality`, and `Locality`. For its other common application, it is used to evaluate a model's baseline `Factuality` and `Factual recall`. The dataset's paraphrased prompts are specifically leveraged to assess `Paraphrastic robustness`, and it is also reported to measure `Knowledge conflict resolution`, `Faithfulness`, and `Knowledge retention`.

## Sources

**[BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)**
> Question-answering dataset used to evaluate a model's factual knowledge, consisting of (subject, relation, answer) tuples with paraphrased prompts, designed to test recovery of specific facts.

**[Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching](https://proceedings.iclr.cc/paper_files/paper/2024/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf) (as "COUNTERFACT")**
> The COUNTERFACT dataset, a collection of factual prompt pairs used to evaluate factual recall and fact editing interventions.

**[Everything is Editable: Extend Knowledge Editing to Unstructured Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/02763667a5761ff92bb15d8751bcd223-Paper-Conference.pdf) (as "Counterfact")**
> A dataset used for evaluating knowledge editing on structured, counterfactual statements.

## Relationships

### → CounterFact
- **Factual knowledge** (constructs) — *measured_by*
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
- **Factual recall** (behaviors tasks) — *measured_by*
  - [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.618.pdf)
- **Knowledge editing** (behaviors tasks) — *measured_by*
  - [Implicit Values Embedded in How Humans andLLMs Complete Subjective Everyday Tasks](https://aclanthology.org/2025.emnlp-main.848.pdf)
- **Generality** (constructs) — *measured_by*
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Locality** (constructs) — *measured_by*
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Knowledge conflict resolution** (constructs) — *measured_by*
  - [Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b99d6cc40b05809c3d84b57a165448cd-Paper-Conference.pdf)
- **Paraphrastic robustness** (constructs) — *measured_by*
  > We evaluate the model’s robustness to paraphrases by computing the percentage of datapoints where the model gets all paraphrases of a given question correct. (Section 5.1)
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
- **Fluency** (constructs) — *measured_by*
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Knowledge retention** (constructs) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Consistency** (constructs) — *measured_by*
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Reliability** (constructs) — *measured_by*
  - [Investigating Pedagogical Teacher and StudentLLMAgents: Genetic Adaptation Meets Retrieval-Augmented Generation Across Learning Styles](https://aclanthology.org/2025.emnlp-main.676.pdf)
- **Context faithfulness** (constructs) — *measured_by*
  - [Joint Modeling of Entities and Discourse Relations for Coherence Assessment](https://aclanthology.org/2025.emnlp-main.1114.pdf)

### Associated with
- **Fact checking** (behaviors tasks)
  - [The Validation Gap: A Mechanistic Analysis of How Language Models Compute Arithmetic but Fail to Validate It](https://aclanthology.org/2025.emnlp-main.1496.pdf)
