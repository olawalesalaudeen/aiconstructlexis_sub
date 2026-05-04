# CNN/DailyMail
**Type:** Measurement  
**Referenced in:** 109 papers  
**Also known as:** CNN-DM, CNN/Daily Mail, CNN Dailymail, Commonsense reasoning benchmarks, PiQA, CNNDM, CNN / DailyMail, CNN, CNN-DailyMail, CNN/Dailymail, CNN Daily Mail, CNN/DM  

## State of the Field

Across the surveyed literature, CNN/DailyMail is a frequently used measurement instrument, consistently described as a large-scale dataset of news articles paired with human-written, multi-sentence summaries. Its prevailing application is to evaluate the behavior of `text summarization`, with many sources specifically using it for `abstractive summarization` and at least one for `document summarization`. Papers operationalize this by fine-tuning models such as T5 and BART on the dataset or by evaluating the quality of generated summaries, sometimes reporting ROUGE scores. While it is widely considered a "challenging text generation benchmark," a smaller line of work employs it for other purposes. For instance, one study uses it to measure `out-of-distribution generalization` by testing a model trained on a different summarization domain. Another paper raises a methodological consideration, noting the dataset has a "higher risk of pretraining contamination".

## Sources

**[Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) (as "CNN/Daily Mail")**
> A large-scale dataset of news articles paired with multi-sentence summaries, commonly used for evaluating text summarization.

**[Conformal Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf) (as "CNN/DM")**
> The CNN/Daily Mail dataset, a large collection of news articles paired with human-written summaries, widely used for evaluating text summarization models.

**[Unbiased Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c5b00c5bdcc6fe35907dbcca03d27652-Paper-Conference.pdf) (as "CNN-DM")**
> The CNN/Daily Mail dataset, a large-scale corpus of news articles paired with multi-sentence summaries, used for evaluating text summarization models.

**[Cascade Speculative Drafting for Even Faster LLM Inference](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cb5b083ba4f5ca6bd05dd307a2fb354-Paper-Conference.pdf) (as "CNN Dailymail")**
> A dataset for text summarization, used in a simulation to evaluate the performance of speculative decoding.

**[FouRA: Fourier Low-Rank Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/83960718b4d12f799985206f1b1cf00f-Paper-Conference.pdf) (as "Commonsense reasoning benchmarks")**
> A collection of benchmark tasks used to evaluate commonsense question answering and inference, including BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC, and OBQA.

**[Divergences between Language Models and Human Brains](https://proceedings.neurips.cc/paper_files/paper/2024/file/f96839fc751b67492e17e70f5c9730e4-Paper-Conference.pdf) (as "PiQA")**
> A multiple-choice dataset of goal-driven questions based on everyday situations, used here for fine-tuning on physical commonsense.

**[PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.748.pdf)**
> A dataset consisting of news articles paired with multi-sentence summaries, commonly used to evaluate abstractive text summarization.

**[Reading Between the Prompts: How Stereotypes ShapeLLM’s Implicit Personalization](https://aclanthology.org/2025.emnlp-main.1030.pdf) (as "CNNDM")**
> Document summarization benchmark based on CNN and Daily Mail articles, used to assess performance in settings with potential pretraining contamination.

**[RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf) (as "CNN / DailyMail")**
> A widely used dataset for abstractive text summarization, consisting of news articles from CNN and the Daily Mail paired with human-written summaries.

**[Whoever Started the interference Should End It: Guiding Data-Free Model Merging via Task Vectors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25h/cheng25h.pdf) (as "CNN")**
> A benchmark used to evaluate summarization or news-related language understanding in the paper's Qwen-14B evaluation table.

**[Towards Optimal Multi-draft Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0907335ecf28faf15be54485dbcbe70e-Paper-Conference.pdf) (as "CNN-DailyMail")**
> A dataset consisting of news articles and their corresponding summaries, used to evaluate text summarization.

**[On Speeding Up Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a38cfba4c717e5a37b200294615e546e-Paper-Conference.pdf) (as "CNN/Dailymail")**
> A dataset of news articles paired with summaries, commonly used for evaluating text summarization.

**[Distributed Speculative Inference (DSI): Speculation Parallelism for Provably Faster Lossless Language Model Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/b36554b97da741b1c48c9de05c73993e-Paper-Conference.pdf) (as "CNN Daily Mail")**
> A dataset for text summarization, composed of news articles from CNN and the Daily Mail paired with human-written summaries. The paper refers to it as CNN-DM in tables.

## Relationships

### → CNN/DailyMail
- **Text summarization** (behaviors tasks) — *measured_by*
  > For TS, we utilize XSum (Narayan et al., 2018), SamSum (Gliwa et al., 2019), and the CNN/-DailyMail (See et al., 2017) dataset.
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Out-of-distribution generalization** (constructs) — *measured_by*
  > For summarisation, the ID test set is the original TL;DR test set from (Stiennon et al., 2022), and the OOD test set is the CNN/DailyMail test set, a dataset of news articles and corresponding summaries (Nallapati et al., 2016). This tests the ability of the model to have learnt the more general skill of summarisation and to apply it in a very different domain. (Section 5.1)
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
- **Abstractive summarization** (behaviors tasks) — *measured_by*
  - [R-BPE: ImprovingBPE-Tokenizers with Token Reuse](https://aclanthology.org/2025.emnlp-main.1170.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [FouRA: Fourier Low-Rank Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/83960718b4d12f799985206f1b1cf00f-Paper-Conference.pdf)
- **News summarization** (behaviors tasks) — *measured_by*
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **Document summarization** (behaviors tasks) — *measured_by*
  - [Reading Between the Prompts: How Stereotypes ShapeLLM’s Implicit Personalization](https://aclanthology.org/2025.emnlp-main.1030.pdf)
