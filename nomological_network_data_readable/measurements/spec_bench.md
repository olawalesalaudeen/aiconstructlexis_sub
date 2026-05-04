# Spec-Bench
**Type:** Measurement  
**Referenced in:** 14 papers  
**Also known as:** SpecBench, Spec Bench  

## State of the Field

Across the provided literature, Spec-Bench is consistently described as a benchmark or evaluation suite designed to assess speculative decoding methods. Its primary use is to measure the efficiency and performance of these methods across a diverse set of language generation tasks. The papers consistently list a core set of subtasks evaluated by the benchmark, including multi-turn conversation, retrieval-augmented generation (RAG), summarization, translation, question answering, and mathematical reasoning. Performance on these tasks is operationalized through specific efficiency metrics. The most commonly cited metrics are the "Mean Accepted Tokens (MAT) and the throughput (Tokens/s)," which one paper notes are "widely adopted in the speculative decoding community" (BanditSpec: Adaptive Speculative Decoding via Bandit Algorithms). Another paper also reports using the benchmark to measure the speed-up ratio relative to standard autoregressive decoding.

## Sources

**[Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)**
> A benchmark suite for speculative decoding that includes multiple generation subtasks such as conversation, retrieval-augmented generation, summarization, translation, question answering, and mathematical reasoning.

**[Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf) (as "SpecBench")**
> An evaluation suite featuring a collection of language benchmarks used for assessing speculative decoding methods.

**[BanditSpec: Adaptive Speculative Decoding via Bandit Algorithms](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25h/hou25h.pdf) (as "Spec Bench")**
> Benchmark for evaluating speculative decoding methods across multiple topics, used to measure mean accepted tokens and throughput.

## Relationships

### → Spec-Bench
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **Dialogue** (behaviors tasks) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **Machine translation** (behaviors tasks) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
