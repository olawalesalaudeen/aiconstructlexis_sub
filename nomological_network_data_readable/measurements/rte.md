# RTE
**Type:** Measurement  
**Referenced in:** 58 papers  

## State of the Field

Across the provided literature, RTE (Recognizing Textual Entailment) is a benchmark consistently used to measure a model's ability to perform textual entailment. The task is most commonly operationalized as a binary classification problem where a model must determine if a given premise sentence logically entails a hypothesis, often by predicting 'True' or 'False'. While the binary framing is prevalent, one study also describes its use in a three-way classification context that includes 'contradicted' and 'neutral' labels. Reflecting its core task, RTE is frequently employed to evaluate the broader constructs of `Natural language inference` (NLI) and `Natural language understanding` (NLU). Its connection to the GLUE benchmark is a recurring theme, with numerous papers identifying it as one of the suite's inference tasks. Researchers utilize RTE in diverse evaluation settings, including standard fine-tuning, zero-shot and few-shot in-context learning scenarios, and for assessing model performance after techniques like pruning. While primarily positioned as an inference task, at least one paper also categorizes it as a 'commonsense benchmark'.

## Sources

**[An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)**
> A textual entailment benchmark used to evaluate whether one sentence entails another.

## Relationships

### → RTE
- **Natural language inference** (behaviors tasks) — *measured_by*
  > We also evaluate KnOTS in the NLI setting, by merging six PEFT llama3-8B (AI, 2024) models finetuned on SNLI (Bowman et al., 2015), MNLI (Williams et al., 2018), SICK (Marelli et al., 2014), QNLI, RTE (Wang et al., 2019), and SCITAIL (Khot et al., 2018). (§ 5.2)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Textual entailment** (behaviors tasks) — *measured_by*
  > We evaluate each method on a wide range of reasoning tasks. These tasks include RTE for textual entailment (Dagan et al., 2005) [...] (Section 4.1)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > For NLU tasks, we compare baselines on five datasets, including CoLA (Warstadt et al., 2018), MRPC (Dolan & Brockett, 2005), RTE (Wang et al., 2019), SST-2 (Socher et al., 2013), and WNLI (Wang et al., 2019).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  - [Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/db6ccc979860d7a233ecaf588bb23512-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  - [ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf)

### Associated with
- **GLUE** (measurements)
  > Table 1: DeBERTaV3-base fine-tuning on GLUE benchmark. ... RTE ... (Acc)
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
