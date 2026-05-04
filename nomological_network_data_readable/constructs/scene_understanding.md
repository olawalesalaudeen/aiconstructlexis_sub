# Scene understanding
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Scene recognition  

## State of the Field

Across the provided literature, scene understanding is most commonly defined as a cognitive ability to perceive a visual environment, identify critical objects, and interpret their semantic, spatial, and motion attributes. A narrower framing, referred to as "scene recognition," treats it as the ability to identify and classify scenes, while another definition focuses on its role in supporting navigation decisions. The construct is operationalized and measured using benchmarks like MUIRBENCH, which evaluates the ability to understand a scene from "multiple views from multiple surveillance images." Some work also describes using a Vision-Language Model (VLM) as a component for scene understanding. The concept is frequently positioned as a precursor to other capabilities, with some research stating it influences decision-making, particularly in the context of autonomous driving. This application is a recurring theme, where the goal is to simplify the environment by focusing on "critical objects that may affect driving decisions" to ensure safety. This focus on navigation is also present in work on UAVs, where enhanced scene understanding is reported to produce "more accurate and adaptable pose sequences."

## Sources

**[Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)**
> The cognitive ability to perceive a visual environment, selectively identify critical objects, and interpret their semantic, spatial, and motion attributes to form a comprehensive understanding.

**[UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Scene recognition")**
> The ability to identify and classify scenes or environments depicted in images.

## Relationships

### Scene understanding →
- **Decision-making** (constructs) — *causes*
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **MUIRBENCH** (measurements) — *measured_by*
  > [SCENE UNDERSTANDING] aims to evaluate the ability of models to understand a scene comprised of multiple views from multiple surveillance images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
