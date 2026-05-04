# Subj
**Type:** Measurement  
**Referenced in:** 10 papers  
**Also known as:** SUBJ  

## State of the Field

Across the provided literature, Subj is consistently used as a benchmark to measure a model's ability to perform subjectivity classification. The task is operationalized as a binary classification problem, requiring models to distinguish between subjective and objective sentences. Papers frequently position Subj as a tool for evaluating general natural language understanding (NLU) and text classification, often alongside other benchmarks like TREC and CB. The provided definitions describe its application in specific contexts, such as for the in-context evaluation of fine-tuned models and for assessing NLU in a low-data regime. While most descriptions are general, one definition cluster specifies that the dataset consists of movie reviews. For instance, one study reports using the benchmark to measure the "Test accuracy (%) on SUBJ using an instruct-fine-tuned GPT-J 6B" (Amortizing intractable inference in large language models).

## Sources

**[Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf)**
> A subjectivity classification benchmark used for in-context evaluation of fine-tuned models.

**[Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf) (as "SUBJ")**
> A binary classification dataset of movie reviews, labeled as objective or subjective, used to evaluate natural language understanding in a low-data regime.

## Relationships

### → Subj
- **Text classification** (behaviors tasks) — *measured_by*
  > text classification using TREC, MR, Subj, and AG News datasets (Voorhees & Tice, 2000; Pang & Lee, 2004; 2005; Zhang et al., 2015). (Section 4.1)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
- **Subjectivity classification** (behaviors tasks) — *measured_by*
  > “3 general NLU tasks, including TREC (Voorhees & Tice, 2000), Subj (Pang & Lee, 2004), and CB (De Marneffe et al., 2019)”
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)
