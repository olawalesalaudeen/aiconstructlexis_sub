# Visual question answering
**Type:** Behavior  
**Referenced in:** 292 papers  
**Also known as:** Visual Question Answering, Image question answering, Vision question answering, Object analysis, Egocentric question answering, GUI question answering, Image-referenced answering, 3D scene VQA, Embodied VQA, Region-text interleaved VQA, Embedded image question answering, Multi-image question answering, Simple question answering, Single-image question answering, General visual question answering, Image-grounded text generation, Scene text question answering  

## State of the Field

The most prevalent framing of visual question answering (VQA) across the provided literature is the task of generating a natural language answer to a question about visual content. This visual content most commonly consists of a single static image, but a subset of work extends the task to include multiple images, videos, 3D scenes, or images embedded within documents and webpages. The behavior is operationalized and measured using a wide array of benchmarks, with the most frequently cited instruments for general VQA including VQA-v2, GQA, TextVQA, VizWiz, and ScienceQA. Specialized forms of the task are assessed with dedicated benchmarks, such as POPE for evaluating object hallucination, OK-VQA for knowledge-based reasoning, and domain-specific datasets like SLAKE and VQA-RAD for biomedical applications. While many evaluations expect open-ended, generated text answers, some definitions and benchmarks frame the task as a multiple-choice problem, as noted in papers like "Task Me Anything". VQA is frequently studied as a core component of broader capabilities like multimodal understanding and visual perception, and it is also a common context for investigating issues such as hallucination. Beyond general-purpose VQA, researchers also define more specific variants like "scene text question answering" for reading text in images, "embodied VQA" for 3D environments, and "egocentric question answering" for first-person video. Overall, the literature treats VQA as a representative vision-language task, with a core definition centered on answering questions about images but with numerous variations in input modality, question complexity, and evaluation format.

## Sources

**[An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/674ad201bc8fa74b3c9979230aa0c63b-Paper-Conference.pdf)**
> Generating answers to natural language questions about visual content in images or 3D scenes.

**[A Hitchhiker's Guide to Fine-Grained Face Forgery Detection Using Common Sense Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/059d2b9188cdb7ae00f4d78cc9469704-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Visual Question Answering")**
> Answering questions about an image by generating natural language responses based on visual and text inputs.

**[Task Me Anything](https://proceedings.neurips.cc/paper_files/paper/2024/file/237ffa9a473eff1c66d085dba7f813ba-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Image question answering")**
> The task of providing a text-based answer to a question about a static image, typically in a multiple-choice format.

**[Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf) (as "Vision question answering")**
> Answering natural language questions based on visual input provided to the model.

**[ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf) (as "Region-text interleaved VQA")**
> The model answers visual questions whose inputs and outputs can contain interleaved image-region tokens and text.

**[MMEgo: Towards Building Egocentric Multimodal LLMs for Video QA](https://proceedings.iclr.cc/paper_files/paper/2025/file/b29a95e7d9f1e1a6dfc567b556733744-Paper-Conference.pdf) (as "Egocentric question answering")**
> Answering questions about first-person videos using visual and textual evidence from the video content.

**[Learning Interleaved Image-Text Comprehension in Vision-Language Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b441276ce6097177f1c001b3ea643f7a-Paper-Conference.pdf) (as "Image-referenced answering")**
> The observable behavior of explicitly citing a specific image from the input context within a generated answer, often using a standardized format like '[Picture n]'.

**[BigDocs: An Open Dataset for Training Multimodal Models on Document and Code Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4659191ae1e89faa09864c23fa91f31-Paper-Conference.pdf) (as "GUI question answering")**
> The task of answering questions about the content, elements, and layout of a website based on its screenshot.

**[LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf) (as "Embodied VQA")**
> Answering questions about embodied 3D environments, including dialogue and planning.

**[LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf) (as "3D scene VQA")**
> Answering questions about 3D scenes, including captioning and grounding from multi-view images.

**[MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d91ffbe9c126765755ff52d36b715683-Paper-Conference.pdf) (as "Object analysis")**
> The observable task of answering detailed questions about an object's components, structure, appearance, or purpose.

**[Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf) (as "Embedded image question answering")**
> Answering specific questions about the visual content of an embedded image in a webpage.

**[MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf) (as "Multi-image question answering")**
> The task of providing a textual answer to a question based on information presented across multiple images.

**[DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf) (as "Simple question answering")**
> The task of providing a direct, often factual, answer to a straightforward question about an image.

**[Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf) (as "Single-image question answering")**
> The observable task of answering a textual question based on information contained within a single image provided as input.

**[AbGen: Evaluating Large Language Models in Ablation Study Design and Evaluation for Scientific Research](https://aclanthology.org/2025.acl-long.612.pdf) (as "General visual question answering")**
> Answering broad visual questions not specific to mathematical or scientific content, contributing noise when used in math-focused evaluation.

**[Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf) (as "Image-grounded text generation")**
> The task of generating a textual response that is conditioned on and consistent with a given input image and a textual query.

**[CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning inSLMs](https://aclanthology.org/2025.emnlp-main.705.pdf) (as "Scene text question answering")**
> Answering questions about naturally occurring text in real-world scenes such as signs, menus, and labels, requiring both text recognition and contextual understanding.

## Relationships

### Visual question answering →
- **VQA-v2** (measurements) — *measured_by*
  > “Table 4 presents a comparison between LLaVA-1.5 and Text4Seg across various VQA and RES benchmarks.”
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  > “GQA is a popular compositional visual reasoning dataset with synthesis multi-hop questions, making it suitable for multi-step reasoning.”
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **TextVQA** (measurements) — *measured_by*
  > “Table 4 presents a comparison between LLaVA-1.5 and Text4Seg across various VQA and RES benchmarks.”
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VizWiz** (measurements) — *measured_by*
  > ...general visual question answering (VQA) on VQAv2 (Goyal et al., 2019), OKVQA (Marino et al., 2019), VizWiz (Gurari et al., 2018)... (Section 4.1)
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **ScienceQA** (measurements) — *measured_by*
  > We perform Visual Question Answering (VQA) on ScienceQA (Lu et al., 2022), classification on CIFAR-10 (Krizhevsky et al., 2009), captioning on Flickr30K (Young et al., 2014) and facial attribute recognition on CelebA (Liu et al., 2018). (Section 4.1)
  - [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  > We use three complex visual reasoning datasets, including GQA (Hudson & Manning, 2019), OK-VQA (Marino et al., 2019), and A-OKVQA (Schwenk et al., 2022)... OK-VQA and A-OKVQA mainly use external real-world knowledge of objects or actions in the image. (Section 3.1)
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **POPE** (measurements) — *measured_by*
  > “Table 4 presents a comparison between LLaVA-1.5 and Text4Seg across various VQA and RES benchmarks.”
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
- **OK-VQA** (measurements) — *measured_by*
  > In order to assess multimodal vision and language capabilities of DEEM , we conduct evaluation against current SOTA LMMs ... across several tasks, including ... visual question answering on ... OKVQA (Marino et al., 2019) (Section 3.2).
  - [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  > General VQA benchmarks, including GQA (Hudson and Manning, 2019), MMBench (Liu et al., 2023c), and SEED (Li et al., 2023a) (Section 4.1).
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  > DeCo also achieves better results on MME, which evaluates the multifaceted VQA capabilities of LLaVA-1.5. (Section 4.3)
  - [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf)
- **MMMU** (measurements) — *measured_by*
  > We further validate our findings in a multi-modal setting using the vision-language model LLaVa (Liu et al., 2023) on the MMMU (Yue et al., 2024) visual question answering benchmark, see Appendix A.8. (Section 3.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ChartQA** (measurements) — *measured_by*
  > We collect question-document pairs from a series of VQA datasets, targeting different document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024b), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for various figure types, and SlideVQA (Tanaka et al., 2023) for presentation slides.
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **SEED-Bench** (measurements) — *measured_by*
  > Table 2: Evaluated tasks with corresponding dataset and MLLM. Task Dataset MLLM Captioning COCO Karpathy Test (Karpathy & Fei-Fei, 2015) LLaMA-Adapter (Zhang et al., 2024a) VQA SEED-Bench (Li et al., 2023a) Honeybee (Cha et al., 2024)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
- **MM-Vet** (measurements) — *measured_by*
  > ...we also evaluate MIRAGE on conventional VQA tasks, including the RetVQA multi-image QA (Penamakuri et al., 2023) and several single-image QA tasks, such as VQA-v2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), TextVQA (Singh et al., 2019), POPE (Li et al., 2023c), MMB (Liu et al., 2024c), MMB-CN (Liu et al., 2024c), MME (Fu et al., 2023), SEED-Bench (Li et al., 2023a), and MM-Vet (Yu et al., 2023b). (Section 5)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **SQA** (measurements) — *measured_by*
  > we evaluate γ-MoD on six image question answering benchmarks: VQAv2 (Goyal et al., 2017), VizWiz (Gurari et al., 2018), TextVQA (Singh et al., 2019), SQA (Lu et al., 2022), GQA (Hudson & Manning, 2019) and SEED (Ge et al., 2023). (Section 5.1)
  - [Discovering Sparsity Allocation for  Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **SEED** (measurements) — *measured_by*
  > we evaluate γ-MoD on six image question answering benchmarks: VQAv2 (Goyal et al., 2017), VizWiz (Gurari et al., 2018), TextVQA (Singh et al., 2019), SQA (Lu et al., 2022), GQA (Hudson & Manning, 2019) and SEED (Ge et al., 2023). (Section 5.1)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **IconQA** (measurements) — *measured_by*
  > Task Type: Visual Question Answering (VQA), Dataset Name: IconQA (Lu et al., 2021), Task Description: Diagram Understanding VQA (Table 1)
  - [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf)
- **SLAKE** (measurements) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M.
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
- **DocVQA** (measurements) — *measured_by*
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **MMVet** (measurements) — *measured_by*
  > “We selected five popular benchmarks to assess current LVLMs, encompassing Yes/No Questions (MME), Multiple Choice Questions (MMBench, SEEDBench), and Visual Question Answering (MMvet, LLaVABench).”
  - [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLaVA-Bench** (measurements) — *measured_by*
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **MMStar** (measurements) — *measured_by*
  > “We select 6 VQA benchmarks covering both perception and reasoning.”
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **VQA-RAD** (measurements) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M.
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
- **PathVQA** (measurements) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M.
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
- **LLaVA-Bench-in-the-Wild** (measurements) — *measured_by*
  > “We selected five popular benchmarks to assess current LVLMs, encompassing Yes/No Questions (MME), Multiple Choice Questions (MMBench, SEEDBench), and Visual Question Answering (MMvet, LLaVABench).”
  - [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)
- **ScanQA** (measurements) — *measured_by*
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
- **ScienceQA-IMG** (measurements) — *measured_by*
  > Table 2: A comprehensive investigation conducted to explore resolution preferences across eight vision-language tasks. For each task, the accuracy scores corresponding to five different resolutions are presented. (Table 2)
  - [What You Read Isn’t What You Hear: Linguistic Sensitivity in Deepfake Speech Detection](https://aclanthology.org/2025.emnlp-main.795.pdf)
- **VisDial** (measurements) — *measured_by*
  > In order to assess multimodal vision and language capabilities of DEEM , we conduct evaluation against current SOTA LMMs ... across several tasks, including ... visual question answering on ... VisDial (Das et al., 2017) (Section 3.2).
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Mantis-Eval** (measurements) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AI2D** (measurements) — *measured_by*
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **SciQA** (measurements) — *measured_by*
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **ActivityNet-QA** (measurements) — *measured_by*
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **MathVista** (measurements) — *measured_by*
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **MMT-Bench** (measurements) — *measured_by*
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **OCR-VQA** (measurements) — *measured_by*
  > Task Type: Visual Question Answering (VQA), Dataset Name: OCR-VQA (Mishra et al., 2019), Task Description: Text Understanding VQA (Table 1)
  - [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf)
- **ST-VQA** (measurements) — *measured_by*
  > We conduct extensive experiments on 9 benchmarks from 4 categories, including TextVQA (Singh et al., 2019), ST-VQA (Biten et al., 2019), TallyVQA (Acharya et al., 2019), and GQA Hudson & Manning (2019) for detailed visual question answering (Section 1)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
- **CVQA** (measurements) — *measured_by*
  > To measure Western bias in question answering, we use A-OKVQA and CVQA (Schwenk et al., 2022; Romero et al., 2024). (Section 4.1)
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **SlideVQA** (measurements) — *measured_by*
  > We collect question-document pairs from a series of VQA datasets, targeting different document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024b), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for various figure types, and SlideVQA (Tanaka et al., 2023) for presentation slides.
  - [VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)
- **MMB** (measurements) — *measured_by*
  > ...we also evaluate MIRAGE on conventional VQA tasks, including the RetVQA multi-image QA (Penamakuri et al., 2023) and several single-image QA tasks, such as VQA-v2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), TextVQA (Singh et al., 2019), POPE (Li et al., 2023c), MMB (Liu et al., 2024c), MMB-CN (Liu et al., 2024c), MME (Fu et al., 2023), SEED-Bench (Li et al., 2023a), and MM-Vet (Yu et al., 2023b). (Section 5)
  - [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf)
- **MMBench-CN** (measurements) — *measured_by*
  > ...we also evaluate MIRAGE on conventional VQA tasks, including the RetVQA multi-image QA (Penamakuri et al., 2023) and several single-image QA tasks, such as VQA-v2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), TextVQA (Singh et al., 2019), POPE (Li et al., 2023c), MMB (Liu et al., 2024c), MMB-CN (Liu et al., 2024c), MME (Fu et al., 2023), SEED-Bench (Li et al., 2023a), and MM-Vet (Yu et al., 2023b). (Section 5)
  - [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf)
- **ArXivQA** (measurements) — *measured_by*
  > We collect question-document pairs from a series of VQA datasets, targeting different document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024b), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for various figure types, and SlideVQA (Tanaka et al., 2023) for presentation slides.
  - [VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8a2070082ad05b4deeff4ffb4312a6f-Paper-Conference.pdf)
- **MSVD-QA** (measurements) — *measured_by*
  > Visual Question Answering (VQA): We evaluate the performance of visual question answering on the following benchmark datasets:... We also use MSVD-QA
  - [Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf)
- **VizWiz-VQA** (measurements) — *measured_by*
  > Task Type: Visual Question Answering (VQA), Dataset Name: VizWiz-VQA (Gurari et al., 2018), Task Description: Natural Image VQA (Table 1)
  - [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf)
- **MMVP** (measurements) — *measured_by*
  > General VQA: Assessing visual perception and reasoning abilities through single-image question answering, including MMBench (Liu et al., 2025b), MME (Fu et al., 2023), and MMVP (Zhong et al., 2023). (Section 4.5).
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **PMC-VQA** (measurements) — *measured_by*
  > Task Type: Visual Question Answering (VQA), Dataset Name: PMC-VQA (Zhang et al., 2024a), Task Description: Medical VQA (Table 1)
  - [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf)
- **HallusionBench** (measurements) — *measured_by*
  > “Additionally, we evaluate performance on specific-domain VQA tasks, which include ChartQA (Masry et al., 2022), LLaVABench (Liu et al., 2024c), and HallusionBench (Guan et al., 2023).” (Section 4.1)
  - [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf)

### → Visual question answering
- **Reliability** (constructs) — *measured_by*
  - [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generality** (constructs) — *measured_by*
  - [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Locality** (constructs) — *measured_by*
  - [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual grounding** (constructs) — *causes*
  > Ablation studies also empirically show that the integration of visual grounding capability allows medical VLMs to achieve improved performance on other downstream tasks.
  - [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.89.pdf)
- **Personalization** (constructs) — *causes*
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Object recognition** (behaviors tasks) — *measured_by*
  > We manually curate a set of 100 images with specific questions about objects, such as “What is on the bed?”. ... We prefill the model’s response with “It is a” and compare the next generated token before and after ablation. (Section 3)
  - [Towards Interpreting Visual Information Processing in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/900fb3439e4968df79a6f2bfedec49cd-Paper-Conference.pdf)
- **Stereotyping** (constructs) — *measured_by*
  - [Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf)

### Associated with
- **Multimodal understanding** (constructs)
  > “most of these models are limited to multimodal tasks for text generation, such as visual question answering (VQA) and image captioning”
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  > This issue is particularly prevalent in tasks such as image captioning and visual question answering (Liu et al., 2023a; Yin et al., 2023; Zhou et al., 2023b; Zhu et al., 2024a; Gunjal et al., 2024), where maintaining coherence between modalities is critical. (Section 2)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Multimodal reasoning** (constructs)
  - [Q-VLM: Post-training Quantization for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cffbaf4f47546ece96bb42c0edda40ee-Paper-Conference.pdf)
- **Visual dialogue** (behaviors tasks)
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
- **Perception** (constructs)
  > Our hypothesis is that “General VQA” primarily evaluates perception ability and knowledge recall, while “Math VQA” assesses perception ability and reasoning ability.
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Open-ended question answering** (behaviors tasks)
  - [VRSBench: A Versatile Vision-Language Benchmark Dataset for Remote Sensing Image Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/05b7f821234f66b78f99e7803fffa78a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual perception** (constructs)
  > Visual perception is assessed through image captioning, where VLMs produce descriptions of the input images, or visual-question answering (VQA), where VLMs are asked to answer questions pertaining to the images. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual understanding** (constructs)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Visual Genome** (measurements)
  > “For VQA data, we synthesize hard negatives from Visual Genome (VG100K) dataset (Krishna et al., 2016), which contains 108,077 images with over 1.7 million question-answer pairs.”
  - [TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **Versatility** (constructs)
  > Our MedRegA not only enables three region-centric tasks, but also achieves the best performance for visual question answering, report generation and medical image classification over 8 modalities, showcasing significant versatility.
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks)
  > "POPE is a VQA-based metric for assessing object hallucination in MLLMs"
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks)
  - [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.248.pdf)
- **Compositional reasoning** (constructs)
  > In many compositional reasoning tasks, interactions are key and marginal attributions are insufficient. We illustrate this using an image of a dog playing with a basketball and prompting the LLaVA-NeXT-Mistral-7B model (Liu et al., 2023) with “What is shown in this image?”. (Sec. 7.2)
  - [SPEX: Scaling Feature Interaction Explanations for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kang25a/kang25a.pdf)
- **Conversational ability** (constructs)
  > We evaluate ChatVLA across three dimensions: conversational ability (visual question answering), general multimodal understanding, and general robot control. (Section 1)
  - [Cost-Optimal Grouped-Query Attention for Long-Context Modeling](https://aclanthology.org/2025.emnlp-main.273.pdf)
