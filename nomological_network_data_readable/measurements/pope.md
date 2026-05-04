# POPE
**Type:** Measurement  
**Referenced in:** 117 papers  

## State of the Field

Across the provided literature, POPE is overwhelmingly described as a benchmark for evaluating hallucination in multimodal large language models, with a specific and frequently mentioned focus on object-level or visual hallucination. The benchmark operationalizes this evaluation through a visual question answering (VQA) format, where models are prompted with balanced, binary questions about the presence of objects in an image, such as “Is there a car in the image?”. Several sources note that POPE is structured into distinct splits—most commonly cited as random, popular, and adversarial—which are based on different strategies for sampling objects that are not present in the image. While its primary application is measuring hallucination, some papers also employ POPE more broadly to assess general capabilities like visual understanding, multimodal understanding, and visual reasoning. In evaluation sections, it is often used alongside other hallucination-focused instruments like CHAIR and AMBER. A single paper offers an alternative framing, defining POPE as "Positional Object Perception Evaluation" for assessing object localization and counting, though this is not the prevailing usage in the provided data.

## Sources

**[Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)**
> POPE, a benchmark for evaluating object hallucinations in multimodal large language models using balanced yes/no visual question answering tasks.

## Relationships

### → POPE
- **Hallucination** (behaviors tasks) — *measured_by*
  > Moreover, POPE (Li et al., 2023d) results show our method could mitigate object hallucinations. (Section 5.2)
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  > “POPE (Li et al., 2023d) is a widely used benchmark for assessing object hallucinations in LVLMs”
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > “Table 4 presents a comparison between LLaVA-1.5 and Text4Seg across various VQA and RES benchmarks.”
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > “For image understanding, we evaluate LLaVA-1.5 and LLaVA-NeXT on (a) diverse multimodal benchmarks: POPE (Li et al., 2023c), GQA (Hudson & Manning, 2019), MMBench (Liu et al., 2023b), VizWiz (Gurari et al., 2018), SEEDBench (Li et al., 2023a), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024)”
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **Visual hallucination** (behaviors tasks) — *measured_by*
  > “The MLLM-specific benchmarks are POPE Li et al. (2023c), MME Fu et al. (2023), MMB Liu et al. (2023d), SEED Li et al. (2023a) and MM-Vet Yu et al. (2023). Compared to common VL evaluations, these benchmarks aim to evaluate MLLMs from various aspects, such as fine-grained reasoning and visual hallucination.”
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > Figure 8 presents the rate-accuracy performance of our re-trained scheme applied to two MLLMs that do not use the pre-trained CLIP ViT visual encoder: (1) mPLUG-Owl2 (Ye et al., 2024) on MMBench and Osprey (Yuan et al., 2024) on POPE (popular setting). Our method under all three settings clearly outperforms the Reconstruction baseline, confirming the generalizability of the proposed framework.
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **Visual perception** (constructs) — *measured_by*
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > Following LLaVA (Liu et al., 2024b), we evaluate the multimodal understanding capabilities of Show-o on POPE, MME, Flickr30k, VQAv2, GQA, and MMMU benchmarks. (Section 4.1)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **Object hallucination detection** (behaviors tasks) — *measured_by*
  - [Unified Generative and Discriminative Training for Multi-modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/29416b66c2149872b9d1415a3fd2c5e0-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *measured_by*
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Hallucination detection** (behaviors tasks) — *measured_by*
  > Specifically, we assess our method’s performance in hallucination detection using the POPE dataset (Li et al., 2023c) and HallusionBench (Guan et al., 2023). (Section 4.1)
  - [(Almost) Free Modality Stitching of Foundation Models](https://aclanthology.org/2025.emnlp-main.1002.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > “We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA 2 (Singh et al., 2019), V∗ (Wu and Xie, 2023), POPE (Li et al., 2023c), DocVQA (Mathew et al., 2021))”
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > "We evaluated our DAMO method on the comprehensive hallucination dataset MME and examined object hallucination using the SEEM-annotated MSCOCO and A-OKVQA datasets from POPE."
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **Object recognition** (behaviors tasks) — *measured_by*
  - [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25c/park25c.pdf)
- **Knowledge retention** (constructs) — *measured_by*
  - [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf)
