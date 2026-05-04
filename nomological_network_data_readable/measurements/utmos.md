# UTMOS
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, UTMOS is consistently used as an automated evaluation instrument for synthesized speech, with its full name given as Universal Text-to-Speech Model-based Objective Scorer. The instrument is used to measure the construct of "Speech quality," and in one case, the more general "Generation quality." The specific aspect of quality being assessed is variously described as "overall speech quality," "naturalness," or "perceptual quality." The most common operationalization involves using UTMOS as a pre-trained model to predict a Mean Opinion Score (MOS). As one paper states, its purpose is "to predict the mean opinion score (MOS) of the generated speech" to assess its naturalness ("DNASpeech: A Contextualized and Situated Text-to-Speech Dataset with Dialogues, Narratives and Actions"). Another study incorporates the "quality score evaluated by the UTMOS model" as a component in a reward function ("Exploring Changes in Nation Perception with Nationality-Assigned Personas inLLMs"). The provided sources are in agreement, framing UTMOS as a model-based objective scorer for the quality of generated speech.

## Sources

**[Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)**
> A system (Universal Text-to-Speech Model-based Objective Scorer) used to automatically evaluate the overall quality of synthesized speech.

## Relationships

### → UTMOS
- **Speech quality** (constructs) — *measured_by*
  > “we measured ASR-WER to assess the alignment between generated speech and text, as well as UTMOS (Saeki et al., 2022) to evaluate overall speech quality”
  - [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [GenSE: Generative Speech Enhancement via Language Models using Hierarchical Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/acde98fb254b8021d194ccdb80a1241e-Paper-Conference.pdf)
