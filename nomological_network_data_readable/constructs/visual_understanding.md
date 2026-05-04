# Visual understanding
**Type:** Construct  
**Referenced in:** 95 papers  
**Also known as:** Single-image visual understanding, Image comprehension, Image understanding, Visual comprehension, Vision understanding, Visual scene comprehension, Medical visual comprehension, Structured image understanding, Visual-semantic understanding, Global image comprehension, Image comprehension ability, Image-level understanding, Visual information comprehension, Scene recognition  

## State of the Field

Across the surveyed literature, visual understanding is predominantly framed as a model's latent ability to interpret, comprehend, and extract meaningful information from visual inputs, a concept also referred to as image comprehension, vision understanding, and visual comprehension. While this general definition is prevalent, a smaller body of work specifies this construct for particular domains, such as 'medical visual comprehension' for clinical images or 'structured image understanding' for tables and charts. The field operationalizes this construct primarily through performance on a range of evaluation benchmarks, with the most frequently cited instruments being MMBench, MM-Vet, VQA-v2, GQA, MME, and POPE. These benchmarks are used to assess various facets of the construct, from 'compositional reasoning and real-world visual understanding' (GQA) to integrating text within images (TextVQA). Visual understanding is often studied alongside concepts like textual reasoning, spatial reasoning, and hallucination, with one paper noting that models can "suffer from hallucination - generating content inconsistent with visual inputs." Some work suggests that enhanced visual comprehension directly benefits multimodal reasoning abilities. Specific challenges in visual understanding are also noted, such as difficulties with "people-related visual facts, particularly actions and expressions" and the need for evaluations that "heavily rely on image inputs" to prevent models from using textual priors.

## Sources

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The ability to interpret and extract meaningful chemical information from visual data, specifically from images of various molecular spectra.

**[MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf) (as "Single-image visual understanding")**
> The ability to comprehend and interpret the content and context of a single visual input.

**[MMSearch: Unveiling the Potential of Large Models as Multi-modal Search Engines](https://proceedings.iclr.cc/paper_files/paper/2025/file/04e6525463afaa460b5a2e6868b18f18-Paper-Conference.pdf) (as "Image comprehension")**
> The latent ability to understand visual inputs well enough to extract relevant query information or recognize important objects and cues.

**[From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf) (as "Image understanding")**
> The model's ability to comprehend and interpret the content and context of visual data.

**[OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf) (as "Visual comprehension")**
> The latent ability to interpret and understand visual information within a language modeling framework.

**[Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf) (as "Vision understanding")**
> The latent ability of a multimodal model to interpret, comprehend, and reason about information presented in images.

**[Dysca: A Dynamic and Scalable Benchmark for Evaluating Perception Ability of LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2372bb107ef0ba85e47c6a2dc7dafda-Paper-Conference.pdf) (as "Visual scene comprehension")**
> The ability to understand and interpret the components, relationships, and overall meaning of a visual scene.

**[Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25n/feng25n.pdf) (as "Visual-semantic understanding")**
> The ability to integrate visual observations with textual context to understand objects, scenes, and task instructions.

**[ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf) (as "Structured image understanding")**
> The ability to interpret and reason about information presented in structured formats like tables and charts.

**[HealthGPT: A Medical Large Vision-Language Model for Unifying Comprehension and Generation via Heterogeneous Knowledge Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25n/lin25n.pdf) (as "Medical visual comprehension")**
> The latent ability of a model to understand and interpret medical images across various modalities and extract meaningful, clinically relevant information through language-based interaction.

**[MuCAL: Contrastive Alignment for Preference-DrivenKG-to-Text Generation](https://aclanthology.org/2025.emnlp-main.721.pdf) (as "Global image comprehension")**
> The ability to form a coherent, integrated understanding of an entire image by connecting multiple objects and their multi-scale representations.

**[Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Image comprehension ability")**
> The ability to accurately interpret visual content in multimodal documents, including details and counts of images.

**[OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf) (as "Image-level understanding")**
> The model's ability to comprehend and reason about the entire image as a whole, including its overall scene, context, and global properties.

**[Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf) (as "Visual information comprehension")**
> The ability to comprehend and process visual data, including capturing diverse semantic information within text-image pair data.

**[Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf) (as "Scene recognition")**
> The task of identifying and classifying the overall environment or setting depicted in an image.

## Relationships

### Visual understanding →
- **MMBench** (measurements) — *measured_by*
  > “For image understanding, we evaluate LLaVA-1.5 and LLaVA-NeXT on (a) diverse multimodal benchmarks: POPE (Li et al., 2023c), GQA (Hudson & Manning, 2019), MMBench (Liu et al., 2023b), VizWiz (Gurari et al., 2018), SEEDBench (Li et al., 2023a), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024)”
  - [MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf)
- **MM-Vet** (measurements) — *measured_by*
  > “MM-Vet examines MLLMs on complicated multimodal reasoning tasks with open-ended Q&A. It focuses on the integration of different core vision-language capabilities, including general visual recognition”
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **VQA-v2** (measurements) — *measured_by*
  > To evaluate its effectiveness, we assess the model's performance on various visual understanding benchmarks... Table 4 presents a comparison... across various VQA and RES benchmarks.
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  > “We compare LLaVA-Mini with LLaVA-v1.5 across 11 benchmarks to thoroughly assess the performance of LLaVA-Mini with minimal vision tokens.”
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **POPE** (measurements) — *measured_by*
  > “For image understanding, we evaluate LLaVA-1.5 and LLaVA-NeXT on (a) diverse multimodal benchmarks: POPE (Li et al., 2023c), GQA (Hudson & Manning, 2019), MMBench (Liu et al., 2023b), VizWiz (Gurari et al., 2018), SEEDBench (Li et al., 2023a), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024)”
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  > Our method demonstrates superior image understanding capabilities, achieving the 80.0%, 63.0%, 48.6%, 70.9%, and 58.8% performance on VQAv2, GQA, VisWiz, SQAI, and VQAT, respectively.
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **TextVQA** (measurements) — *measured_by*
  > Our method demonstrates superior image understanding capabilities, achieving the 80.0%, 63.0%, 48.6%, 70.9%, and 58.8% performance on VQAv2, GQA, VisWiz, SQAI, and VQAT, respectively.
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
- **MMMU** (measurements) — *measured_by*
  > “For image understanding, we evaluate LLaVA-1.5 and LLaVA-NeXT on (a) diverse multimodal benchmarks: POPE (Li et al., 2023c), GQA (Hudson & Manning, 2019), MMBench (Liu et al., 2023b), VizWiz (Gurari et al., 2018), SEEDBench (Li et al., 2023a), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024)”
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
- **MMVP** (measurements) — *measured_by*
  > Furthermore, we also use the vision-centric vision understanding benchmarks, such as MMVP (Tong et al., 2024b), RealWorldQA (xAI, 2024) and CVBench-2D (Tong et al., 2024a). (Section 4.1)
  - [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf)
- **VizWiz** (measurements) — *measured_by*
  > “we evaluate our methods on seven vision datasets, spanning both image classification tasks (CIFAR-10, CIFAR-100, Food101) and visual question-answering tasks (COCO-Color, COCO-Number, VQAv2 and VizWiz)”
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
- **SEED** (measurements) — *measured_by*
  > “We compare LLaVA-Mini with LLaVA-v1.5 across 11 benchmarks to thoroughly assess the performance of LLaVA-Mini with minimal vision tokens.”
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **SciQA** (measurements) — *measured_by*
  > “We compare LLaVA-Mini with LLaVA-v1.5 across 11 benchmarks to thoroughly assess the performance of LLaVA-Mini with minimal vision tokens.”
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
- **CVBench-2D** (measurements) — *measured_by*
  > Furthermore, we also use the vision-centric vision understanding benchmarks, such as MMVP (Tong et al., 2024b), RealWorldQA (xAI, 2024) and CVBench-2D (Tong et al., 2024a). (Section 4.1)
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
- **NLVR2** (measurements) — *measured_by*
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **COCO Caption** (measurements) — *measured_by*
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **SEED-Bench** (measurements) — *measured_by*
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **AI2D** (measurements) — *measured_by*
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **ALFWorld** (measurements) — *measured_by*
  > We next test CoSo on the ALFWorld (Shridhar et al., 2021), an embodied environment for testing decision-making in scenarios requiring visual-semantic understanding. (Section 5.1).
  - [Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25n/feng25n.pdf)
- **MMStar** (measurements) — *measured_by*
  > To assess their visual understanding capability, numerous benchmarks have been developed, focusing on question-answering tasks, such as MMVet (Yu et al., 2023), MMStar (Chen et al., 2024a), and MMMU (Yue et al., 2024). (Section 1)
  - [Painting with Words: Elevating Detailed Image Captioning with Benchmark and Alignment Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6af791af7ef0f3e02bccef011211ca5-Paper-Conference.pdf)
- **RealWorldQA** (measurements) — *measured_by*
  > Furthermore, we also use the vision-centric vision understanding benchmarks, such as MMVP (Tong et al., 2024b), RealWorldQA (xAI, 2024) and CVBench-2D (Tong et al., 2024a). (Section 4.1)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **SQA** (measurements) — *measured_by*
  > We evaluate LWM on standard benchmarks for image and short video understanding, with results presented in Table 5. (Section 4.3.2)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **ChartMimic** (measurements) — *measured_by*
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
- **LLaVA-Bench** (measurements) — *measured_by*
  > LLaVA-Bench consists of 60 carefully designed open-ended questions across 24 images, evaluating models’ visual reasoning and understanding capabilities. (Section 6.1)
  - [EAC-MoE: Expert-Selection Aware Compressor for Mixture-of-Experts Large Language Models](https://aclanthology.org/2025.acl-long.634.pdf)
- **MME-P** (measurements) — *measured_by*
  > For visual understanding and generation, Orthus achieves a GenEval score of 0.58 and an MME-P score of 1265.8 using 7B parameters, outperforming competing baselines including Show-o and Chameleon. (Abstract)
  - [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf)

### → Visual understanding
- **Visual recognition** (constructs) — *causes*
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)

### Associated with
- **Image captioning** (behaviors tasks)
  > The IC instruction exhibits a high degree of shared information with prompts VQ1, VQ2, CR, and IU1.
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **Visual perception** (constructs)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Visual dialogue** (behaviors tasks)
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **Image description** (behaviors tasks)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  > Large Vision-Language Models (LVLMs) have demonstrated impressive capabilities in multi-modal understanding, but they frequently suffer from hallucination - generating content inconsistent with visual inputs. (Abstract)
  - [EAC-MoE: Expert-Selection Aware Compressor for Mixture-of-Experts Large Language Models](https://aclanthology.org/2025.acl-long.634.pdf)
- **Social bias** (constructs)
  > In this work, we characterize the Western bias of VLMs in image understanding and investigate the role that language plays in this disparity. (Section 1)
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **Image classification** (behaviors tasks)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **Spatial perception** (constructs)
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
- **Textual reasoning** (behaviors tasks)
  > “the four datasets where ORM performs better (MathVista, MathVerse, MMStar, and MMMU Pro) primarily feature formal reasoning and mathematical problems, whereas RealWorldQA focuses on real-world scenarios.”
  - [When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using SmallVLMs](https://aclanthology.org/2025.emnlp-main.1614.pdf)
