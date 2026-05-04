# Attribute recognition
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Based on the provided data, attribute recognition is defined as the task of identifying visual attributes from an image, with position and color cited as specific examples. This behavior is primarily studied in the context of model failures, particularly what one paper calls "attribute-level hallucinations." To operationalize and measure this capability, the field uses the MM-Hal-Bench benchmark. This instrument is explicitly reported to evaluate large vision-language models on several question types, including "object attributes." The available sources consistently frame attribute recognition as a specific sub-task for assessing vision-language models, and its study is shown to be related to the broader topic of hallucination.

## Sources

**[Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf)**
> Identifying visual attributes such as position and color from an image.

## Relationships

### Attribute recognition →
- **MM-Hal-Bench** (measurements) — *measured_by*
  > "MMHAL-Bench (Sun et al., 2023): This benchmark evaluates LVLMs beyond object hallucination and contains eight question types: object attributes, adversarial objects, comparisons, counting, spatial relations, environment, holistic description, and others."
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
