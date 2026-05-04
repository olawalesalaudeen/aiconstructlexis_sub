# SEED
**Type:** Measurement  
**Referenced in:** 15 papers  

## State of the Field

SEED is consistently defined as a comprehensive benchmark for evaluating multimodal models. Across the provided literature, its most prevalent use is to measure the capabilities of `Visual understanding` and `Visual question answering` in vision-language models. One definition specifies that the benchmark operationalizes this evaluation through both video and image-based questions designed to assess spatial, temporal, and event understanding. Papers frequently include SEED in evaluation suites alongside other instruments like GQA, MME, and MM-Vet. A less common application is also reported, with one study using SEED to evaluate `Visual hallucination` and fine-grained reasoning.

## Sources

**[Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)**
> A comprehensive benchmark for evaluating multimodal models.

## Relationships

### → SEED
- **Visual understanding** (constructs) — *measured_by*
  > “We compare LLaVA-Mini with LLaVA-v1.5 across 11 benchmarks to thoroughly assess the performance of LLaVA-Mini with minimal vision tokens.”
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > we evaluate γ-MoD on six image question answering benchmarks: VQAv2 (Goyal et al., 2017), VizWiz (Gurari et al., 2018), TextVQA (Singh et al., 2019), SQA (Lu et al., 2022), GQA (Hudson & Manning, 2019) and SEED (Ge et al., 2023). (Section 5.1)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **Visual hallucination** (behaviors tasks) — *measured_by*
  > “The MLLM-specific benchmarks are POPE Li et al. (2023c), MME Fu et al. (2023), MMB Liu et al. (2023d), SEED Li et al. (2023a) and MM-Vet Yu et al. (2023). Compared to common VL evaluations, these benchmarks aim to evaluate MLLMs from various aspects, such as fine-grained reasoning and visual hallucination.”
  - [Routing Experts: Learning to Route Dynamic Experts in Existing Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49a4829a2ccaaa4706cc82e68c39a9c6-Paper-Conference.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
