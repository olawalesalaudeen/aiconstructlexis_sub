# Closed-book question answering
**Type:** Behavior  
**Referenced in:** 11 papers  

## State of the Field

Across the provided literature, Closed-book question answering (CBQA) is consistently defined as the task of answering questions using only the general knowledge stored within a model's parameters, without access to external documents or evidence. This behavior is framed as a test of a model's ability to "recall their parametric memory" or, as one paper states, to "recall information from the weights" (The Cost of Scaling Down Large Language Models...). The field operationalizes and measures this behavior using several datasets; the most frequently mentioned instruments in this set are TriviaQA and Web Questions, with Natural Questions and Entity Questions also cited as evaluation tools. One paper specifically describes Entity Questions as a "CBQA-specific dataset" (MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework). The task is associated with the challenge of `Hallucination`, with one study noting that a problem in CBQA is addressing "instances where the model generates incorrect or fabricated answers." Finally, CBQA is also situated within the context of `Multi-task capability`, where it is treated as a distinct "task type" that can be contrasted with open-book QA.

## Sources

**[Adaptive Chameleon  or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://proceedings.iclr.cc/paper_files/paper/2024/file/99261adc8a6356b38bcf999bba9a26dc-Paper-Conference.pdf)**
> The task of answering questions based on general knowledge stored in the model's parameters, without access to external documents.

## Relationships

### Closed-book question answering →
- **Entity Questions** (measurements) — *measured_by*
  > we use the ENTITYQUESTIONS (Sciavolino et al., 2021) to construct the training and testing datasets for our experiments, which is a CBQA-specific dataset containing knowledge across 24 topics extracted from Wikipedia (Section 3.1).
  - [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.25.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  > One significant challenge in CBQA is addressing hallucinations-instances where the model generates incorrect or fabricated answers (Section 2).
  - [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.25.pdf)
- **Multi-task capability** (constructs)
  > AQuilt achieves better task generalization by incorporating Chinese data and defining more flexible task types. Specifically, AQuilt assigns the task type as closed/open-book QA and uses task requirements as question prefixes. (Section 4.3)
  - [OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf)
