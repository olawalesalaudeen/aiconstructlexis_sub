# MedQA
**Type:** Measurement  
**Referenced in:** 38 papers  

## State of the Field

Across the provided literature, MedQA is consistently described as a benchmark dataset for medical question answering, composed of multiple-choice questions from or styled after the United States Medical Licensing Examination (USMLE). Its most prevalent use is to evaluate model capabilities in the medical domain, with papers frequently using it to measure `Medical question answering`, `Medical reasoning`, and `Domain-specific knowledge`. The operationalization of these constructs involves assessing model performance on the dataset's questions, which one paper describes as "clinical vignettes paired with multiple choice diagnosis questions" used to test the diagnostic reasoning construct. A smaller body of work employs MedQA to assess more general abilities like `Chain-of-thought reasoning` or specific methods such as `Retrieval-augmented generation` and `Zero-shot generalization`. Beyond direct evaluation, the dataset is also used as a source of few-shot examples for generation tasks and as a baseline for establishing the difficulty of other medical datasets. The data also indicates MedQA is included within the MIRAGE benchmark and its performance is tracked on the Open Medical LLM Leaderboard.

## Sources

**[From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf)**
> A dataset containing US Medical Licensing Examination (USMLE) questions used to evaluate model knowledge and reasoning in the medical domain.

## Relationships

### → MedQA
- **Medical question answering** (behaviors tasks) — *measured_by*
  > "MedQA (Jin et al., 2021) ... is a medical QA dataset from professional exams"
  - [DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf)
- **Domain-specific knowledge** (constructs) — *measured_by*
  > “we define five fundamental LLM capabilities, namely Mathematical Reasoning, Reading Comprehension, Commonsense Reasoning, Scientific Reasoning, and Professional Expertise”
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Medical reasoning** (constructs) — *measured_by*
  > Suppose we focus on diagnostic reasoning as the LLM capability of interest and use a benchmark like MedQA, which comprises clinical vignettes paired with multiple choice diagnosis questions, to test the diagnostic reasoning construct. (Section 3.1)
  - [Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf)
- **Domain knowledge** (constructs) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  > Figure 6: % of test hypotheses fully groundable after adding various microtheories (n-sized Random, Usage, QC, & PC Mts) to a base Corpus. ... MedQA Grounding Rate (%) of Test Hypotheses
  - [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5ec50eb177908f21f78ed0d76ed525c-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  > We use one dataset from each of these categories for fine-tuning the LLM and we use all the datasets to evaluate the effect of fine-tuning on the given dataset... i) MedQA (Jin et al., 2021): Multiple choice question answers from the United States Medical License Exams (USMLE)... (Section 4)
  - [LBC: Language-Based-Classifier for Out-Of-Variable Generalization](https://aclanthology.org/2025.naacl-long.584.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  > To evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three unseen KGQA datasets: FreebaseQA (Jiang et al., 2019), CSQA (Talmor et al., 2019) and MedQA (Jin et al., 2021). (Section 5.4)
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **Knowledge acquisition** (constructs) — *measured_by*
  > most medical benchmarks (Jin et al., 2021; Pal et al., 2022; Wang et al., 2024; Cai et al., 2024; Qiu et al., 2024) evaluate LLMs’ capabilities through question-answering (QA) tasks, which mainly focus on assessing LLMs’ preliminary knowledge grasp (Section 1)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **Knowledge graph question answering** (behaviors tasks) — *measured_by*
  > We evaluate KGQA benchmarks spanning different backbone KGs. ... MedQA (Jin et al., 2021) consists of questions extracted from USMLE exams. (Section 4.1)
  - [Social Bias in Multilingual Language Models: A Survey](https://aclanthology.org/2025.emnlp-main.1417.pdf)
