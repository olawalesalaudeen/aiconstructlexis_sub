# GUI understanding
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** GUI grounding, UI grounding, GUI Understanding, UI understanding  

## State of the Field

Across the surveyed literature, GUI understanding is predominantly characterized in two interrelated ways, with authors using the terms "GUI" and "UI" interchangeably. The first and broader framing defines it as the capability to comprehend the structure, content, and function of graphical user interfaces from visual inputs. The second, more specific framing, frequently referred to as "GUI grounding," focuses on the ability to transform natural language instructions into executable, coordinate-based actions. Some work treats these as distinct concepts, while other definitions of understanding encompass grounding, such as the capacity to "interpret complex mobile interface layouts and identify relevant on-screen information for action selection" (SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION). The more action-oriented "grounding" is described as converting instructions into "actions and associated parameters (e.g., element coordinates)" (OS-ATLAS: Foundation Action Model for Generalist GUI Agents). This construct is operationalized and measured using various benchmarks. Among the provided sources, `ScreenSpot` is a commonly mentioned instrument for assessing "single-step GUI grounding capabilities." Other benchmarks used to evaluate the construct include `WebSRC` and `GUI-WORLD`. Some research reports that GUI understanding enhances downstream tasks like `Code generation`, and that pre-training for grounding is linked to improved `Out-of-distribution generalization`.

## Sources

**[OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf) (as "GUI grounding")**
> The model's ability to transform natural language instructions into executable actions, such as coordinate-based operations, within a graphical user interface.

**[AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf) (as "UI grounding")**
> The ability to accurately map a natural language instruction to the specific coordinates of the corresponding graphical user interface (GUI) element on a screen.

**[Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)**
> The capability to comprehend the structure, content, and function of graphical user interfaces from visual inputs.

**[OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf) (as "GUI Understanding")**
> The latent capability to interpret visual screen information and accurately identify interactive UI elements.

**[SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf) (as "UI understanding")**
> The capacity to interpret complex mobile interface layouts and identify relevant on-screen information for action selection.

## Relationships

### GUI understanding →
- **ScreenSpot** (measurements) — *measured_by*
  > “We begin by conducting a comprehensive evaluation of the GUI grounding performance of OS-Atlas-Base. Our evaluation utilizes ScreenSpot (Cheng et al., 2024), which assesses single-step GUI grounding capabilities across multiple platforms.”
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **WebSRC** (measurements) — *measured_by*
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **GUI-WORLD** (measurements) — *measured_by*
  > Likewise, we also establish a comprehensive benchmark for GUI understanding, which encompasses nine mainstream MLLMs (e.g., GPT-4o (OpenAI, 2024) and Gemini-1.5-Pro (Team et al., 2023)), five keyframe selection strategies (e.g., UVD (Zhang et al., 2024d)), and six GUI scenarios, aiming to provide a thorough evaluation of the GUI-oriented understanding capabilities of MLLMs. (Section 1)
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **Out-of-distribution generalization** (constructs) — *causes*
  > omitting the pre-training stage significantly degrades performance... These results highlight the critical importance of the data infrastructure for grounding data synthesis; with this infrastructure in place, we can easily improve OOD downstream performance simply by scaling the pre-training corpus. (Section 5.3)
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)

### Associated with
- **Action grounding** (behaviors tasks)
  - [SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf)
