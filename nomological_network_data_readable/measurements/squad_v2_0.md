# SQuAD v2.0
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** SQuADv2, SQuAD v2  

## State of the Field

Across the provided literature, SQuAD v2.0 is consistently described as a benchmark dataset used to measure model capabilities. The most prevalent applications are for evaluating `Reading comprehension` and `Question answering`, with multiple papers using it for these purposes. The core task, as defined in the sources, presents a model with a question and a corresponding Wikipedia article, from which it must derive an answer. One definition specifies that this includes the ability to identify unanswerable questions. While its primary use is for question answering, some papers adapt it for other tasks; for instance, one study uses SQuAD v2.0 to create a `Document retrieval` task where the model must select the correct document for a given query. Another paper mentions its use in evaluating downstream performance without fine-tuning.

## Sources

**[AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf) (as "SQuAD 2.0")**
> Stanford Question Answering Dataset 2.0, a reading comprehension benchmark where a model must answer questions based on a provided Wikipedia article, including identifying unanswerable questions.

**[Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf) (as "SQuADv2")**
> A reading comprehension question answering benchmark used to evaluate downstream performance without fine-tuning.

**[DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf) (as "SQuAD v2")**
> The Stanford Question Answering Dataset (v2), used in this paper to create a document retrieval task.

## Relationships

### → SQuAD v2.0
- **Question answering** (behaviors tasks) — *measured_by*
  - [Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > Document Retrieval In this task the model receives a query and Ndocs randomly assorted documents, and its objective is to return the id of the matching document. Our data is sampled from SQuAD v2 (Rajpurkar et al., 2018). (Section 5)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
