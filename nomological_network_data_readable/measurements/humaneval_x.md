# HumanEval-X
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** HumanEval-Multi  

## State of the Field

HumanEval-X is consistently described across the provided literature as a multilingual benchmark for evaluating large language models on code-related tasks. The definitions converge on its role in assessing model-generated code, with one paper framing this as evaluating 'code generation capabilities' and another as assessing 'functional correctness' and 'model utility'. The benchmark is also referred to as 'HumanEval-Multi', described as the 'multi-lingual version of Humaneval' in one study. In practice, papers use HumanEval-X to measure several capabilities. The most frequently measured behavior is Text generation, though it is also used to assess Faithfulness and Machine translation. Its application extends to evaluating specific models like DeepSeekV2-Lite and serving as a general 'test dataset for utility'. One study also leverages the benchmark to analyze internal model mechanics, such as 'expert activation frequencies' ('MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design').

## Sources

**[MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duanmu25a/duanmu25a.pdf)**
> A multilingual benchmark for evaluating the code generation capabilities of large language models.

**[ProSec: Fortifying Code LLMs with Proactive Security Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25aa/xu25aa.pdf) (as "HumanEval-Multi")**
> A multilingual benchmark for evaluating the functional correctness of model-generated code, used in this paper to assess model utility.

## Relationships

### → HumanEval-X
- **Text generation** (behaviors tasks) — *measured_by*
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25as/huang25as.pdf)
- **Machine translation** (behaviors tasks) — *measured_by*
  - [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf)
