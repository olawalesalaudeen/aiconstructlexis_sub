# Direct prompting
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** Direct Prompting, DIRECT PROMPT  

## State of the Field

Across the surveyed literature, "Direct prompting" is most commonly described as an evaluation protocol where a language model is directly queried to generate a prediction or response for a given task. This method is frequently positioned as a baseline for comparison against other techniques, such as embedding-based classification or more complex reasoning approaches. The prevailing operationalization involves providing a model with test questions or examples and asking it to infer an output "without intermediate reasoning steps" (`Hypothesis Search: Inductive Reasoning with Language Models`), a framing that is sometimes explicitly contrasted with Chain-of-Thought prompting. However, a minority view defines it as a "textual reasoning mode" that incorporates Chain-of-Thought examples to decompose and verify answers for TableQA (`Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA`). The applications of this method are varied, including testing for memorized private content, generating structured forecasts, and performing zero-shot classification. As a measurement procedure, direct prompting is used to assess constructs such as `Programming ability` and `Natural language understanding`. Some sources characterize it as a "naïve approach" (`X-FLoRA: Cross-modal Federated Learning with Modality-expertLoRAfor MedicalVQA`), reinforcing its common role as a straightforward baseline.

## Sources

**[Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)**
> Human evaluation protocol where language models are directly queried for predictions to compare against embedding-based zero-shot classification.

**[Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf) (as "Direct Prompting")**
> A textual TableQA prompting procedure that uses prompts such as Chain-of-Thought examples or zero-shot instructions to decompose, reason, and verify answers.

**[Context is Key: A Benchmark for Forecasting with Essential Textual Information](https://raw.githubusercontent.com/mlresearch/v267/main/assets/williams25a/williams25a.pdf) (as "DIRECT PROMPT")**
> A prompt-based evaluation method where an LLM is instructed to directly output a forecast as a structured output for all required timestamps in a single pass.

## Relationships

### → Direct prompting
- **Programming** (behaviors tasks) — *measured_by*
  - [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://proceedings.iclr.cc/paper_files/paper/2025/file/f12b4df26344f3be803c06b555252efe-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  - [Topic Coverage-based Demonstration Retrieval for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1008.pdf)
