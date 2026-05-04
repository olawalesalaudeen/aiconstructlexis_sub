# OpenCompass
**Type:** Measurement  
**Referenced in:** 25 papers  
**Also known as:** OpenCompass VLMEvalKit, Opencompass  

## State of the Field

Across the provided literature, OpenCompass is consistently described as an open-source evaluation framework, toolkit, or platform for the standardized and systematic assessment of large language models. It is explicitly used to measure constructs such as `Faithfulness` and `Commonsense understanding`. The framework's application covers a wide range of domains, with one paper noting its use for evaluating five areas: "Reasoning, Language, Knowledge, Examination, and Understanding" (ChartLens). Papers report using OpenCompass to run evaluations on numerous specific benchmarks, including commonsense reasoning tasks like PIQA and ARC, code generation benchmarks like HumanEval, and a large suite of multimodal VQA datasets such as MMBench, MMStar, and MathVista. Operationally, researchers employ the framework with its "official scripts in zero-shot or few-shot settings" (ChartLens) to enable what one paper calls the "unified reproduction of the results" (InternLM-XComposer2-4KHD). The platform is also studied alongside other evaluation methods like the `Needle-in-a-haystack test`.

## Sources

**[InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf) (as "OpenCompass VLMEvalKit")**
> A universal evaluation platform used to reproduce multimodal benchmark results.

**[Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf) (as "Opencompass")**
> An open-source evaluation framework used to systematically assess large language models on various benchmarks.

**[Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf)**
> An open-source evaluation toolkit for large language models, providing standardized assessment across a wide range of benchmarks.

## Relationships

### → OpenCompass
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Mask-Enhanced Autoregressive Prediction: Pay Less Attention to Learn More](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25b/zhuang25b.pdf)

### Associated with
- **PIQA** (measurements)
  > We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA (Bisk et al., 2019), ARC-challenge (ARC-C) (Clark et al., 2018), ARC-easy (ARC-E) (Clark et al., 2018), WinoGrande (WG) (Sakaguchi et al., 2019), HellaSwag (HLSG) (Zellers et al., 2019), and CommonSenseQA (CSQA) (Talmor et al., 2019). (Section 5.1)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
- **Needle-in-a-haystack test** (measurements)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
