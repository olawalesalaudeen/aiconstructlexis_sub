# MM-SafetyBench
**Type:** Measurement  
**Referenced in:** 15 papers  
**Also known as:** MM-Safetybench, MM-SafeBench  

## State of the Field

MM-SafetyBench is a benchmark commonly used to evaluate the safety of vision-language models (VLMs). The prevailing definition across the provided literature describes it as an instrument for testing whether VLMs produce unsafe responses to harmful multimodal inputs. Papers use this benchmark to measure several constructs, most frequently general `Safety`, `Jailbreaking`, and `Adversarial robustness`, with some also using it to assess `Safety alignment` and `Harmfulness detection`. A recurring theme is its application in evaluating resilience to attacks; some sources define it specifically as a "jailbreak robustness benchmark" for testing against "multimodal adversarial attacks." The benchmark's composition is detailed in one paper as containing "5,040 text-image pairs across 13 scenarios," while another notes its contents include "typographical images, stable diffusion-generated images... and text-based attack samples." One source explains its mechanism for measuring `Harmfulness detection`, stating that its items consist of a "seemingly benign" text query that becomes harmful when combined with a specific image. Source snippets show that MM-SafetyBench is frequently employed alongside other evaluation tools like FigStep, SafeBench, and HADES in studies of model safety.

## Sources

**[ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)**
> A multimodal safety benchmark used to test whether VLMs produce unsafe responses to harmful inputs.

**[How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf) (as "MM-Safetybench")**
> A benchmark for assessing the safety of models in multimodal (vision-language) contexts.

**[“Yes, MyLoRD.” Guiding Language Model Extraction with Locality Reinforced Distillation](https://aclanthology.org/2025.acl-long.74.pdf) (as "MM-SafeBench")**
> A benchmark featuring 5,040 text-image pairs across 13 scenarios, designed to assess the safety and robustness of vision-language models against multimodal jailbreak attacks.

## Relationships

### → MM-SafetyBench
- **Safety** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **Safety alignment** (constructs) — *measured_by*
  - [Defending LVLMs Against Vision Attacks Through Partial-Perception Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25z/zhou25z.pdf)
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  > MM-safetybench, RTVLM, and VLSBench consist of an image and a query where the text query is seemingly benign, but when combined with the respective image, it is harmful
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
