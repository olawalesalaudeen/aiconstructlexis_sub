# Audio classification
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Music genre classification, Music classification, Sound classification  

## State of the Field

Across the provided literature, audio classification is most commonly defined as the task of assigning a category or label to an audio clip. This general behavior encompasses more specific sub-tasks, such as "Music classification," which involves categorizing musical elements like "instruments, genres, and emotions," and "Sound classification." One paper defines sound classification specifically in the context of using "tokenizer-derived representations" for the task. The behavior is frequently treated as a foundational auditory task, often mentioned alongside captioning, and is used to measure model performance. To operationalize and measure this behavior, researchers employ a range of "audio classification benchmarks." The provided data shows that models are evaluated on datasets including FSD50k, ESC-50, GTZAN, and US8K. Specific instances of this behavior are measured with particular datasets; for example, one study conducts "sound classification tasks on the ESC-50 dataset" and another uses Medley-solos-DB for "music classification tasks."

## Sources

**[Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf)**
> Assigning an audio clip to a sound category or label.

**[Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf) (as "Music genre classification")**
> Categorizing a piece of music into a specific genre.

**[Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1a7774429d5c06cc744ff4260a8e9f-Paper-Conference.pdf) (as "Music classification")**
> Categorizing musical content such as instruments, genres, or emotions.

**[ALMTokenizer: A Low-bitrate and Semantic-rich Audio Codec Tokenizer for Audio Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25q/yang25q.pdf) (as "Sound classification")**
> Assigning sound clips to semantic categories using tokenizer-derived representations.

## Relationships

### Audio classification →
- **FSD50k** (measurements) — *measured_by*
  > “Foundational benchmarks include ClothoAQA, MusicAVQA (audio-only), NonSpeech7k, NSynth, CREMA-D, Ravdess, GTZAN, Medley-solos-DB and USD8K and Clotho-v2 and AudioCaps.”
  - [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf)
- **ESC-50** (measurements) — *measured_by*
  > Table 1. Comparision results on audio classification benchmarks and ClothoAQA benchmark. (Table 1)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
- **GTZAN** (measurements) — *measured_by*
  > “Foundational benchmarks include ClothoAQA, MusicAVQA (audio-only), NonSpeech7k, NSynth, CREMA-D, Ravdess, GTZAN, Medley-solos-DB and USD8K and Clotho-v2 and AudioCaps.”
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
- **US8K** (measurements) — *measured_by*
  > “Foundational benchmarks include ClothoAQA, MusicAVQA (audio-only), NonSpeech7k, NSynth, CREMA-D, Ravdess, GTZAN, Medley-solos-DB and USD8K and Clotho-v2 and AudioCaps.”
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
