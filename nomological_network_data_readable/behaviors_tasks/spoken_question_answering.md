# Spoken question answering
**Type:** Behavior  
**Referenced in:** 8 papers  
**Also known as:** Speech question answering  

## State of the Field

The behavior of spoken question answering is defined in several distinct ways across the surveyed literature. The most prevalent framing describes it as a model's ability to answer spoken questions about "broad factual knowledge without access to external knowledge," with responses being either spoken or textual. A different line of work defines it as a multimodal task involving answering a question posed in speech about the content of a given image. A third definition, termed "Audio Question Answering (AQA)," involves generating open-ended answers to questions about the content of an audio input itself, covering both factual and reasoning-based queries. To operationalize this behavior, researchers frequently use datasets such as WebQuestions and TriviaQA, with some studies noting the use of synthesized audio versions of these benchmarks. For the vision-language variant of the task, the SQA dataset is mentioned as a measurement instrument. The behavior is also studied in relation to speech understanding.

## Sources

**[Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)**
> The model answers spoken questions with either spoken or textual responses.

**[VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf) (as "Speech question answering")**
> The task of answering a question posed in speech based on the content of a given image.

**[Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf) (as "Audio question answering")**
> Generating answers to questions about audio content, including both factual and reasoning-based queries.

## Relationships

### Spoken question answering →
- **WebQuestions** (measurements) — *measured_by*
  > Spoken Question Answering ... We evaluate our model on 3 datasets in D´efossez et al. (2024): Web Questions (Berant et al., 2013), Llama Questions (Nachmani et al., 2024), and TriviaQA (Joshi et al., 2017).
  - [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  > Spoken Question Answering ... We evaluate our model on 3 datasets in D´efossez et al. (2024): Web Questions (Berant et al., 2013), Llama Questions (Nachmani et al., 2024), and TriviaQA (Joshi et al., 2017).
  - [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)
- **SQA** (measurements) — *measured_by*
  > “the model is fine-tuned using both our curated speech question answering (SQA) dataset and the original visual question answering (VQA) datasets from LLaVA”
  - [VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf)

### Associated with
- **Speech understanding** (constructs)
  - [SVD-LLMV2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.218.pdf)
