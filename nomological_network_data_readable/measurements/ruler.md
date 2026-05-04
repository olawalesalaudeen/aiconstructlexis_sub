# RULER
**Type:** Measurement  
**Referenced in:** 60 papers  
**Also known as:** Ruler  

## State of the Field

Across the provided literature, RULER is consistently characterized as a synthetic benchmark suite designed to evaluate the long-context capabilities of large language models. Its most prevalent application is to measure `long-context processing` and `long-context understanding`, often by testing model performance across customizable or increasing sequence lengths. A dominant focus of the benchmark is assessing `information retrieval`, with numerous papers highlighting its use of "needle-in-a-haystack" (NIAH) tasks to evaluate abilities like passkey retrieval. Beyond simple recall, RULER is also used to evaluate more complex behaviors, as it is stated to contain tasks for `complex reasoning`, `multi-hop tracing`, `state tracking`, and `aggregation`. Several sources specify that the benchmark comprises around 13 synthetic tasks organized into these categories, along with `question answering`. As one paper notes, the benchmark's purpose is to "assess long-context capabilities beyond simple in-context recall" ("Modeling Uncertainty in Composed Image Retrieval via Probabilistic Embeddings"). The instrument is also used to measure `length generalization` and `synthetic recall`.

## Sources

**[FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)**
> A synthetic benchmark dataset created to evaluate long-context LLMs with customizable sequence lengths and task complexities, including tasks like needle-in-a-haystack, multi-hop tracing, and aggregation.

**[MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/13f972adf12bdf886583d48cd528002f-Paper-Conference.pdf) (as "Ruler")**
> A benchmark suite designed to evaluate the long-context capabilities of language models across various tasks.

## Relationships

### → RULER
- **Long-context understanding** (constructs) — *measured_by*
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > RULER (Hsieh et al., 2024) is a more complex benchmark containing NIAH tests, such as finding multiple passkeys and tracking variable changes inside complicated essay-style haystack sentences. (Section 5.3)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **Long-context reasoning** (constructs) — *measured_by*
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/13f972adf12bdf886583d48cd528002f-Paper-Conference.pdf)
- **Length generalization** (constructs) — *measured_by*
  - [To Mask or to Mirror: Human-AIAlignment in Collective Reasoning](https://aclanthology.org/2025.emnlp-main.123.pdf)
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
- **Synthetic recall** (behaviors tasks) — *measured_by*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **State tracking** (constructs) — *measured_by*
  > “This benchmark comprises four types of synthetic tasks across variable sequence lengths (4K to 128K): Needle-in-a-haystack (NIAH) retrieval, Multi-hop Tracing with Variable Tracking (VT)”
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
- **Context retrieval** (behaviors tasks) — *measured_by*
  > Notably, APB significantly enhances performance in complex context retrieval tasks, such as R.KV in ∞Bench and MK3 in RULER. (Section 4.2)
  - [LongReD: Mitigating Short-Text Degradation of Long-Context Large Language Models via Restoration Distillation](https://aclanthology.org/2025.acl-long.525.pdf)
- **Long-context generalization** (constructs) — *measured_by*
  > RULER (Hsieh et al., 2024) offers flexible sequence lengths and task complexities with 13 sub-task categories, including retrieval and question answering. We supplement more details about these benchmark in Appendix E. (Section 5.2)
  - [HyKGE: A Hypothesis Knowledge Graph EnhancedRAGFramework for Accurate and Reliable MedicalLLMs Responses](https://aclanthology.org/2025.acl-long.581.pdf)
- **Long-range dependency modeling** (constructs) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)

### Associated with
- **BABILong** (measurements)
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Needle-in-a-haystack test** (measurements)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
