# Llama-Guard
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, Llama-Guard is consistently described as a model used for safety evaluation. It is defined as a "dedicated safety classifier LLM" trained to detect unsafe content, and it is applied to both prompts and generated responses. Papers use Llama-Guard to operationalize safety assessment in a few ways: one study uses it to "determine the safety of the responses" from another model, while another employs it to evaluate "bypass rates," which are defined as the percentage of malicious requests it misclassifies as safe. In addition to its role as an evaluation tool, one paper also frames Llama-Guard as a deployable "safety mechanism" designed to "detect and filter adversarial or harmful prompts" in settings like multi-agent systems. The effectiveness of Llama-Guard itself is also a subject of study, with one paper noting that it can "fail to defend against" certain attacks.

## Sources

**[TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)**
> A safety evaluation model used to judge whether generated responses are safe.

**[Using Shapley interactions to understand how models use structure](https://aclanthology.org/2025.acl-long.1012.pdf) (as "LlamaGuard")**
> A dedicated safety classifier LLM trained to detect unsafe prompts or responses, used to evaluate bypass rates under adversarial tokenization.

## Relationships

### → Llama-Guard
- **Harmlessness** (constructs) — *measured_by*
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
