# Downstream task performance
**Type:** Behavior  
**Referenced in:** 11 papers  
**Also known as:** Downstream task evaluation  

## State of the Field

Across the provided literature, downstream task performance is consistently defined as the observable performance of a pre-trained model on a suite of specific, often supervised, tasks. This behavior is evaluated to assess the capabilities a model has acquired during processes like pre-training or continual growth. The operationalization of this behavior is frequently standardized using evaluation frameworks, with the LLM Evaluation Harness being a widely cited tool for this purpose. This framework, along with direct evaluations, is used to measure performance on a wide array of specific benchmarks. Among the most frequently mentioned benchmarks in this dataset are HellaSwag, PIQA, WinoGrande, COPA, MMLU, and various versions of ARC (ARC-Easy and ARC-Challenge). Other datasets cited for measuring this behavior include LAMBADA, BoolQ, SST-2, and AG News. Researchers use this metric to compare models, for instance, to show that a new method can reduce computational costs while "retaining equivalent or better downstream performance" (LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently). The scope of these evaluations is broad, with papers reporting the use of these benchmarks to measure "NLU capabilities" and "general knowledge and reasoning capabilities".

## Sources

**[LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently](https://proceedings.iclr.cc/paper_files/paper/2025/file/03945380ca5af0dc80782d8e0b72a8d7-Paper-Conference.pdf)**
> Producing outputs that support strong performance on supervised language tasks after pre-training or continual growth.

**[The Sharpness Disparity Principle in Transformers for Accelerating Language Model Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dl/wang25dl.pdf) (as "Downstream task evaluation")**
> The observable performance of a pre-trained model on a suite of specific, often supervised, tasks to assess its acquired capabilities.

## Relationships

### Downstream task performance →
- **LLM Evaluation Harness** (measurements) — *measured_by*
  > “We use LM Evaluation Harness framework (Gao et al., 2024) to assess model performance on HellaSwag ... as well as ARC-Easy and ARC-Challenge”
  - [Domain2Vec: Vectorizing Datasets to Find the Optimal Data Mixture without Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bu/zhang25bu.pdf)
- **MMLU** (measurements) — *measured_by*
  > “We also compare the models’ general knowledge and reasoning capabilities by measuring accuracy across 57 diverse academic subjects using the MMLU benchmark (Hendrycks et al., 2020).”
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **LAMBADA** (measurements) — *measured_by*
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **WinoGrande** (measurements) — *measured_by*
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > We utilize validation sets from six benchmarks: PIQA (Bisk et al., 2020), HellaSwag (Zellers et al., 2019), ARC-E (Clark et al., 2018), ARC-C (Clark et al., 2018), COPA (Roemmele et al., 2011), Winograd (Levesque et al., 2012), and MathQA (Amini et al., 2019). (Section 4.2.3)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **PIQA** (measurements) — *measured_by*
  > We utilize validation sets from six benchmarks: PIQA (Bisk et al., 2020), HellaSwag (Zellers et al., 2019), ARC-E (Clark et al., 2018), ARC-C (Clark et al., 2018), COPA (Roemmele et al., 2011), Winograd (Levesque et al., 2012), and MathQA (Amini et al., 2019). (Section 4.2.3)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **BoolQ** (measurements) — *measured_by*
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **SST-2** (measurements) — *measured_by*
  > For fine-tuning tasks, we consider four different datasets, i.e., SST2, AGNEWS, GSM8K and AlpacaEval. (Sec. 5.1)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **AG News** (measurements) — *measured_by*
  > For fine-tuning tasks, we consider four different datasets, i.e., SST2, AGNEWS, GSM8K and AlpacaEval. (Sec. 5.1)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **COPA** (measurements) — *measured_by*
  > We utilize validation sets from six benchmarks: PIQA (Bisk et al., 2020), HellaSwag (Zellers et al., 2019), ARC-E (Clark et al., 2018), ARC-C (Clark et al., 2018), COPA (Roemmele et al., 2011), Winograd (Levesque et al., 2012), and MathQA (Amini et al., 2019). (Section 4.2.3)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Winograd** (measurements) — *measured_by*
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
