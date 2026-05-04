# Radiology report generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Radiology report generation is defined in the provided literature as the task of creating a descriptive and clinically relevant text report from one or more radiology images and their associated context. This behavior is most commonly operationalized and evaluated using the MIMIC-CXR dataset, which is cited across multiple papers in this set. Other datasets mentioned for measuring this task include IU-Xray, and the GREEN benchmark is also listed as an evaluation tool. The quality of the generated reports is assessed using standard Natural Language Generation (NLG) metrics. Specifically, one paper notes the use of BERTScore, alongside BLEU and ROUGE, by comparing a model's output to references written by radiologists. The task is described as playing a role in chest X-ray interpretation, and some work focuses on enhancing it through methods like supplementary knowledge injection.

## Sources

**[Balancing Diversity and Risk inLLMSampling: How to Select Your Method and Parameter for Open-Ended Text Generation](https://aclanthology.org/2025.acl-long.1279.pdf)**
> The task of generating a descriptive, clinically relevant text report based on one or more radiology images and associated clinical context.

## Relationships

### Radiology report generation →
- **MIMIC-CXR** (measurements) — *measured_by*
  > We evaluate our model using three publicly available radiology report generation datasets: MIMIC-CXR, CHEXPERT PLUS, and IU X-RAY (Section 4.1)
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
- **IU-Xray** (measurements) — *measured_by*
  > We evaluate our method on two public datasets, MIMIC-CXR (Johnson et al., 2019) and IU-Xray (Demner-Fushman et al., 2016). (Section 5.1)
  - [Weaving Context Across Images: Improving Vision-Language Models through Focus-Centric Visual Chains](https://aclanthology.org/2025.acl-long.1348.pdf)
- **GREEN** (measurements) — *measured_by*
  - [LLM×MapReduce: Simplified Long-Sequence Processing using Large Language Models](https://aclanthology.org/2025.acl-long.1342.pdf)
- **BERTScore** (measurements) — *measured_by*
  > Since we have radiologist-written reference available, it is possible to employ standard, general domain, NLG metrics such as BLEU (Papineni et al., 2002), ROUGE (Lin, 2004), and the BERTScore (Zhang et al., 2019). (Section 3.2)
  - [LLM×MapReduce: Simplified Long-Sequence Processing using Large Language Models](https://aclanthology.org/2025.acl-long.1342.pdf)
