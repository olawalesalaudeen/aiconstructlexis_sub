# SimpleQA
**Type:** Measurement  
**Referenced in:** 10 papers  

## State of the Field

Across the provided literature, SimpleQA is consistently described as a benchmark for evaluating language models. It is explicitly used to measure both the construct of `Faithfulness` and the behavior of `Fact-seeking question answering`. The prevailing usage positions it as an instrument for assessing a model's 'factual capabilities' in general knowledge areas, with one paper calling it a 'representative benchmark for factual QA'. The benchmark itself is composed of what sources call 'concise, fact-oriented questions' or 'fact-seeking questions', with one paper noting it contains 4.3k items. Evaluation on this benchmark involves categorizing model responses as correct, incorrect, or not attempted. Multiple sources state that SimpleQA was introduced by OpenAI.

## Sources

**[Crab: A Novel Configurable Role-PlayingLLMwith Assessing Benchmark](https://aclanthology.org/2025.acl-long.732.pdf)**
> A benchmark introduced by OpenAI comprising numerous concise, fact-oriented questions to assess the factual capabilities of LLMs in general knowledge areas.

## Relationships

### → SimpleQA
- **Truthfulness** (constructs) — *measured_by*
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **Factuality** (constructs) — *measured_by*
  - [Controlled Low-Rank Adaptation with Subspace Regularization for Continued Training on Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)
