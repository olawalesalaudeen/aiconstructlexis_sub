# Needle-in-a-haystack test
**Type:** Measurement  
**Referenced in:** 53 papers  
**Also known as:** Needle-in-the-Haystack, Needle-in-a-Haystack, Needle in A Haystack, Needle In A Haystack, Needle in a Haystack, Needle-In-A-Haystack, Needle-in-a-haystack, Needle-in-the-haystack, Needle in A Haystack test, Needle in a haystack test, Needle-in-the-Haystack test, Needle-in-the-haystack test, Passkey retrieval task, Passkey Retrieval Task, NIAH, Passkey Retrieval, Needle-in-a-Haystack (NIAH), Passkey retrieval, Needle-in-Haystack, Needle in a Haystack (NIAH), PasskeyRetrieval  

## State of the Field

The Needle-in-a-haystack test is consistently described across the provided literature as an evaluation paradigm, benchmark, or controlled experiment designed to measure a model's ability to retrieve information from long contexts. The common procedure involves embedding a specific, often irrelevant, piece of information—the "needle"—at various depths within a long, distracting text, or "haystack," and then querying the model to find it. The needle is variously defined as a "fact," an "unrelated sentence," a "statement," or, in a popular variant known as the "Passkey retrieval task," a specific "5-digit code" or "random number." This test is most frequently used to operationalize and assess `Information retrieval` and `Long-context processing`, but is also employed to evaluate `Length generalization`, `Knowledge recall`, `Factuality`, and `Understanding`. It is widely used to "assess how robustly a model utilizes information positioned in the long context" ("Make Your LLM Fully Utilize the Context") and is often studied alongside other benchmarks like LongBench and RULER. While prevalent, at least one paper characterizes it as a "synthetic benchmark" that is "potentially inadequate for evaluating real-world RAG challenges" ("Long-Context LLMs Meet RAG..."). The evaluation protocol has also been adapted to test retrieval from "long video sequences" ("SurveyPilot: an Agentic Framework for Automated Human Opinion Collection from Social Media").

## Sources

**[Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf) (as "Needle-in-the-Haystack")**
> A long-context retrieval benchmark that tests whether a model can find a target item embedded in a long document-style context.

**[An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf) (as "Needle-in-a-Haystack")**
> An evaluation test where a specific, irrelevant fact (the "needle") is placed at various depths within a long, distracting text (the "haystack"), and the model is queried to retrieve it.

**[Differential Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/00b67df24009747e8bbed4c2c6f9c825-Paper-Conference.pdf) (as "Needle-In-A-Haystack")**
> An evaluation test designed to measure a model's ability to retrieve a specific piece of information (the "needle") embedded within a long, distracting context (the "haystack").

**[TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf) (as "Needle-in-the-Haystack test")**
> A benchmark that assesses a model's ability to retrieve a specific piece of information ('needle') embedded deep within a long, distracting context ('haystack').

**[From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf) (as "Needle-in-a-haystack")**
> An evaluation procedure where a specific fact (the "needle") is placed within a long, irrelevant text (the "haystack") to test a model's information retrieval capability.

**[RazorAttention: Efficient KV Cache Compression Through Retrieval Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/2a98af4fea6a24b73af7b588ca95f755-Paper-Conference.pdf) (as "Needle in A Haystack")**
> A benchmark designed to evaluate a model's ability to retrieve a specific, targeted piece of information ('the needle') placed at various depths within a long, distracting document ('the haystack').

**[NovelQA: Benchmarking Question Answering on Documents Exceeding 200K Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/file/3adb85a348a18cdd74ce99fbbab20301-Paper-Conference.pdf) (as "Needle in A Haystack test")**
> An evaluation procedure that tests information retrieval in long contexts by inserting a distinct, unrelated sentence (the "needle") into a long document (the "haystack") and asking the model to retrieve it.

**[Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf) (as "Needle-in-the-haystack")**
> A synthetic benchmark designed to test a model's ability to retrieve a specific piece of information from a long, distracting context, noted as potentially inadequate for evaluating real-world RAG challenges.

**[Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf) (as "Needle-in-the-haystack test")**
> A controlled experiment designed to evaluate a model's ability to find and use a small piece of relevant information ('needle') placed within a larger, irrelevant context ('haystack').

**[World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf) (as "Needle In A Haystack")**
> An evaluation task designed to test a model's ability to retrieve a specific piece of information ('needle') embedded within a long, distracting context ('haystack').

**[Needle Threading: Can LLMs Follow Threads Through Near-Million-Scale Haystacks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/acfcb9e8f066f14cab7368e07cfab5be-Paper-Conference.pdf) (as "Needle in a haystack test")**
> A general evaluation paradigm for long-context retrieval where a small, relevant piece of information (the 'needle') is placed within a large volume of irrelevant text (the 'haystack') to test if a model can find it.

**[Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf) (as "Needle in a Haystack")**
> A long-context retrieval benchmark in which a statement is inserted into a long document and the model must retrieve it from context.

**[MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf) (as "Passkey retrieval task")**
> A long-context retrieval evaluation in which a hidden 5-digit code must be recovered from within a long input sequence.

**[DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf) (as "Passkey Retrieval Task")**
> A synthetic evaluation protocol designed to test long-context retrieval by requiring a model to find and repeat a random passkey hidden within a long text sample.

**[SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf) (as "NIAH")**
> Needle in a Haystack, a benchmark designed to test if a model can retrieve a small, specific piece of information ('needle') placed within a long, irrelevant context ('haystack').

**[Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf) (as "Passkey Retrieval")**
> A needle-in-haystack benchmark that evaluates a model's ability to retrieve a short target token (e.g., a five-digit number) from a long context of distractor text, testing long-range dependency and information retention.

**[RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/behnam25a/behnam25a.pdf) (as "Needle-in-a-Haystack (NIAH)")**
> An evaluation procedure that tests a model's ability to retrieve a specific piece of information ('needle') embedded within a long, distracting text ('haystack').

**[Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf) (as "Passkey retrieval")**
> Task where a model must retrieve a hidden passkey (random number) embedded in long, distracting text; used to evaluate maximum effective context length.

**[WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf) (as "Needle-in-Haystack")**
> An evaluation task that tests a model's ability to retrieve a specific piece of information (the "needle") intentionally placed within a long, distracting context (the "haystack").

**[SurveyPilot: an Agentic Framework for Automated Human Opinion Collection from Social Media](https://aclanthology.org/2025.acl-long.222.pdf) (as "Needle in a Haystack (NIAH)")**
> Evaluation protocol testing a model's ability to retrieve specific information from long video sequences, analogous to finding a needle in a haystack.

**[VISA: Retrieval Augmented Generation with Visual Source Attribution](https://aclanthology.org/2025.acl-long.1457.pdf) (as "PasskeyRetrieval")**
> A synthetic benchmark from the LongEmbed study used to evaluate long-context retrieval by requiring the model to retrieve a random 'passkey' from a long, distracting document.

## Relationships

### → Needle-in-a-haystack test
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c1ddd2e59df46fd2aa85c833b1b36ed-Paper-Conference.pdf)
- **Length generalization** (constructs) — *measured_by*
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  - [Hymba: A Hybrid-head Architecture for Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f32def07618040e540e0a6182e290562-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
- **Quality** (constructs) — *measured_by*
  - [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf)
- **Understanding** (constructs) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)

### Associated with
- **RULER** (measurements)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **OpenCompass** (measurements)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
