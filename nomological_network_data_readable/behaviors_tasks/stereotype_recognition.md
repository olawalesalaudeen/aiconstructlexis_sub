# Stereotype recognition
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Stereotype identification, Stereotype detection  

## State of the Field

Across the provided literature, stereotype recognition is consistently framed as a task requiring a model to identify or distinguish stereotypical content from other statements. The most common definitions describe it as a classification or distinction task, such as the ability to 'distinguish between stereotypical and anti-stereotypical statements' or to identify which of multiple sentences expresses a stereotype. A slightly different framing presents it as an ability to not only recognize but also 'critically explain the presence of stereotypes' in response to specific prompts. To operationalize this behavior, researchers use the StereoSet benchmark, and one study also mentions adapting the EspanStereo dataset for a 'stereotype detection format'. The prevalent use of this task, as stated in the data, is as a measure of a model's fairness. As one paper specifies, the task is performed 'To evaluate the alignment of fairness'.

## Sources

**[Does quantization affect models’ performance on long-context tasks?](https://aclanthology.org/2025.emnlp-main.480.pdf)**
> A task designed to assess fairness by requiring the model to distinguish between stereotypical and anti-stereotypical statements.

**[REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf) (as "Stereotype identification")**
> The observable ability to recognize and critically explain stereotypical content in input prompts.

**[Graph-R1: Incentivizing the Zero-Shot Graph Learning Capability inLLMs via Explicit Reasoning](https://aclanthology.org/2025.emnlp-main.1221.pdf) (as "Stereotype detection")**
> The task of classifying or identifying which of two or more sentences expresses a stereotype, given a context.

## Relationships

### Stereotype recognition →
- **StereoSet** (measurements) — *measured_by*
  - [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf)

### → Stereotype recognition
- **Fairness** (constructs) — *measured_by*
  > "To evaluate the alignment of fairness, we perform stereotype recognition task (Sun et al., 2024) based on benchmark StereoSet (Nadeem et al., 2021) with Stereotype Score (SS) and Accuracy (Acc)."
  - [Does quantization affect models’ performance on long-context tasks?](https://aclanthology.org/2025.emnlp-main.480.pdf)
