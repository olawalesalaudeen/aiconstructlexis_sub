# Medical visual question answering
**Type:** Behavior  
**Referenced in:** 9 papers  

## State of the Field

Across the provided literature, medical visual question answering (MedVQA or MVQA) is consistently defined as a task requiring a model to answer questions about medical images by processing both visual and textual inputs. The dominant framing, as one paper notes, is that the model must generate answers that "integrate textual questions and visual context" (FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection). While the core definition is stable, some sources add nuance, specifying that the task can range from "simple pattern recognition to complex diagnostic reasoning" (Visual and Domain Knowledge for Professional-level Graph-of-Thought Medical Reasoning) and may involve both open-ended and closed-form answers. This behavior is operationalized and measured using several benchmarks. The most frequently cited datasets for evaluating this task are VQA-RAD and SLAKE. Other instruments mentioned include PathVQA, MIMIC-CXR, and IU-Xray. One paper provides a specific example of operationalization, noting that SLAKE evaluates the task using "chest X-ray test samples with close-ended questions in English." The visual question-answering format is described as a common structure for many medical datasets used to evaluate large vision-language models.

## Sources

**[FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Answering questions about medical images using both visual and textual inputs.

## Relationships

### Medical visual question answering →
- **VQA-RAD** (measurements) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M. (Section 4.1)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **SLAKE** (measurements) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M. (Section 4.1)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **PathVQA** (measurements) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M. (Section 4.1)
  - [MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf)
- **MIMIC-CXR** (measurements) — *measured_by*
  > "We utilize five medical vision-language datasets for medical VQA and report generation tasks, i.e., MIMIC-CXR (Johnson et al., 2019), IU-Xray (Demner-Fushman et al., 2016), Harvard-FairVLMed (Luo et al., 2024), PMC-OA (Lin et al., 2023a) (we only select the pathology part) and Quilt-1M (Ikezogwo et al., 2024)."
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
- **IU-Xray** (measurements) — *measured_by*
  > "We utilize five medical vision-language datasets for medical VQA and report generation tasks, i.e., MIMIC-CXR (Johnson et al., 2019), IU-Xray (Demner-Fushman et al., 2016), Harvard-FairVLMed (Luo et al., 2024), PMC-OA (Lin et al., 2023a) (we only select the pathology part) and Quilt-1M (Ikezogwo et al., 2024)."
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
- **PMC-VQA** (measurements) — *measured_by*
  - [Is In-Context Learning a Type of Error-Driven Learning? Evidence from the Inverse Frequency Effect in Structural Priming](https://aclanthology.org/2025.naacl-long.587.pdf)
