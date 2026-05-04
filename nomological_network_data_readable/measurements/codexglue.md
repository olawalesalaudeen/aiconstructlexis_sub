# CodeXGLUE
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** CodeXGlue  

## State of the Field

Across the provided literature, CodeXGLUE is consistently described as a benchmark suite for evaluating programming language models on various code intelligence tasks. The papers do not present a single, unified purpose, but rather use different components of the suite to measure distinct behaviors. One common application is for code-to-text tasks, where it is used to evaluate the generation of "a natural language explanation of the code," a behavior also identified as code summarization. Another prevalent use is for assessing code defect detection, which is operationalized as a binary classification task to identify insecure C code and is linked to the behavior of code debugging. Additionally, CodeXGLUE is used to evaluate models on single-file code completion. The suite is noted to contain datasets such as PY150 and the Github Java Corpus, and is employed in evaluation settings like "3-shot evaluations."

## Sources

**[LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf) (as "CodeXGlue")**
> CodeXGlue is a code-to-text benchmark used here to evaluate natural-language explanation of code snippets.

**[CODE REPRESENTATION LEARNING AT SCALE](https://proceedings.iclr.cc/paper_files/paper/2024/file/cfbba5249393100ada0bfb37557d2fd9-Paper-Conference.pdf)**
> A benchmark suite for code intelligence that includes the task of code defect detection in the C programming language.

## Relationships

### → CodeXGLUE
- **Code debugging** (behaviors tasks) — *measured_by*
  - [ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding](https://proceedings.iclr.cc/paper_files/paper/2025/file/23ff02034404b65776080cbf7148addd-Paper-Conference.pdf)
- **Code summarization** (behaviors tasks) — *measured_by*
  - [YESciEval: RobustLLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.676.pdf)
