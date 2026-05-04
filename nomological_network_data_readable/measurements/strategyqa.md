# StrategyQA
**Type:** Measurement  
**Referenced in:** 87 papers  
**Also known as:** STRATEGYQA  

## State of the Field

Across the surveyed literature, StrategyQA is predominantly used as a benchmark to evaluate various forms of reasoning in large language models. It is consistently characterized as a question-answering dataset composed of yes/no or true/false questions that require multi-step, multi-hop, or implicit reasoning to solve. A recurring theme is that the questions demand a model to infer a solution strategy based on commonsense or world knowledge, with some papers noting that models must also generate a rationale to support their answer. The most common application of StrategyQA is to operationalize and measure constructs like `commonsense understanding`, `complex reasoning`, and `multi-hop question answering`. It is also frequently employed to assess `chain-of-thought reasoning` and general `question answering` capabilities. While the prevailing usage focuses on reasoning, a smaller set of studies applies StrategyQA in more specialized contexts, such as evaluating `adversarial robustness`, model calibration, or downstream fine-tuning performance. The format is variously described as binary, boolean, or, in one instance, a "classification-style" task.

## Sources

**[BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf)**
> A benchmark for commonsense question answering used to evaluate commonsense reasoning.

**[Adaptive Chameleon  or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://proceedings.iclr.cc/paper_files/paper/2024/file/99261adc8a6356b38bcf999bba9a26dc-Paper-Conference.pdf) (as "STRATEGYQA")**
> An implicit multi-hop question answering benchmark requiring commonsense reasoning and decomposition to answer yes/no questions.

## Relationships

### → StrategyQA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We employ Web Questions (WebQA) (Berant et al., 2013; Chang et al., 2021), MultiModalQA (Talmor et al.), ManyModalQA (Hannan et al., 2020) and StrategyQA (Geva et al., 2021a) dataset for experiments. (Section 5.1)
  - [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb113910e9c3f6242541c1652e30dfd6-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  > We select four typical complex multi-hop question-answering datasets, i.e., HotpotQA (Yang et al., 2018), 2Wiki-MultihopQA (Ho et al., 2020), MusiQue (Trivedi et al., 2022), and StrategyQA (Geva et al., 2021). (Section 5.1)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  > We use MMLU Hendrycks et al. (2020), BigBench Hard (BBH) Srivastava et al. (2022), and 4 reasoning benchmarks: GSM8K Cobbe et al. (2021), SVAMP Patel et al. (2021), ASDIV Miao et al. (2020), and StrategyQA Geva et al. (2021) (Section 3.1).
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  > Given that most commonsense reasoning datasets are structured in a multiple-choice question (MCQ) format (Talmor et al., 2019; Mihaylov et al., 2018; Geva et al., 2021), we designed a three-stage process inspired by human problem-solving strategies. (Section 1)
  - [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.503.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  > Following prior work (Zhang et al., 2024a; Chuang et al., 2023), we evaluate chain-of-thought reasoning capabilities using StrategyQA (Geva et al., 2021) and GSM8K (Cobbe et al., 2021). (Section 3.1)
  - [MAIN: Mutual Alignment Is Necessary for instruction tuning](https://aclanthology.org/2025.emnlp-main.645.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  > We conducted our confidence elicitation attacks on Meta-Llama-3-8B-Instruct (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) while performing classification on two common datasets to evaluate adversarial robustness: SST-2, AG-News and one modern dataset: StrategyQA (Geva et al., 2021). (Section 4)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **Boolean question answering** (behaviors tasks) — *measured_by*
  - [Script-Agnosticism and its Impact on Language Identification forDravidian Languages](https://aclanthology.org/2025.naacl-long.378.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [Out of Sight, Not Out of Context? Egocentric Spatial Reasoning inVLMs Across Disjoint Frames](https://aclanthology.org/2025.emnlp-main.817.pdf)

### Associated with
- **Chain-of-thought reasoning** (constructs)
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
