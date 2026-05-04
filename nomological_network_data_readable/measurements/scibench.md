# SciBench
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

SciBench is consistently described as a benchmark suite designed to evaluate scientific reasoning through complex, multi-step questions in physics, chemistry, and biology. The tasks are framed as requiring the integration of knowledge, reasoning over evidence, and the application of scientific principles. Across the provided literature, its most common application is to measure scientific reasoning and the related behaviors of scientific question answering and scientific problem solving. The benchmark is also used to assess more specific domains, with individual papers employing it to evaluate chemical reasoning and mathematical reasoning. Beyond these scientific applications, SciBench is sometimes used to measure broader cognitive capabilities. For instance, one study uses it to verify generalization, noting the benchmark is from "a totally different distributions compared to training data" ("MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems"), while another connects it to measuring commonsense knowledge.

## Sources

**[Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)**
> A benchmark suite for scientific reasoning that includes complex, multi-step questions across physics, chemistry, and biology.

## Relationships

### → SciBench
- **Scientific reasoning** (constructs) — *measured_by*
  - [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
- **Chemical reasoning** (constructs) — *measured_by*
  - [ChemAgent: Self-updating Memories in Large Language Models Improves Chemical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa7f64b45970e6a7f8824781e7e01501-Paper-Conference.pdf)
- **Scientific question answering** (behaviors tasks) — *measured_by*
  > SciBench (Wang et al., 2024a) is a benchmark suite of scientific reasoning tasks, where the objective is to answer complex, multi-step scientific questions that require integrating knowledge, reasoning over evidence, and applying scientific principles. (Section 4.4. SciBench)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **Generalization** (constructs) — *measured_by*
  > Among these, AIME-2024, HumanEval, HumanEval+, GPQA, and SciBench are from a totally different distributions compared to training data, serving to verify the generalization capability of MAS-GPT. (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **Scientific problem solving** (behaviors tasks) — *measured_by*
  - [SHARP: Steering Hallucination inLVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.726.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > We assess the effectiveness of our proposed FOA framework through comparisons with representative SOTA methods on a judicious mix of tasks that require a variety of reasoning, planning, and general problem-solving skills.
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
