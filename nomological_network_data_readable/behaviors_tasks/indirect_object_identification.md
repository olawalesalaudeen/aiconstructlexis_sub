# Indirect object identification
**Type:** Behavior  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, Indirect object identification is consistently framed as an observable model behavior, defined as correctly predicting the indirect object in a sentence based on syntactic and semantic context. The behavior is operationalized through a sentence completion task, which papers refer to as the "IOI task". This task typically involves presenting a model with a sentence containing two names, such as "When Mary and John went to the store, John gave a bottle of milk to", and evaluating its ability to generate the non-repeated name ("Mary") as the completion. The explicit goal is for the model to "predict the final token in the sentence to be the IO." One paper notes this task was chosen because it "captures a simple, previously-studied model behaviour". The provided data also indicates that Indirect object identification is studied in relation to "In-context reasoning".

## Sources

**[Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching](https://proceedings.iclr.cc/paper_files/paper/2024/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf)**
> The observable behavior of correctly predicting the indirect object in a sentence based on syntactic and semantic context (e.g., identifying 'Mary' as the recipient in 'John gave a book to Mary').

## Relationships

### Indirect object identification →
- **IOI task** (measurements) — *measured_by*
  > In Wang et al. (2022), the authors analyze how the decoder-only transformer language model GPT-2 Small (Radford et al., 2019) performs the Indirect Object Identification (IOI) task. (Section 3)
  - [Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf)

### Associated with
- **In-context reasoning** (constructs)
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
