# VoiceBench
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

VoiceBench is characterized in the provided data as a benchmark dataset for evaluating speech language models. Its stated purpose is to assess performance on semantic understanding tasks, and one source highlights a methodological feature: it operates without reliance on auxiliary LLMs for scoring. The benchmark is composed of multiple subsets, with papers mentioning the use of AdvBench, IFEval, OBQA, MMSU, and sd-qa. The most explicitly detailed application of VoiceBench is to quantify the "modality gap," which is defined as the drop in performance between text and speech inputs. As one study notes, benchmark results from VoiceBench can reveal a "striking contrast" between different model pipelines, demonstrating its use for comparative evaluation. In addition to measuring the modality gap, VoiceBench is also listed as an instrument for assessing Safety, Commonsense understanding, and Commonsense knowledge.

## Sources

**[Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.262.pdf)**
> Benchmark dataset for evaluating speech language models, comprising multiple subsets including AdvBench, IFEval, OBQA, MMSU, and sd-qa, used to assess performance on semantic understanding tasks without reliance on auxiliary LLMs for scoring.

## Relationships

### → VoiceBench
- **Modality gap** (constructs) — *measured_by*
  > We quantify the modality gap as the drop in benchmark scores between text and speech inputs... For evaluation, we adopt five subsets of the VoiceBench dataset (Chen et al., 2024)—AdvBench, IFEval, OBQA, MMSU, and sd-qa (Sections 4.3 & 3.2)
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.262.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **Safety** (constructs) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)
