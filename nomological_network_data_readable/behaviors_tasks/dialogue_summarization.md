# Dialogue summarization
**Type:** Behavior  
**Referenced in:** 10 papers  

## State of the Field

Across the provided literature, dialogue summarization is most commonly defined as the task of creating a concise or short summary from a multi-turn conversation. Some work situates this task within a specific domain, such as summarizing a "pre-consultation dialogue" or a "patient-doctor interaction" into a medical report. A more specialized framing, found in one paper, treats it as a method for condensing a dialogue to highlight "information indicative of errors in the last agent utterance." To operationalize and evaluate this behavior, researchers predominantly use the DialogSum dataset. Other datasets, such as QMSum and SAMSum, are also mentioned as measurement instruments, though less frequently in this set of papers. The task is presented as a downstream application for evaluating large language models, alongside other tasks like question-answering and translation. Dialogue summarization is also studied in relation to model failure modes, with one paper noting that "the persistence of hallucinations" is a limitation where the model "fabricates features not present in the source content."

## Sources

**[MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The task of creating a concise summary from a multi-turn conversation, such as a pre-consultation dialogue or a patient-doctor interaction.

## Relationships

### Dialogue summarization →
- **DialogSum** (measurements) — *measured_by*
  > We evaluate STAFF on three datasets on different downstream tasks, namely, the BioInstruct dataset (Tran et al., 2024) (biology question-answering), DialogSum dataset (Chen et al., 2021) (dialogue summarization), and the ‘Kazakh-English’ subset of WMT-19 dataset (Barrault et al., 2019) (translation of minority languages). (Section 4.1)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
- **QMSum** (measurements) — *measured_by*
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)
- **SAMSum** (measurements) — *measured_by*
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  > Finally, a notable limitation is the persistence of hallucinations in the generation of item recommendation information and dialogue summaries, where the model fabricates features not present in the source content. (Limitations)
  - [MAviS: A Multimodal Conversational Assistant For Avian Species](https://aclanthology.org/2025.emnlp-main.1456.pdf)
