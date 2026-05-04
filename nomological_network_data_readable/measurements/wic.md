# WiC
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** WIC  

## State of the Field

Across the provided literature, WiC is consistently described as a benchmark dataset used to evaluate word sense disambiguation. The task is operationalized as determining whether a target word has the same meaning across two different sentences or contexts. As such, papers use WiC to measure a model's capacity for what one source calls "contextual word sense disambiguation." It is frequently employed as a downstream task to assess model performance, for instance after fine-tuning. While the prevailing association is with word sense disambiguation, one paper also categorizes it under "Natural language inference" and notes its inclusion in the SuperGLUE benchmark. WiC is often evaluated alongside a diverse set of other tasks, including classification and multiple-choice questions.

## Sources

**[Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)**
> The Word-in-Context dataset, a benchmark for word sense disambiguation that involves determining if a word has the same meaning in two different sentences.

**[Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf) (as "WIC")**
> A word-in-context benchmark requiring judgment of whether a word has the same meaning in two contexts.

## Relationships

### → WiC
- **Word sense disambiguation** (behaviors tasks) — *measured_by*
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
