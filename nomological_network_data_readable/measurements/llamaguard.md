# LlamaGuard
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** Llama Guard, LLaMA Guard 7B, LLM-Guard  

## State of the Field

Across the provided literature, LlamaGuard is predominantly characterized as a model-based evaluation tool or instrument used to assess the safety of large language model outputs. It is most commonly described as a classifier that determines whether a response is harmful or safe, and is used to calculate metrics such as Attack Success Rate (ASR) and safety rates. Papers use LlamaGuard to operationalize and measure constructs such as Harmlessness and, to a lesser extent, Jailbreak resistance. Beyond a post-hoc evaluation tool, some work also frames it as a pretrained 'guardrail system' for content moderation or as a benchmark itself. The definitions specify that it is an open-source model, with one paper identifying it as a 7-billion parameter model. One study notes that while it is 'designed to detect harmful content in LLM inputs and outputs,' it may not be aligned with the requirements of agent safety tasks.

## Sources

**[Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf) (as "Llama Guard")**
> An evaluation tool used to classify model responses and calculate the Attack Success Rate (ASR) by determining if an output is harmful.

**[FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf) (as "LLaMA Guard 7B")**
> A 7-billion parameter open-source guard model used as an instrument to evaluate the effectiveness of jailbreak attacks at bypassing safety filters.

**[GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiang25a/xiang25a.pdf)**
> Pretrained LLM-based guardrail system designed for content moderation in text, used here as a baseline to test its applicability to agent safety tasks.

**[LLM-OREF: An Open Relation Extraction Framework Based on Large Language Models](https://aclanthology.org/2025.emnlp-main.460.pdf) (as "Llama-Guard")**
> A model-based evaluation tool used to classify the safety and harmlessness of LLM-generated responses.

**[In-Context Learning Boosts Speech Recognition via Human-like Adaptation to Speakers and Language Varieties](https://aclanthology.org/2025.emnlp-main.220.pdf) (as "LLM-Guard")**
> LLM-Guard, a safety evaluation procedure used to measure safety rates on safety benchmarks.

## Relationships

### → LlamaGuard
- **Jailbreak resistance** (behaviors tasks) — *measured_by*
  - [Using Shapley interactions to understand how models use structure](https://aclanthology.org/2025.acl-long.1012.pdf)
