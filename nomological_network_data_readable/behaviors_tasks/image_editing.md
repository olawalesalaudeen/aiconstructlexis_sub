# Image editing
**Type:** Behavior  
**Referenced in:** 24 papers  
**Also known as:** Image inpainting, Object creation, Object removal, Instruction-based image compositing, Identity-preserved inpainting, Identity transfer, Object replacement, Background replacement, Color alteration, Style alteration, Drag-based editing, Content dragging, Object moving, Image in-painting, Image out-painting, Image infilling, Generative fill, Visual editing  

## State of the Field

Across the surveyed literature, the most prevalent definition of image editing is the behavior of modifying an image according to a natural-language instruction. This general framing is specified through a wide variety of sub-tasks, most commonly involving object-level manipulations such as adding, removing, replacing, or altering the color of objects. Other frequently mentioned modifications include changing an image's background or its overall artistic style. A distinct line of work operationalizes this behavior as filling in missing or corrupted parts of an image, a task referred to as "image inpainting," "image infilling," or "generative fill." Less common framings include "drag-based editing," which involves moving content via handle points, and "visual editing," where one paper describes modifying an image by programmatically "drawing boxes, highlighting sections, and masking out areas" to guide a model's attention. To measure performance on this behavior, papers frequently use the MagicBrush benchmark, and also mention using datasets like InstructPix2Pix and DragBench. Image editing is studied as a test of model generalization, and one paper reports that visual editing actions can be used to improve performance on visual reasoning tasks.

## Sources

**[GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf)**
> Modifying an image according to a natural-language instruction, such as replacing, hiding, or recoloring an object.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Image inpainting")**
> The task of filling in missing or corrupted parts of an image based on a textual instruction.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Object creation")**
> The task of adding a new object to an image based on a textual instruction.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Object removal")**
> The task of removing a specified object from an image and plausibly filling the background, guided by a textual instruction.

**[$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf) (as "Instruction-based image compositing")**
> The task of generating a composite image by integrating a reference object into a background image according to a natural language instruction that specifies the object's location and spatial relationship.

**[$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf) (as "Identity-preserved inpainting")**
> The task of modifying the pose or view of an object within an image while preserving its unique visual identity, often guided by a user-provided mask.

**[$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf) (as "Identity transfer")**
> The task of applying the visual identity of a reference object to a different target object already present in a background scene.

**[$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf) (as "Object replacement")**
> The task of substituting an existing object in a background image with a new reference object.

**[I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf) (as "Background replacement")**
> Changing the background of an image to match a target background described in the instruction.

**[I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf) (as "Color alteration")**
> The observable task of modifying the color of a specified object in an image based on a text instruction.

**[I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf) (as "Style alteration")**
> The observable task of changing the artistic or visual style of an entire image based on a text instruction.

**[Localize, Understand, Collaborate: Semantic-Aware Dragging via Intention Reasoner](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dd7c683eddc14f8cabcd6ce8d48cd41-Paper-Conference.pdf) (as "Drag-based editing")**
> Editing an image by moving specified handle points toward target points within an editable region.

**[Localize, Understand, Collaborate: Semantic-Aware Dragging via Intention Reasoner](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dd7c683eddc14f8cabcd6ce8d48cd41-Paper-Conference.pdf) (as "Content dragging")**
> The task of moving or deforming the content within a specified region of an image according to drag points.

**[Localize, Understand, Collaborate: Semantic-Aware Dragging via Intention Reasoner](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dd7c683eddc14f8cabcd6ce8d48cd41-Paper-Conference.pdf) (as "Object moving")**
> The task of relocating an entire object from a source position to a target position within an image.

**[Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (as "Image in-painting")**
> The task of filling in a missing or masked region within an image with plausible, contextually appropriate content.

**[Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (as "Image out-painting")**
> The task of extending an image beyond its original boundaries by generating new content that is consistent with the existing visual context.

**[Glauber Generative Model: Discrete Diffusion Models via Binary Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/125be378b39b10676f56e12e6923b902-Paper-Conference.pdf) (as "Image infilling")**
> The task of generating pixels to fill in a masked or missing region of an image based on the visible parts.

**[Can Generative AI Solve Your In-Context Learning Problem?  A Martingale Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/d90268f01ef06a55630b0588227adf4f-Paper-Conference.pdf) (as "Generative fill")**
> Completing missing parts of an image based on in-context visual examples.

**[ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf) (as "Visual editing")**
> The observable act of modifying an input image through operations such as drawing boxes, highlighting regions, or masking out areas to guide visual attention.

## Relationships

### Image editing →
- **MagicBrush** (measurements) — *measured_by*
  > We also have an additional evaluation on image editing on the full test set of MagicBrush
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *causes*
  > We demonstrate that simple visual editing actions generated as Python code from multimodal LLMs–such as drawing boxes, highlighting areas, or masking regions–can significantly improve model performance by directing selective attention. (Section 1)
  - [ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf)

### → Image editing
- **Code generation** (behaviors tasks) — *causes*
  - [ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf)

### Associated with
- **Generalization** (constructs)
  > To further demonstrate the generalization and applicability of ELM, we evaluate its ability to generate samples from novel classes and perform image editing tasks, with the results in Appendix A.2. (Section 4.4)
  - [Elucidating the design space of language models for image generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25w/liu25w.pdf)
