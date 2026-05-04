# Visual grounding
**Type:** Construct  
**Referenced in:** 80 papers  
**Also known as:** Multimodal grounding, Multimodal referring, Object grounding, Shape grounding, Spatio-temporal object grounding, Referring expression segmentation, Region-text alignment, Phrase grounding, UI grounding, Cross-modal misalignment, Referring expression grounding, GUI action grounding, Rule grounding  

## State of the Field

Across the surveyed literature, visual grounding is predominantly defined as a model's latent ability to connect textual descriptions or instructions with their corresponding spatial regions in a visual input. While this core concept is widely shared, the specific terminology varies, including "multimodal grounding," "spatial understanding," "phrase grounding," and "referring expression comprehension," applied to diverse visual media such as images, 3D scenes, videos, and GUIs. A much less common usage, found in one paper, frames "rule grounding" as a logical task of instantiating abstract rules with constants. The field most frequently operationalizes this construct through tasks requiring the localization of objects, which are measured by benchmarks like RefCOCO, RefCOCO+, and RefCOCOg. The expected model behavior is to produce a spatial reference, such as generating bounding box coordinates or segmentation masks, with one study noting that models are "required to explicitly ground objects in images by generating coordinates for them" (Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data). Visual grounding is often discussed in contrast to hallucination, with multiple papers describing hallucinations as responses that are "plausible yet visually ungrounded" (The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering). The construct is reported to influence capabilities like robotic manipulation and visual question answering and is studied alongside related tasks such as object detection and semantic segmentation.

## Sources

**[Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf) (as "Multimodal grounding")**
> The latent ability of a model to associate textual descriptions, such as phrases or referring expressions, with their corresponding spatial regions in an image.

**[Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf) (as "Multimodal referring")**
> The latent ability of a model to understand a visual reference, such as a bounding box, and generate an appropriate textual description for the specified object or region.

**[LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf)**
> The ability to use scene information to connect language instructions with visible objects and their states in the environment.

**[Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf) (as "Spatial understanding")**
> The latent ability to align visual regions with semantic descriptions, enabling both comprehension of spatial references and localization of described content.

**[Multi-modal Situated Reasoning in 3D Scenes](https://proceedings.neurips.cc/paper_files/paper/2024/file/feaeec8ec2d3cb131fe18517ff14ec1f-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Object grounding")**
> The task of localizing a specific 3D object in a scene based on a natural language description.

**[GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shabbir25a/shabbir25a.pdf) (as "Referring expression segmentation")**
> Generating a segmentation mask for a specific object in an image based on a natural language referring expression.

**[Primitive Vision: Improving Diagram Understanding in MLLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25n/zhang25n.pdf) (as "Shape grounding")**
> The alignment of detected shapes in a diagram (e.g., circle, rectangle) with their semantic labels and spatial locations.

**[TUMTraf VideoQA: Dataset and Benchmark for Unified Spatio-Temporal Video Understanding in Traffic Scenes](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25g/zhou25g.pdf) (as "Spatio-temporal object grounding")**
> Predicting the precise spatio-temporal coordinates (frame, x, y) of a referred object in a video as a tuple output.

**[Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf) (as "Referring expression comprehension")**
> The task of localizing an object or region in an image that is described by a natural language phrase.

**[Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf) (as "Phrase grounding")**
> The task of associating specific phrases or words in a text description with their corresponding regions or objects in an image.

**[Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf) (as "Region-text alignment")**
> The model's ability to match textual descriptions with specific image regions, demonstrated through contrastive learning on region-caption pairs.

**[Improbable Bigrams Expose Vulnerabilities of Incomplete Tokens in Byte-Level Tokenizers](https://aclanthology.org/2025.emnlp-main.920.pdf) (as "UI grounding")**
> Producing bounding box coordinates that accurately localize a specified UI element on a mobile screen in response to a textual instruction.

**[CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning inSLMs](https://aclanthology.org/2025.emnlp-main.705.pdf) (as "Cross-modal misalignment")**
> Incorrectly associating textual or visual information from irrelevant regions of the image, leading to inaccurate answers.

**[The Role of Outgoing Connection Heterogeneity in Feedforward Layers of Large Language Models](https://aclanthology.org/2025.emnlp-main.1144.pdf) (as "Referring expression grounding")**
> The task of linking a textual description (referring expression) to the corresponding object or region in an image.

**[MoVa: Towards Generalizable Classification of Human Morals and Values](https://aclanthology.org/2025.emnlp-main.1688.pdf) (as "GUI action grounding")**
> Mapping natural language instructions to specific executable elements or locations on a GUI screen, such as clicking a button or selecting a menu item.

**[Combining Constrained and Unconstrained Decoding via Boosting:BoostCDand Its Application to Information Extraction](https://aclanthology.org/2025.emnlp-main.927.pdf) (as "Rule grounding")**
> Instantiating abstract rules with specific constants to prepare for logical inference.

## Relationships

### Visual grounding →
- **RefCOCO** (measurements) — *measured_by*
  > To thoroughly assess our model’s understanding of pixel-level instances, we evaluate its performance on referring segmentation and grounding benchmarks, including refCOCO (Kazemzadeh et al., 2014), refCOCO+ (Kazemzadeh et al., 2014), and refCOCOg (Caesar et al., 2018).
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **RefCOCOg** (measurements) — *measured_by*
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
- **ScreenSpot** (measurements) — *measured_by*
  > We first evaluate UGround on the ScreenSpot benchmark (Cheng et al., 2024), which is specifically designed for visual grounding on GUIs. (Section 3.1)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **Flickr30k Entities** (measurements) — *measured_by*
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *causes*
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **MMVP** (measurements) — *measured_by*
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **Visual7W** (measurements) — *measured_by*
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [A Concept-Based Explainability Framework for Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f4fba41b554f9aaa013c4062a1c40518-Paper-Conference.pdf)
- **Robotic manipulation** (behaviors tasks) — *causes*
  - [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *causes*
  > Ablation studies also empirically show that the integration of visual grounding capability allows medical VLMs to achieve improved performance on other downstream tasks.
  - [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.89.pdf)
- **MMStar** (measurements) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **MUIRBENCH** (measurements) — *measured_by*
  > [VISUAL GROUNDING] aims to evaluate the ability of models to ground a specific object and seek information about it within multiple images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  > Several causes of hallucinations have been identified including biased training data (Liu et al., 2023), the inability of vision encoders to accurately ground images (Jain et al., 2024), misalignment among different modalities (Liu et al., 2024b), and insufficient context attention in LLM decoders (Huang et al., 2024; Liu et al., 2024d). (Section 2.2)
  - [CityEQA: A HierarchicalLLMAgent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **Grounding** (constructs) — *measured_by*
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)

### → Visual grounding
- **Instruction following** (constructs) — *causes*
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
- **Multimodal reasoning** (constructs) — *causes*
  > In the reasoning stage, RSVP employs multimodal chain-of-thought visual prompts to help MLLMs understand queries and infer targets, generating interpretable region proposals that enhance visual grounding. (Section 1)
  - [QDTSynth: Quality-Driven Formal Theorem Synthesis for Enhancing Proving Performance ofLLMs](https://aclanthology.org/2025.acl-long.715.pdf)

### Associated with
- **Referring expression understanding** (behaviors tasks)
  > flexible switching between referring expression segmentation, open-vocabulary segmentation, and other visual grounding tasks. (Section 1)
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Referring expression generation** (behaviors tasks)
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  > they are far from perfect and still suffer from generating hallucinated texts that are not grounded to the reference image. (Section 1)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Object detection** (behaviors tasks)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
- **Visual recognition** (constructs)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **3D understanding** (constructs)
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
- **Bounding box prediction** (behaviors tasks)
  > a grounding module (Gaze) provides precise visual focus by predicting bounding box annotations. (Section 1)
  - [Revealing and Mitigating the Challenge of Detecting Character Knowledge Errors inLLMRole-Playing](https://aclanthology.org/2025.emnlp-main.1690.pdf)
- **Semantic segmentation** (behaviors tasks)
  > flexible switching between referring expression segmentation, open-vocabulary segmentation, and other visual grounding tasks. (Section 1)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
