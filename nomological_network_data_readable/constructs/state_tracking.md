# State tracking
**Type:** Construct  
**Referenced in:** 23 papers  
**Also known as:** State Tracking, State-tracking, Fluent tracking, Task tracking, Stateful processing, Variable Assignment, Variable tracking, Tracking past actions, Board state prediction, Quantity tracking  

## State of the Field

The prevailing definition across the provided papers characterizes state tracking as a model's ability to maintain and update an internal representation of a system's state based on a sequence of inputs, updates, or actions. This general construct is specified in several ways, including tracking the values of variables ("Variable tracking"), the properties of objects after actions ("Fluent tracking"), the progress of a task ("Task tracking"), or a running total of items ("Quantity tracking"). The field operationalizes this ability through various measurement tasks, such as "Variable Assignment," which requires a model to recall the latest value of a variable, and "Board state prediction," which involves reconstructing a game state from a sequence of moves. The RULER benchmark is also explicitly used to measure state tracking through its variable tracking tasks. State tracking is frequently discussed in the context of complex behaviors like code generation and reasoning, where models are reported to struggle. For example, failures in task tracking are linked to observable errors like "not completing all steps, performing them in the wrong order, or undoing completed steps" (PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks). The construct is also studied alongside planning, theory of mind, mathematical reasoning, and long-context processing, and is reported by one paper to influence plan generation.

## Sources

**[Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)**
> The ability to maintain and update an internal representation of state over a sequence of inputs, crucial for complex reasoning and coding tasks.

**[Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf) (as "State-tracking")**
> The ability of a model to maintain and update an internal representation of a system's state based on a sequence of observed updates.

**[ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf42f133f355e0e07a8957b508b26a1b-Paper-Conference.pdf) (as "State Tracking")**
> The ability to maintain a complete and accurate representation of all properties (fluents) in the world after a sequence of actions has occurred.

**[ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf42f133f355e0e07a8957b508b26a1b-Paper-Conference.pdf) (as "Fluent tracking")**
> The ability to infer which properties of an object remain valid after a sequence of actions from the changed state.

**[PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cf318fbeec1126da21e9185ae9908c-Paper-Conference.pdf) (as "Task tracking")**
> The ability to maintain an internal state of task progress, including which sub-goals have been completed and which are still pending, especially in the presence of a partner's actions.

**[Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf) (as "Stateful processing")**
> The ability to maintain and update an internal state based on a sequence of operations described in the context.

**[Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf) (as "Variable tracking")**
> The task of keeping track of the changing values of variables that are updated multiple times within a long context.

**[Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf) (as "Variable Assignment")**
> A synthetic task where the model must output the latest value for a named variable based on a sequence of repeated assignments.

**[RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b44ee74539ea77d6a0d50d468724371-Paper-Conference.pdf) (as "Tracking past actions")**
> The observable behavior of maintaining and reasoning about the history of actions taken during a task trajectory.

**[What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vafa25a/vafa25a.pdf) (as "Board state prediction")**
> The model reconstructs the full board configuration in Othello from a sequence of moves, going beyond next-token prediction to infer latent state.

**[Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf) (as "Quantity tracking")**
> Maintaining and updating a running total of items through a sequence of add and subtract operations.

## Relationships

### State tracking →
- **RULER** (measurements) — *measured_by*
  > “This benchmark comprises four types of synthetic tasks across variable sequence lengths (4K to 128K): Needle-in-a-haystack (NIAH) retrieval, Multi-hop Tracing with Variable Tracking (VT)”
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **Plan generation** (behaviors tasks) — *causes*
  - [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.440.pdf)

### Associated with
- **Coin Flip** (measurements)
  - [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf)
- **Planning** (constructs)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **Theory of mind** (constructs)
  - [Explore Theory of Mind: program-guided adversarial data generation for theory of mind reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a901d5540789a086ee0881a82211b63d-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  - [Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  - [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **World modeling** (constructs)
  - [Mastering Board Games by External and Internal Planning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schultz25a/schultz25a.pdf)
- **Long-context processing** (constructs)
  - [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beck25b/beck25b.pdf)
