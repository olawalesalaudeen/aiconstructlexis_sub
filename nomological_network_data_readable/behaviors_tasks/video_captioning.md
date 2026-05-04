# Video captioning
**Type:** Behavior  
**Referenced in:** 32 papers  
**Also known as:** Video scripting, Clip summarization, Video description generation, Audio description generation, Video narration, Caption generation, Video description, Teaser narration generation, Video detailed description  

## State of the Field

The prevailing definition of video captioning across the provided literature is the task of generating a textual description of a video's content. While this general framing is widespread, several papers introduce more specialized variants of this behavior, such as 'video scripting' for structured details like shot type ("Vript: A Video Is Worth Thousands of Words"), 'video narration' for real-time events ("VideoLLM-MoD..."), and 'audio description generation' for accessibility ("CALVIN..."). Other variations focus on specific content types, including describing anomalous events ("HAWK...") or producing comprehensive, narrative summaries referred to as 'video detailed description' ("LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding"). This behavior is most commonly operationalized and evaluated using the MSRVTT benchmark, with other papers also employing VATEX and YouCook2. Some work also mentions using generative evaluation benchmarks like Video-ChatGPT and DREAM-1K for what is termed 'video description' ("SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning"). Methodologically, approaches range from a 'differential video captioning strategy' for long videos ("ShareGPT4Video...") to using a video-text scorer to refine outputs ("LLMs can see and hear without any training"). The behavior is also studied alongside 'Mathematical reasoning' and is linked in one paper to enabling 'Cross-modal retrieval'.

## Sources

**[Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The task of generating a textual description of the content of a video.

**[Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Video scripting")**
> Describing a video scene with structured details such as title, content, shot type, and camera movement.

**[ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Clip summarization")**
> The task of generating a summary caption for a specific time-stamped clip within a longer video, potentially by reusing pre-computed differential captions.

**[HAWK: Learning to Understand Open-World Video Anomalies](https://proceedings.neurips.cc/paper_files/paper/2024/file/fca83589e85cb061631b7ebc5db5d6bd-Paper-Conference.pdf) (as "Video description generation")**
> The task of generating a natural language text that describes the content of a video, with a specific focus on anomalous events.

**[CALVIN: Improved Contextual Video Captioning via Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a922b7121007768f78f770c404415375-Paper-Conference.pdf) (as "Audio description generation")**
> The task of generating a verbal narration of the key visual elements in a video, intended to make content accessible to visually impaired individuals.

**[VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf) (as "Video narration")**
> The task of generating real-time, descriptive text that narrates the events occurring in a video stream.

**[Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf) (as "Caption generation")**
> The observable task of producing text descriptions that summarize or detail the content of video segments.

**[TeaserGen: Generating Teasers for Long Documentaries](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf) (as "Teaser narration generation")**
> Producing a short teaser script from a longer documentary narration, including story-like rewriting and an ending question.

**[Is Your Video Language Model a Reliable Judge?](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc4f891373d19087d1ddda33e81e00e4-Paper-Conference.pdf) (as "Video description")**
> Generating a textual description of the content of a video.

**[LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf) (as "Video detailed description")**
> Producing comprehensive, coherent textual summaries of video content, capturing characters, actions, settings, and narrative elements.

## Relationships

### Video captioning →
- **MSRVTT** (measurements) — *measured_by*
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **VATEX** (measurements) — *measured_by*
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *causes*
  - [IMPACT: A Large-scale Integrated Multimodal Patent Analysis and Creation Dataset for Design Patents](https://proceedings.neurips.cc/paper_files/paper/2024/file/e3301977b92f28e32639ec99eb08f4a1-Paper-Datasets_and_Benchmarks_Track.pdf)
- **YouCook2** (measurements) — *measured_by*
  - [Pun Unintended:LLMs and the Illusion of Humor Understanding](https://aclanthology.org/2025.emnlp-main.1420.pdf)

### Associated with
- **Temporal reasoning** (constructs)
  - [DatawiseAgent: A Notebook-CentricLLMAgent Framework for Adaptive and Robust Data Science Automation](https://aclanthology.org/2025.emnlp-main.59.pdf)
