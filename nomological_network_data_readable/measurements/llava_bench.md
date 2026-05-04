# LLaVA-Bench
**Type:** Measurement  
**Referenced in:** 11 papers  

## State of the Field

Across the provided literature, LLaVA-Bench is consistently described as a benchmark for evaluating multimodal or vision-language models. The most frequently cited capabilities it assesses are model helpfulness, instruction-following ability, reasoning, and understanding of images and text. Papers use LLaVA-Bench to measure a range of behaviors and constructs, including visual question answering, complex reasoning, dialogue, detailed description generation, and visual understanding. One source provides a specific description of its composition, noting it "consists of 60 carefully designed open-ended questions across 24 images." A distinct operational detail, mentioned in one paper, is its evaluation method, which "uses GPT-4 to compare generated answers with reference answers" for open-ended tasks. The benchmark is also applied in specific contexts, such as to assess model utility after an intervention by "examining whether unlearning impacts core model capabilities."

## Sources

**[JRE-L: Journalist, Reader, and EditorLLMs in the Loop for Science Journalism for the General Audience](https://aclanthology.org/2025.naacl-long.336.pdf)**
> Benchmark for evaluating multimodal model helpfulness and instruction-following ability, used here to assess model utility post-unlearning.

## Relationships

### → LLaVA-Bench
- **Dialogue** (behaviors tasks) — *measured_by*
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)
- **Detailed description generation** (behaviors tasks) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Image captioning** (behaviors tasks) — *measured_by*
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > LLaVA-Bench consists of 60 carefully designed open-ended questions across 24 images, evaluating models’ visual reasoning and understanding capabilities. (Section 6.1)
  - [EAC-MoE: Expert-Selection Aware Compressor for Mixture-of-Experts Large Language Models](https://aclanthology.org/2025.acl-long.634.pdf)
