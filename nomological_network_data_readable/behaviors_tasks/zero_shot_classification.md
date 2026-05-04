# Zero-shot classification
**Type:** Behavior  
**Referenced in:** 14 papers  
**Also known as:** Zero-shot task classification  

## State of the Field

Across the provided literature, zero-shot classification is consistently described as the observable act of a model assigning class labels to inputs without any task-specific training or fine-tuning. This behavior is understood to rely solely on the model's pre-trained, internal knowledge, which is typically elicited through a prompt. A common element in several definitions is that the model performs this classification on categories for which it has not seen labeled examples during its training. Some work frames this as a paradigm that "obviate[s] the need for data collection and training loops" ("Zero-Shot Robustification of Zero-Shot Models"). While often applied to text, the concept is also extended to multimodal contexts, where a model might assign a label to an image by selecting the most probable option from a set of text descriptions. The performance of this behavior is operationalized and measured using a variety of benchmarks, with results commonly reported as "zero-shot accuracy". The provided papers use datasets such as ImageNet-1k for images, and a suite of what one paper calls "common sense reasoning datasets" including BoolQ, PIQA, HellaSwag, WinoGrande, ARC-Easy, ARC-Challenge, and OpenBookQA to evaluate this capability.

## Sources

**[Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)**
> The observable act of an LLM assigning class labels to input instances without any task-specific training, based solely on a prompt and its internal knowledge.

**[SlimLLM: Accurate Structured Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25a/guo25a.pdf) (as "Zero-shot task classification")**
> The model's ability to correctly classify inputs into predefined categories without any task-specific fine-tuning, based solely on its pre-trained knowledge.

## Relationships

### Zero-shot classification →
- **ImageNet-1k** (measurements) — *measured_by*
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
