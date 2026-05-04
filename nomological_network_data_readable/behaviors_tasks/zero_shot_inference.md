# Zero-shot inference
**Type:** Behavior  
**Referenced in:** 3 papers  

## State of the Field

Based on the provided data, zero-shot inference is characterized as a model's ability to produce predictions on an unseen dataset using a supplied vocabulary, without requiring any dataset-specific retraining. This behavior is discussed in the context of open vocabulary semantic segmentation models. The process is operationalized by training a model on one dataset, referred to as Ctrain, and then directly evaluating it on a different, unseen test set, Ctest. This capability allows a model to perform tasks like segmentation on new data with a customizable vocabulary. The concept is also studied in relation to "In-context and few-shot learning," with one paper proposing that in-context learning may cause zero-shot inference.

## Sources

**[Revisit the Open Nature of Open Vocabulary Semantic Segmentation](https://proceedings.iclr.cc/paper_files/paper/2025/file/17c89f4c14a4aa238616c126f5af19bb-Paper-Conference.pdf)**
> Producing segmentation predictions on an unseen dataset using a supplied vocabulary without dataset-specific retraining.

## Relationships

### → Zero-shot inference
- **In-context learning** (constructs) — *causes*
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)

### Associated with
- **In-context learning** (constructs)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
