# SlideVQA
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, SlideVQA is consistently defined as a public dataset for visual question answering on presentation slides, with a recurring structural detail that each document consists of 20 pages. The prevailing use of SlideVQA is as a measurement instrument. It is most commonly employed to evaluate `Visual question answering`, where it is cited as a tool for domain-specific, multi-image QA problems on slides. The dataset is also used to assess `Information retrieval`, with one paper stating it is used to "evaluate the retrieval accuracy" of a system module ("SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding"). Additionally, SlideVQA is associated with the measurement of `Long-context understanding`. A less frequent application appears in one paper where the dataset serves not for evaluation, but as a source for "refining queries" to construct a new dataset ("ComplexTempQA: A 100m Dataset for Complex Temporal Question Answering").

## Sources

**[SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)**
> A public dataset for visual question answering on presentation slides, where each document consists of 20 pages.

## Relationships

### → SlideVQA
- **Information retrieval** (behaviors tasks) — *measured_by*
  > We first evaluate the retrieval accuracy of the Col-retrieval module within SV-RAG and compare it with several baselines on SlideVQA (Tanaka et al., 2023), MM-LongBench (Ma et al., 2024d), DUDE (Van Landeghem et al., 2023), DocVQA (Mathew et al., 2020; 2021) and VisR-Bench. (Section 5)
  - [SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We collect question-document pairs from a series of VQA datasets, targeting different document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024b), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for various figure types, and SlideVQA (Tanaka et al., 2023) for presentation slides.
  - [VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)
