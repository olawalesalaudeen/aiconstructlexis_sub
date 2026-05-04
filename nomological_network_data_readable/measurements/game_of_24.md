# Game of 24
**Type:** Measurement  
**Referenced in:** 17 papers  
**Also known as:** Game 24, Game24  

## State of the Field

Game of 24 is predominantly described as a benchmark for mathematical reasoning. Across the provided sources, the task is consistently defined: an agent must use four given numbers and basic arithmetic operations (+, −, ×, /) to construct an expression that evaluates to 24. The prevailing use of this benchmark is to measure mathematical reasoning, a connection supported by the largest number of papers. A smaller line of work also frames it as a benchmark for planning, with one definition stating it evaluates "combinatorial search and planning ability." Less frequently, Game of 24 is used to assess logical reasoning, decision-making, and general problem-solving. While several papers associate it with measuring commonsense knowledge, the provided data does not contain specific evidence detailing this relationship.

## Sources

**[Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)**
> A mathematical reasoning and search benchmark in which an agent must combine four numbers with arithmetic operations to obtain 24.

**[Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf) (as "Game 24")**
> A mathematical reasoning benchmark where the goal is to form an equation that evaluates to 24 using a given set of integers.

**[Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf) (as "Game24")**
> Planning and reasoning benchmark where models must use four numbers and basic arithmetic operations to reach 24, evaluating combinatorial search and planning ability.

## Relationships

### → Game of 24
- **Mathematical reasoning** (constructs) — *measured_by*
  > IGE reaches 100% success rate on Game of 24 (Yao et al., 2023a), a standard mathematical reasoning and search problem, 70.8% faster than classic graph search.
  - [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf)
- **Planning** (constructs) — *measured_by*
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Learning to Search from Demonstration Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdf80d651420b47da80f789f2631b1b5-Paper-Conference.pdf)
- **Decision-making** (constructs) — *measured_by*
  > "we conduct extensive experiments on Game of 24 (Yao et al., 2023), WebShop (Yao et al., 2022a), ToolBench (Qin et al., 2023c) and RestBench (Song et al., 2023) datasets"
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > the performance comparison on the Game of 24 validates the effectiveness of the FoT in the mathematical and logical reasoning task. (Section 4.6)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > We assess the effectiveness of our proposed FOA framework through comparisons with representative SOTA methods on a judicious mix of tasks that require a variety of reasoning, planning, and general problem-solving skills.
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)

### Associated with
- **Evaluation** (behaviors tasks)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
