# CruxEval
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** CRUXEVAL, CRUXEval, CRUX  

## State of the Field

Across the surveyed literature, CruxEval is consistently described as a benchmark for evaluating the capabilities of large language models in the domain of code. The prevailing usage of this instrument is to measure constructs of "code reasoning," "code understanding," and "code execution." This is operationalized through the task of code output prediction, where models are evaluated on their ability to predict the execution results of code snippets. While "code reasoning" is the most frequently targeted construct, a smaller set of studies uses CruxEval to assess more specific reasoning types, including deductive, abductive, and logical reasoning. In one instance, it is also used to evaluate "commonsense knowledge." One paper notes that the benchmark's coverage "remains incomplete with respect to real-world repository-scale tasks" (RuCCoD: Towards AutomatedICDCoding inRussian).

## Sources

**[LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf) (as "CRUXEVAL")**
> A benchmark that measures reasoning and execution abilities through code output prediction.

**[Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf) (as "CRUXEval")**
> A benchmark designed to evaluate code understanding and execution, used in the paper to test both deductive and abductive code reasoning.

**[As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf) (as "CRUX")**
> A benchmark used to evaluate a model's reasoning abilities in the context of code generation and understanding.

**[CodeIO: Condensing Reasoning Patterns via Code Input-Output Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25t/li25t.pdf)**
> CruxEval is a benchmark for evaluating code understanding and execution-result prediction.

## Relationships

### → CruxEval
- **Code reasoning** (constructs) — *measured_by*
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
- **Code execution** (behaviors tasks) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Abductive reasoning** (constructs) — *measured_by*
  > Deductive code and abductive code reasoning can be regarded as opposite processes; therefore, we selected two identical and representative datasets, CRUXEval (Gu et al., 2024) and LiveCodeBench (Jain et al., 2024), as benchmarks to validate these two capabilities.
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)

### Associated with
- **Code execution** (behaviors tasks)
  > The code execution scenario is based on the output prediction setup used in CRUXEVAL (Gu et al., 2024).
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
