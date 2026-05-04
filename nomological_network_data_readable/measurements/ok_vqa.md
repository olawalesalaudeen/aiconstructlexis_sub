# OK-VQA
**Type:** Measurement  
**Referenced in:** 20 papers  

## State of the Field

Across the provided literature, OK-VQA is consistently defined as a benchmark for Open-ended Knowledge-based Visual Question Answering. A recurring feature highlighted in all definitions is its requirement for external or outside knowledge, beyond what is directly depicted in the image, to answer questions correctly. The most prevalent use of OK-VQA is to evaluate the behavior of "Visual question answering," with multiple papers using it to assess the "visual perception and reasoning abilities" of multimodal models. It is also used more broadly to measure "Multimodal understanding." A smaller set of sources list it as an instrument for evaluating "In-context and few-shot learning" and "Long-context processing," and it is also studied in relation to "Commonsense understanding." In practice, OK-VQA is frequently employed alongside other VQA datasets, with papers often citing its use in conjunction with benchmarks such as VQAv2, GQA, and VizWiz.

## Sources

**[DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)**
> Open-ended Knowledge-based Visual Question Answering, a benchmark used to assess multimodal question answering requiring external knowledge.

## Relationships

### → OK-VQA
- **Visual question answering** (behaviors tasks) — *measured_by*
  > In order to assess multimodal vision and language capabilities of DEEM , we conduct evaluation against current SOTA LMMs ... across several tasks, including ... visual question answering on ... OKVQA (Marino et al., 2019) (Section 3.2).
  - [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > “we conduct evaluation against current SOTA LMMs including ... across several tasks, including image captioning on COCO ... visual question answering on VQAv2, OKVQA, GQA, VizWiz, and VisDial”
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)

### Associated with
- **World knowledge** (constructs)
  - [Visual Riddles: a Commonsense and World Knowledge Challenge for Large Vision and Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fbf5efe979e6754dc06a0869233f2510-Paper-Datasets_and_Benchmarks_Track.pdf)
