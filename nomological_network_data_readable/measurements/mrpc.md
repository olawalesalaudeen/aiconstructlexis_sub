# MRPC
**Type:** Measurement  
**Referenced in:** 31 papers  

## State of the Field

Across the provided literature, MRPC (Microsoft Research Paraphrase Corpus) is consistently described as a benchmark used to measure a model's ability for paraphrase identification. The task is most commonly defined as detecting whether two sentences are paraphrases of each other, with some sources framing it as determining if two sentences are semantically equivalent. A prevalent theme in the data is the instrument's inclusion as a task within the GLUE benchmark, where it is often evaluated alongside other datasets. While its primary stated purpose is measuring paraphrase detection, some papers also use MRPC as part of a suite of tasks to evaluate broader natural language understanding (NLU) capabilities. The benchmark is applied in various evaluation contexts, such as assessing the performance of fine-tuned models, the impact of model compression, and downstream capabilities after model editing.

## Sources

**[Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf)**
> The Microsoft Research Paraphrase Corpus, a benchmark for detecting whether two sentences are paraphrases of each other.

## Relationships

### → MRPC
- **Paraphrase detection** (behaviors tasks) — *measured_by*
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > For NLU tasks, we compare baselines on five datasets, including CoLA (Warstadt et al., 2018), MRPC (Dolan & Brockett, 2005), RTE (Wang et al., 2019), SST-2 (Socher et al., 2013), and WNLI (Wang et al., 2019).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **Paraphrase identification** (behaviors tasks) — *measured_by*
  > We employ eight datasets across various NLP tasks to evaluate the impact of bit-flip errors on model performance: MRPC (paraphrase detection) (Dolan and Brockett, 2005)... (Section 5.1)
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)

### Associated with
- **GLUE** (measurements)
  > ...we omit the time-intensive MNLI and QQP tasks, thus forgoing the use of the MNLI trick3 for tasks MRPC, RTE, and STS-B. (Section 4.1)
  - [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)
