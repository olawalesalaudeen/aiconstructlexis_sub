# SAMSum
**Type:** Measurement  
**Referenced in:** 28 papers  
**Also known as:** SAMsum, SAMSUM, Samsum, SamSum  

## State of the Field

Across the provided literature, SAMSum is predominantly characterized as a dataset for evaluating dialogue summarization. It is consistently described as consisting of chat transcripts or messenger-like conversations paired with human-written summaries. The most frequent application of SAMSum is to measure the behavior of text summarization, with one paper specifying the use of ROUGE scores for this evaluation. Beyond general performance assessment, some papers also use the dataset for fine-tuning models, as in the case of low-rank adaptation. A smaller body of work employs SAMSum for more specific evaluations, including privacy-preserving summarization, LLM inference under KV-cache compression, and selective generation uncertainty. Additionally, it is identified as part of the LongBench suite, where it is used to assess few-shot learning performance.

## Sources

**[Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf) (as "SAMsum")**
> Dialogue summarization dataset consisting of chat transcripts and human-written summaries, used to evaluate privacy-preserving summarization.

**[Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf)**
> A dialogue summarization dataset used to evaluate language generation performance, particularly in summarizing multi-party conversations.

**[SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b0a8df568ec496a717566a7f8158aaa-Paper-Conference.pdf) (as "SAMSUM")**
> A dialogue summarization dataset used as an evaluation set for LLM inference under KV-cache compression.

**[Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf) (as "Samsum")**
> A dataset of chat dialogues and their summaries, used for evaluating and fine-tuning models on summarization tasks.

**[Cascading Large Language Models for Salient Event Graph Generation](https://aclanthology.org/2025.naacl-long.113.pdf) (as "SamSum")**
> A dialogue summarization benchmark used to evaluate selective generation uncertainty methods on generated summaries.

## Relationships

### → SAMSum
- **Text summarization** (behaviors tasks) — *measured_by*
  > We further evaluate the methods on three summarization datasets. ... SAMSum (Gliwa et al., 2019) is a dataset of messenger conversations about daily-life topics, annotated with short summaries. (Section 4.1)
  - [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **Dialogue summarization** (behaviors tasks) — *measured_by*
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)

### Associated with
- **LongBench** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
