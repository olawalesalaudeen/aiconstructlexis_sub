# CHAIR
**Type:** Measurement  
**Referenced in:** 32 papers  

## State of the Field

Across the provided literature, CHAIR (Caption Hallucination Assessment with Image Relevance) is a widely-used metric and benchmark for evaluating hallucination, specifically within image captioning tasks. Its primary and most frequently described function is to measure the construct of `Object hallucination`. The core operationalization, consistent across nearly all sources, involves quantifying the proportion of objects mentioned in a generated caption that are not present in the source image by comparing them to ground-truth annotations. This is typically calculated at two levels: the instance level (CHAIRi), defined as the "fraction of hallucinated object instances," and the sentence level (CHAIRs), the "fraction of sentences containing a hallucinated object." Some papers specify that the evaluation is conducted on images from the MS-COCO dataset. While the predominant focus is on object presence, a few sources describe a broader application of CHAIR to assess attribute and positional correctness. Overall, CHAIR is presented as a standard tool for quantitatively assessing the fidelity of generated image descriptions, where lower scores indicate better performance.

## Sources

**[Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)**
> Evaluation metric for hallucination in image captioning, measuring the fraction of hallucinated object instances (CHAIRi) and sentences containing hallucinated objects (CHAIRs).

## Relationships

### → CHAIR
- **Hallucination** (behaviors tasks) — *measured_by*
  > CHAIR (Rohrbach et al., 2018) evaluates object hallucinations in open-ended captioning tasks (Section 4.1).
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  > “CHAIR (Rohrbach et al., 2018) evaluates object hallucinations in open-ended captioning tasks”
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **Image captioning** (behaviors tasks) — *measured_by*
  > “CHAIR (Rohrbach et al., 2018) evaluates object hallucinations in open-ended captioning tasks”
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **Multimodal alignment** (constructs) — *measured_by*
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
- **Visual hallucination** (behaviors tasks) — *measured_by*
  > Visual hallucination task evaluates whether the response of the model is consistent with the image content to ensure the trustworthiness and reliability of the model. We use CHAIR (Rohrbach et al., 2018), POPE (Li et al., 2023c), and MMHal-Bench (Sun et al., 2023).
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [Interpretation Meets Safety: A Survey on Interpretation Methods and Tools for ImprovingLLMSafety](https://aclanthology.org/2025.emnlp-main.1092.pdf)

### Associated with
- **MS-COCO** (measurements)
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
