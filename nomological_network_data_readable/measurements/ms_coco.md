# MS-COCO
**Type:** Measurement  
**Referenced in:** 52 papers  
**Also known as:** MSCOCO, MSCOCO-2014, MS COCO  

## State of the Field

Across the provided literature, MS-COCO (Microsoft Common Objects in Context) is consistently positioned as a large-scale dataset for evaluating a range of vision-language capabilities. The most prevalent use of the dataset is to measure behaviors such as image captioning, image generation (also termed text-to-image synthesis), and cross-modal retrieval. Papers frequently specify using the MS-COCO validation set for these evaluations, often in a zero-shot context. Beyond these primary applications, MS-COCO is also used to assess object detection, segmentation, multimodal understanding, and object hallucination. A smaller set of studies employs the dataset in other ways, such as a source of text prompts for generation tasks, a collection of images for creating adversarial examples, or for evaluating model perplexity on the image-text modality. One definition characterizes it as featuring "complex scenes with multiple objects," aligning with its use across these diverse evaluation scenarios.

## Sources

**[Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf) (as "COCO")**
> MS-COCO validation set used for zero-shot image-to-text captioning and text-to-image generation evaluation.

**[An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/674ad201bc8fa74b3c9979230aa0c63b-Paper-Conference.pdf)**
> The validation set of the Microsoft Common Objects in Context (MS-COCO) dataset, used here to evaluate text-to-image synthesis quality.

**[Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.39.pdf) (as "MSCOCO")**
> A large-scale benchmark dataset for image captioning, featuring complex scenes with multiple objects.

**[Syntax-Aware Retrieval Augmentation for Neural Symbolic Regression](https://aclanthology.org/2025.emnlp-main.665.pdf) (as "MSCOCO-2014")**
> Microsoft Common Objects in Context 2014, a large-scale dataset for image captioning and object detection, used in this paper to evaluate the image modality.

**[Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf) (as "MS COCO")**
> The Microsoft Common Objects in Context (MS COCO) dataset is a large-scale object detection, segmentation, and captioning dataset.

## Relationships

### → MS-COCO
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
- **Image generation** (behaviors tasks) — *measured_by*
  > We use two benchmarks: MS-COCO (Lin et al., 2014) Karpathy test split and Flickr30K (Plummer et al., 2015). (Section 3.2)
  - [Kosmos-G: Generating Images in Context with Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b2fe1ee8d936ac08dd26f2ff58986c8f-Paper-Conference.pdf)
- **Image captioning** (behaviors tasks) — *measured_by*
  > Flickr30K (Young et al., 2014) and MSCOCO (Lin et al., 2014) for captioning; (Section 4.1)
  - [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf)
- **Object detection** (behaviors tasks) — *measured_by*
  - [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > “We evaluate the multimodal vision and language capabilities of DREAMLLM across several benchmarks, including image-to-text captioning on COCO”
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Image reconstruction** (behaviors tasks) — *measured_by*
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks) — *measured_by*
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **Visual generation** (constructs) — *measured_by*
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **Multimodal generation** (constructs) — *measured_by*
  > To evaluate visual generation capabilities, we use MS-COCO (Lin et al., 2014) and GenEval (Ghosh et al., 2024). (Section 4.2)
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)

### Associated with
- **Image captioning** (behaviors tasks)
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **CHAIR** (measurements)
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
