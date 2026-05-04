# Code debugging
**Type:** Behavior  
**Referenced in:** 60 papers  
**Also known as:** Code defect detection, Bug fixing, Code repair, Debugging, Self-repair, First error step identification, Self-debugging, Automatic debugging, Runtime debugging, Bug identification, Error correction, Crash resolution, Program repair, Data science code debugging, Code refinement, Code correction, Code repair capability  

## State of the Field

Across the provided literature, code debugging is most commonly described as the behavior of identifying and fixing errors in code, a process also referred to as "bug fixing" or "code repair." While this dual action is the prevailing framing, a smaller line of work isolates these as distinct sub-tasks, such as "error localization" or "program repair." Other definitions are more specific, focusing on interactive modification based on runtime feedback or resolving system-level issues like kernel crashes. This behavior is operationalized and measured using a range of benchmarks, including InfiniteBench, CodeXGLUE, LiveCodeBench, Codeforces, APPS, and Defects4J. A recurring element in its operationalization is the use of feedback, where a model is given an "exception message or a failing test case" to guide its correction, a process often called "self-repair" or "self-debugging" ("LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code"). The behavior is studied alongside related concepts like iterative refinement, self-reflection, and code generation. Some research suggests that code debugging performance is influenced by factors such as in-context learning and model scalability.

## Sources

**[Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)**
> The process of interactively modifying and correcting code based on feedback from a runtime environment to resolve errors and achieve successful execution.

**[CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf) (as "Code repair")**
> The observable task of identifying and fixing errors in a provided code snippet to make it correct.

**[SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf) (as "Bug fixing")**
> The observable task of identifying and correcting errors or unintended behaviors in a software codebase based on a problem description.

**[SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf) (as "Error localization")**
> The observable action of identifying and indicating the specific step in a reasoning chain that contains a flaw or error.

**[ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding](https://proceedings.iclr.cc/paper_files/paper/2025/file/23ff02034404b65776080cbf7148addd-Paper-Conference.pdf) (as "Code defect detection")**
> The task of identifying whether a given code snippet contains bugs, vulnerabilities, or other defects.

**[WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf) (as "Debugging")**
> The task of identifying and fixing errors in existing computer code.

**[LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf) (as "Self-repair")**
> The observable task of fixing an incorrect program after being provided with error feedback, such as an exception message or a failing test case.

**[MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf) (as "First error step identification")**
> The observable sub-task of identifying the specific initial step in a flawed reasoning process where the logic first deviates from a correct path.

**[DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50e9ad960ae78b741a6b4fea533f2eaf-Paper-Conference.pdf) (as "Self-debugging")**
> The observable process where a model identifies errors in its own generated code or reasoning and attempts to correct them.

**[A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf) (as "Automatic debugging")**
> The task of inferring the state of a program, such as the value of a variable at a specific line, given only partial code.

**[AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf) (as "Runtime debugging")**
> Diagnosing and fixing issues that arise during code execution.

**[Position: Scaling LLM Agents Requires Asymptotic Analysis with LLM Primitives](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meyerson25a/meyerson25a.pdf) (as "Bug identification")**
> The action of locating and describing a flaw or error within a piece of code.

**[MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf) (as "Error correction")**
> The observable task of generating a revised version of an incorrect reasoning step to rectify the identified error.

**[kGym: A Platform and Dataset to Benchmark Large Language Models on Linux Kernel Crash Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/8e9ed2a28af7d9085180e3817b2c9a57-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Crash resolution")**
> Editing the kernel so that the reproducer no longer causes a crash within the allotted execution window.

**[Hints-In-Browser: Benchmarking Language Models for Programming Feedback Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/34cc2ded6daba59357134c0b9fb06bfe-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Program repair")**
> Generating a repaired version of a buggy program with minimal edits that preserves the original context and style.

**[SynC-LLM: Generation of Large-Scale Synthetic Circuit Code with Hierarchical Language Models](https://aclanthology.org/2025.emnlp-main.878.pdf) (as "Data science code debugging")**
> The task of identifying, localizing, and explaining logical runtime errors within Python scripts that use data science libraries.

**[Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.286.pdf) (as "Code refinement")**
> Enhancing code readability and style by adding docstrings, comments, and standardizing conventions without changing functionality.

**[MrGuard: A Multilingual Reasoning Guardrail for UniversalLLMSafety](https://aclanthology.org/2025.emnlp-main.1393.pdf) (as "Code correction")**
> The observable process of identifying an error in a generated code snippet and producing a revised version of the code to fix the error.

**[AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf) (as "Code repair capability")**
> The latent ability of an LLM to identify and correct errors in its own generated code, improving functional correctness without external fine-tuning.

## Relationships

### Code debugging →
- **InfiniteBench** (measurements) — *measured_by*
  > "Table 2 shows that our method preserves most of the model’s performance in retrieval and QA tasks, while maintaining efficacy in complex mathematical and coding tasks."
  - [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
- **CodeXGLUE** (measurements) — *measured_by*
  - [ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding](https://proceedings.iclr.cc/paper_files/paper/2025/file/23ff02034404b65776080cbf7148addd-Paper-Conference.pdf)
- **Codeforces** (measurements) — *measured_by*
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **MR-GSM8K** (measurements) — *measured_by*
  - [MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Assessing the State of the Art in Scene Segmentation](https://aclanthology.org/2025.naacl-long.501.pdf)
- **LiveCodeBench** (measurements) — *measured_by*
  > We use 7 datasets that contain problems and test cases from competitive programming contests: 1) CodeForces (8.8k problems), 2) AtCoder (1.3k problems), 3) HackerEarth (1.2k problems), 4) CodeChef (768 problems), 5) LiveCodeBench (400 problems), 6) CodeJam (180 problems), and 7) Aizu (2.2k problems) (Li et al., 2022b; Jain et al., 2024).
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **APPS** (measurements) — *measured_by*
  - [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.80.pdf)
- **Defects4J** (measurements) — *measured_by*
  - [SUE: Sparsity-based Uncertainty Estimation via Sparse Dictionary Learning](https://aclanthology.org/2025.emnlp-main.1672.pdf)

### → Code debugging
- **In-context learning** (constructs) — *causes*
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **Scalability** (constructs) — *causes*
  > Our algorithm yields a significant boost in performance compared to best-of-N and self-repair, and also exhibits strong generalisation across datasets and models. Moreover, our approach shows stronger scaling with inference-time compute budget compared to baselines.
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **Textual reasoning** (behaviors tasks) — *causes*
  - [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.80.pdf)

### Associated with
- **Critique** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Feedback generation** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks)
  - [Hints-In-Browser: Benchmarking Language Models for Programming Feedback Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/34cc2ded6daba59357134c0b9fb06bfe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coding** (behaviors tasks)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Generalization** (constructs)
  > "Our algorithm yields a significant boost in performance compared to best-of-N and self-repair, and also exhibits strong generalisation across datasets and models."
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
