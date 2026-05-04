# Object hallucination
**Type:** Behavior  
**Referenced in:** 35 papers  

## State of the Field

Across the provided papers, object hallucination is consistently defined as an observable failure mode where a model generates text referring to objects not present in the corresponding visual input. A less common framing expands this to include the neglect of visible objects. The field operationalizes this behavior using numerous evaluation instruments, with the POPE benchmark being the most frequently cited. POPE is described as a "widely used benchmark" that quantifies object hallucination through VQA-based tasks or binary classification to determine the presence or absence of specific objects. Another common measurement instrument is CHAIR, which is designed for open-ended captioning and calculates the proportion of mentioned objects that are not in the ground-truth image labels. Other benchmarks such as MME, AMBER, and MM-Hal-Bench are also used to assess aspects like object existence and count. This behavior is treated as a specific type of hallucination and is studied in the context of tasks like visual question answering and image description.

## Sources

**[VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf)**
> An observable failure mode where the model generates text that refers to objects not present in the corresponding image or video frame.

## Relationships

### Object hallucination →
- **POPE** (measurements) — *measured_by*
  > “POPE (Li et al., 2023d) is a widely used benchmark for assessing object hallucinations in LVLMs”
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **CHAIR** (measurements) — *measured_by*
  > “CHAIR (Rohrbach et al., 2018) evaluates object hallucinations in open-ended captioning tasks”
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  > MME (Fu et al., 2024) provides a benchmark for assessing LVLMs across various tasks. Following Yin et al. (2023), we evaluate hallucination using four subtasks: Existence, Count, Position, and Color
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **AMBER** (measurements) — *measured_by*
  > To evaluate performance on both generative and discriminative tasks, we use AMBER (Wang et al., 2023b), which measures hallucination using several metrics. For generative tasks, AMBER assesses the frequency of hallucinated objects in image descriptions... (Section 4.1)
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **COCO** (measurements) — *measured_by*
  > To evaluate object hallucination in visual caption, we use images from the COCO validation and Nocaps (Agrawal et al., 2019) datasets (Section 5.1).
  - [Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention](https://proceedings.iclr.cc/paper_files/paper/2025/file/8001c3568152d134d821cd46d4d84768-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **MS-COCO** (measurements) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **NoCaps** (measurements) — *measured_by*
  > To evaluate object hallucination in visual caption, we use images from the COCO validation and Nocaps (Agrawal et al., 2019) datasets (Section 5.1).
  - [Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention](https://proceedings.iclr.cc/paper_files/paper/2025/file/8001c3568152d134d821cd46d4d84768-Paper-Conference.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  > POPE ... is a scalable framework for detecting object hallucinations in LVLMs, utilizing SEEM-annotated datasets from ... A-OKVQA Schwenk et al. (2022)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
- **MM-Hal-Bench** (measurements) — *measured_by*
  > we benchmark VTI on the MMHAL dataset with the evaluations of eight different hallucination types.
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Object HalBench** (measurements) — *measured_by*
  - [LibEvolutionEval: A Benchmark and Study for Version-Specific Code Generation](https://aclanthology.org/2025.naacl-long.349.pdf)

### → Object hallucination
- **Modality alignment** (constructs) — *causes*
  - [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  > "we compared with various decoding strategies on the SEEM-annotated MSCOCO and A-OKVQA datasets provided by POPE" and "addressing object hallucinations"
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Perception** (constructs)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  > "POPE is a VQA-based metric for assessing object hallucination in MLLMs"
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Image description** (behaviors tasks)
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
