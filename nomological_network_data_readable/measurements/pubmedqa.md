# PubMedQA
**Type:** Measurement  
**Referenced in:** 38 papers  
**Also known as:** PubmedQA, Pubmedqa  

## State of the Field

Across the provided literature, PubMedQA is consistently characterized as a question-answering dataset designed for the biomedical domain, often based on research abstracts from PubMed. The instrument is most frequently used to measure `Medical question answering`, but also serves to evaluate `Text generation`, `Natural language inference`, `Contextual reasoning`, and general `Domain knowledge`. There is some variation in how the task format is described; the prevailing definition specifies answers are "yes/no/maybe and may require a long-form explanation," while a smaller number of papers describe it as requiring "long free-form answers" or as a "multiple-choice" task. Papers commonly employ PubMedQA as a held-out evaluation benchmark, particularly for assessing model performance on domain-specific or out-of-distribution data. Its application extends to testing the detection of machine-generated text in technical contexts. Additionally, it is used as a source for creating other benchmarks, as seen with the MedHallu dataset which is "derived from the established PubMedQA dataset".

## Sources

**[Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf) (as "PubmedQA")**
> A held-out question-answering benchmark used in the paper’s single-task finetuning comparisons.

**[Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf)**
> A question answering dataset designed for biomedical research questions, where answers are yes/no/maybe and may require a long-form explanation.

**[AreLLM-Judges Robust to Expressions of Uncertainty? Investigating the effect of Epistemic Markers onLLM-based Evaluation](https://aclanthology.org/2025.naacl-long.453.pdf) (as "Pubmedqa")**
> Biomedical multiple-choice question-answering dataset used to evaluate LLM performance on domain-specific long-tail knowledge in the medical field.

## Relationships

### → PubMedQA
- **Medical question answering** (behaviors tasks) — *measured_by*
  > "General IF data are sampled from Alpaca-GPT42, and medical data are sampled from PubMedQA (Jin et al., 2019) 3. The validation and testing datasets are derived from the validation and testing sets of PubMedQA."
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > Medical QA. We apply our method to medical question answering as target domain T... We use... PubMedQA (Jin et al., 2019), which contains approximately 200K QA pairs
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Domain knowledge** (constructs) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Shh, don't say that! Domain Certification in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/27befed4547edcb4bdeacef9472cadee-Paper-Conference.pdf)
- **Contextual reasoning** (constructs) — *measured_by*
  - [Reading between the Lines: CanLLMs Identify Cross-Cultural Communication Gaps?](https://aclanthology.org/2025.naacl-long.410.pdf)
- **Natural language inference** (behaviors tasks) — *measured_by*
  > For yes/no QA, we select PubMedQA (Jin et al., 2019), an English natural language inference task related to medical research papers. (Section 4.2)
  - [OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf)

### Associated with
- **MedHallu** (measurements)
  > MedHallu comprises 10,000 high-quality question-answer pairs derived from the established PubMedQA dataset.
  - [Ask Patients with Patience: EnablingLLMs for Human-Centric Medical Dialogue with Grounded Reasoning](https://aclanthology.org/2025.emnlp-main.143.pdf)
