# InfiniteBench
**Type:** Measurement  
**Referenced in:** 25 papers  
**Also known as:** ∞-Bench, ∞Bench, ∞BENCH, ∞-bench  

## State of the Field

InfiniteBench is consistently characterized as a benchmark for evaluating large language models on tasks involving very long contexts, with sources frequently specifying lengths exceeding 100,000 tokens. Across the provided literature, its primary application is to measure the construct of `Long-context processing` by assessing an LLM's ability to understand and reason over long dependencies. The most common operationalization focuses on a narrow set of tasks, particularly long-book question answering (`En.QA`), multiple-choice question answering (`En.MC`), and `Text summarization` (`En.Sum`). However, a smaller set of papers describes a more diverse collection of what one source calls "10 real-world and synthetic tasks." This broader scope includes the evaluation of `Information retrieval` (such as passkey and key-value retrieval), `Code debugging`, and `Mathematical reasoning`. The benchmark is also used to assess more general capabilities like `Length generalization` and `Long-context understanding`. Several papers refer to it as a "widely used" instrument for these purposes.

## Sources

**[LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf) (as "∞Bench")**
> A long-context benchmark evaluating summarization, long-book question answering, and multiple-choice question answering over contexts beyond 100K tokens.

**[Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf) (as "∞BENCH")**
> Long-context benchmark with average length of 100K tokens, including English question answering and multiple-choice question answering tasks on long novels.

**[Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf) (as "∞-Bench")**
> A benchmark specifically designed to evaluate LLMs on very long context tasks, including various forms of retrieval like passkey, key-value, and number retrieval.

**[FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)**
> A benchmark dataset designed to test LLMs’ understanding of long dependencies within extensive contexts, including 10 synthetic and real-world tasks across various domains.

**[LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dv/li25dv.pdf) (as "∞-bench")**
> ∞-bench, a long-context benchmark with En.QA and En.MC tasks used in the paper as a comparison point and critique target.

## Relationships

### → InfiniteBench
- **Text summarization** (behaviors tasks) — *measured_by*
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **Code debugging** (behaviors tasks) — *measured_by*
  > "Table 2 shows that our method preserves most of the model’s performance in retrieval and QA tasks, while maintaining efficacy in complex mathematical and coding tasks."
  - [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
- **Length generalization** (constructs) — *measured_by*
  > We compare our method with existing length extrapolation approaches...on LongBench (Bai et al., 2023) and InfiniteBench (Zhang et al., 2024), evaluating them on Llama2-7B-chat-hf... (Section 5.1)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
- **Context retrieval** (behaviors tasks) — *measured_by*
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  > maintaining efficacy in complex mathematical and coding tasks.
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > Table 2 shows that our method preserves most of the model's performance in retrieval and QA tasks
  - [Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf)
- **Long-context reasoning** (constructs) — *measured_by*
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
- **Document question answering** (behaviors tasks) — *measured_by*
  > "Infinite Bench: a benchmark dataset designed to test LLMs’ understanding of long dependencies within extensive contexts"
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > Table 2 shows that our method preserves most of the model's performance in retrieval and QA tasks
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > "In Table 3, we provide results across the InfiniteBench tasks" and the table includes "Dialogue" tasks under InfiniteBench
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **Key-value retrieval** (behaviors tasks) — *measured_by*
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
