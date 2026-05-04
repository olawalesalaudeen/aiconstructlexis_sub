# Pronunciation assessment
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Phoneme sequence comparison, ASR output scoring  

## State of the Field

The task of pronunciation assessment is characterized in several distinct ways across the provided literature. It is broadly defined as evaluating the quality or correctness of pronunciation using textual descriptions, and is also framed as the task of scoring the output of an Automatic Speech Recognition (ASR) system. A more granular operationalization describes the behavior as aligning transcript words with phoneme sequences to identify mismatches indicative of mispronunciation. In this view, an LLM identifies mispronunciations by "comparing the recognized IPA and CMU sequences" against a transcript. One paper title suggests this can be performed as a zero-shot task. The behavior is measured by the LASER benchmark, which is described as an "LLM-based ASR Scoring and Evaluation Rubric," reinforcing the connection to ASR evaluation.

## Sources

**[User Feedback in Human-LLMDialogues: A Lens to Understand Users But Noisy as a Learning Signal](https://aclanthology.org/2025.emnlp-main.134.pdf) (as "Phoneme sequence comparison")**
> The model's observable behavior of aligning transcript words with corresponding phoneme sequences and identifying mismatches indicative of mispronunciation.

**[2025.emnlp-main.134.checklist](https://aclanthology.org/attachments/2025.emnlp-main.134.checklist.pdf)**
> The observable task of evaluating the quality or correctness of pronunciation, performed by an LLM using textual descriptions.

**[2025.emnlp-main.1257.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1257.checklist.pdf) (as "ASR output scoring")**
> The task of using a model to score or evaluate the quality of text transcribed by an Automatic Speech Recognition (ASR) system.

## Relationships

### Pronunciation assessment →
- **LASER** (measurements) — *measured_by*
  > Paper title: LASER: An LLM-based ASR Scoring and Evaluation Rubric
  - [2025.emnlp-main.1257.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1257.checklist.pdf)
