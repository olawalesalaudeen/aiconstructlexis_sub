# Emotion understanding
**Type:** Construct  
**Referenced in:** 9 papers  
**Also known as:** Emotion perception, Emotional recognition, Fine-grained emotion recognition, Nuanced emotion recognition  

## State of the Field

Across the surveyed literature, "Emotion understanding" is consistently characterized as a model's ability to perceive, interpret, and infer emotional states from multimodal inputs like images, text, and voice. A prevalent theme is the distinction between basic classification and more complex comprehension, with many definitions emphasizing "fine-grained" or "nuanced" recognition of "subtle, compound, or culturally specific emotional states" (OV-MER: Towards Open-Vocabulary Multimodal Emotion Recognition). This advanced capability is often contrasted with "naive discriminative tasks," aiming instead for generative descriptions of complex emotions (AffectGPT: A New Dataset, Model, and Benchmark for Emotion Understanding with Multimodal Large Language Models). The construct is operationalized and measured using several benchmarks, including MVSA-S and MVSA-M for sentiment polarity classification, TumEmo for classifying six basic emotions, and the MELD dataset. Some work highlights that models still struggle with this ability, finding it difficult to "distinguish between semantically similar emotions" or filter "irrelevant visual information" (Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models). The construct is studied alongside "Emotional reasoning" and is explicitly positioned as a component of "Fine-grained understanding."

## Sources

**[ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The ability to infer or form an opinion about the emotional or atmospheric qualities of a scene based on visual evidence.

**[II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/52764eb83bf0a0bd32766ce5c01612e5-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Emotional understanding")**
> The ability to perceive and interpret the human emotions, sentiment, and affective tone conveyed by an image.

**[Emotion-LLaMA: Multimodal Emotion Recognition and Reasoning with Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/c7f43ada17acc234f568dc66da527418-Paper-Conference.pdf) (as "Emotion perception")**
> The latent ability to accurately identify and interpret emotional expressions from multimodal inputs.

**[Emotion-LLaMA: Multimodal Emotion Recognition and Reasoning with Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/c7f43ada17acc234f568dc66da527418-Paper-Conference.pdf) (as "Emotional recognition")**
> The latent ability to infer a person's emotion category from multimodal evidence such as facial expression, voice, and text.

**[AffectGPT: A New Dataset, Model, and Benchmark for Emotion Understanding with Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lian25a/lian25a.pdf) (as "Fine-grained emotion recognition")**
> The capacity to identify and generate detailed, nuanced emotional categories beyond basic emotions, reflecting the diversity and subtlety of human affective states.

**[OV-MER: Towards Open-Vocabulary Multimodal Emotion Recognition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lian25b/lian25b.pdf) (as "Nuanced emotion recognition")**
> The ability to detect and represent subtle, compound, or culturally specific emotional states that are not captured by basic emotion taxonomies.

## Relationships

### Emotion understanding →
- **MVSA-S** (measurements) — *measured_by*
  > “Emotion: Following (Yang et al., 2023; Huang et al., 2024), we conduct experiments on 4 benchmark datasets. MVSA-S and MVSA-M (Niu et al., 2016) are datasets used for sentiment polarity classification (positive or negative), while TumEmo (Yang et al., 2021) is a multimodal dataset designed for classifying six basic emotions. Additionally, HFM (Liu et al., 2022) is a multimodal dataset focused on recognizing high-level implicit emotion of sarcasm.”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **MVSA-M** (measurements) — *measured_by*
  > “Emotion: Following (Yang et al., 2023; Huang et al., 2024), we conduct experiments on 4 benchmark datasets. MVSA-S and MVSA-M (Niu et al., 2016) are datasets used for sentiment polarity classification (positive or negative), while TumEmo (Yang et al., 2021) is a multimodal dataset designed for classifying six basic emotions. Additionally, HFM (Liu et al., 2022) is a multimodal dataset focused on recognizing high-level implicit emotion of sarcasm.”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **TumEmo** (measurements) — *measured_by*
  > “Emotion: Following (Yang et al., 2023; Huang et al., 2024), we conduct experiments on 4 benchmark datasets. MVSA-S and MVSA-M (Niu et al., 2016) are datasets used for sentiment polarity classification (positive or negative), while TumEmo (Yang et al., 2021) is a multimodal dataset designed for classifying six basic emotions. Additionally, HFM (Liu et al., 2022) is a multimodal dataset focused on recognizing high-level implicit emotion of sarcasm.”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **MELD** (measurements) — *measured_by*
  - [Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection](https://aclanthology.org/2025.emnlp-main.1216.pdf)

### Associated with
- **Emotional reasoning** (constructs)
  - [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf)
- **Fine-grained understanding** (constructs)
  > While recent MLLMs show promising results in basic perception, they still struggle to perceive fine-grained details (Tong et al., 2024b), which is essential for understanding cognition and emotion.
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Emotion analysis** (behaviors tasks)
  - [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf)
