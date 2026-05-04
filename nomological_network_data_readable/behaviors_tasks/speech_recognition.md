# Speech recognition
**Type:** Behavior  
**Referenced in:** 32 papers  
**Also known as:** Automatic speech recognition, Speech-to-text transcription, Text transcription, Word identity prediction, Phoneme recognition  

## State of the Field

Across the provided literature, speech recognition is overwhelmingly defined as the task of converting a spoken language utterance from an audio signal into its corresponding written text, frequently referred to as Automatic Speech Recognition (ASR). This behavior is most commonly operationalized and measured using the LibriSpeech benchmark, though datasets such as FLEURS, ATIS, and CoVoST 2 are also used for evaluation. Performance is often quantified using Word Error Rate (WER), with one paper specifying the accuracy metric as (1 −WER). Some sources describe ASR as a foundational task for enabling speech understanding, with one study noting it "requires learning precisely frame-level alignment instead of utterance-level understanding" ("It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition"). A few papers offer more granular definitions, framing the task as "phoneme recognition" or "word identity prediction." In a divergent usage, one paper defines "text transcription" as extracting text from an image or document, which contrasts with the audio-centric focus of all other sources. The task is also studied alongside related behaviors like speech understanding and machine translation.

## Sources

**[It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf) (as "Automatic speech recognition")**
> The task of converting a spoken language utterance (speech signal) into its corresponding textual transcription.

**[SD-Eval: A  Benchmark Dataset for Spoken Dialogue Understanding Beyond Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/681fe4ec554beabdc9c84a1780cd5a8a-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The observable task of transcribing spoken language from an audio signal into written text.

**[Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf) (as "Speech-to-text transcription")**
> Converting input speech tokens into intermediate text transcripts.

**[What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf) (as "Text transcription")**
> The task of accurately extracting and transcribing textual content from an image or document.

**[Improving Semantic Understanding in Speech Language Models via Brain-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/95b7a93e60fdfd10cc202f44fd6adf5f-Paper-Conference.pdf) (as "Word identity prediction")**
> The task of identifying a specific keyword or command from a spoken utterance.

**[Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1a7774429d5c06cc744ff4260a8e9f-Paper-Conference.pdf) (as "Phoneme recognition")**
> Recognizing and distinguishing individual phonemes within speech audio.

## Relationships

### Speech recognition →
- **LibriSpeech** (measurements) — *measured_by*
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
- **FLEURS** (measurements) — *measured_by*
  - [TokenSkip: Controllable Chain-of-Thought Compression inLLMs](https://aclanthology.org/2025.emnlp-main.166.pdf)
- **ATIS** (measurements) — *measured_by*
  - [It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf)
- **CoVoST 2** (measurements) — *measured_by*
  - [The Power of Many: Multi-Agent Multimodal Models for Cultural Image Captioning](https://aclanthology.org/2025.naacl-long.153.pdf)

### Associated with
- **SUPERB** (measurements)
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)
- **Machine translation** (behaviors tasks)
  - [ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.599.pdf)
- **Speech understanding** (constructs)
  - [SVD-LLMV2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.218.pdf)
