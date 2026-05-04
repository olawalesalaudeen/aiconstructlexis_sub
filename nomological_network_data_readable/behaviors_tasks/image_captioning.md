# Image captioning
**Type:** Behavior  
**Referenced in:** 181 papers  
**Also known as:** Literal description writing, Visual captioning, Caption generation, Scene description, Image description generation, Image Caption Generation, Image Captioning, Image caption generation, Captioning, Diagram captioning, Situated captioning, Generic caption generation, Region-level captioning, Ultra-detailed image caption generation, Frame-level caption generation  

## State of the Field

Across the surveyed literature, image captioning is consistently defined as the observable behavior of producing textual descriptions for input images. While this general framing is prevalent, the expected nature of the description varies considerably, with some work focusing on 'brief' or 'surface-level' summaries and others on 'dense' or 'ultra-detailed' narratives. The task is also adapted for specialized inputs, including generating captions for scientific figures, mathematical diagrams, earth-observation images, and specific marked regions within an image. A few papers frame the task functionally, where the goal is to produce a description that can 'replace the diagram for math problem-solving' (Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset). To operationalize this behavior, researchers most frequently use datasets such as COCO, MS-COCO, and Flickr30k, with NoCaps also appearing in multiple studies. Evaluation is conducted using automated metrics like CLIP score, human evaluation, and LLM-as-a-judge approaches. A recurring theme is the use of the CHAIR metric, which is specifically designed to measure object hallucination within the generated captions. Consequently, image captioning is frequently studied in relation to hallucination and is also used to assess broader constructs like visual perception and multimodal understanding.

## Sources

**[VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The observable task of producing textual descriptions of input images.

**[Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf) (as "Literal description writing")**
> The task of generating a short, surface-level text description that illustrates the narrative depicted in the two panels of a comic.

**[MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Image description")**
> Generating textual descriptions of the visual content within an image.

**[Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf) (as "Visual captioning")**
> Generating descriptive text that summarizes or details the content of an image.

**[SciFIBench: Benchmarking Large Multimodal Models for Scientific Figure Interpretation](https://proceedings.neurips.cc/paper_files/paper/2024/file/217bb44ab14621754db8a392163e6b07-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Caption generation")**
> The task of generating a suitable and descriptive textual caption for a given scientific figure.

**[Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdcc6d47c1627350014a3076112ab824-Paper-Conference.pdf) (as "Scene description")**
> The task of generating a structured (e.g., JSON) or natural language description of all objects and their features (e.g., color, shape) in a visual scene.

**[Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Image description generation")**
> The task of producing a natural language text that describes the visual content of a given image.

**[Unified Generative and Discriminative Training for Multi-modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/29416b66c2149872b9d1415a3fd2c5e0-Paper-Conference.pdf) (as "Image Caption Generation")**
> The observable task of generating textual descriptions for provided images.

**[DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf) (as "Image Captioning")**
> The observable task of generating detailed textual descriptions of image content and style.

**[Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad0edc7d5fa1a783f063646968b7315b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Image caption generation")**
> Describing a diagram or image in text so that the description can substitute for the visual input in downstream problem solving.

**[TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac3af725ae398b6184faae0828bdbd6c-Paper-Conference.pdf) (as "Captioning")**
> Generating descriptive natural-language text about the content of an earth-observation image.

**[SPARTUN3D: Situated Spatial Understanding of 3D World in Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/b633e7052970b8f5aa1a69164d99e9e8-Paper-Conference.pdf) (as "Situated captioning")**
> Generating brief descriptions of surrounding objects and their spatial directions from the agent’s current standing point and orientation.

**[MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine](https://proceedings.iclr.cc/paper_files/paper/2025/file/db36dcad6baee298a34ffca324b84b09-Paper-Conference.pdf) (as "Diagram captioning")**
> The observable behavior of generating a textual description that accurately identifies the mathematical elements and their relationships within a given diagram.

**[Can We Talk Models Into Seeing the World Differently?](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a6594daf38b3c1dea5a63e47ac41ed3-Paper-Conference.pdf) (as "Generic caption generation")**
> An observable behavior where the model produces a vague or non-specific description of an image that does not identify the primary objects.

**[TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf) (as "Dense captioning")**
> The task of generating detailed, comprehensive textual descriptions that cover multiple objects, attributes, and relationships within an image.

**[Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf) (as "Region-level captioning")**
> Generating concise or detailed natural language descriptions for specific marked regions in an image.

**[Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bm/chen25bm.pdf) (as "Image-to-text generation")**
> The task of generating descriptive or relevant text based on a given image as input.

**[2025.emnlp-main.1357.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1357.checklist.pdf) (as "Ultra-detailed image caption generation")**
> The observable production of highly fine-grained and descriptive textual captions from input images by a vision-language model.

**[2025.emnlp-main.1588.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1588.checklist.pdf) (as "Frame-level caption generation")**
> Producing natural language descriptions for individual video frames as part of a video understanding pipeline.

## Relationships

### Image captioning →
- **Flickr30k** (measurements) — *measured_by*
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **COCO** (measurements) — *measured_by*
  > We evaluate our models on VQA benchmarks (Goyal et al., 2017; Singh et al., 2019; Gurari et al., 2018; Marino et al., 2019) and image captioning benchmarks (Chen et al., 2015; Young et al., 2014). (Section 5.1)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **CHAIR** (measurements) — *measured_by*
  > “CHAIR (Rohrbach et al., 2018) evaluates object hallucinations in open-ended captioning tasks”
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **NoCaps** (measurements) — *measured_by*
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **MS-COCO** (measurements) — *measured_by*
  > Flickr30K (Young et al., 2014) and MSCOCO (Lin et al., 2014) for captioning; (Section 4.1)
  - [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf)
- **COCO Caption** (measurements) — *measured_by*
  > Comparison with the state-of-the-art Multimodal Large Language Model (MLLM) Fine-Tuning Solutions on the image caption task: Flickr30k and COCO-Capation datasets (Table 5).
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **CLIP score** (measurements) — *measured_by*
  > More recent works propose reference-free metrics for robust automatic evaluation of T2I and image captioning, with notable examples being CLIP-Score (Hessel et al., 2021) and PickScore (Kirstain et al., 2023).
  - [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf)
- **CUB-200-2011** (measurements) — *measured_by*
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf)
- **LLaVA-Bench** (measurements) — *measured_by*
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > Following Leng et al. (2024), we use GPT-4 to assess the accuracy and detailedness of LVLM’s image captioning using a 10-point Likert scale (Section 4.1).
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **RefCOCOg** (measurements) — *measured_by*
  > Region-level captioning performance on the validation set of RefCOCOg
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)

### → Image captioning
- **Generalization** (constructs) — *measured_by*
  > Meanwhile, image captioning is conducted on the unseen BLIP-2 (OPT-2.7b) (Li et al., 2023), to demonstrate the generalization capacity. (Section 4.1)
  - [Privacy-Shielded Image Compression: Defending Against Exploitation from Vision-Language Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25k/shen25k.pdf)

### Associated with
- **Multimodal understanding** (constructs)
  - [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  > To strike a balance between the realism and complexity of the experiments, we primarily focus on the generation of objects in image description scenarios (image caption tasks). (Section 2)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Visual understanding** (constructs)
  > The IC instruction exhibits a high degree of shared information with prompts VQ1, VQ2, CR, and IU1.
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **MS-COCO** (measurements)
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **Perception** (constructs)
  - [Is Your Multimodal Language Model Oversensitive to Safe Queries?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50d4f8ff0416cedfe0771b7ad947a197-Paper-Conference.pdf)
- **Visual perception** (constructs)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
