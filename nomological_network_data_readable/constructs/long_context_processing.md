# Long-context processing
**Type:** Construct  
**Referenced in:** 21 papers  
**Also known as:** Long-context capability, Long-context comprehension, Long-context modeling, Long-context processing ability, Long-text comprehension  

## State of the Field

Across the surveyed literature, long-context processing is consistently defined as a model's latent ability to handle, comprehend, and utilize information from extended input sequences. Definitions vary slightly in terminology, using phrases like 'long-context comprehension,' 'long-text processing,' and 'long-context capability,' but converge on the core idea of integrating information distributed throughout a document rather than from isolated segments. One definition extends this to multimodal contexts, involving both visual and textual inputs. This construct is operationalized and measured through a wide range of benchmarks, with LongBench, RULER, InfiniteBench, and the Needle-in-a-haystack test being the most frequently used evaluation instruments. A broader set of tools, including L-Eval, PG-19, and various question-answering and language modeling datasets, are also employed to assess this ability. For instance, the MMNeedle benchmark is specifically cited for evaluating this capability in multimodal models by requiring retrieval of a 'sub-image (needle) from long-context images (haystack)'. The construct is studied in relation to other capabilities such as information retrieval, complex reasoning, and length generalization. Some work also explores directional relationships, suggesting it is influenced by coreference resolution and can, in turn, affect programming ability.

## Sources

**[Aligning Sentence Simplification withESLLearner’s Proficiency for Language Acquisition](https://aclanthology.org/2025.naacl-long.22.pdf) (as "Long-context modeling")**
> The ability of a model to process and utilize information from very long documents or contexts to perform a task.

**[Entangled Relations: LeveragingNLIand Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.166.pdf) (as "Long-context capability")**
> The latent ability of a multimodal large language model to understand and effectively process extended sequences of visual and textual inputs, maintaining performance as context length increases.

**[AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf) (as "Long-text comprehension")**
> The latent ability of a model to understand and process information across extended input sequences, maintaining coherence and extracting relevant details over long contexts.

**[Are We Done withMMLU?](https://aclanthology.org/2025.naacl-long.263.pdf)**
> The capacity to extract relevant information from lengthy and complex input contexts, such as detailed patient case histories, to support accurate parameter extraction and decision-making.

**[CAMIEval: EnhancingNLGEvaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.439.pdf) (as "Long-context comprehension")**
> The latent ability of a model to understand and integrate information distributed throughout an extended input context, rather than relying on isolated segments.

**[Reading between the Lines: CanLLMs Identify Cross-Cultural Communication Gaps?](https://aclanthology.org/2025.naacl-long.410.pdf) (as "Long-context processing ability")**
> The model's latent capability to effectively handle, integrate, and utilize information from very long sequences of input text.

**[LLM-guided Plan and Retrieval: A Strategic Alignment for Interpretable User Satisfaction Estimation in Dialogue](https://aclanthology.org/2025.naacl-long.524.pdf) (as "Long-context understanding")**
> The ability of a model to process, comprehend, and utilize information from extended input sequences that exceed its standard context window.

## Relationships

### Long-context processing →
- **LongBench** (measurements) — *measured_by*
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **RULER** (measurements) — *measured_by*
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **PG-19** (measurements) — *measured_by*
  - [Reading between the Lines: CanLLMs Identify Cross-Cultural Communication Gaps?](https://aclanthology.org/2025.naacl-long.410.pdf)
- **Needle-in-a-haystack test** (measurements) — *measured_by*
  - [DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c1ddd2e59df46fd2aa85c833b1b36ed-Paper-Conference.pdf)
- **L-Eval** (measurements) — *measured_by*
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **NarrativeQA** (measurements) — *measured_by*
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **Multi-Needle-in-a-Haystack** (measurements) — *measured_by*
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **RACE** (measurements) — *measured_by*
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)
- **WikiText-103** (measurements) — *measured_by*
  - [Reading between the Lines: CanLLMs Identify Cross-Cultural Communication Gaps?](https://aclanthology.org/2025.naacl-long.410.pdf)
- **WikiText-2** (measurements) — *measured_by*
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)

### → Long-context processing
- **Knowledge forgetting** (constructs) — *causes*
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)

### Associated with
- **Length generalization** (constructs)
  - [Long-Short Alignment for Effective Long-Context Modeling in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25a/du25a.pdf)
- **Information retrieval** (behaviors tasks)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks)
  - [Are We Done withMMLU?](https://aclanthology.org/2025.naacl-long.263.pdf)
- **Long-context understanding** (constructs)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **Video understanding** (constructs)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Multimodal understanding** (constructs)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Short-context capability** (constructs)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [CAMIEval: EnhancingNLGEvaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.439.pdf)
- **Logical reasoning** (constructs)
  - [CAMIEval: EnhancingNLGEvaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.439.pdf)
- **Reasoning** (constructs)
  - [Beyond Logits: Aligning Feature Dynamics for Effective Knowledge Distillation](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Code generation** (behaviors tasks)
  - [Beyond Logits: Aligning Feature Dynamics for Effective Knowledge Distillation](https://aclanthology.org/2025.acl-long.1126.pdf)
- **State tracking** (constructs)
  - [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beck25b/beck25b.pdf)
- **Complex reasoning** (behaviors tasks)
  - [SpeculatingLLMs’Chinese Training Data Pollution from Their Tokens](https://aclanthology.org/2025.emnlp-main.1328.pdf)
