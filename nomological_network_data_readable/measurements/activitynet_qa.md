# ActivityNet-QA
**Type:** Measurement  
**Referenced in:** 26 papers  

## State of the Field

Across the provided literature, ActivityNet-QA is consistently used as a benchmark to evaluate model capabilities in video question answering and the broader construct of video understanding. The benchmark is described as being derived from ActivityNet videos, with a focus on assessing model comprehension of longer video content that contains diverse and complex human activities. A recurring definition specifies its use for "zero-shot video understanding evaluation." While its primary application is measuring general video QA, a smaller line of work also positions it as a tool for assessing "long-term spatiotemporal reasoning," as one paper notes it "is designed to assess" this capability. In practice, ActivityNet-QA is frequently employed in evaluations alongside other video QA benchmarks, most commonly MSVD-QA, MSRVTT-QA, and TGIF-QA. The prevailing use of this instrument is to operationalize and measure a model's ability to answer open-ended questions about complex, activity-rich video.

## Sources

**[Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf)**
> A video question-answering benchmark used for zero-shot video understanding evaluation.

## Relationships

### → ActivityNet-QA
- **Video question answering** (behaviors tasks) — *measured_by*
  > We evaluate AURORACAP on MSVD-QA (Xu et al., 2017), ActivityNet-QA (Yu et al., 2019), MSRVTT-QA (Xu et al., 2017), and iVQA (Yang et al., 2021) for video question answering tasks as shown in Table 4. (Section 2.3)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **Video understanding** (constructs) — *measured_by*
  > Specifically, we showcased Dolphin’s comparison with various methods on MSR-VTT-QA, MSVD-QA, and ActivityNet-QA benchmarks. (Section 5.2)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Spatiotemporal reasoning** (constructs) — *measured_by*
  > ActivityNet-QA (Yu et al., 2019) encompasses human-annotated QA pairs on 5,800 videos derived from the ActivityNet (Caba Heilbron et al., 2015) dataset. This benchmark is designed to assess the capabilities of VideoQA models in long-term spatiotemporal reasoning.
  - [Streaming Video Question-Answering with In-context Video KV-Cache Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/67a9b444cbcd647572c88194619f72d5-Paper-Conference.pdf)
