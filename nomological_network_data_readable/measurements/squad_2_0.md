# SQuAD 2.0
**Type:** Measurement  
**Referenced in:** 19 papers  
**Also known as:** SQuAD v2, SQuAD2.0-Eval, SQuAD 2, SQuADv2, SQuAD2.0, SQuAD2  

## State of the Field

Across the provided literature, SQuAD 2.0 is consistently characterized as a reading comprehension benchmark for question answering. Its most frequently mentioned feature is the inclusion of unanswerable questions, designed to evaluate a model's ability to abstain from answering when the provided context is insufficient. This is often framed as testing whether a model "knows what it doesn't know" ("Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus"). Papers use this instrument to measure general question answering and text understanding, as well as more specific behaviors like "minimizing the hallucination" ("Supervised Knowledge Makes Large Language Models Better In-context Learners"). A derivative, SQuAD2.0-Eval, is noted for assessing "adherence and robustness" in retrieval-augmented models, and one paper uses the benchmark to measure `Safety`. The dataset, which is based on Wikipedia articles, also serves as a source for creating other corpora, such as True-False datasets or the UQA corpus.

## Sources

**[Representation Deficiency in Masked Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfde7fb279709eff53faa074b45840d8-Paper-Conference.pdf)**
> The Stanford Question Answering Dataset 2.0, a reading comprehension dataset that includes unanswerable questions, used to evaluate a model's ability to abstain from answering when no correct answer is present in the context.

**[Gender Inclusivity Fairness Index (GIFI): A Multilevel Framework for Evaluating Gender Diversity in Large Language Models](https://aclanthology.org/2025.acl-long.129.pdf) (as "SQuAD v2")**
> Question answering dataset combining span extraction and unanswerable questions, requiring models to either extract an answer or correctly identify when no answer exists.

**[AGD: Adversarial Game Defense Against Jailbreak Attacks in Large Language Models](https://aclanthology.org/2025.acl-long.852.pdf) (as "SQuAD v2.0")**
> The Stanford Question Answering Dataset v2.0, a reading comprehension benchmark based on expository Wikipedia articles where answers are text spans and some questions may be unanswerable.

**[Jailbreaking? One Step Is Enough!](https://aclanthology.org/2025.acl-long.571.pdf) (as "SQuAD2.0-Eval")**
> Evaluation dataset derived from SQuAD2.0, designed to assess adherence and robustness in retrieval-augmented language models under complex retrieval scenarios with conflicting and irrelevant contexts.

**[The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf) (as "SQuAD 2")**
> Question answering benchmark with unanswerable questions, used to assess a model's ability to refrain from answering when context is insufficient.

**[Alignment with Fill-In-the-Middle for Enhancing Code Generation](https://aclanthology.org/2025.emnlp-main.420.pdf) (as "SQuADv2")**
> The Stanford Question Answering Dataset (SQuAD) version 2.0, which includes unanswerable questions to test a model's ability to abstain from answering when the text does not support it.

**[Enhancing Chain-of-Thought Reasoning via Neuron Activation Differential Analysis](https://aclanthology.org/2025.emnlp-main.818.pdf) (as "SQuAD2.0")**
> The Stanford Question Answering Dataset version 2.0, used as a source for creating other QA corpora like UQA.

**[Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf) (as "SQuAD2")**
> The Stanford Question Answering Dataset (version 2), which includes unanswerable questions to test whether a model knows what it doesn't know.

## Relationships

### → SQuAD 2.0
- **Reading comprehension** (constructs) — *measured_by*
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
- **Document question answering** (behaviors tasks) — *measured_by*
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Jailbreaking? One Step Is Enough!](https://aclanthology.org/2025.acl-long.571.pdf)
