# Audio captioning
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Music captioning  

## State of the Field

Across the surveyed literature, audio captioning is predominantly defined as the task of generating natural language descriptions for audio content. The most common definitions specify that this applies to non-speech audio, such as "environmental sounds or events," although one paper also includes music in this category. A more specialized variant, "music captioning," is also described, focusing exclusively on generating text for music clips. This behavior is consistently operationalized and evaluated using several benchmarks, with AudioCaps and Clotho being the most frequently cited datasets for this purpose, alongside MusicCaps for the music-specific version of the task. One paper illustrates a direct method for eliciting this behavior from a model using the prompt, "write an audio caption describing the sound". The task is generally positioned as a "conventional" or "fundamental" audio processing capability, often studied as a component of broader "General Auditory Awareness and Processing."

## Sources

**[Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf)**
> Generating natural language descriptions of non-speech audio content such as environmental sounds or events.

**[ALMTokenizer: A Low-bitrate and Semantic-rich Audio Codec Tokenizer for Audio Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25q/yang25q.pdf) (as "Music captioning")**
> Generating descriptive text for music clips, used to evaluate the understanding capabilities of the audio tokenizer in a language model.

## Relationships

### Audio captioning →
- **AudioCaps** (measurements) — *measured_by*
  > The results on all 15 tasks produced by SALMONN are shown in Table 3. From the results, SALMONN, without or with activation tuning, can produce competitive results on all level 1 tasks. (Section 5.1)
  - [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf)
- **Clotho** (measurements) — *measured_by*
  > We evaluate our approach on a popular audio captioning dataset, Clotho (Drossos et al., 2020). (Section 4.3)
  - [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf)
- **MusicCaps** (measurements) — *measured_by*
  > Table 2 summarizes the comparative results for audio captioning tasks on AudioCaps, Clotho, and MusicCaps benchmarks. (Section 4.2.1)
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)

### Associated with
- **Audio understanding** (constructs)
  - [MA-GTS: A Multi-Agent Framework for Solving Complex Graph Problems in Real-World Applications](https://aclanthology.org/2025.emnlp-main.974.pdf)
