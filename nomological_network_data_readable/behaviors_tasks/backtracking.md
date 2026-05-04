# Backtracking
**Type:** Behavior  
**Referenced in:** 16 papers  
**Also known as:** Branching and backtracking, State traceback, State rollback  

## State of the Field

Across the provided literature, backtracking is predominantly characterized as a behavior where a model or agent returns to a previous state to correct an error or explore an alternative path. The most common framing presents it as an autonomous error-correction mechanism during complex reasoning, where a model “explores multiple paths (branching) and reverts to earlier points if a particular path proves wrong” (Demystifying Long Chain-of-Thought Reasoning). A more specialized line of work defines backtracking as a safety-oriented behavior, operationalized by the model emitting a special `[RESET]` token to “undo” and recover from its own unsafe generation. A few papers also describe it as an interactive feature, termed “state rollback” or “dialog backtracking,” which allows a human user to revert the system to a prior state for correction. Backtracking is consistently studied in the context of advanced reasoning and is frequently associated with Chain-of-thought and Long Chain-of-Thought reasoning, with some papers suggesting these reasoning strategies enable or encourage the behavior. The function of this behavior is often to mitigate error propagation; one paper notes that its absence means “an early misstep... cannot be corrected, resulting in deteriorated performance.” The behavior is also studied alongside Planning and Non-monotonic reasoning and is reported to contribute to model Safety.

## Sources

**[Backtracking Improves Generation Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/65beb73449888fabcf601b3a3ef4b3a7-Paper-Conference.pdf)**
> The observable behavior of a model first generating a partial unsafe response, then emitting a special [RESET] token, and finally re-generating a safe response from scratch.

**[Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf) (as "Branching and backtracking")**
> An observable reasoning pattern where the model explores multiple solution paths (branching) and returns to an earlier point upon identifying a flawed path (backtracking).

**[MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bc/zhang25bc.pdf) (as "State traceback")**
> Returning to a previous step or state to correct earlier mistakes or refine intermediate outputs.

**[ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.227.pdf) (as "State rollback")**
> The observable behavior of reverting the agent system to a prior execution state upon user intervention, allowing resumption from that point without full restart.

## Relationships

### Backtracking →
- **Error propagation** (constructs) — *causes*
  > The performance drop highlights the importance of backtracking in mitigating error propagation, where an early misstep without backtracking cannot be corrected, resulting in deteriorated performance. (Section 5.3)
  - [End-to-End Learnable Psychiatric Scale Guided Risky Post Screening for Depression Detection on Social Media](https://aclanthology.org/2025.emnlp-main.202.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [End-to-End Learnable Psychiatric Scale Guided Risky Post Screening for Depression Detection on Social Media](https://aclanthology.org/2025.emnlp-main.202.pdf)
- **Robustness** (constructs) — *causes*
  - [End-to-End Learnable Psychiatric Scale Guided Risky Post Screening for Depression Detection on Social Media](https://aclanthology.org/2025.emnlp-main.202.pdf)

### → Backtracking
- **Chain-of-thought reasoning** (constructs) — *causes*
  > The Transformer model simulates logical assumption, deduction, and backtracking by generating new tokens and ultimately outputs a SAT/UNSAT label as the result of the 3-SAT decision problem.
  - [Can Transformers Reason Logically? A Study in SAT Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25d/pan25d.pdf)

### Associated with
- **Chain-of-thought reasoning** (constructs)
  > The backtrack operation involves multiple actions, as the policy specifies how many steps to backtrack.
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Planning** (constructs)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **Non-monotonic reasoning** (constructs)
  - [ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25i/lin25i.pdf)
