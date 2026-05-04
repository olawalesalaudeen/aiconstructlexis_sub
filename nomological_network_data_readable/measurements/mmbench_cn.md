# MMBench-CN
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** MMBench-Chinese, MMB-CN  

## State of the Field

Across the provided literature, MMBench-CN is consistently defined as the Chinese version of the MMBench benchmark, designed to evaluate multi-modal models. The instrument is most commonly used to measure constructs such as `Multimodal understanding` and `Visual question answering`, with one paper also using it to assess `Safety`. A specific operational feature mentioned in several sources is its method of evaluating "answer robustness with all-round shuffling on multiple choice answers" ("Efficient Large Multi-modal Models via Visual Context Compression"). While its general purpose is to assess vision-language capabilities in a non-English context, some papers apply it more specifically, for instance as a "standard evaluation for single-image QA performance" ("Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark"). Overall, the data shows its use as a benchmark for evaluating multimodal models on tasks within the Chinese language.

## Sources

**[InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf) (as "MMBench-Chinese")**
> MMBench-Chinese (MMBCN) is the Chinese version of the MMBench benchmark for evaluating multi-modal models.

**[Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)**
> The Chinese version of the MMBench benchmark, which evaluates answer robustness with shuffled multiple-choice answers.

**[Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf) (as "MMB-CN")**
> A Chinese multimodal benchmark used here as a standard evaluation for single-image QA performance.

## Relationships

### → MMBench-CN
- **Robustness** (constructs) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > ...we also evaluate MIRAGE on conventional VQA tasks, including the RetVQA multi-image QA (Penamakuri et al., 2023) and several single-image QA tasks, such as VQA-v2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), TextVQA (Singh et al., 2019), POPE (Li et al., 2023c), MMB (Liu et al., 2024c), MMB-CN (Liu et al., 2024c), MME (Fu et al., 2023), SEED-Bench (Li et al., 2023a), and MM-Vet (Yu et al., 2023b). (Section 5)
  - [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > We conduct experiments on MME (Fu et al., 2023), MMB (Liu et al., 2023c), and MMBCN. Each encompasses various sub-tasks, enabling comprehensive evaluation of multimodal understanding and reasoning capabilities. (Section 4.1)
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
