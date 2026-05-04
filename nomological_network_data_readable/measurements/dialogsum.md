# DialogSum
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** Dialogsum  

## State of the Field

Across the provided literature, DialogSum is most commonly described as a dataset or benchmark used to measure the performance of models on the task of dialogue summarization. It is frequently employed to evaluate outcomes from different model training and inference strategies, such as fine-tuning after coreset selection and zero-shot generative performance. Some papers position it more broadly as a benchmark for text summarization, where it is used alongside other datasets like CNN/DM, with performance sometimes reported using ROUGE-L scores. While its primary application is evaluating summarization, a few papers document alternative uses. For instance, one study reverses the typical task, using DialogSum for "summary-to-dialogue generation" to evaluate long-form conversational generation. Another paper repurposes the dataset to instruction-tune an "event summary module." Finally, some work treats it simply as a corpus of dialogue, analyzing it for linguistic patterns like "grammar skill co-occurrence patterns."

## Sources

**[STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf)**
> A dialogue summarization dataset used to evaluate fine-tuning performance after coreset selection.

**[Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf) (as "Dialogsum")**
> A benchmark dataset used for evaluating dialogue summarization performance.

## Relationships

### → DialogSum
- **Dialogue summarization** (behaviors tasks) — *measured_by*
  > We evaluate STAFF on three datasets on different downstream tasks, namely, the BioInstruct dataset (Tran et al., 2024) (biology question-answering), DialogSum dataset (Chen et al., 2021) (dialogue summarization), and the ‘Kazakh-English’ subset of WMT-19 dataset (Barrault et al., 2019) (translation of minority languages). (Section 4.1)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  > For the decoding stage evaluation, we conduct experiments on two summarization benchmarks: DialogSum (Chen et al., 2021) and CNN/DM (Hermann et al., 2015) (Section 4.1).
  - [Reward Model Perspectives: Whose Opinions Do Reward Models Reward?](https://aclanthology.org/2025.emnlp-main.755.pdf)
