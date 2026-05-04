# BigCodeBench
**Type:** Measurement  
**Referenced in:** 23 papers  
**Also known as:** BigCodeBench-Full-Instruct, BigCodeBench-Complete, BigCodeBench-Instruct  

## State of the Field

Across the surveyed literature, BigCodeBench is a benchmark predominantly used to evaluate the code generation capabilities of large language models, particularly in Python. The most common framing is its use for assessing a model's ability to generate code that correctly utilizes diverse library APIs and function calls, with one paper specifying it contains "1,140 fine-grained tasks" from "139 libraries and 7 domains". The benchmark is operationalized in multiple ways to target different programming scenarios: `BigCodeBench-Complete` evaluates generation from structured docstrings, while `BigCodeBench-Instruct` focuses on generating code from short, natural-language instructions. A variant named `BigCodeBench-Full-Instruct` is also described as a large-scale, single-turn code generation benchmark. Beyond general code generation, several papers state that BigCodeBench measures a model's capacity for `tool use`, specifically its ability to call external functions. A single paper also suggests it assesses `compositional reasoning`, as its tasks frequently require a sequence of function calls for a solution.

## Sources

**[ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding](https://proceedings.iclr.cc/paper_files/paper/2025/file/23ff02034404b65776080cbf7148addd-Paper-Conference.pdf)**
> A benchmark designed to evaluate a code model's ability to generate code that correctly utilizes various library APIs in a completion setting.

**[ConvCodeWorld: Benchmarking Conversational Code Generation in Reproducible Feedback Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/6091f2bb355e960600f62566ac0e2862-Paper-Conference.pdf) (as "BigCodeBench-Full-Instruct")**
> A large-scale, single-turn Python code generation benchmark with challenging problem sets and comprehensive test coverage, used as the basis for CONVCODEWORLD.

**[BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf) (as "BigCodeBench-Complete")**
> The structured-docstring version of BigCodeBench used to evaluate code generation from verbose programming prompts.

**[BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf) (as "BigCodeBench-Instruct")**
> A variant of BigCodeBench that evaluates instruction-to-code generation, where models generate code from short, natural-language-oriented instructions.

## Relationships

### → BigCodeBench
- **Code generation** (behaviors tasks) — *measured_by*
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *measured_by*
  > We introduce BigCodeBench, a new high-quality programming benchmark constructed via the collaboration between human experts and LLMs, assessing the capability of tool use and complex instruction following. (Section 6)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **Compositional reasoning** (constructs) — *measured_by*
  > BigCodeBench frequently invokes a sequence of function calls from multiple libraries to solve a single task, requiring significant compositional reasoning ability for task-solving. (Section 3)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *measured_by*
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf)
