# WikiHow
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** Wikihow  

## State of the Field

Across the provided literature, WikiHow is consistently framed as a dataset derived from instructional articles. Its most common application is as a basis for evaluating script generation, particularly within the InterleavedBench benchmark. A separate line of work uses it as a multimodal dataset for the project-based learning category of the MMIE benchmark, where it is stated to test a model's ability to "choose the correct procedural steps based on given text and image contexts." Other reported uses include measuring "How-to question answering" and, in a modified form, evaluating "organizing skill on expository text." One study describes this modification as using summaries as subheadings to form documents from related paragraphs. The dataset is thus used to operationalize and measure a range of procedural and organizational abilities in models.

## Sources

**[Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf)**
> A dataset of instructional articles, used as a basis for the script generation task in the InterleavedBench evaluation benchmark.

**[MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf) (as "Wikihow")**
> A multimodal dataset used as a source for MMIE's project-based learning category, originally designed for testing a model's ability to select correct procedural steps from text and images.

## Relationships

### → WikiHow
- **How-to question answering** (behaviors tasks) — *measured_by*
  - [Understanding the Thinking Process of Reasoning Models: A Perspective from Schoenfeld’s Episode Theory](https://aclanthology.org/2025.emnlp-main.923.pdf)
