# Modality gap
**Type:** Construct  
**Referenced in:** 4 papers  

## State of the Field

The term "Modality gap" is used in the provided literature to describe two related but distinct concepts. The more general framing, found in work on cross-modality prompt transfer, defines it as a discrepancy between source and target modalities that arises from differences in their data distributions and model architectures. As one paper notes, this gap is "the distribution difference between source and target data that comes from different data types" ("Release the Powers of Prompt Tuning..."). A different usage treats the concept more specifically as a performance disparity between speech and text inputs within the same model, which is attributed to suboptimal alignment between the modalities. This latter framing is explicitly operationalized as a measurable performance drop. The gap is quantified by the formula `GAP = Mt − Ms`, representing the difference in overall benchmark scores between text (`Mt`) and speech (`Ms`) inputs. To conduct this measurement, the `VoiceBench` dataset is used to assess this drop in scores. Thus, the concept is treated both as a general distributional difference and as a specific, measurable performance deficit between speech and text.

## Sources

**[Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ae9589ff1a691d09ef0528e4e309b2f-Paper-Conference.pdf)**
> The discrepancy between a source and target modality arising from differences in their data distributions and underlying model architectures.

## Relationships

### Modality gap →
- **VoiceBench** (measurements) — *measured_by*
  > We quantify the modality gap as the drop in benchmark scores between text and speech inputs... For evaluation, we adopt five subsets of the VoiceBench dataset (Chen et al., 2024)—AdvBench, IFEval, OBQA, MMSU, and sd-qa (Sections 4.3 & 3.2)
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.262.pdf)
