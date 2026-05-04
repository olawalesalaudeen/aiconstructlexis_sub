# Retrieval-augmented generation
**Type:** Behavior  
**Referenced in:** 43 papers  
**Also known as:** Retrieval-augmented question answering, Generation with citations, Grounded question answering, Source-supported response generation, Chunk-level citation generation, Sentence-level citation generation, RAG  

## State of the Field

Retrieval-augmented generation (RAG) is predominantly described as a two-step behavior where a model first retrieves relevant information from an external knowledge source to augment its context, and then generates a response based on that augmented context. A common specialization of this behavior is retrieval-augmented question answering, with one paper equating open-domain question answering with RAG applications. While most definitions are general, a few papers frame RAG for specific domains, such as retrieving code examples for code generation. A distinct line of work emphasizes the verifiability of the output, defining related behaviors like "grounded question answering" and "source-supported response generation," which require the generated text to be "systematically entailed by" or "explicitly backed by" the provided documents. This focus on attribution is further operationalized through tasks like "sentence-level" and "chunk-level" citation generation. The behavior, particularly its grounded variant, is measured using benchmarks such as ARC and MedQA, where evaluation centers on a "Grounding Rate" of test hypotheses. The external knowledge source itself is variously described as a "non-parametric datastore," a "knowledge corpus," or knowledge chunks modeled as a graph. The emphasis on verifiability also connects the behavior to textual entailment.

## Sources

**[BioBridge: Bridging Biomedical Foundation Models via Knowledge Graphs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a5a9f5c15632e9f52c9c1ba4134f13c-Paper-Conference.pdf)**
> A generation process where a model first retrieves relevant information from an external knowledge source to augment its context before generating a response.

**[Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf) (as "Retrieval-augmented question answering")**
> The task of answering questions by first retrieving relevant information from an external knowledge source and then synthesizing an answer based on that information.

**[HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf) (as "Generation with citations")**
> The task of generating a long-form answer to a multi-faceted question and correctly attributing each sentence to the source passages provided in the context.

**[From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf) (as "Grounded question answering")**
> The observable behavior of providing an answer to a question while also showing how that answer is systematically entailed by a set of verifiable documents or facts.

**[Ward: Provable RAG Dataset Inference via LLM Watermarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9409aff8c8a430fd7db7c3ea7fdf581-Paper-Conference.pdf) (as "Source-supported response generation")**
> The observable behavior of generating text that is explicitly backed by information present in provided source documents.

**[SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25a/chuang25a.pdf) (as "Sentence-level citation generation")**
> Producing citations after individual response statements that reference specific sentences from the provided context.

**[SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25a/chuang25a.pdf) (as "Chunk-level citation generation")**
> The behavior of citing larger blocks of text, such as paragraphs, as evidence for a generated statement.

**[ReMedy: Learning Machine Translation Evaluation from Human Preferences with Reward Modeling](https://aclanthology.org/2025.emnlp-main.218.pdf) (as "RAG")**
> Retrieval-Augmented Generation, a method that retrieves relevant code examples from a database to enhance prompt context for code generation tasks.

## Relationships

### Retrieval-augmented generation →
- **Spec-Bench** (measurements) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [AISees YourLocation—But With A Bias Toward The Wealthy World](https://aclanthology.org/2025.emnlp-main.911.pdf)
- **ARC** (measurements) — *measured_by*
  > Figure 6: % of test hypotheses fully groundable after adding various microtheories (n-sized Random, Usage, QC, & PC Mts) to a base Corpus. ... ARC Grounding Rate (%) of Test Hypotheses
  - [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf)
- **MedQA** (measurements) — *measured_by*
  > Figure 6: % of test hypotheses fully groundable after adding various microtheories (n-sized Random, Usage, QC, & PC Mts) to a base Corpus. ... MedQA Grounding Rate (%) of Test Hypotheses
  - [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf)
- **HELMET** (measurements) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **LongBench v2** (measurements) — *measured_by*
  - [Graph World Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25p/feng25p.pdf)
- **DPR** (measurements) — *measured_by*
  - [polybasic Speculative Decoding Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25az/wang25az.pdf)
- **GPQA** (measurements) — *measured_by*
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1041.pdf)

### → Retrieval-augmented generation
- **Ranking** (behaviors tasks) — *correlates*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)

### Associated with
- **Multimodal question answering** (behaviors tasks)
  - [BioBridge: Bridging Biomedical Foundation Models via Knowledge Graphs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a5a9f5c15632e9f52c9c1ba4134f13c-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  - [Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  - [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf)
- **Distribution alignment** (constructs)
  - [Fine-grained Analysis of In-context Linear Estimation: Data, Architecture, and Beyond](https://proceedings.neurips.cc/paper_files/paper/2024/file/f9dc462382fef56d58279e75de2438f3-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.365.pdf)
- **Textual entailment** (behaviors tasks)
  - [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [Improving Model Evaluation usingSMARTFiltering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.236.pdf)
