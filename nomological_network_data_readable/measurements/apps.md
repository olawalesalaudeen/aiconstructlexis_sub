# APPS
**Type:** Measurement  
**Referenced in:** 27 papers  
**Also known as:** APPs  

## State of the Field

Across the surveyed literature, APPS is consistently described as a benchmark for evaluating code generation systems, with its full name cited as both "Algorithmic Programming Problems" and "Automated Programming Progress Standard". The benchmark is composed of 10,000 programming problems, typically split evenly between training and test sets, which are presented as natural language descriptions and paired with test cases to assess the functional correctness of generated code. A recurring feature noted in the data is its structure of tiered difficulty, with problems categorized as introductory, interview, and competition level. The primary and most widely documented application of APPS is to measure the behavior of code generation, and it is frequently used alongside other benchmarks like HumanEval and CodeContests. Evaluation is commonly operationalized through metrics such as pass@k, which measures success against hidden unit tests. While its use for code generation is prevalent, a few papers also identify APPS as a tool for measuring code debugging, self-reflection, faithfulness, and few-shot prompting.

## Sources

**[$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf)**
> Algorithmic Programming Problems benchmark containing natural language problem descriptions and test cases for evaluating code generation systems.

**[Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf) (as "APPs")**
> A programming benchmark used to evaluate code generation across problems of varying difficulty.

## Relationships

### → APPS
- **Code generation** (behaviors tasks) — *measured_by*
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *measured_by*
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Few-shot prompting** (measurements) — *measured_by*
  - [DeFT: Decoding with Flash Tree-attention for Efficient Tree-structured LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6df53f082619d02b9fad64a022e5de3-Paper-Conference.pdf)
- **Code debugging** (behaviors tasks) — *measured_by*
  - [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.80.pdf)
