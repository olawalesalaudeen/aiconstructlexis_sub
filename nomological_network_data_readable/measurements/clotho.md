# Clotho
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, Clotho is consistently characterized as a benchmark dataset composed of audio clips paired with corresponding text captions. The most prevalent application of this instrument is to evaluate the behavior of audio captioning; several papers refer to it as a "popular audio captioning dataset" and use it for comparative performance analysis. One paper specifies its use in assessing zero-shot performance on this task. A second, commonly mentioned application is for measuring audio-retrieval, with one source calling it one of the "most commonly used audio-retrieval benchmarks." A smaller body of work also uses Clotho to measure cross-modal retrieval and generalization, though these uses are less frequently detailed in the provided data. One definition offers more specific insight into the dataset's content, describing it as containing "long, diverse soundscapes" with "natural language descriptions."

## Sources

**[CompA: Addressing the Gap in Compositional Reasoning in Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/43c18853329c7504996b255252b6cb1f-Paper-Conference.pdf)**
> A benchmark dataset used for evaluating audio-retrieval tasks, consisting of audio clips and their corresponding text captions.

## Relationships

### → Clotho
- **Audio captioning** (behaviors tasks) — *measured_by*
  > We evaluate our approach on a popular audio captioning dataset, Clotho (Drossos et al., 2020). (Section 4.3)
  - [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf)
