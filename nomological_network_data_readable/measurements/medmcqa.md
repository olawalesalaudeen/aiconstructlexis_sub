# MedMCQA
**Type:** Measurement  
**Referenced in:** 39 papers  

## State of the Field

Across the surveyed literature, MedMCQA is consistently characterized as a multiple-choice question answering benchmark for the medical domain. Its most frequent application is to assess domain-specific knowledge and reasoning, operationalizing the evaluation of behaviors like medical question answering and constructs such as knowledge acquisition. Several papers specify its composition, noting it is a 4-way multiple-choice dataset derived from Indian medical school entrance exams, particularly the AIIMS and NEET. While its primary focus is on medical knowledge, it is also used more broadly to evaluate general text generation and question answering capabilities. Some work also applies it to measure more specific constructs like chain-of-thought reasoning and faithfulness. A less common application appears in one study, which uses MedMCQA to probe answer-confidence prediction. The benchmark is frequently included in larger evaluation suites, such as the MIRAGE benchmark, alongside other knowledge-intensive tasks.

## Sources

**[Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf)**
> MedMCQA is a medical multiple-choice question answering benchmark used to assess medical knowledge and reasoning.

## Relationships

### → MedMCQA
- **Medical question answering** (behaviors tasks) — *measured_by*
  - [DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
- **Domain knowledge** (constructs) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Domain-specific knowledge** (constructs) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  > We use one dataset from each of these categories for fine-tuning the LLM and we use all the datasets to evaluate the effect of fine-tuning on the given dataset... ii) MedMCQA (Pal et al., 2022): Multiple choice question answers from the All India Institute of Medical Sciences (AIIMS) and National Eligibility cum Entrance Exam (NEET)... (Section 4)
  - [LBC: Language-Based-Classifier for Out-Of-Variable Generalization](https://aclanthology.org/2025.naacl-long.584.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **Knowledge acquisition** (constructs) — *measured_by*
  > most medical benchmarks (Jin et al., 2021; Pal et al., 2022; Wang et al., 2024; Cai et al., 2024; Qiu et al., 2024) evaluate LLMs’ capabilities through question-answering (QA) tasks, which mainly focus on assessing LLMs’ preliminary knowledge grasp (Section 1)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
