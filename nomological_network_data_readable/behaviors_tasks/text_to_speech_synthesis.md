# Text-to-speech synthesis
**Type:** Behavior  
**Referenced in:** 14 papers  
**Also known as:** Conversational speech synthesis, Speech generation, Text-to-speech generation, Text-to-speech, Spoken dialogue generation, Text-to-audio generation, Text-to-sound generation  

## State of the Field

Across the surveyed literature, text-to-speech synthesis is most commonly defined as the task of generating human-like, audible speech from written text. While the core task involves converting a text transcript into speech, some definitions also incorporate generating speech that matches specific "acoustic style" instructions or is "contextually appropriate for interactive, multi-turn dialogues." A smaller set of papers frames the task more broadly as "text-to-audio generation," which can include non-speech sounds, or more specifically as "speech continuation," which focuses on extending an existing speech prompt. The behavior is frequently operationalized using LLM-based systems, which are noted for enabling "prompt-based customization" and producing speech with "human-like intonation." To evaluate performance on this task, researchers use benchmarks such as AudioCaps, and in some cases, human raters to assess the naturalness of generated speech. Text-to-speech synthesis is studied in relation to voice cloning and multimodal reasoning. A recurring challenge discussed in the context of LLM-based systems is hallucination, which is described as a "prominent issue" for this behavior.

## Sources

**[TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.40.pdf) (as "Conversational speech synthesis")**
> The task of generating speech that is contextually appropriate for interactive, multi-turn dialogues.

**[TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.40.pdf)**
> The task of generating human-like speech from a given text input.

**[Exploring Changes in Nation Perception with Nationality-Assigned Personas inLLMs](https://aclanthology.org/2025.emnlp-main.182.pdf) (as "Speech generation")**
> The observable task of converting textual content and style instructions into an audible speech signal.

**[Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1076.pdf) (as "Text-to-speech generation")**
> The observable task of synthesizing audible speech from a given text transcript.

**[AFRIDOC-MT: Document-levelMTCorpus forAfrican Languages](https://aclanthology.org/2025.emnlp-main.1414.pdf) (as "Text-to-speech")**
> The task of synthesizing audible speech from written text.

**[A Variational Framework for Improving Naturalness in Generative Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25z/chen25z.pdf) (as "Speech continuation")**
> The task of generating a coherent and natural-sounding continuation of a given speech prompt.

**[NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf) (as "Spoken dialogue generation")**
> Generating spoken conversational responses in a dialogue setting from prior speech context.

**[Generative Audio Language Modeling with Continuous-valued Tokens and Masked Next-Token Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25n/yang25n.pdf) (as "Text-to-audio generation")**
> The task of generating a relevant audio waveform or spectrogram based on a given natural language text prompt.

**[ALMTokenizer: A Low-bitrate and Semantic-rich Audio Codec Tokenizer for Audio Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25q/yang25q.pdf) (as "Text-to-sound generation")**
> Generating non-speech audio (e.g., environmental sounds) from textual descriptions using an audio language model.

## Relationships

### Text-to-speech synthesis →
- **AudioCaps** (measurements) — *measured_by*
  - [Generative Audio Language Modeling with Continuous-valued Tokens and Masked Next-Token Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25n/yang25n.pdf)

### Associated with
- **Multimodal reasoning** (constructs)
  - [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf)
- **Voice cloning** (behaviors tasks)
  - [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25a/jia25a.pdf)
- **Hallucination** (behaviors tasks)
  > LLM-based TTS systems face challenges, with hallucinations being a prominent issue (Sahoo et al., 2024; Song et al., 2024; Neekhara et al., 2024a; Borsos et al., 2023).
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1076.pdf)
