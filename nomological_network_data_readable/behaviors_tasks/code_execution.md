# Code execution
**Type:** Behavior  
**Referenced in:** 17 papers  
**Also known as:** Execution reasoning, Output prediction  

## State of the Field

Across the surveyed literature, code execution is most commonly characterized as the observable behavior of a model running generated code within an interpreter and receiving the output. This behavior is frequently framed as a form of tool use for tasks like computation, data analysis, and arithmetic. Several papers describe its application in multi-step problem-solving, where a model can "generate and execute code incrementally" and use the results for self-correction ("Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification"). The behavior is operationalized and measured using benchmarks such as CruxEval and LiveCodeBench. A distinct, less common line of work treats this concept as a reasoning task, using terms like "execution reasoning" or "output prediction," where the goal is to predict a program's output rather than run the code. Another minority view defines it as "plan execution," where running code is one step in a larger planned sequence. Code execution is studied alongside tool use and is reported to influence evaluation, while difficulties in reasoning about execution are reported to affect test generation.

## Sources

**[GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)**
> The observable process where the model runs generated code within an interpreter and receives the output.

**[SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf) (as "Execution reasoning")**
> The observable task of predicting program outputs given inputs or inferring inputs given outputs, often involving step-by-step simulation.

**[From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf) (as "Plan execution")**
> Retrieving and running code snippets associated with chosen models to perform the steps of a planned action sequence.

**[Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf) (as "Output prediction")**
> Predicting the final output of a program given the program and its inputs.

## Relationships

### Code execution →
- **Critique** (behaviors tasks) — *causes*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **CruxEval** (measurements) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **LiveCodeBench** (measurements) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Test generation** (constructs) — *causes*
  > This is primarily due to models struggling to reason about execution, and their frequent assertion errors when addressing complex code paths.
  - [TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/26ded5c8ee8ec1bc4caced4e1c9b1584-Paper-Conference.pdf)

### Associated with
- **Tool use** (behaviors tasks)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **CruxEval** (measurements)
  > The code execution scenario is based on the output prediction setup used in CRUXEVAL (Gu et al., 2024).
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
