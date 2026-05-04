# FigStep
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Figstep  

## State of the Field

FigStep is consistently characterized across the provided literature as a benchmark for evaluating the safety of Vision Language Models (VLMs) and Multimodal Large Language Models (MLLMs). The relationships show it is used to measure constructs such as `Safety`, `Safety alignment`, and `Adversarial robustness`. The most prevalent description of its methodology is that it assesses model safety against attacks involving both figures and text. A frequently cited mechanism within the benchmark is the use of typography to transfer unsafe content into images, which, as one paper notes, "can bypass the safety mechanism of models." Some papers offer more specific framings, describing it as an "adversarial multimodal benchmark" for evaluating "jailbreak attempts" through step-by-step instructions, or as a "dataset of harmful questions." The data also shows that FigStep is sometimes adapted for specific studies, for example by excluding categories like legal or medical advice. It is often evaluated alongside other multimodal safety benchmarks, such as MM-Safetybench and SIUO.

## Sources

**[ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)**
> A benchmark designed to test VLM safety, particularly against attacks involving figures and text.

**[How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf) (as "Figstep")**
> A multimodal safety benchmark used to assess harmful-response behavior from image-based prompts.

## Relationships

### → FigStep
- **Safety alignment** (constructs) — *measured_by*
  - [Single Ground Truth Is Not Enough: Adding Flexibility to Aspect-Based Sentiment Analysis Evaluation](https://aclanthology.org/2025.naacl-long.604.pdf)
- **Safety** (constructs) — *measured_by*
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)
