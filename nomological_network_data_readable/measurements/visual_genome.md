# Visual Genome
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** VISUAL GENOME  

## State of the Field

Across the surveyed literature, Visual Genome is predominantly described as a dataset containing dense annotations of objects, attributes, and relationships within images. It is frequently used as a measurement instrument to evaluate a model's region-level image captioning ability, open-vocabulary object detection, and relation understanding. A less common framing, presented in one paper, characterizes it as a visual question-answering (VQA) dataset that "grounds visual concepts to language" using scene graphs. This connection to VQA is also evident in its use as a source to synthesize question-answer pairs for other models. Beyond evaluation, Visual Genome also serves as a source of training data for detection models and for creating new instruction-following examples from its existing data on "object relationships and region captions" (Ferret: Refer and Ground Anything Anywhere at Any Granularity). Thus, while its most common application is evaluating fine-grained visual understanding, it is also used as a versatile resource for data synthesis and model training.

## Sources

**[Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)**
> A dataset containing dense annotations of objects, attributes, and relationships within images, used here to evaluate region-level captioning ability.

**[HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf) (as "VISUAL GENOME")**
> A visual question-answering dataset grounded in scene graphs, used to assess visual concept grounding and reasoning.

## Relationships

### → Visual Genome
- **Dense captioning** (behaviors tasks) — *measured_by*
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
- **Open-vocabulary object detection** (behaviors tasks) — *measured_by*
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
- **Relation understanding** (constructs) — *measured_by*
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Visual question answering** (behaviors tasks)
  > “For VQA data, we synthesize hard negatives from Visual Genome (VG100K) dataset (Krishna et al., 2016), which contains 108,077 images with over 1.7 million question-answer pairs.”
  - [TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf)
