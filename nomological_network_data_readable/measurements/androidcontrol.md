# AndroidControl
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

AndroidControl is consistently described as a benchmark for evaluating agent performance on tasks within the Android mobile platform. Across the provided literature, it is used to measure constructs such as `Agency`, `Generalization`, and `Cross-domain generalization`. The benchmark is operationalized with at least two distinct variants mentioned in one paper: `AndroidControl-Low`, which provides agents with both low-level and high-level instructions, and `AndroidControl-High`, which provides only high-level instructions. Some work also characterizes it as an "offline GUI benchmark" and an "in-distribution" dataset, positioning it alongside other evaluation tools for mobile, web, and desktop environments.

## Sources

**[OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)**
> A benchmark for evaluating mobile agent tasks on Android platforms, with variants for low-level and high-level instruction scenarios.

## Relationships

### → AndroidControl
- **Cross-domain generalization** (constructs) — *measured_by*
  - [On the Effects of Data Scale on UI Control Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/a79f3ef3b445fd4659f44648f7ea8ffd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Agency** (constructs) — *measured_by*
  > We examine five distinct agent benchmarks across three different platforms: AndroidControl (Li et al., 2024) and GUI-Odyssey (Lu et al., 2024a) for mobile agents; GUI-Act-Web (Chen et al., 2024a) and OmniAct-Web (Kapoor et al., 2024) for web agents; and OmniAct-Desktop for Windows environments.
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://aclanthology.org/2025.acl-long.277.pdf)
