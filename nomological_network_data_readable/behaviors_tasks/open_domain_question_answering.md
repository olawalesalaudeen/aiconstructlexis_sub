# Open-domain question answering
**Type:** Behavior  
**Referenced in:** 48 papers  
**Also known as:** Long-context question answering, Long-document question answering  

## State of the Field

Across the surveyed literature, open-domain question answering is most commonly defined as the task of answering questions about a wide range of topics, not limited to a specific domain. A recurring theme in its conceptualization is the need to find and synthesize information from an external source, with papers describing it as leveraging a large corpus of documents or using "retrieved documents as in-context evidence." To operationalize this behavior, researchers frequently employ a set of established benchmarks, with TriviaQA, Natural Questions, WebQuestions, and PopQA being the most cited instruments in this dataset. While the general definition is broad, a few papers specify that the expected answer is "typically a short phrase or sentence." A smaller body of work defines related sub-tasks, such as "long-document question answering," which focuses on integrating information from long texts and is measured by benchmarks like HELMET. Another variant, "open-ended question answering," is used to assess whether models provide incorrect answers or refuse to respond. Some studies also use open-domain QA settings to investigate model behavior when parametric knowledge conflicts with provided context.

## Sources

**[BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)**
> The task of answering questions about a wide range of topics, not limited to a specific domain or context.

**[SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25a/chuang25a.pdf) (as "Long-context question answering")**
> Generating multi-statement answers to queries based on long input contexts, with each statement supported by sentence-level citations.

**[NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf) (as "Long-document question answering")**
> Answering questions that require extracting and integrating information from long documents.

**[Towards Statistical Factuality Guarantee for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.577.pdf) (as "Open-ended question answering")**
> Generating free-form textual responses to questions about specific facts, used to assess whether models provide incorrect answers (obfuscation) or refuse to respond (unlearning).

## Relationships

### Open-domain question answering →
- **TriviaQA** (measurements) — *measured_by*
  > Finally, we apply our method to open-domain QA using the TriviaQA (Joshi et al., 2017) dataset.
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  > To thoroughly evaluate model performance across both in-domain (ID) and out-of-domain (OOD) settings, we construct a diverse benchmark suite spanning a range of open-domain QA challenges. For in-domain evaluation, we include the dev sets of NQ... (Section 4.2.1)
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
- **WebQuestions** (measurements) — *measured_by*
  > Moreover, in order to examine ToG on more generic tasks, we also prepare one open-domain QA dataset: WebQuestions (Berant et al., 2013);
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
- **PopQA** (measurements) — *measured_by*
  > Short-form generations tasks include two open-domain question answering (QA) datasets, PopQA (Mallen et al., 2023) and TriviaQA-unfiltered (Joshi et al., 2017)... (Section 4.1)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **NarrativeQA** (measurements) — *measured_by*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **TriviaQA-unfiltered** (measurements) — *measured_by*
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf)
- **AmbigNQ** (measurements) — *measured_by*
  - [SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
- **HELMET** (measurements) — *measured_by*
  > The evaluation spans five task types from the HELMET benchmark: synthetic recall, retrieval-augmented generation (RAG), many-shot in-context learning (ICL), passage re-ranking, and long-document QA, covering a total of 17 sub-tasks. (Section 4.1. Evaluation)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **MSMARCO** (measurements) — *measured_by*
  - [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf)
- **RULER** (measurements) — *measured_by*
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
- **NaturalQA** (measurements) — *measured_by*
  > We experiment on two tasks using four English datasets: (1) open-domain question answering, including TriviaQA (Joshi et al., 2017), NaturalQA (Kwiatkowski et al., 2019), and PopQA (Mallen et al., 2023); (Section 4.1)
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.365.pdf)
