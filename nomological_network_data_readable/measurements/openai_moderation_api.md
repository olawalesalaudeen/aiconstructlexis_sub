# OpenAI moderation API
**Type:** Measurement  
**Referenced in:** 16 papers  
**Also known as:** OpenAI Moderation API, OpenAI Moderation, OpenAI Mod  

## State of the Field

The OpenAI moderation API is predominantly characterized in the provided literature as a content-safety evaluation procedure used to classify text against safety policies. Most definitions specify that it identifies various violation categories, such as hate, harassment, self-harm, and sexual content. One paper notes it provides both a binary tag indicating if a response is safe and a continuous harmfulness score. Researchers employ this API in several ways: to evaluate model responses to jailbreak prompts, to tag and filter unsafe conversations in large datasets, and as a preprocessing step to remove toxic content. For instance, one study deems a conversation unsafe "if any of its messages is flagged by the API" (LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset). Across the surveyed work, it is consistently used to measure constructs like `Safety` and `Harmlessness`, and behaviors such as `Harmful content detection` and `Harmful content generation`. It is sometimes used in conjunction with other tools, such as the Perspective API and Detoxify, for toxicity classification. A smaller number of papers frame it differently, referring to it as a 'standard safety dataset' or 'benchmark' (under the names 'OpenAI Mod' or 'OpenAI Moderation') for assessing guardrail models.

## Sources

**[LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf)**
> OpenAI Moderation API, a content-safety evaluation procedure that assigns violation categories to messages and is used here to tag unsafe conversations and evaluate moderation and jailbreak responses.

**[WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf) (as "OpenAI Moderation API")**
> Official API provided by OpenAI to classify text content based on safety policies, including categories like hate, harassment, self-harm, and sexual content.

**[Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf) (as "OpenAI Moderation")**
> A publicly available tool from OpenAI used to assess the safety of text data by scoring it on dimensions like harassment, sexual content, hate speech, and violence.

**[$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf) (as "OpenAI Mod")**
> A standard safety dataset used to evaluate the performance of guardrail models in detecting unsafe content.

## Relationships

### → OpenAI moderation API
- **Harmlessness** (constructs) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Harmful content detection** (behaviors tasks) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Content moderation** (behaviors tasks) — *measured_by*
  - [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
