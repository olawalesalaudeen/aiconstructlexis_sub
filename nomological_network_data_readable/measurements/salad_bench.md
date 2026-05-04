# SALAD-Bench
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** SALAD-BENCH  

## State of the Field

SALAD-Bench is consistently described across the provided literature as a measurement instrument for evaluating large language models. The prevailing usage is as a safety benchmark, with one paper defining it as a tool for assessing "LLM safety and its relationship to value systems," while another frames it as a dataset of "harmful prompts" for evaluating refusal mechanisms. It is reported to provide both prompts and associated "safety scores." As an instrument, SALAD-Bench is used to operationalize and measure constructs including `Safety alignment` and `Privacy awareness`. For example, one study uses it alongside the Do-Not-Answer dataset as a benchmark for safety. Another paper describes using it as a source to "construct a dataset of harmless and harmful prompts" for its own experiments.

## Sources

**[UniLR: Unleashing the Power ofLLMs on Multiple Legal Tasks with a Unified Legal Retriever](https://aclanthology.org/2025.acl-long.585.pdf)**
> Established safety benchmark providing prompts and safety scores for evaluating LLM safety and its relationship to value systems.

**[The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wollschlager25a/wollschlager25a.pdf) (as "SALAD-BENCH")**
> A dataset used as a source of harmful prompts for training and evaluating refusal mechanisms.

## Relationships

### → SALAD-Bench
- **Safety alignment** (constructs) — *measured_by*
  > We use the Antropic Hh-rlhf red-teaming prompts from Antropic (Bai et al., 2022), the Do-Not-Answer dataset (Wang et al., 2024b) and Salad Bench (Li et al., 2024b) as the benchmark. (Section 4.1)
  - [Diffusion Models Through a Global Lens: Are They Culturally Inclusive?](https://aclanthology.org/2025.acl-long.1504.pdf)
- **Privacy awareness** (constructs) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
