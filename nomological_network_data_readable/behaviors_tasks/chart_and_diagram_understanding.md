# Chart and diagram understanding
**Type:** Behavior  
**Referenced in:** 24 papers  
**Also known as:** Chart interpretation, Chart understanding, Diagram interpretation, Flowchart understanding, Diagram comprehension, Figure question answering, Diagram understanding, Diagram and table interpretation, Scientific figure analysis, Scientific diagram analysis, Diagram Understanding, Science diagram comprehension, Chart reasoning  

## State of the Field

Across the provided literature, chart and diagram understanding is predominantly framed as the observable behavior of interpreting and reasoning about information presented in structured visual formats. The scope of this behavior is broad, encompassing various types of visualizations such as bar charts, line charts, pie charts, flowcharts, and scientific or schematic diagrams. The field operationalizes and measures this behavior using a range of benchmarks, including ChartQA, AI2D, MMMU, MMC, and MUIRBENCH. For instance, ChartQA is frequently used to evaluate a model's "understanding, reasoning, and data extraction skills," while AI2D is cited for assessing "science diagram comprehension." While most definitions center on question-answering that requires extracting data and performing logical or arithmetic processing, a smaller set of work expands the behavior to include tasks like captioning, summarization, and description, as seen in the definition of "Scientific figure analysis." The contexts for this behavior vary, with a recurring focus on scientific diagrams, as one study notes current models have "poor perception abilities in understanding diagrams related to physical sciences (e.g., circuit diagrams)" (Chain-of-region: Visual Language Models Need  Details for Diagram Analysis). At a higher level of abstraction, some work categorizes both chart and diagram understanding as components of a broader "Image Recognition & Reasoning" capability.

## Sources

**[Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf) (as "Chart interpretation")**
> The task of extracting and reasoning about data presented in graphical charts.

**[Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf) (as "Chart question answering")**
> Answering questions that require arithmetic and logical processing with data visualizations like bar charts, line charts, and pie charts.

**[MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf) (as "Chart understanding")**
> Interpreting charts or plots and extracting information from them.

**[Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf) (as "Diagram interpretation")**
> Interpreting the structure and meaning of diagram elements and their interrelations.

**[Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf) (as "Flowchart understanding")**
> Interpreting flowchart diagrams and answering questions about steps, decisions, or outcomes represented in the chart.

**[Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf) (as "Diagram comprehension")**
> The observable task of understanding and answering questions about the content of a diagram.

**[Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf) (as "Figure question answering")**
> A specific type of visual question answering where the questions pertain to data visualizations like charts and figures.

**[ConsistentChat: Building Skeleton-Guided Consistent Multi-Turn Dialogues for Large Language Models from Scratch](https://aclanthology.org/2025.emnlp-main.425.pdf) (as "Diagram understanding")**
> The task of interpreting and answering questions about scientific or schematic diagrams.

**[TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning](https://aclanthology.org/2025.emnlp-main.711.pdf) (as "Diagram and table interpretation")**
> The task of extracting and understanding information presented in structured visual formats like diagrams, charts, and tables.

**[SmartBench: Is YourLLMTruly a GoodChinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.195.pdf) (as "Scientific figure analysis")**
> Interpreting scientific figures and producing analytical text about them.

**[Chain-of-region: Visual Language Models Need  Details for Diagram Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/464012c83279e19be4cd42c25f341c92-Paper-Conference.pdf) (as "Scientific diagram analysis")**
> The observable task of interpreting and answering questions about complex, structured images such as charts, graphs, and technical illustrations.

**[Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf) (as "Science diagram comprehension")**
> The task of interpreting and answering questions about diagrams, charts, and figures from scientific contexts.

**[Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf) (as "Diagram Understanding")**
> Interpreting visual diagrams as part of image recognition and reasoning cross capabilities.

**[TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types](https://proceedings.iclr.cc/paper_files/paper/2025/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf) (as "Chart reasoning")**
> Interpreting and deriving insights from visual data representations like graphs and charts.

## Relationships

### Chart and diagram understanding →
- **ChartQA** (measurements) — *measured_by*
  > Previous works focus on chart question answering (Masry et al., 2022; Methani et al., 2020; Xu et al., 2023; Wang et al., 2024b; Li et al., 2024c; Zeng et al., 2024) and chart captioning (Rahman et al., 2023; Kantharaj et al., 2022). (Section 5)
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **AI2D** (measurements) — *measured_by*
  > AI2D (Kembhavi et al., 2016), a multiple-choice benchmark, evaluates the model capabilities for science diagram comprehension. (Section 4.1)
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
- **CharXiv** (measurements) — *measured_by*
  - [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MathVista** (measurements) — *measured_by*
  - [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMC** (measurements) — *measured_by*
  > "MathVista and MATH-Vision (mathematical reasoning), MMC (chart understanding), and MME and HallusionBench."
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **MUIRBENCH** (measurements) — *measured_by*
  > [DIAGRAM UNDERSTANDING] aims to evaluate the ability of models to understand information conveyed in diagram images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **MMMU** (measurements) — *measured_by*
  > To align our research focus, we conduct experiments on several sub-categories of MMMU that consists exclusively of scientific diagrams (Section 4).
  - [Chain-of-region: Visual Language Models Need  Details for Diagram Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/464012c83279e19be4cd42c25f341c92-Paper-Conference.pdf)
- **MME-RealWorld** (measurements) — *measured_by*
  - [TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning](https://aclanthology.org/2025.emnlp-main.711.pdf)
