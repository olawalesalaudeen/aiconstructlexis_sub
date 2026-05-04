# A-OKVQA
**Type:** Measurement  
**Referenced in:** 25 papers  
**Also known as:** AOKVQA, OKVQA  

## State of the Field

Across the provided literature, A-OKVQA is consistently characterized as a benchmark for visual question answering (VQA). The prevailing definition describes it as a dataset where questions require knowledge beyond what is directly visible in the image, frequently termed "external, real-world knowledge" or "broader commonsense and world knowledge." Consequently, it is most commonly used to measure a model's `Visual question answering` and `real-world knowledge reasoning` capabilities. Some papers also employ A-OKVQA to evaluate more specific phenomena, such as `Social bias`, with one study using it to "measure Western bias," and its data is also used in frameworks for assessing `Object hallucination`. The dataset is described as containing image-question pairs with images sourced from MSCOCO, and it offers both open-ended and multiple-choice settings. One paper specifies that the questions and multiple-choice options, consisting of one correct answer and three distractors, were created by "English speakers on Mechanical Turk." While most sources emphasize its knowledge-intensive nature, a less common framing describes it as a "general-purpose" VQA benchmark for evaluating performance on "larger visual concepts."

## Sources

**[CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)**
> A visual question answering dataset where questions require external, real-world knowledge about objects or actions depicted in the image.

**[MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf) (as "AOKVQA")**
> A general-purpose visual question answering benchmark used to evaluate performance on larger visual concepts.

**[DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf) (as "OKVQA")**
> The Outside Knowledge Visual Question Answering (OK-VQA) dataset, which requires external knowledge to answer questions about images.

**[DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf) (as "OK-VQA")**
> The Outside Knowledge Visual Question Answering (OK-VQA) benchmark, which requires external knowledge to answer questions about images.

## Relationships

### → A-OKVQA
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We use three complex visual reasoning datasets, including GQA (Hudson & Manning, 2019), OK-VQA (Marino et al., 2019), and A-OKVQA (Schwenk et al., 2022)... OK-VQA and A-OKVQA mainly use external real-world knowledge of objects or actions in the image. (Section 3.1)
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **External knowledge** (constructs) — *measured_by*
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **Knowledge** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Fairness** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multilingual ability** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/efc549c2d22edf2f244b7013387c6251-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  > POPE ... is a scalable framework for detecting object hallucinations in LVLMs, utilizing SEEM-annotated datasets from ... A-OKVQA Schwenk et al. (2022)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Social bias** (constructs) — *measured_by*
  > “To measure Western bias in question answering, we use A-OKVQA and CVQA (Schwenk et al., 2022; Romero et al., 2024).”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
