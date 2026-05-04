# Code editing
**Type:** Behavior  
**Referenced in:** 16 papers  
**Also known as:** Program editing, Code modification, Code refinement, Code deletion, Code insertion, Multi-file code refactoring, Program revision, CSS style adjustment, Code refactoring  

## State of the Field

Across the surveyed literature, code editing is most commonly defined as the task of modifying an existing program based on a natural-language instruction. A broader framing, found in several papers, describes it as 'code refinement' or 'code modification'—the general process of improving, correcting, or altering source code to implement fixes or new features. The behavior is operationalized at various levels of granularity, from atomic actions like 'code insertion' and 'code deletion' to more complex tasks like 'code refactoring,' which involves rewriting code to improve its structure while preserving functionality. One paper highlights that 'multi-file refactoring requires comprehensive reasoning and composition of multiple smaller changes' (RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code). To measure this behavior, researchers use benchmarks such as DS-1000. Some definitions also emphasize an iterative process, such as 'program revision,' which involves updating code using feedback from execution traces or rewards. In a specialized context, the task is framed as 'CSS style adjustment,' where an agent edits styles to match a visual target. Code editing is studied alongside 'compositional reasoning,' and one paper suggests that reasoning about edits can aid in 'generalization'.

## Sources

**[Learning to Edit Visual Programs with Self-Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/c585301e1c4b7c50039de5413ef585b5-Paper-Conference.pdf) (as "Program editing")**
> The task of modifying an existing program in a goal-directed manner to alter its output or correct errors.

**[SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)**
> Editing an existing program according to a natural-language instruction to produce an updated code snippet.

**[MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d1f02132ef51602adf07000ca5b6138-Paper-Conference.pdf) (as "Code modification")**
> The observable action of altering existing source code by adding, deleting, or changing lines to implement a fix or new feature.

**[Source Code Foundation Models are Transferable Binary Analysis Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/cc83e97320000f4e08cb9e293b12cf7e-Paper-Conference.pdf) (as "Code refinement")**
> The task of improving or correcting an existing piece of source code.

**[RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b44ee74539ea77d6a0d50d468724371-Paper-Conference.pdf) (as "Multi-file code refactoring")**
> Editing code across multiple files to implement a specified refactor in a repository.

**[Let the Code LLM Edit Itself When You Edit the Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/9530635032b95cea9585bd800d308300-Paper-Conference.pdf) (as "Code insertion")**
> An observable code editing task where new lines of code are inserted into an existing context before the model is required to perform a prediction.

**[Let the Code LLM Edit Itself When You Edit the Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/9530635032b95cea9585bd800d308300-Paper-Conference.pdf) (as "Code deletion")**
> An observable code editing task where existing lines of code are removed from a context before the model is required to perform a prediction.

**[Synthesizing Programmatic Reinforcement Learning Policies with Large Language Model Guided Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf887f2bfe2776584e3bce80ed206ef-Paper-Conference.pdf) (as "Program revision")**
> Updating previously generated programs using feedback such as rewards or execution traces.

**[VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/eea71dc576381b88f2a0ca4dedc2140d-Paper-Conference.pdf) (as "CSS style adjustment")**
> The task of iteratively editing CSS style rules to make a web page's rendering match a target design.

**[Position: Future Research and Challenges Remain Towards AI for Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gu25e/gu25e.pdf) (as "Code refactoring")**
> The observable act of rewriting parts of a software implementation to improve its structure or quality while preserving its external functionality.

## Relationships

### Code editing →
- **DS-1000** (measurements) — *measured_by*
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  > Reasoning over the differences between the two states admits a more local task (as evidenced by our data efficient learning), and this property can aid in generalization. (Appendix B.1)
  - [Learning to Edit Visual Programs with Self-Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/c585301e1c4b7c50039de5413ef585b5-Paper-Conference.pdf)

### Associated with
- **Compositional reasoning** (constructs)
  > Unlike isolated function-level edits, multi-file refactoring requires comprehensive reasoning and composition of multiple smaller changes. (Section 1)
  - [RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b44ee74539ea77d6a0d50d468724371-Paper-Conference.pdf)
