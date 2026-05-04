# OCRVQA
**Type:** Measurement  
**Referenced in:** 3 papers  

## State of the Field

OCRVQA is characterized in the provided literature as a visual question answering dataset with a specific focus on questions that require optical character recognition (OCR) to understand text in images. In line with this definition, papers use OCRVQA to explicitly "examine their ability to recognize optical character" ("Ranked from Within: Ranking Large Multimodal Models Without Labels"). Beyond this function, the dataset is also employed to "assess the learned generalization ability" of models ("Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning"). The provided sources consistently position OCRVQA within a suite of evaluation tools, often listed alongside other VQA datasets like TextVQA, GQA, and DocVQA. The available data presents a unified view of OCRVQA as a specialized instrument for measuring text-recognition capabilities in a VQA context.

## Sources

**[Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)**
> A visual question answering dataset focused on questions that require optical character recognition (OCR) to understand text in images.

## Relationships

### → OCRVQA
- **Optical character recognition** (behaviors tasks) — *measured_by*
  > ChartQA (Masry et al., 2022), OCRVQA (Mishra et al., 2019), TextVQA (Singh et al., 2019) and DocVQA (Mathew et al., 2021) to examine their ability to recognize optical character (Section 5.1)
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
- **Generalization** (constructs) — *measured_by*
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
