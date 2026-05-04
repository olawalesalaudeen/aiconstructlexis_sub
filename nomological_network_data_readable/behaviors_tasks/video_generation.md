# Video generation
**Type:** Behavior  
**Referenced in:** 20 papers  
**Also known as:** Text-to-video generation, Image-to-video generation, Impossible video generation  

## State of the Field

Across the surveyed literature, video generation is most commonly defined as the task of producing coherent and realistic video sequences. The generation process is typically conditioned on various inputs, with a prevalent framing involving generation from textual prompts, a behavior often specified as text-to-video generation. Other conditioning inputs mentioned include class labels, previous video frames, or static images, the latter defining image-to-video generation. A more specialized line of work investigates "impossible video generation," which examines the creation of videos from text prompts describing scenes that violate real-world laws. To operationalize and measure this behavior, researchers employ several benchmarks. VBench is used for the comprehensive evaluation of text-to-video models on dimensions like quality and consistency, while UCF-101 is used for class-conditional generation. Other datasets cited for evaluation include MSRVTT, K600 for frame prediction, and SkyTimelapse. The stated goal is to "faithfully generating videos with the desired attributes and motion patterns" that align with the input prompt or condition.

## Sources

**[LLM-grounded Video Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d9f8b5abc8e0926539ecbb492af7b2f1-Paper-Conference.pdf)**
> Generating coherent and realistic video sequences, either conditioned on class labels or previous frames.

**[Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf) (as "Text-to-video generation")**
> Creating dynamic video content from textual prompts.

**[Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf) (as "Image-to-video generation")**
> Creating dynamic video content based on a static input image.

**[Impossible Videos](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25a/bai25a.pdf) (as "Impossible video generation")**
> The observable act of producing a video that depicts a scene violating real-world physical, biological, geographical, or social laws, as prompted by a text description.

## Relationships

### Video generation →
- **VBench** (measurements) — *measured_by*
  > Our proposed “Probe-Analyze-Refine” workflow, validated through practical use cases on multimodal tasks such as image-text pre-training with CLIP, image-to-text generation with LLaVA-like models, and text-to-video generation with DiT-based models, yields transferable and notable performance boosts, such as topping the VBench leaderboard. (Abstract)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **UCF-101** (measurements) — *measured_by*
  > "Video generation. We consider two standard video benchmarks, UCF-101 for class-conditional generation and K600 for frame prediction with 5-frame condition."
  - [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf)
- **MSRVTT** (measurements) — *measured_by*
  - [LLM-grounded Video Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d9f8b5abc8e0926539ecbb492af7b2f1-Paper-Conference.pdf)
