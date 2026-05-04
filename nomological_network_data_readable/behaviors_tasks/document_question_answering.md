# Document question answering
**Type:** Behavior  
**Referenced in:** 68 papers  
**Also known as:** Contextual question answering, Document-based question answering, Long-context question answering, Open-book question answering, Webpage question answering, Flexible length question answering, Long-book question answering, Multi-document question answering, Long-document question answering, Context-based question answering, Privacy question answering, Privacy policy question answering  

## State of the Field

Across the surveyed literature, document question answering is predominantly framed as the task of generating answers based on information provided within a given context, such as one or more documents, rather than relying on parametric knowledge. A frequent distinction is made between single-document QA, which involves one long document, and multi-document QA, where models must synthesize information or identify a correct source among irrelevant "distractor" documents. The task is further specified by context length, with variants like "long-context" and "long-book" QA, and by content type, including multimodal documents, webpages, and specialized texts like privacy policies. Most definitions, such as "open-book" or "contextual" QA, emphasize reliance on the provided passage, with some studies explicitly using contexts that are "counterfactual to the model’s pretrained knowledge" to test this capability. In contrast, "open-domain question answering" is described as a task that typically requires retrieving information from an external knowledge source. This behavior is commonly measured using a range of benchmarks, with `LongBench` appearing as a prevalent instrument for evaluating both single- and multi-document QA. Other datasets used to operationalize this behavior include `InfiniteBench` for book-length contexts, `HotpotQA` and `2WikiMultihopQA` for multi-document scenarios, and `SQuAD` for general context-based QA. In the specific application of privacy policy QA, this behavior is also studied in relation to `Hallucination`.

## Sources

**[Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/27571b74d6cd650b8eb6cf1837953ae8-Paper-Conference.pdf)**
> The task of answering questions based on the content of multimodal documents that may contain text, charts, and images.

**[RazorAttention: Efficient KV Cache Compression Through Retrieval Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/2a98af4fea6a24b73af7b588ca95f755-Paper-Conference.pdf) (as "Long-context question answering")**
> The observable action of generating answers to questions based on information contained within a lengthy input context.

**[AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf) (as "Open-book question answering")**
> The task of answering a question using information provided in a given context, where the model is not expected to rely solely on its pre-trained knowledge.

**[Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf) (as "Webpage question answering")**
> Answering questions about non-image content in webpages using page structure and textual information.

**[Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf) (as "Single-document question answering")**
> Answering questions that require extracting or reasoning over information from a single long document.

**[Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf) (as "Document-based question answering")**
> Answering questions using information contained in provided documents or passages, especially under varying context lengths.

**[FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf) (as "Contextual question answering")**
> The task of generating an answer to a question based solely on the information provided in a given context passage.

**[StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf) (as "Knowledge-based question answering")**
> Generating answers to questions based on large sets of dispersed documents.

**[LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf) (as "Long-book question answering")**
> The observable task of answering questions based on information contained within an extensive, book-length text.

**[From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf) (as "Multi-document question answering")**
> The task of answering a question based on information contained within one of several documents provided in the context, where other documents act as distractors.

**[From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf) (as "Flexible length question answering")**
> The task of answering a True/False question that requires reasoning over two key sentences within a context of varying length.

**[RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf) (as "Open-domain question answering")**
> The task of answering questions on a wide range of topics, which typically requires retrieving information from an external knowledge source.

**[Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf) (as "Domain-specific question answering")**
> Answering questions about facts contained in a specialized document or newly learned domain.

**[SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf) (as "Long-document question answering")**
> The observable task of answering questions by locating, aggregating, or filtering information from a long document provided in the context.

**[Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa27ac7aca4e462da1439b43ceebc04c-Paper-Conference.pdf) (as "Context-based question answering")**
> Answering questions by using information supplied in the input context, especially when that context conflicts with pretrained knowledge.

**[Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf) (as "Privacy question answering")**
> The observable task of providing accurate answers to specific user questions based on the content of a given privacy policy.

**[Multi-Level Explanations for Generative Language Models](https://aclanthology.org/2025.acl-long.1554.pdf) (as "Privacy policy question answering")**
> The observable task of generating a concise and relevant answer to a user's query based on the text of a given privacy policy document.

## Relationships

### Document question answering →
- **DocVQA** (measurements) — *measured_by*
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  > In Table 3 we present the results of different algorithms on LongBench (Bai et al., 2023b), which provides a comprehensive assessment to evaluate long-context related abilities of LLMs.
  - [Audio-centric Video Understanding Benchmark without Text Shortcut](https://aclanthology.org/2025.emnlp-main.334.pdf)
- **HotpotQA** (measurements) — *measured_by*
  > Performance comparison on eight LongBench datasets evaluating single/multi-document QA, summarization, and retrieval tasks... (Table 3)
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **2WikiMultihopQA** (measurements) — *measured_by*
  > Performance comparison on eight LongBench datasets evaluating single/multi-document QA, summarization, and retrieval tasks... (Table 3)
  - [HVGuard: Utilizing Multimodal Large Language Models for Hateful Video Detection](https://aclanthology.org/2025.emnlp-main.457.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  > "Infinite Bench: a benchmark dataset designed to test LLMs’ understanding of long dependencies within extensive contexts"
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  > Here, we consider the scenario where the model needs to adapt to new knowledge based on documents. ... we use two question answering (QA) datasets, SQuAD (Rajpurkar et al., 2016) and StreamingQA (Liska et al., 2022)
  - [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf)
- **FLenQA** (measurements) — *measured_by*
  > Our goal is to investigate whether finetuning LLMs ... improves their long context capabilities on natural language tasks: ... flexible length question answering (FLenQA) (Section 3)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
- **SQuAD 2.0** (measurements) — *measured_by*
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **Qasper** (measurements) — *measured_by*
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **MMLongBench-Doc** (measurements) — *measured_by*
  > We evaluate the performance of our proposed DocAgent on two multi-modal long-context document question answering benchmarks. (Section 4)
  - [Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://aclanthology.org/2025.emnlp-main.893.pdf)
- **DocBench** (measurements) — *measured_by*
  > We conduct experiments on two multi-modal long-context document understanding and question-answering benchmarks, including MMLongBench-Doc (Ma et al., 2024) and DocBench (Zou et al., 2025). (Section 4.1)
  - [Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://aclanthology.org/2025.emnlp-main.893.pdf)
- **HAGRID** (measurements) — *measured_by*
  - [AISees YourLocation—But With A Bias Toward The Wealthy World](https://aclanthology.org/2025.emnlp-main.911.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  > However, we also observed that autoregressive large language models like GPT-4o-mini tend to hallucinate responses... in answering questions within the privacy policy context.
  - [Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf)
- **Multi-task capability** (constructs)
  - [OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf)
