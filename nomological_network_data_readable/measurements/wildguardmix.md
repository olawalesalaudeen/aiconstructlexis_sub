# WildGuardMix
**Type:** Measurement  
**Referenced in:** 3 papers  
**Also known as:** WildGuardMix Test Response  

## State of the Field

A public benchmark dataset used to evaluate the performance of response classification for content safety.

## Sources

**[On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf) (as "WildGuardMix Test Response")**
> A public benchmark dataset used to evaluate the performance of response classification for content safety.

**[HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)**
> A benchmark dataset used for both training and testing safety guard models on the task of instruction-response pair classification.

## Relationships

### → WildGuardMix
- **Response classification** (behaviors tasks) — *measured_by*
  > For the response classification, we utilize datasets containing BeaverTails Test (Ji et al., 2024), SafeRLHF Test (Dai et al., 2023), Harmbench Response (Mazeika et al., 2024), and WildGuardMix Test Response (Han et al., 2024).
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)

### Associated with
- **Content moderation** (behaviors tasks)
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf)
