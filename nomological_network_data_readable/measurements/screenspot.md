# ScreenSpot
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

ScreenSpot is consistently described across the provided literature as a benchmark for assessing grounding capabilities within Graphical User Interfaces (GUIs). The prevailing usage is to evaluate "single-step GUI grounding capabilities across multiple platforms," a concept closely related to visual grounding, which it is also explicitly stated to measure. Some work also uses ScreenSpot to validate model adaptability, particularly a model's "universal grounding capability across platforms." The benchmark's evaluation procedure is defined in one paper, which notes that "a prediction is considered correct if the predicted location falls within the ground truth element's bounding box" ("OS-ATLAS: Foundation Action Model for Generalist GUI Agents"). This assessment is conducted across environments including mobile, desktop, and web. A smaller line of work also positions it as a tool for evaluating general multi-modal task performance.

## Sources

**[OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)**
> A benchmark that assesses single-step GUI grounding capabilities across multiple platforms by evaluating whether predicted locations fall within ground truth element bounding boxes.

## Relationships

### → ScreenSpot
- **GUI understanding** (constructs) — *measured_by*
  > “We begin by conducting a comprehensive evaluation of the GUI grounding performance of OS-Atlas-Base. Our evaluation utilizes ScreenSpot (Cheng et al., 2024), which assesses single-step GUI grounding capabilities across multiple platforms.”
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **Visual grounding** (constructs) — *measured_by*
  > We first evaluate UGround on the ScreenSpot benchmark (Cheng et al., 2024), which is specifically designed for visual grounding on GUIs. (Section 3.1)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **Adaptability** (constructs) — *measured_by*
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **Grounding** (constructs) — *measured_by*
  - [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf)
