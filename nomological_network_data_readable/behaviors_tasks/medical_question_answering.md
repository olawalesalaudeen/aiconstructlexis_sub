# Medical question answering
**Type:** Behavior  
**Referenced in:** 38 papers  
**Also known as:** Biomedicine inquiry answering, Answering medical questions, Biomedical question answering  

## State of the Field

Across the surveyed literature, medical question answering is most commonly defined as the observable task of responding to questions within biomedical research and clinical contexts. A few papers offer alternative framings, with one defining it more narrowly as retrieving entities like drugs or diseases from a knowledge base, and others describing it as the general action of an LLM providing responses on medical knowledge or patient care. This behavior is operationalized and measured through a range of domain-specific benchmarks. The most frequently used instruments are MedQA, which is based on professional medical exams, and PubMedQA, which is derived from biomedical research literature. Evaluation formats vary, encompassing multiple-choice questions based on "clinical vignettes" as well as open-ended formats, for which frameworks like MinosEval are sometimes used. Other benchmarks cited for measuring this behavior include MedMCQA, MMLU, MMCU-Medical, and CMB-Exam. The task is studied in contexts ranging from domain-specific fine-tuning to the development of medical chatbots.

## Sources

**[LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)**
> The observable task of answering questions related to biomedical research and clinical contexts.

**[STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Biomedicine inquiry answering")**
> The task of retrieving entities such as drugs, diseases, or genes from a biomedical knowledge base to answer complex questions.

**[MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3ac952d0264ef7a505393868a70a46b6-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Answering medical questions")**
> The observable action of an LLM providing responses to queries regarding medical knowledge or patient care.

**[BannerAgency: Advertising Banner Design with MultimodalLLMAgents](https://aclanthology.org/2025.emnlp-main.215.pdf) (as "Biomedical question answering")**
> The observable task of answering questions related to biology and medicine, often requiring specialized domain knowledge.

## Relationships

### Medical question answering →
- **MedQA** (measurements) — *measured_by*
  > "MedQA (Jin et al., 2021) ... is a medical QA dataset from professional exams"
  - [DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf)
- **PubMedQA** (measurements) — *measured_by*
  > "General IF data are sampled from Alpaca-GPT42, and medical data are sampled from PubMedQA (Jin et al., 2019) 3. The validation and testing datasets are derived from the validation and testing sets of PubMedQA."
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **MedMCQA** (measurements) — *measured_by*
  - [DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > we use Google Translate to translate the questions and answers from the medical-clinical section of the MMLU dataset (Section 3.1.2).
  - [Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1551c01d7a3d0bf21e2518331e9f7074-Paper-Conference.pdf)
- **MMLU-Med** (measurements) — *measured_by*
  - [SALAD: Improving Robustness and Generalization through Contrastive Learning with Structure-Aware andLLM-Driven Augmented Data](https://aclanthology.org/2025.naacl-long.635.pdf)
- **MMCU-Medical** (measurements) — *measured_by*
  > Our experiments are conducted on two multi-task medical datasets MMCU-Medical (Zeng, 2023) and CMB-Exam (Wang et al., 2023b), and one open-domain Q&A medical dataset CMB-Clin (Wang et al., 2023b). (Section 6.1)
  - [Croppable Knowledge Graph Embedding](https://aclanthology.org/2025.acl-long.580.pdf)
- **CMB-Exam** (measurements) — *measured_by*
  > Our experiments are conducted on two multi-task medical datasets MMCU-Medical (Zeng, 2023) and CMB-Exam (Wang et al., 2023b), and one open-domain Q&A medical dataset CMB-Clin (Wang et al., 2023b). (Section 6.1)
  - [Croppable Knowledge Graph Embedding](https://aclanthology.org/2025.acl-long.580.pdf)
- **CMB-Clin** (measurements) — *measured_by*
  > Our experiments are conducted on two multi-task medical datasets MMCU-Medical (Zeng, 2023) and CMB-Exam (Wang et al., 2023b), and one open-domain Q&A medical dataset CMB-Clin (Wang et al., 2023b). (Section 6.1)
  - [Croppable Knowledge Graph Embedding](https://aclanthology.org/2025.acl-long.580.pdf)
- **MinosEval** (measurements) — *measured_by*
  > To address the limitations of traditional metrics for open-ended medical consultation tasks, we adopt MinosEval (Fan et al., 2025), a framework for evaluating medical question answering. (Section 4.2)
  - [Quantized but Deceptive? A Multi-Dimensional Truthfulness Evaluation of QuantizedLLMs](https://aclanthology.org/2025.emnlp-main.1549.pdf)
