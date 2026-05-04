# Modality bias
**Type:** Construct  
**Referenced in:** 4 papers  
**Also known as:** Multimodal bias, Modality reliance  

## State of the Field

Across the provided literature, modality bias is consistently described as a model's or dataset's tendency to rely disproportionately on one input modality over others, which is said to limit the effectiveness of multimodal integration. This is most commonly framed as an over-reliance on text, with one study noting that models "struggle with figure and table-based questions compared to text-based questions." A related framing defines it as an "imbalanced capability" or, as "modality reliance," the degree to which a model depends on a specific input. The construct is operationalized and measured in multiple ways. One approach uses benchmarks like M-LongDoc to reveal performance disparities across different modalities. Another common measurement approach is human evaluation, which is used to "confirm the modality bias of these datasets." This is sometimes implemented by using an external LLM as a judge to determine which input modality a model primarily uses for its inferences. The concept is also studied alongside cross-modal retrieval.

## Sources

**[VLASCD: A Visual Language Action Model for Simultaneous Chatting and Decision Making](https://aclanthology.org/2025.emnlp-main.469.pdf) (as "Multimodal bias")**
> A model's tendency to perform better on one modality (e.g., text) than others (e.g., figures, tables), indicating an imbalanced capability.

**[Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.501.pdf) (as "Modality reliance")**
> The degree to which a model depends on a specific input modality, such as vision versus text, when making multimodal inferences.

**[Evaluating the Evaluators: Are readability metrics good measures of readability?](https://aclanthology.org/2025.emnlp-main.1226.pdf)**
> The tendency of a model or dataset to rely disproportionately on one input modality (e.g., text) over others (e.g., audio, video), limiting the effectiveness of multimodal integration.

## Relationships

### Modality bias →
- **M-LongDoc** (measurements) — *measured_by*
  > With the proposed M-LongDoc and evaluation framework, our preliminary study on existing models show that they struggle with figure and table-based questions compared to text-based questions, revealing their multimodal bias and weaknesses
  - [VLASCD: A Visual Language Action Model for Simultaneous Chatting and Decision Making](https://aclanthology.org/2025.emnlp-main.469.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > "As shown in Figure 9, most predictions are judged as mostly visual with some text"
  - [Evaluating the Evaluators: Are readability metrics good measures of readability?](https://aclanthology.org/2025.emnlp-main.1226.pdf)

### Associated with
- **Cross-modal retrieval** (behaviors tasks)
  - [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf)
