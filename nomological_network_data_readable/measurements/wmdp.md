# WMDP
**Type:** Measurement  
**Referenced in:** 17 papers  

## State of the Field

Across the provided literature, WMDP is consistently described as a benchmark for evaluating a model's capacity to unlearn hazardous knowledge. It is primarily used to measure the behavior of `Machine unlearning`, with one paper also using it to measure `Text generation`. The stated goal is to assess the "unlearning capability in hazardous domains" and to "mitigate sociotechnical harms in model generation" (Towards LLM Unlearning Resilient to Relearning Attacks...). The domains most frequently covered are biosecurity and cybersecurity, with one source also including chemical security. While most papers refer to it as the "World Model Development Project," a single paper defines it as the "Weapons of Mass Destruction Proxy benchmark." One source specifies its format, describing the dataset as comprising "multiple-choice questions" on its subject domains (Eliciting Implicit Acoustic Styles from Open-domain Instructions to Facilitate Fine-grained Controllable Generation of Speech).

## Sources

**[Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/18fd48d9cbbf9a20e434c9d3db6973c5-Paper-Conference.pdf)**
> The World Model Development Project (WMDP) benchmark, which is used to evaluate a model's capacity for generating, and subsequently unlearning, hazardous knowledge in domains like biosecurity and cybersecurity.

## Relationships

### → WMDP
- **Unlearning** (constructs) — *measured_by*
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
- **Unlearning efficacy** (constructs) — *measured_by*
  - [Exploring Criteria of Loss Reweighting to Enhance LLM Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ak/yang25ak.pdf)
