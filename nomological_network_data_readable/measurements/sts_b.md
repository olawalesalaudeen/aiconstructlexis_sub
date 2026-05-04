# STS-B
**Type:** Measurement  
**Referenced in:** 11 papers  

## State of the Field

Across the provided literature, STS-B is consistently identified as the Semantic Textual Similarity Benchmark, used as a downstream task for evaluating sentence-pair similarity. The most detailed definition describes it as a dataset for measuring "fine-grained semantic similarity between sentence pairs using human-annotated similarity scores" (SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models). The benchmark is frequently used to assess the performance of models after various procedures, including fine-tuning, compression, and training with specific methods like ReLoRA. Several papers situate STS-B as a task within the GLUE benchmark suite, and one study notes that results are reported using Spearman correlation. A less common framing, found in one paper, treats STS-B as a "classification-style controlled environment" or a "classification dataset with a modest number of labels" (Vanishing Gradients in Reinforcement Finetuning of Language Models).

## Sources

**[Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf)**
> The Semantic Textual Similarity Benchmark, used here as a downstream sentence-pair similarity evaluation.
