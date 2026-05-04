# Binary classification
**Type:** Behavior  
**Referenced in:** 14 papers  

## State of the Field

Across the provided literature, binary classification is consistently defined as an observable task or output pattern where a model must assign one of two predefined labels to a given input. This behavior is applied to various data modalities, including text, images for face forgery detection, and tabular data records. The specific labels used depend on the application, with examples such as "True" or "False", "real" or "fake", and "offensive" or "non-offensive". Models are commonly operationalized to perform this task through fine-tuning on dedicated binary classification datasets. One paper notes the use of binary cross entropy loss for the supervised learning objective in this context. Binary classification is also categorized as a distinct task type, studied alongside and contrasted with multi-class classification and question answering. The provided data also indicates a relationship with in-context classification, though the nature of this connection is not specified.

## Sources

**[Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)**
> An observable output pattern where the model is constrained to generate one of two predefined labels, such as "True" or "False".

## Relationships

### Associated with
- **In-context classification** (behaviors tasks)
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
