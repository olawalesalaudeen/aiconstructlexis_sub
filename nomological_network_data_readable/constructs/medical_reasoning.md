# Medical reasoning
**Type:** Construct  
**Referenced in:** 21 papers  
**Also known as:** Diagnostic reasoning  

## State of the Field

Across the surveyed literature, "medical reasoning" is most commonly defined as the ability to perform complex, domain-specific reasoning and inference to support medical analysis and diagnostic tasks. The terms "clinical reasoning" and "diagnostic reasoning" are also frequently used, with definitions that overlap but sometimes carry specific nuances. For instance, some work frames "clinical reasoning" as an interactive process involving information-seeking for medical decision-making, while other papers focus on "diagnostic reasoning" as the specific cognitive ability to infer a diagnosis from patient data, explicitly distinguishing it from "mere factual recall or pattern matching" ("Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity"). A smaller set of studies also describes it as a multimodal capability that integrates "clinical visual perception with professional-level medical knowledge" ("Visual and Domain Knowledge for Professional-level Graph-of-Thought Medical Reasoning"). This construct is operationalized and measured using several benchmarks. The most frequently mentioned instrument is MedQA, which is described as comprising "clinical vignettes paired with multiple choice diagnosis questions" and is used "to test the diagnostic reasoning construct." Other benchmarks reported to measure medical reasoning include DDXPlus and MOLERR2FIX. The construct is also studied in relation to interpretability and explainability.

## Sources

**[Biomedical Visual Instruction Tuning with Clinician Preference Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec33ab89b5986605cd7c331396e7e5c-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The ability to perform complex, domain-specific reasoning and inference to support medical analysis and diagnostic tasks.

**[MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf) (as "Clinical reasoning")**
> The cognitive process of analyzing patient information, identifying knowledge gaps, and integrating new evidence to arrive at a medical diagnosis or decision.

**[MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Diagnostic reasoning")**
> The cognitive ability to analyze patient information, consider differential diagnoses, and arrive at a likely medical diagnosis.

## Relationships

### Medical reasoning →
- **MedQA** (measurements) — *measured_by*
  > Suppose we focus on diagnostic reasoning as the LLM capability of interest and use a benchmark like MedQA, which comprises clinical vignettes paired with multiple choice diagnosis questions, to test the diagnostic reasoning construct. (Section 3.1)
  - [Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf)
- **DDXPlus** (measurements) — *measured_by*
  - [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf)
- **MOLERR2FIX** (measurements) — *measured_by*
  - [Mitigating Hallucinations inLM-BasedTTSModels via Distribution Alignment UsingGFlowNets](https://aclanthology.org/2025.emnlp-main.977.pdf)

### Associated with
- **Interpretability and explainability** (constructs)
  - [DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/892850bf793e03b5c410dfd9425b94c8-Paper-Datasets_and_Benchmarks_Track.pdf)
