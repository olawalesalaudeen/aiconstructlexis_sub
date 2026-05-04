# Object recognition
**Type:** Behavior  
**Referenced in:** 15 papers  
**Also known as:** Object presence detection, Attribute identification, Color identification, Object identification, Element identification, Lesion identification, Structure identification  

## State of the Field

Across the surveyed literature, object recognition is most commonly defined as the behavior of identifying and naming specific objects present in an image. Some papers offer more specialized definitions that focus on related sub-tasks, such as determining an object's presence, identifying its attributes, or naming its color. One study explicitly treats these as distinct categories alongside object recognition when selecting questions from the TDIUC dataset. The application of this behavior also extends to specialized domains, with definitions covering the identification of GUI elements in user interfaces and the naming of anatomical structures or lesions in medical scans.

To operationalize and measure this behavior, researchers employ several instruments. The provided data shows that object recognition is measured by benchmarks such as ImageNet-1k and POPE. It is also evaluated using visual question answering tasks, where models are prompted with direct questions like "What is on the bed?". Additionally, the Dollar Street dataset is used to measure object identification in studies of cultural bias. The behavior is studied in the context of hallucination, where it is one of the tasks used to assess model failures, and is also described as being related to the broader construct of Perception.

## Sources

**[WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Identifying specific objects present in the image.

**[Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf) (as "Object presence detection")**
> The task of determining whether a specific object exists within an image.

**[Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf) (as "Attribute identification")**
> The task of identifying specific properties or characteristics of objects within an image.

**[Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf) (as "Color identification")**
> The task of identifying and naming the colors of objects in an image.

**[See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf) (as "Object identification")**
> The task of correctly naming an everyday object depicted in an image.

**[Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf) (as "Element identification")**
> The action of correctly selecting or pointing to a specific GUI element based on a textual description or query.

**[Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf) (as "Structure identification")**
> The specific task of identifying and naming anatomical structures, such as organs, within a specified region of a medical scan.

**[Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf) (as "Lesion identification")**
> The specific task of identifying and naming abnormalities, such as tumors or cancers, within a specified region of a medical scan.

## Relationships

### Object recognition →
- **ImageNet-1k** (measurements) — *measured_by*
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We manually curate a set of 100 images with specific questions about objects, such as “What is on the bed?”. ... We prefill the model’s response with “It is a” and compare the next generated token before and after ablation. (Section 3)
  - [Towards Interpreting Visual Information Processing in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/900fb3439e4968df79a6f2bfedec49cd-Paper-Conference.pdf)
- **POPE** (measurements) — *measured_by*
  - [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25c/park25c.pdf)

### Associated with
- **Perception** (constructs)
  - [AI-Assisted Human Evaluation of Machine Translation](https://aclanthology.org/2025.naacl-long.256.pdf)
- **Hallucination** (behaviors tasks)
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
