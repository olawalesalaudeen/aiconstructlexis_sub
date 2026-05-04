# AudioCaps
**Type:** Measurement  
**Referenced in:** 12 papers  

## State of the Field

Across the provided literature, AudioCaps is consistently defined as a benchmark dataset for evaluating audio-language tasks, composed of audio clips from AudioSet paired with human-written captions. Its most prevalent application is to measure model performance on audio captioning, as evidenced by multiple papers that use it to evaluate generated audio descriptions. Several sources position it as one of the most commonly used benchmarks for this purpose, frequently studied alongside the Clotho dataset. While audio captioning is the dominant use case, a smaller set of definitions also describe its utility for evaluating audio-retrieval and audio question answering. The data indicates it is operationalized through its test set, with some studies referencing specific evaluation metrics like CIDEr or zero-shot variants of the benchmark. AudioCaps is also listed as a measurement instrument for cross-modal retrieval and text-to-speech synthesis, though the provided evidence centers on its captioning and retrieval applications.

## Sources

**[CompA: Addressing the Gap in Compositional Reasoning in Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/43c18853329c7504996b255252b6cb1f-Paper-Conference.pdf)**
> A benchmark dataset used for evaluating audio-retrieval and captioning tasks, containing audio clips from AudioSet with human-written captions.

## Relationships

### → AudioCaps
- **Audio captioning** (behaviors tasks) — *measured_by*
  > The results on all 15 tasks produced by SALMONN are shown in Table 3. From the results, SALMONN, without or with activation tuning, can produce competitive results on all level 1 tasks. (Section 5.1)
  - [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf)
- **Text-to-speech synthesis** (behaviors tasks) — *measured_by*
  - [Generative Audio Language Modeling with Continuous-valued Tokens and Masked Next-Token Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25n/yang25n.pdf)
