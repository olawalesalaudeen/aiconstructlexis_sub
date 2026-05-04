# Medical diagnosis
**Type:** Behavior  
**Referenced in:** 15 papers  
**Also known as:** Disease Prediction, Differential diagnosis, Lung opacity detection, COVID-19 detection, ECG abnormal detection, Enlarged cardiomediastinum detection, Diagnosis classification, Diagnosis prediction, New diagnosis assignment, Freezing of gait detection, Arrhythmia diagnosis, Full-path clinical diagnosis, Phenotype prediction, Pathology detection, Seizure detection  

## State of the Field

Across the surveyed literature, medical diagnosis is most commonly framed as a predictive classification task based on patient data. This broad operationalization includes predicting a primary diagnosis from a clinical note, identifying which of a predefined set of conditions are present, or performing binary classification on medical signals and images, such as detecting lung opacity in radiographs or arrhythmias in ECG signals. A smaller set of studies conceptualizes it as a more complex reasoning process. For instance, some papers define it as "differential diagnosis," which involves generating a list of possible conditions to mimic a physician's process, while one paper describes a "full-path clinical diagnosis" task that "simulates a real-world diagnostic process" of sequential information gathering. To measure this behavior, researchers employ datasets such as MIMIC-III, MIMIC-IV, and the DDXPlus benchmark. On these datasets, tasks include predicting future medical codes, identifying phenotypes, and engaging in full-path diagnostic scenarios. The ability to perform medical diagnosis is reported to be influenced by constructs like semantic understanding and temporal reasoning, and the more complex version of the task is studied alongside problem-solving.

## Sources

**[MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Disease Prediction")**
> Inferring the patient's disease or diagnosis based on available medical information.

**[MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf) (as "Differential diagnosis")**
> The observable task of generating a list of possible medical conditions that could explain a given set of patient symptoms and clinical data.

**[FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Lung opacity detection")**
> Classifying chest radiographs as showing lung opacity or normal.

**[FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "COVID-19 detection")**
> A classification task to determine from an X-ray image whether a patient has symptoms indicative of COVID-19.

**[FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "ECG abnormal detection")**
> Classifying ECG signals as abnormal or normal.

**[FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Enlarged cardiomediastinum detection")**
> Classifying chest radiographs for the likelihood of enlarged cardiomediastinum.

**[Instruction Tuning Large Language Models to Understand Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/62986e0a78780fe5f17b495aeded5bab-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Diagnosis classification")**
> The clinical predictive task of identifying which of a predefined set of acute care conditions are present for a patient based on their admission data.

**[StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Selecting a diagnosis from a fixed set based on a patient profile and symptoms.

**[DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/892850bf793e03b5c410dfd9425b94c8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Diagnosis prediction")**
> Predicting the patient’s primary discharge diagnosis from a clinical note, optionally with external knowledge.

**[Multimodal Medical Code Tokenizer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25b/su25b.pdf) (as "Phenotype prediction")**
> Identifying the specific clinical manifestation or subtype of a disease based on a patient's medical history.

**[Multimodal Medical Code Tokenizer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25b/su25b.pdf) (as "New diagnosis assignment")**
> Predicting the first occurrence of a disease diagnosis in a patient's record based on longitudinal health data.

**[Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf) (as "Arrhythmia diagnosis")**
> Identifying abnormal heart rhythms from ECG signals, distinguishing between normal and various types of arrhythmic heartbeats.

**[Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf) (as "Freezing of gait detection")**
> Detecting episodes where Parkinson’s disease patients experience sudden inability to move while walking, using multimodal physiological and motion signals.

**[Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf) (as "Full-path clinical diagnosis")**
> The task of simulating a real-world diagnostic process by sequentially ordering examinations, integrating information from results, and arriving at a final diagnosis.

**[CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25b/dai25b.pdf) (as "Disease diagnosis")**
> The observable task of identifying a specific disease or medical condition from a patient's clinical data.

**[EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf) (as "Pathology detection")**
> The observable task of classifying an EEG recording as either normal or containing pathological abnormalities.

**[EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf) (as "Seizure detection")**
> The observable task of classifying a segment of an EEG recording as containing either seizure or background activity.

## Relationships

### Medical diagnosis →
- **MIMIC-IV** (measurements) — *measured_by*
  > The evaluation encompasses five tasks: 1 mortality prediction (MT), 2 readmission prediction (RA), 3 length-of-stay prediction (LOS), 4 phenotype prediction (Pheno), and 5 drug recommendation (DrugRec). ... Table 3 presents the AUPRC values for each baseline and their integration with our MEDTOK for five tasks in two in-patient datasets. (Section 4)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)
- **DDXPlus** (measurements) — *measured_by*
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MIMIC-III** (measurements) — *measured_by*
  > The evaluation encompasses five tasks: 1 mortality prediction (MT), 2 readmission prediction (RA), 3 length-of-stay prediction (LOS), 4 phenotype prediction (Pheno), and 5 drug recommendation (DrugRec). ... Table 3 presents the AUPRC values for each baseline and their integration with our MEDTOK for five tasks in two in-patient datasets. (Section 4)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)

### → Medical diagnosis
- **Semantic understanding** (constructs) — *causes*
  > Recent advancements in Language Models (LMs) have demonstrated their potential to address the few-shot learning problem by incorporating the semantic understanding of medical concepts (Section 1).
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)
- **Temporal reasoning** (constructs) — *causes*
  > Furthermore, in the box-aware diagnosis prediction module, an evolve-and-memorize patient box learning mechanism is proposed to model the temporal dynamics of patient visits, and a volume-based similarity measurement is proposed to enable accurate diagnosis prediction (Abstract).
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)
- **Multimodal alignment** (constructs) — *causes*
  - [EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf)

### Associated with
- **Problem-solving** (behaviors tasks)
  > For High-Level tasks (f3), we follow Hager et al. (2024) and assess LLMs’ capabilities of solving scenario-based problems using a full-path clinical diagnosis task... this task simulates a real-world diagnostic process by requiring the model to sequentially order examinations and integrate information from the obtained examination results to arrive at a final diagnosis. (Section 3.3)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
