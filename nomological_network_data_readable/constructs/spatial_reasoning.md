# Spatial reasoning
**Type:** Construct  
**Referenced in:** 123 papers  
**Also known as:** Visual-spatial reasoning, Spatial awareness, Scene-level visual perception, Spatial language understanding, Large-scale spatial cognition, Small-scale spatial cognition, Spatial cognition, Spatial localization ability, Spatial orientation, Spatial visualization, Spatial intelligence, Image-level visual perception, Directional reasoning, Spatiality, Spatial-temporal orientation awareness, Multi-frame integration, Spatial-temporal knowledge, 3D scene representation  

## State of the Field

Across the provided literature, spatial reasoning is most commonly defined as the ability to understand, navigate, and comprehend relationships within 2D or 3D environments. This broad concept is also framed under more specific terms such as 'spatial understanding,' 'spatial awareness,' and 'spatial cognition,' which emphasize aspects like interpreting object positions, maintaining an internal model of location, and mentally manipulating shapes. A more detailed framing distinguishes between 'large-scale spatial cognition' for navigating environments and 'small-scale spatial cognition' for mentally transforming objects. The field operationalizes this construct using a variety of benchmarks, including VSR, RefCOCO, Maze, Bongard Problems, and GQA, which one paper notes 'validates spatial reasoning'. Several papers observe that this is a challenging capability for models; for example, one study states that 'spatial understanding appears to be the most challenging across all textual models' (ScImage: How good are multimodal large language models at scientific text-to-image generation?). The construct is frequently studied alongside visual reasoning, geometric reasoning, and referring expression understanding. Some research suggests that spatial reasoning influences downstream behaviors like robotic manipulation and pathfinding, with one paper proposing it allows models to 'generalize to novel scenarios' (Vision Language Models are In-Context Value Learners). Overall, the construct encompasses abilities ranging from interpreting simple relative positions, such as 'an orange on the left of an apple', to building and maintaining complex 3D scene representations from visual inputs over time.

## Sources

**[DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf)**
> The ability to understand and navigate within 2D or 3D environments and comprehend spatial relationships.

**[Enhancing LLM Reasoning via Vision-Augmented Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/328c922d068dd4ccb23cec5c64e6c7fc-Paper-Conference.pdf) (as "Visual-spatial reasoning")**
> The ability to interpret, process, and reason about information presented through visual and spatial clues, rather than purely textual descriptions.

**[ScImage: How good are multimodal large language models at scientific text-to-image generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/146b5b0feb14fe8e630669ad1faba25e-Paper-Conference.pdf) (as "Spatial understanding")**
> The model's latent ability to correctly interpret and represent spatial relationships between objects, such as their relative positions.

**[Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf) (as "Spatial awareness")**
> The model's internal understanding of the location and spatial relationships of objects or regions within an image.

**[Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf) (as "Visual recognition")**
> The ability to identify and describe visual elements and their relationships within an image, such as objects or specific details.

**[Do Vision-Language Models Represent Space and How? Evaluating Spatial Frame of Reference under Ambiguities](https://proceedings.iclr.cc/paper_files/paper/2025/file/af2d9fb5bcee19ef2dfa70d843520c97-Paper-Conference.pdf) (as "Spatial language understanding")**
> The model's ability to interpret the meaning of natural language expressions that describe spatial relations.

**[ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf) (as "Scene-level visual perception")**
> The ability to understand and describe whole-image content at the scene level.

**[ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb261df4322a8bd0a73093c4d8a0d02d-Paper-Conference.pdf) (as "Spatial perception")**
> The model's ability to interpret and understand spatial properties and relationships from visual inputs, without relying on an explicit map.

**[Does Spatial Cognition Emerge in Frontier Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb92196c6d2afe416528be19ba9963bc-Paper-Conference.pdf) (as "Spatial cognition")**
> The ability to perceive, interpret, represent, and interact with objects and environments, including building mental representations to support navigation and manipulation.

**[Does Spatial Cognition Emerge in Frontier Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb92196c6d2afe416528be19ba9963bc-Paper-Conference.pdf) (as "Large-scale spatial cognition")**
> The ability to build and use spatial representations of large environments for tasks like navigation and spatial reasoning.

**[Does Spatial Cognition Emerge in Frontier Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb92196c6d2afe416528be19ba9963bc-Paper-Conference.pdf) (as "Small-scale spatial cognition")**
> The ability to perceive, imagine, and mentally transform objects or shapes in two or three dimensions.

**[Does Spatial Cognition Emerge in Frontier Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb92196c6d2afe416528be19ba9963bc-Paper-Conference.pdf) (as "Spatial orientation")**
> The ability to imagine a different viewpoint in space and determine relative directions or orientations from that perspective.

**[Does Spatial Cognition Emerge in Frontier Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb92196c6d2afe416528be19ba9963bc-Paper-Conference.pdf) (as "Spatial visualization")**
> The ability to mentally manipulate and transform 2D or 3D stimuli and complex spatial configurations.

**[ThinkBot: Embodied Instruction Following with Thought Chain Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ffa8551239448e07ced48311bf88f6f3-Paper-Conference.pdf) (as "Spatial localization ability")**
> The latent capacity of a model to determine the physical position of objects in an environment, particularly when reasoning from linguistic descriptions.

**[Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf) (as "Image-level visual perception")**
> The broader ability to understand whole-image content and preserve general vision-language performance while adding region-level prompting.

**[Where Am I and What Will I See: An Auto-Regressive Model for Spatial Localization and View Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/786e39208b37bfcb0ad89413f155df99-Paper-Conference.pdf) (as "Spatial intelligence")**
> The ability of a machine to perceive, reason, and act in three dimensions within space and time, encompassing the understanding of spatial relationships between objects and scenes.

**[Core Knowledge Deficits in Multi-Modal Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25p/li25p.pdf) (as "Spatiality")**
> The a priori understanding of spatial properties and Euclidean structure in the world.

**[Hypo3D: Exploring Hypothetical Reasoning in 3D](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mao25b/mao25b.pdf) (as "Directional reasoning")**
> The ability to understand and reason about directional terms and spatial orientation within a consistent reference frame.

**[LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf) (as "Spatial-temporal orientation awareness")**
> The ability to perceive and reason about the movement, positioning, and directional changes of objects across both space and time in a video sequence.

**[ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming](https://aclanthology.org/2025.emnlp-main.810.pdf) (as "Spatial-temporal knowledge")**
> The latent ability to construct and update a mental model of the environment that integrates spatial layout and dynamic state changes over time.

**[Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries](https://aclanthology.org/2025.emnlp-main.816.pdf) (as "Multi-frame integration")**
> The capacity to accumulate and synthesize geometric and visual cues across non-overlapping video frames to form a unified understanding of a scene.

**[Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries](https://aclanthology.org/2025.emnlp-main.816.pdf) (as "3D scene representation")**
> The internal construction and maintenance of a metrically accurate, three-dimensional model of a scene from egocentric visual inputs, enabling spatial inference across time.

## Relationships

### Spatial reasoning →
- **VSR** (measurements) — *measured_by*
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **Robotic manipulation** (behaviors tasks) — *causes*
  - [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)
- **Pathfinding** (behaviors tasks) — *causes*
  - [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)
- **BLINK** (measurements) — *measured_by*
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **RefCOCO** (measurements) — *measured_by*
  - [ReMI: A Dataset for Reasoning with Multiple Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ea56c0baacac9f7764257a43a93c90a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (constructs) — *causes*
  > state-of-the-art VLMs have exhibited strong spatial reasoning and temporal understanding capabilities across various vision tasks (Nag et al., 2022; Chen et al., 2024; Hong et al., 2023; Gao et al., 2024), allowing them to generalize to novel scenarios. (Section 1)
  - [Vision Language Models are In-Context Value Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/54854cf15a24fff9f5134a8641136fe4-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  > GQA Hudson & Manning (2019) validates spatial reasoning
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Maze** (measurements) — *measured_by*
  > We validate MVoT’s effectiveness through controlled experiments across three dynamic spatial reasoning tasks. MAZE (Ivanitskiy et al., 2023) and MINIBEHAVIOR (Jin et al., 2023) focus on interactions with spatial layouts. (1. Introduction)
  - [Imagine While Reasoning in Space: Multimodal Visualization-of-Thought](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cz/li25cz.pdf)
- **Bongard Problems** (measurements) — *measured_by*
  > When focusing on the different BP categories (cf. Figure 4 middle), we observe that humans are substantially better at solving BPs that have spatial reasoning components. I.e., spatial is one of the trickiest categories for current VLM models, with all investigated models solving under 25%.
  - [Bongard in Wonderland: Visual Puzzles that Still Make AI Go Mad?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wust25a/wust25a.pdf)
- **TTT-Bench** (measurements) — *measured_by*
  > In this work, we introduce TTT-Bench, a new benchmark that is designed to evaluate basic strategic, spatial, and logical reasoning abilities in LRMs through a suite of four two-player Tic-Tac-Toe-style games that humans can effortlessly solve from a young age. (Abstract)
  - [MultiMatch: Multihead Consistency Regularization Matching for Semi-Supervised Text Classification](https://aclanthology.org/2025.emnlp-main.140.pdf)

### → Spatial reasoning
- **Abstract reasoning** (constructs) — *causes*
  - [Conan-Embedding-v2: Training anLLMfrom Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.759.pdf)

### Associated with
- **Visual reasoning** (constructs)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Webpage understanding** (constructs)
  - [Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cb66be286795d71f89367d596bf78ea7-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination** (behaviors tasks)
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Referring expression understanding** (behaviors tasks)
  > Referring Expression Comprehension (REC) (Mao et al., 2016), which involves localizing an object in an image based on a complex textual query, requiring both spatial and semantic reasoning.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Spatial perception** (constructs)
  - [Does Spatial Cognition Emerge in Frontier Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb92196c6d2afe416528be19ba9963bc-Paper-Conference.pdf)
- **Physical world understanding** (constructs)
  > “Physical Object Relationships: Evaluation of spatial relationships involving objects’ relative or absolute positions and motions.”
  - [PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf)
- **Situated question answering** (behaviors tasks)
  > Situated QA is designed with different types of questions targeting various levels of spatial reasoning ability for embodied agents.
  - [SPARTUN3D: Situated Spatial Understanding of 3D World in Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/b633e7052970b8f5aa1a69164d99e9e8-Paper-Conference.pdf)
- **Geometric reasoning** (constructs)
  > "Geometric ability is a significant challenge for large language models (LLMs) due to the need for advanced spatial comprehension and abstract thinking."
  - [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf)
- **Object localization** (behaviors tasks)
  > "It includes two task types: spatial object localization (2,361 samples), which helps models learn spatial reasoning"
  - [Cognitive Linguistic Identity Fusion Score (CLIFS): A ScalableCognition‐Informed Approach to Quantifying Identity Fusion from Text](https://aclanthology.org/2025.emnlp-main.589.pdf)
- **Information extraction** (behaviors tasks)
  - [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.844.pdf)
- **SQA** (measurements)
  > It encompasses a diverse range of question types, including object identification, spatial relationships, scene-level understanding, and general reasoning. (Section 5)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
- **3D question answering** (behaviors tasks)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
