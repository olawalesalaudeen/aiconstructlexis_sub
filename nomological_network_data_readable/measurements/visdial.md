# VisDial
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, VisDial is consistently defined as a dataset for evaluating a model's ability to engage in a multi-turn conversation about an image. The benchmark is most commonly used to measure `Visual question answering` and the broader capability of `Multimodal understanding`. The core task is framed as a conversational AI challenge involving answering a series of questions grounded in a visual context. While this is the prevailing usage, some papers apply the dataset to more specific evaluations; for instance, one study uses VisDial to assess "chat-to-image acquisition in multi-turn chat scenarios" (`TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models`). The dataset is also mentioned in the context of methodological analyses, such as its inclusion in an ablation study on training paradigms.

## Sources

**[Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)**
> The Visual Dialog dataset, which evaluates a model's ability to engage in a multi-turn conversation about an image.

## Relationships

### → VisDial
- **Multimodal understanding** (constructs) — *measured_by*
  > “we conduct evaluation against current SOTA LMMs including ... across several tasks, including image captioning on COCO ... visual question answering on VQAv2, OKVQA, GQA, VizWiz, and VisDial”
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > In order to assess multimodal vision and language capabilities of DEEM , we conduct evaluation against current SOTA LMMs ... across several tasks, including ... visual question answering on ... VisDial (Das et al., 2017) (Section 3.2).
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
