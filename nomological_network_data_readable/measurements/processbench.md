# PROCESSBENCH
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** ProcessBench  

## State of the Field

Across the provided sources, PROCESSBENCH is consistently described as a benchmark for evaluating a model's ability to identify errors within step-by-step mathematical reasoning. The evaluation is specifically designed to assess the identification of the *first* or *earliest* incorrect step in a solution, a focus mentioned across multiple papers. The benchmark is composed of 3,400 test cases, which are characterized as "competition- and Olympiad-level math problems" in one source and problems of "varying difficulty" in another. Each problem is paired with a solution that includes human-annotated error locations, with one paper noting that these annotations are provided by "multiple human experts." While most descriptions focus on the human annotations, one paper specifies that the benchmark assesses error detection in "LLM-generated mathematical solutions." Therefore, papers use PROCESSBENCH to operationalize and measure a model's capacity for fine-grained error detection in complex mathematical problem-solving.

## Sources

**[PunchBench: BenchmarkingMLLMs in Multimodal Punchline Comprehension](https://aclanthology.org/2025.acl-long.50.pdf)**
> A benchmark consisting of 3,400 test cases with competition- and Olympiad-level math problems, each containing a step-by-step solution with human-annotated error locations, used to assess models' ability to identify the earliest erroneous reasoning step.

**[Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mukherjee25a/mukherjee25a.pdf) (as "ProcessBench")**
> A benchmark containing human-annotated stepwise labels for mathematical solutions, used to evaluate step-level error identification with focus on the first incorrect step.
