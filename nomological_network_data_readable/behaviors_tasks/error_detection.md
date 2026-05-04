# Error detection
**Type:** Behavior  
**Referenced in:** 27 papers  
**Also known as:** Bug detection, Accounting bug detection, Error awareness, Stepwise error detection, Invalid node identification, Fault localization, Misleading region localization  

## State of the Field

Across the provided literature, "Error detection" is a behavior centered on identifying mistakes, failures, or bugs across various domains. The most common operationalization is in the context of software, where it is frequently termed "bug detection" or "fault localization." In this framing, the task involves identifying specific vulnerabilities in source code, such as "divide-by-zero, cross-site scripting" or common software weaknesses like "Null Pointer Dereference (NPD), Memory Leak (MLK), or Use-After-Free (UAF)." A second prevalent line of work treats error detection as the identification of flaws in reasoning processes, such as an agent identifying mistakes in its own or another's actions, or examining a single step in a solution to "determine its correctness." The behavior is also studied in more specialized contexts, including identifying the presence of errors in videos ("Error Awareness"), localizing deceptive regions in charts, or finding chemical errors in molecular descriptions. The required granularity of detection varies across these operationalizations. Some tasks only require binary identification of an error's presence, while others demand precise localization. For instance, "Misleading region localization" involves outputting the coordinates of a deceptive area, and "Error localization" requires pinpointing the "specific erroneous text spans" in a description. Similarly, "Invalid node identification" aims to find the specific points in a reasoning chain "where the logical progression or coherence breaks down."

## Sources

**[LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf) (as "Bug detection")**
> The observable task of identifying specific categories of vulnerabilities or errors in source code, such as divide-by-zero, cross-site scripting, or OS command injection.

**[Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf)**
> The observable process of an agent identifying mistakes or failures in its own or another agent's reasoning or actions.

**[Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1d8400fec75f683c4d823f5836a81bb-Paper-Conference.pdf) (as "Accounting bug detection")**
> Identifying smart-contract statements or code regions that violate domain-specific financial-model constraints.

**[Targeted Syntactic Evaluation for Grammatical Error Correction](https://aclanthology.org/2025.acl-long.1027.pdf) (as "Error awareness")**
> The observable task of identifying the presence of general errors in a given video, typically evaluated with binary (Yes/No) questions.

**[Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bb/wang25bb.pdf) (as "Stepwise error detection")**
> The observable task of examining a specified step within a given solution to a problem and determining whether that step is correct or incorrect.

**[SafeKey: Amplifying Aha-Moment Insights for Safety Reasoning](https://aclanthology.org/2025.emnlp-main.1292.pdf) (as "Invalid node identification")**
> The task of identifying the specific papers within an invalid reasoning chain where the logical progression or coherence breaks down.

**[RuCCoD: Towards AutomatedICDCoding inRussian](https://aclanthology.org/2025.emnlp-main.130.pdf) (as "Fault localization")**
> Identifying the source of a bug or failure within code or a repository.

**[DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.695.pdf) (as "Misleading region localization")**
> The observable task of identifying and outputting the coordinates of specific regions within a chart that are considered deceptive or misleading.

**[Mitigating Hallucinations inLM-BasedTTSModels via Distribution Alignment UsingGFlowNets](https://aclanthology.org/2025.emnlp-main.977.pdf) (as "Error localization")**
> The observable task of pinpointing the specific contiguous span of text within a molecular description that contains a chemical error.

## Relationships

### Error detection →
- **Self-reflection** (behaviors tasks) — *causes*
  - [FinRAGBench-V: A Benchmark for MultimodalRAGwith Visual Citation in the Financial Domain](https://aclanthology.org/2025.emnlp-main.212.pdf)
