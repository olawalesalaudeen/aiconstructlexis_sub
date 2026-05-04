# Speech synthesis
**Type:** Behavior  
**Referenced in:** 8 papers  
**Also known as:** Text-to-speech generation, Spoken dialogue generation, Speech-to-speech translation, Spoken dialog generation, Spoken dialogue response generation, Text-to-audio generation, Acoustic token generation  

## State of the Field

Across the provided literature, speech synthesis is most commonly framed as the task of generating human-like speech from text, often referred to as text-to-speech (TTS). This process is frequently operationalized as translating text into sequences of discrete audio tokens, which are then used to synthesize an audible waveform. A second prevalent framing situates the behavior within conversational contexts, where it is described as spoken dialogue generation. This is typically defined as producing a spoken response to a conversational input, though one paper describes the output as a textual response to spoken audio. Less common conceptualizations include speech-to-speech translation, the broader task of text-to-audio generation, and the generation of intermediate representations like clean acoustic tokens. The behavior is evaluated using specific datasets, such as the Free Spoken Digit Dataset for text-to-speech tasks, and dedicated benchmarks for spoken dialogue generation. Additionally, one study reports a directional relationship where chain-of-thought reasoning is proposed to cause speech synthesis.

## Sources

**[UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf) (as "Text-to-speech generation")**
> The task of synthesizing human-like speech from a given text input.

**[Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf) (as "Text-to-speech synthesis")**
> Generating speech audio from written text or intermediate text responses.

**[SD-Eval: A  Benchmark Dataset for Spoken Dialogue Understanding Beyond Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/681fe4ec554beabdc9c84a1780cd5a8a-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Spoken dialogue generation")**
> The observable task of generating a textual response based on a spoken audio input, as part of a conversation.

**[Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf) (as "Speech-to-speech translation")**
> The task of translating spoken language in a source language directly into spoken language in a target language.

**[Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf) (as "Spoken dialog generation")**
> Generating a spoken response to a spoken conversational input.

**[VoxDialogue: Can Spoken Dialogue Systems Understand Information Beyond Words?](https://proceedings.iclr.cc/paper_files/paper/2025/file/011df158529ddceb5f2f7a65f2732a5a-Paper-Conference.pdf) (as "Spoken dialogue response generation")**
> Producing the next assistant utterance in a multi-turn spoken conversation given prior user utterances and assistant replies.

**[MixEval-X: Any-to-any Evaluations from Real-world Data Mixture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6de2e84b8da47bb2eb5e2ac96c63d2b0-Paper-Conference.pdf) (as "Text-to-audio generation")**
> The observable task of generating a novel audio clip that corresponds to a given textual description.

**[Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)**
> The observable process of generating audible speech waveforms from an internal representation, such as discrete speech tokens.

**[GenSE: Generative Speech Enhancement via Language Models using Hierarchical Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/acde98fb254b8021d194ccdb80a1241e-Paper-Conference.pdf) (as "Acoustic token generation")**
> Generating clean acoustic tokens conditioned on semantic and noisy acoustic prompts.

## Relationships

### → Speech synthesis
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf)
