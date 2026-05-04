# LongBench
**Type:** Measurement  
**Referenced in:** 90 papers  
**Also known as:** Longbench  

## State of the Field

Across the surveyed literature, LongBench is consistently described as a benchmark suite designed to evaluate the long-context understanding and processing capabilities of large language models. It operationalizes this evaluation through a diverse set of tasks, with the most frequently mentioned being question answering (often specified as single- and multi-document QA), text summarization, and code completion. Other behaviors assessed using LongBench include few-shot learning, information retrieval, contextual reasoning, and fact checking. The benchmark is framed as a collection of datasets, with papers citing the use of subsets like HotpotQA, MuSiQue, 2WikiMQA, and MultiNews from within the suite. The input lengths are a defining feature, with different papers reporting ranges from "5k to 15k tokens" to contexts longer than 32k tokens. A smaller set of sources also characterize it as a bilingual benchmark covering tasks in both English and Chinese. The evaluation is commonly conducted in a zero-shot setting, as noted by one study, and is said to encompass both real-world and synthetic tasks.

## Sources

**[CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)**
> Benchmark for evaluating long-context understanding in LLMs across diverse tasks including question answering, summarization, and code completion, with input lengths ranging from 5k to 15k tokens.

**[LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf) (as "Longbench")**
> A benchmark consisting of various tasks, such as long-document question answering and query-based summarization, to evaluate long-context understanding.

## Relationships

### → LongBench
- **Long-context understanding** (constructs) — *measured_by*
  > "we use the LongBench benchmark (Bai et al., 2023) to evaluate the long context prompt and decoding performance of HiP"
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  > We present our main results on language modeling tasks, synthetic long-context tasks, and real-world long-context tasks... we evaluate AdaGroPE on the LongBench (Bai et al., 2024) benchmark... [which includes] Summarization... (Section 3, Table 3)
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **Code completion** (behaviors tasks) — *measured_by*
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **Few-shot learning** (measurements) — *measured_by*
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *measured_by*
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Document summarization** (behaviors tasks) — *measured_by*
  > ZeroSCROLLS (Shaham et al., 2023) and LongBench (Bai et al., 2023) tackle tasks like long-document QA and query-based summarization. (Section 5)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
- **Single-document question answering** (behaviors tasks) — *measured_by*
  > We conduct evaluations on three types of tasks within LongBench: Single-Doc QA, Multi-Doc QA, and Summarization... (Section 4.3)
  - [SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning](https://aclanthology.org/2025.acl-long.560.pdf)
- **Length generalization** (constructs) — *measured_by*
  > We compare our method with existing length extrapolation approaches...on LongBench (Bai et al., 2023) and InfiniteBench (Zhang et al., 2024), evaluating them on Llama2-7B-chat-hf... (Section 5.1)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Document question answering** (behaviors tasks) — *measured_by*
  > In Table 3 we present the results of different algorithms on LongBench (Bai et al., 2023b), which provides a comprehensive assessment to evaluate long-context related abilities of LLMs.
  - [Audio-centric Video Understanding Benchmark without Text Shortcut](https://aclanthology.org/2025.emnlp-main.334.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > In LongBench, we merge four tasks into 'QA' and merge two tasks into the 'Summary' column in the table.
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dd/li25dd.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > We believe that this benchmark is the most important because it shows both long context generation performance and knowledge retrieval performance
  - [Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf)
- **Quality** (constructs) — *measured_by*
  - [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf)
- **Contextual reasoning** (constructs) — *measured_by*
  > For LongBench, we use datasets from the Single-Doc QA and Multi-Doc QA categories to assess contextual reasoning.
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
- **Fact checking** (behaviors tasks) — *measured_by*
  > LongBench (Bai et al., 2024): Focused on medium-context tasks (10K tokens), it assesses summarization, QA, and fact-checking across multiple domains...
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **Knowledge retrieval** (behaviors tasks) — *measured_by*
  - [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf)
- **Long-context generalization** (constructs) — *measured_by*
  > In addition, our method remains competitive on Llama3-8B and Qwen2 while outperforming others on Mistral on LongBench (Bai et al., 2023), which is the first bilingual benchmark for long context understanding. (Section 6.1)
  - [HyKGE: A Hypothesis Knowledge Graph EnhancedRAGFramework for Accurate and Reliable MedicalLLMs Responses](https://aclanthology.org/2025.acl-long.581.pdf)
- **Long-context reasoning** (constructs) — *measured_by*
  - [Alignment for Efficient Tool Calling of Large Language Models](https://aclanthology.org/2025.emnlp-main.899.pdf)

### Associated with
- **HotpotQA** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
- **MuSiQue** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
- **2WikiMultihopQA** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
- **SAMSum** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
- **MultiNews** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
