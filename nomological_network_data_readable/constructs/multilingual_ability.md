# Multilingual ability
**Type:** Construct  
**Referenced in:** 83 papers  
**Also known as:** Multilingual capability, Multilinguality, Multilingual performance, Cross-lingual linguistic capabilities, Bilingual ability, Multilingual proficiency, Multilingualism, Multilingual capabilities, Multi-lingual abilities  

## State of the Field

Across the provided literature, multilingual ability is predominantly defined as a model's latent capacity to understand and generate content across multiple languages, with terms like "multilinguality" and "multilingual capability" used interchangeably. While this core definition is widely shared, some papers offer more specific framings, such as the ability to transfer grammatical rules between languages ("cross-lingual linguistic capabilities") or a narrow focus on two languages for a specific domain ("bilingual ability"). This construct is most commonly operationalized and measured through performance on a range of benchmarks, including TyDiQA and MIRACL for question answering and retrieval, WMT16 for translation, and MMBench for vision-language tasks. A recurring theme is the performance disparity between high-resource and underrepresented languages, with one paper noting the need to ensure that model compression "does not disproportionately harm performance in non-English languages." Some work also distinguishes linguistic skill from cultural understanding, cautioning that evaluation on translation alone could "risk overestimation of an LMM’s multilingual capability without truly understanding the context of the individual cultures." The concept is frequently studied alongside zero-shot cross-lingual transfer, catastrophic forgetting, and grammatical error correction.

## Sources

**[HyperFM: Fact-Centric Multimodal Fusion for Link Prediction over Hyper-Relational Knowledge Graphs](https://aclanthology.org/2025.acl-long.143.pdf)**
> The latent capacity of a model to understand and generate content across multiple languages, encompassing both language understanding and language fidelity in vision-language contexts.

**[SGIC: A Self-Guided Iterative Calibration Framework forRAG](https://aclanthology.org/2025.acl-long.1377.pdf) (as "Multilingual capability")**
> The ability of a model to understand and generate text across a diverse range of languages and writing systems.

**[VLSBench](https://aclanthology.org/2025.acl-long.406.pdf) (as "Multilinguality")**
> The ability to understand and reason using textual information in languages other than English, particularly when such content is essential to resolving a query.

**[Leveraging Text-to-Text Transformers as Classifier Chain for Few-Shot Multi-Label Classification](https://aclanthology.org/2025.emnlp-main.1369.pdf) (as "Multilingual performance")**
> The latent ability of a model to maintain strong language understanding and task performance across multiple languages, particularly balancing performance between high-resource and underrepresented languages.

**[JUDGEBERT: Assessing Legal Meaning Preservation Between Sentences](https://aclanthology.org/2025.emnlp-main.6.pdf) (as "Cross-lingual linguistic capabilities")**
> The ability of a multilingual model to transfer linguistic knowledge across languages, particularly in understanding and applying grammatical rules from one language to another.

**[Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf) (as "Bilingual ability")**
> The capacity to operate in both English and Chinese for medical vision-language tasks, including report generation and question answering.

**[MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf) (as "Multilingual proficiency")**
> The model's capability to understand and process information in multiple languages.

**[Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.303.pdf) (as "Multilingualism")**
> The ability to understand, generate, and reason in multiple languages while preserving meaning, cultural nuance, and grammatical correctness.

**[Co-EvolvingLLMs and Embedding Models via Density-Guided Preference Optimization for Text Clustering](https://aclanthology.org/2025.emnlp-main.242.pdf) (as "Multilingual capabilities")**
> The ability of a model to perform effectively across a diverse range of tasks and languages beyond English.

**[Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Multi-lingual abilities")**
> The capability of a model to understand and perform tasks across multiple languages within the online shopping domain.

## Relationships

### Multilingual ability →
- **TyDiQA** (measurements) — *measured_by*
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WMT16** (measurements) — *measured_by*
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
- **TyDi QA** (measurements) — *measured_by*
  - [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf)
- **MBXP** (measurements) — *measured_by*
  - [The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/9aa4e5caaf6d62767787500ee487c7fb-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [MetaDesigner: Advancing Artistic Typography through AI-Driven, User-Centric, and Multilingual WordArt Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/a10c3d85879c29331ba4d73ede56c7d3-Paper-Conference.pdf)
- **Belebele** (measurements) — *measured_by*
  - [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://aclanthology.org/2025.acl-long.1406.pdf)
- **M-MMLU** (measurements) — *measured_by*
  - [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://aclanthology.org/2025.acl-long.1406.pdf)
- **MIRACL** (measurements) — *measured_by*
  > Our main evaluations are conducted on BEIR (Thakur et al., 2021) and MIRACL (Zhang et al., 2023), to assess the generalization of dense retrievers and multilingual retrieval capability. (Section 4.5).
  - [VISA: Retrieval Augmented Generation with Visual Source Attribution](https://aclanthology.org/2025.acl-long.1457.pdf)
- **WildChat** (measurements) — *measured_by*
  - [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf)
- **MMBench** (measurements) — *measured_by*
  - [Parrot: Multilingual Visual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25ad/sun25ad.pdf)
- **NOVA-63** (measurements) — *measured_by*
  - [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.364.pdf)

### → Multilingual ability
- **Representation alignment** (constructs) — *causes*
  - [from Benign import Toxic: Jailbreaking the Language Model via Adversarial Metaphors](https://aclanthology.org/2025.acl-long.239.pdf)

### Associated with
- **Expert specialization** (constructs)
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **Societal bias** (constructs)
  - [Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf)
- **Grammatical error correction** (behaviors tasks)
  - [Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning](https://aclanthology.org/2025.naacl-long.251.pdf)
- **Knowledge transferability** (constructs)
  - [FoREST: Frame of Reference Evaluation in Spatial Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [Neutral residues: revisiting adapters for model extension](https://raw.githubusercontent.com/mlresearch/v267/main/assets/talla25a/talla25a.pdf)
- **Zero-shot cross-lingual transfer** (behaviors tasks)
  > “we investigate the role of multilinguality in cross-lingual transfer”
  - [2025.emnlp-main.1773.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1773.checklist.pdf)
