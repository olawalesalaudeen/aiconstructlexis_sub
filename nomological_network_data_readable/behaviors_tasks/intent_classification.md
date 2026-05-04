# Intent classification
**Type:** Behavior  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, intent classification is consistently defined as the task of identifying a user's underlying goal or intention from an utterance. This behavior is commonly operationalized as a multiclass classification problem, where a model assigns a predefined intent label to the user's input. While several definitions refer to 'text inputs', some work also frames it in the context of Spoken Language Understanding (SLU), where the input is a 'spoken command'. To measure performance on this task, researchers use specific datasets. The Banking-77 dataset is cited for evaluating intent classification from text, while the Fluent Speech Commands (FSC) corpus is used for spoken inputs. One paper also notes the application of this task in the context of conversational agents.

## Sources

**[Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf)**
> Classifying user intent from text inputs, evaluated on the Banking-77 dataset.

## Relationships

### Intent classification →
- **CLINC150** (measurements) — *measured_by*
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
- **SLURP** (measurements) — *measured_by*
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)
- **ATIS** (measurements) — *measured_by*
  - [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.539.pdf)
- **SNIPS** (measurements) — *measured_by*
  - [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.539.pdf)
