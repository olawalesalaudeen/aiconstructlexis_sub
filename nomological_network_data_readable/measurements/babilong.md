# BABILong
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** bAbILong, BABILONG  

## State of the Field

Across the provided literature, BABILong is consistently presented as a benchmark for evaluating the long-context capabilities of language models. It is explicitly used to measure constructs such as `Long-context understanding` and `Long-context processing`. The most prevalent description of the benchmark's design states that it tests a model's ability to find and reason over multiple pieces of evidence or supporting facts that are randomly placed within a long sequence. One paper specifies that BABILong consists of five such tasks designed to generate accurate answers from context. A secondary but recurring framing describes it as a "long-context extension of the bAbI dataset" intended to test reasoning over extended narratives. In evaluations, BABILong is frequently studied alongside other long-context benchmarks like RULER and is also noted to correlate with MMLU.

## Sources

**[A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)**
> A benchmark designed to test long-context reasoning and retrieval by requiring models to find and reason over multiple pieces of evidence randomly placed in a long sequence.

**[Episodic Memories Generation and Evaluation Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ff013b7e372ba5b790352ccd6908f03-Paper-Conference.pdf) (as "bAbILong")**
> A long-context extension of the bAbI dataset designed to test reasoning capabilities over extended narratives.

**[Holistic Reasoning with Long-Context LMs: A Benchmark for Database Operations on Massive Textual Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/c2f75bb334e1592a3da55589af75161a-Paper-Conference.pdf) (as "BABILONG")**
> A benchmark for evaluating long-context language models, mentioned in a comparison of existing benchmarks.

## Relationships

### BABILong →
- **MMLU** (measurements) — *correlates*
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)

### → BABILong
- **Long-context reasoning** (constructs) — *measured_by*
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)

### Associated with
- **bAbI** (measurements)
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **RULER** (measurements)
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
