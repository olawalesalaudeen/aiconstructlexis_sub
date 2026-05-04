# Hallucination detection
**Type:** Behavior  
**Referenced in:** 27 papers  
**Also known as:** Hallucination Detection, Knowledge conflict detection, Medical hallucination detection  

## State of the Field

Across the provided literature, hallucination detection is predominantly characterized as the observable task of identifying factually incorrect, fabricated, or unsupported information within a model's generated output. This is frequently applied in multi-modal settings, where the goal is to find inconsistencies between text and a source image, such as "tagging object phrases in a description that do not correspond to objects in the image" (Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions). The task is also specified for particular domains, including "Medical hallucination detection" and knowledge-grounded contexts, where it is framed as identifying sentences that contradict a reasoning graph. The field operationalizes this behavior using a range of benchmarks, with papers citing the use of HaluEval, POPE, TruthfulQA, and the domain-specific MedHallu to measure performance. Methodologically, approaches range from comparing outputs to a knowledge base to using a model's internal states, such as "contextual embeddings from intermediate layers" (Towards Quantifying Commonsense Reasoning with Mechanistic Insights). While the prevailing view is of an observable task, a less common framing describes it as a "latent ability" of a model to recognize unsupported content. Hallucination detection is studied in relation to concepts like "Consistency" and "Semantic uncertainty" and is considered relevant across tasks like "Question answering" and "Text summarization." One paper title also suggests that "Self-reflection" can be used to perform this task.

## Sources

**[Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Hallucination Detection")**
> The observable task of identifying and tagging object phrases in a description that do not correspond to objects in the image.

**[Hallo3D: Multi-Modal Hallucination Detection and Mitigation for Consistent 3D Content Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/d75660d6eb0ce31360c768fef85301dd-Paper-Conference.pdf)**
> The task of using a large multi-modal model to identify and describe concrete hallucinations or inconsistencies within a rendered 2D image.

**[Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf) (as "Knowledge conflict detection")**
> Identifying explanation sentences that contradict or are unsupported by comparison triples from the reasoning graph.

**[Ask Patients with Patience: EnablingLLMs for Human-Centric Medical Dialogue with Grounded Reasoning](https://aclanthology.org/2025.emnlp-main.143.pdf) (as "Medical hallucination detection")**
> The observable task of judging whether a given answer to a medical question is hallucinated (factually incorrect) or not, based on factual accuracy.

## Relationships

### Hallucination detection →
- **HaluEval** (measurements) — *measured_by*
  > "First we evaluate a model’s ability to judge whether an answer to a question contains a hallucination or not using the HaluEval dataset"
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
- **AUROC** (measurements) — *measured_by*
  - [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf)
- **POPE** (measurements) — *measured_by*
  > Specifically, we assess our method’s performance in hallucination detection using the POPE dataset (Li et al., 2023c) and HallusionBench (Guan et al., 2023). (Section 4.1)
  - [(Almost) Free Modality Stitching of Foundation Models](https://aclanthology.org/2025.emnlp-main.1002.pdf)
- **Linear probing** (measurements) — *measured_by*
  - [MeNTi: Bridging Medical Calculator andLLMAgent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.264.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > On the challenging TruthfulQA benchmark (Lin et al., 2022a), our approach achieves a significant +12.8% improvement in hallucination detection accuracy (AUROC) compared to state-of-the-art methods. (Section 1. Introduction)
  - [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf)
- **MedHallu** (measurements) — *measured_by*
  > To address this, we introduce MedHallu, one of the first benchmark specifically designed for medical hallucination detection.
  - [Ask Patients with Patience: EnablingLLMs for Human-Centric Medical Dialogue with Grounded Reasoning](https://aclanthology.org/2025.emnlp-main.143.pdf)
- **NegHalu** (measurements) — *measured_by*
  > we conduct this analysis by reconstructing existing hallucination detection benchmarks with negated expressions and introducing NegHalu, a dataset in which hallucination labels are newly assigned to account for the effects of negation.
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **Logit lens** (measurements) — *measured_by*
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)

### → Hallucination detection
- **Self-reflection** (behaviors tasks) — *causes*
  - [2025.emnlp-main.1063.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1063.checklist.pdf)

### Associated with
- **Semantic uncertainty** (constructs)
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.158.pdf)
- **SelfCheckGPT** (measurements)
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.158.pdf)
- **Question answering** (behaviors tasks)
  > We demonstrate that the influence of negated text on hallucination detection extends across multiple tasks, including question answering (QA), dialogue, summarization, and completion, indicating its task-agnostic.
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **Text summarization** (behaviors tasks)
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **Text generation** (behaviors tasks)
  > We demonstrate that the influence of negated text on hallucination detection extends across multiple tasks, including question answering (QA), dialogue, summarization, and completion, indicating its task-agnostic.
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **Consistency** (constructs)
  - [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf)
- **FoCus** (measurements)
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.158.pdf)
- **Refusal to answer** (behaviors tasks)
  > The hallucination detection task aims to test the model’s ability to decline answering questions that are not mentioned in the given context. (Section 3.2)
  - [LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dv/li25dv.pdf)
