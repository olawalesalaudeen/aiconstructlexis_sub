# Instruction understanding
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Instruction comprehension, Input comprehension  

## State of the Field

Across the provided literature, instruction understanding is predominantly characterized as a latent ability of a model to comprehend the meaning and intent of an input. Definitions vary in scope, with some focusing on mapping task instructions to "appropriate actions in constrained environments" ("Plan Dynamically, Express Rhetorically..."), while others describe a broader "input comprehension" of context-sensitive language that occurs prior to output generation ("NitiBench..."). One paper posits that failures in this internal comprehension can be masked by otherwise coherent outputs, suggesting that "high-confidence generation masks a fundamental interpretive error." The construct is frequently studied in specialized domains with "intricate terminologies" like healthcare, as well as in embodied contexts involving "sequential navigation and manipulation." Instruction understanding is operationalized through its effect on downstream tasks; for example, it is reported to influence a model's performance in robotic manipulation. One paper proposes that internal comprehension could be measured by analyzing "surprisal and related features derived from input token probabilities." The construct is also studied in relation to code generation, which is presented as a factor that can influence it.

## Sources

**[Plan Dynamically, Express Rhetorically: A Debate-Driven Rhetorical Framework for Argumentative Writing](https://aclanthology.org/2025.emnlp-main.484.pdf) (as "Instruction comprehension")**
> The model's ability to understand task instructions and map them to appropriate actions in constrained environments.

**[Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.983.pdf)**
> The latent ability of an LLM to comprehend the meaning and intent of an instruction, particularly in specialized domains with complex terminology.

**[NitiBench: BenchmarkingLLMFrameworks onThai Legal Question Answering Capabilities](https://aclanthology.org/2025.emnlp-main.1740.pdf) (as "Input comprehension")**
> The latent ability of a language model to correctly interpret the meaning of an input sequence, particularly in context-sensitive or non-literal constructions, prior to generating any output.

## Relationships

### Instruction understanding →
- **Robotic manipulation** (behaviors tasks) — *causes*
  - [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf)

### → Instruction understanding
- **Code generation** (behaviors tasks) — *causes*
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
