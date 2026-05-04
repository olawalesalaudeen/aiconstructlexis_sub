# TextVQA
**Type:** Measurement  
**Referenced in:** 86 papers  
**Also known as:** TextQA, VQAT  

## State of the Field

Across the provided literature, TextVQA is predominantly characterized as a benchmark dataset for visual question answering (VQA). Its defining feature, consistently noted across definitions, is the requirement for models to answer questions by reading and reasoning about text embedded within images. The most common application of TextVQA is to evaluate VQA capabilities, where it is frequently used in evaluation suites alongside other VQA benchmarks. A substantial body of work also uses TextVQA specifically to measure Optical Character Recognition (OCR), with some papers stating that its tasks "require mainly OCR capabilities" and grouping it with other OCR-related datasets. Less frequently, it is used to assess the broader construct of visual understanding or the more specific capability of fine-grained visual understanding, being described as a "detail-sensitive dataset." One study also employs it to assess model generalization. While most papers use the name TextVQA, a few refer to it by the synonyms VQAT or TextQA.

## Sources

**[Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf) (as "TextQA")**
> A benchmark dataset that requires models to read and reason about text in images to answer questions.

**[ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)**
> A visual question answering dataset where questions require reading and reasoning about text within images, used to evaluate general VLM capabilities.

**[Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf) (as "VQAT")**
> Visual question answering benchmark used in multimodal evaluation.

## Relationships

### → TextVQA
- **Visual question answering** (behaviors tasks) — *measured_by*
  > “Table 4 presents a comparison between LLaVA-1.5 and Text4Seg across various VQA and RES benchmarks.”
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Optical character recognition** (behaviors tasks) — *measured_by*
  > TextVQA and ST-VQA are two texts understanding benchmarks requiring models to answer questions through textual cues on images. (Section 5.1.1)
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > Our method demonstrates superior image understanding capabilities, achieving the 80.0%, 63.0%, 48.6%, 70.9%, and 58.8% performance on VQAv2, GQA, VisWiz, SQAI, and VQAT, respectively.
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA, V∗, POPE, DocVQA)... (Sec. 6)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **Visual dialogue** (behaviors tasks) — *measured_by*
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.248.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
