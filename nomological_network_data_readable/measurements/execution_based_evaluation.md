# Execution-based evaluation
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Sandbox execution, Execution-based focused evaluation  

## State of the Field

Across the provided literature, execution-based evaluation is predominantly framed as a method for verifying task completion or code correctness by programmatically running a model's output in a computational environment. This approach is explicitly contrasted with static methods like string matching. The most common operationalization involves executing generated code against a set of test cases to determine if the output matches expected results, a procedure one paper describes as measuring the "success rate" ("McEval: Massively Multilingual Code Evaluation"). A related approach, used for agent-based tasks, verifies completion by using a custom script to check the "final state of the computer environment" ("OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"). Some work emphasizes safety, implementing this evaluation within a secure, isolated "sandbox environment" such as a Docker container to validate correctness ("SelfCodeAlign: Self-Alignment for Code Generation"). A more specialized variant, "execution-based focused evaluation," is applied to database tasks, where scripts programmatically retrieve results and assess success by concentrating on the "essential components of the answers" ("Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows").

## Sources

**[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)**
> A method of evaluation where task completion is verified by a custom script that checks the final state of the computer environment, rather than relying on static demonstrations or string matching.

**[SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf) (as "Sandbox execution")**
> An evaluation procedure where model-generated code and test cases are executed in a secure, isolated environment to validate correctness.

**[Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://proceedings.iclr.cc/paper_files/paper/2025/file/46c10f6c8ea5aa6f267bcdabcb123f97-Paper-Conference.pdf) (as "Execution-based focused evaluation")**
> An evaluation protocol where scripts programmatically obtain results from the database and assess success by focusing on the essential components of the answer, ignoring non-essential columns.
