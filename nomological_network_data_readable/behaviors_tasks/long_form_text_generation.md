# Long-form text generation
**Type:** Behavior  
**Referenced in:** 35 papers  
**Also known as:** Long-form generation, Open-ended generation, Wikipedia article generation, Open-ended response generation, Long-form answer generation, Coherent multi-paragraph generation, Open-ended long text generation, Long-text generation, Long-context generation, Long-response generation, Ultra-long sequence generation  

## State of the Field

Across the surveyed literature, long-form text generation is predominantly defined as the observable behavior of producing extended, coherent, and structured text, such as biographies, Wikipedia articles, or detailed answers spanning multiple paragraphs. While most definitions focus on the length and structure of the output, with some specifying lengths exceeding 10,000 or even 100,000 tokens, a less common framing defines it as generation conditioned on a very long input context. This behavior is frequently positioned as representative of real-world applications, with one paper noting it is "more similar to downstream tasks than providing a rating as in a Likert scale" (REAL-MM-RAG: A Real-World Multi-Modal Retrieval Benchmark). The behavior is operationalized and measured using a wide array of instruments, including benchmarks like LongGenBench, HelloBench, TruthfulQA, and LongBench, as well as evaluation procedures like LLM-as-a-judge. For instance, the ASQA dataset is specifically used to evaluate how well models generate comprehensive answers that cover multiple valid interpretations of a question. Long-form text generation is studied alongside concepts such as instruction following, length generalization, self-consistency, and code generation. One line of work explicitly frames it as one of three primary strategies for disambiguation, alongside query rewriting and asking clarifying questions. Finally, enhancing factuality in these extended outputs is noted as a "challenging and underexplored area" (Unleashing the Reasoning Potential ofLLMs by Critique Fine-Tuning on One Problem).

## Sources

**[MemeQA: Holistic Evaluation for Meme Understanding](https://aclanthology.org/2025.acl-long.928.pdf) (as "Long-form generation")**
> Producing extended, coherent text responses (e.g., biographies) that contain multiple factual claims, often spanning hundreds of words.

**[KERL: Knowledge-Enhanced Personalized Recipe Recommendation using Large Language Models](https://aclanthology.org/2025.acl-long.939.pdf) (as "Open-ended generation")**
> Producing unstructured, long-form text responses to open-ended prompts in multiple languages.

**[Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](https://aclanthology.org/2025.acl-long.7.pdf)**
> The observable act of producing extended, context-specific text in response to a prompt, as required for many real-world tasks.

**[Tree-of-Debate: Multi-Persona Debate Trees Elicit Critical Thinking for Scientific Comparative Analysis](https://aclanthology.org/2025.acl-long.1423.pdf) (as "Wikipedia article generation")**
> Producing full-length, structured Wikipedia-style articles from web-sourced information, including section organization and content synthesis.

**[REAL-MM-RAG: A Real-World Multi-Modal Retrieval Benchmark](https://aclanthology.org/2025.acl-long.1529.pdf) (as "Open-ended response generation")**
> Producing free-text answers to political statements without constrained output formats, reflecting how models express opinions in naturalistic settings.

**[VC4VG: Optimizing Video Captions for Text-to-Video Generation](https://aclanthology.org/2025.emnlp-main.60.pdf) (as "Long-form answer generation")**
> Producing detailed, multi-sentence responses to user questions, typically requiring synthesis of information and structured explanation.

**[Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.93.pdf) (as "Coherent multi-paragraph generation")**
> The specific task of producing a well-structured and logically flowing text composed of multiple paragraphs from a collection of unordered points.

**[Good Intentions BeyondACL: Who DoesNLPfor Social Good, and Where?](https://aclanthology.org/2025.emnlp-main.260.pdf) (as "Open-ended long text generation")**
> Producing lengthy, coherent, and informative responses to complex questions that require synthesis of knowledge across multiple topics or domains.

**[CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.474.pdf) (as "Long-text generation")**
> The task of producing coherent and contextually relevant text sequences that are exceptionally long, such as exceeding 10,000 tokens.

**[RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf) (as "Long-context generation")**
> Generating text while conditioning on very long input contexts, often beyond 100K tokens.

**[Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf) (as "Long-response generation")**
> The task of generating a substantial number of output tokens from a relatively short input prompt, such as in essay writing or code synthesis.

**[TokenSwift: Lossless Acceleration of Ultra Long Sequence Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25z/wu25z.pdf) (as "Ultra-long sequence generation")**
> The observable task of producing a continuous, coherent text sequence of exceptional length, such as 100,000 tokens.

## Relationships

### Long-form text generation →
- **TruthfulQA** (measurements) — *measured_by*
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **LongGenBench** (measurements) — *measured_by*
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [GuideLLM: ExploringLLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.288.pdf)
- **HelloBench** (measurements) — *measured_by*
  > To evaluate the performance of PIC in long-form text generation, we select HelloBench (Que et al., 2024) and LongBench-Write (Bai et al., 2024) as the evaluation benchmarks. (Section 4.1)
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **MBPP** (measurements) — *measured_by*
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **L-Eval** (measurements) — *measured_by*
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  - [KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dd/li25dd.pdf)
- **ToxiGen** (measurements) — *measured_by*
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **WikiText** (measurements) — *measured_by*
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **PG-19** (measurements) — *measured_by*
  - [TokenSwift: Lossless Acceleration of Ultra Long Sequence Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25z/wu25z.pdf)
- **ASQA** (measurements) — *measured_by*
  > To the best of our knowledge, ASQA (Stelmakh et al., 2022) is the only dataset that falls into this category. (Section 4)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-OnlyLLMs](https://aclanthology.org/2025.emnlp-main.482.pdf)
- **CHAIR** (measurements) — *measured_by*
  - [Interpretation Meets Safety: A Survey on Interpretation Methods and Tools for ImprovingLLMSafety](https://aclanthology.org/2025.emnlp-main.1092.pdf)
- **LLaVA-Bench-in-the-Wild** (measurements) — *measured_by*
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)

### Associated with
- **Instruction following** (constructs)
  - [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
- **Self-consistency** (measurements)
  - [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf)
- **Length generalization** (constructs)
  - [DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f050fa9f0d898e3f265d515f50ae8f9-Paper-Conference.pdf)
- **Understanding** (constructs)
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [Unveiling Internal Reasoning Modes inLLMs: A Deep Dive into Latent Reasoning vs. Factual Shortcuts with Attribute Rate Ratio](https://aclanthology.org/2025.emnlp-main.112.pdf)
- **Disambiguation** (constructs)
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-OnlyLLMs](https://aclanthology.org/2025.emnlp-main.482.pdf)
