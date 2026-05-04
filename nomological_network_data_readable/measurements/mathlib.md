# Mathlib
**Type:** Measurement  
**Referenced in:** 3 papers  

## State of the Field

Mathlib is characterized in the provided literature as Lean's largest community-maintained repository, consistently used as a data source for models performing theorem proving. The repository serves a dual role, acting as both a primary training corpus and an evaluation source. As a training set, it is described as the library on which "most neural theorem provers based on Lean are primarily trained." For evaluation, it is used to assess model generalization. This is operationalized by sourcing evaluation theorems from the repository, with one study specifically using "newly added" theorems to create distinct test and validation sets.

## Sources

**[miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf)**
> Lean's largest community-maintained repository, used here as a source for evaluation theorems to test generalization.

## Relationships

### Associated with
- **Theorem proving** (behaviors tasks)
  > Most neural theorem provers based on Lean are primarily trained on Lean's mathematical library, Mathlib.
  - [Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation](https://proceedings.iclr.cc/paper_files/paper/2025/file/43f55776896a2e33239c2954519f605e-Paper-Conference.pdf)
