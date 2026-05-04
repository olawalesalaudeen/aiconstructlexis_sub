# e-SNLI
**Type:** Measurement  
**Referenced in:** 10 papers  

## State of the Field

Across the provided literature, e-SNLI is consistently described as a dataset that extends the SNLI dataset by adding human-written explanations to the original premise-hypothesis pairs. The most common use of the dataset is to evaluate a model's ability to perform natural language inference (NLI) by determining the logical relationship (entailment, contradiction, or neutral) between a premise and a hypothesis. A less frequent framing, presented in one paper, views it as a multi-premise entailment task where the "premise and explanation together entailing the hypothesis" is the central challenge. In line with these uses, e-SNLI is most frequently positioned as a measurement instrument for 'Natural language inference'. It is also reported in the provided sources as a tool for evaluating 'Logical reasoning' and 'Interpretability and explainability'.

## Sources

**[Lost in the Context: Insufficient and Distracted Attention to Contexts in Preference Modeling](https://aclanthology.org/2025.acl-long.286.pdf)**
> An extension of the SNLI dataset that adds explanations to premise-hypothesis pairs, enabling evaluation of multi-premise entailment where the premise and explanation jointly entail the hypothesis.

## Relationships

### → e-SNLI
- **Logical reasoning** (constructs) — *measured_by*
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **Natural language inference** (behaviors tasks) — *measured_by*
  > The task of e-SNLI is to determine the logical relationship (contradiction, neutral or entailment) between the premise and hypothesis. (Section 4.1)
  - [When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity](https://aclanthology.org/2025.emnlp-main.427.pdf)
- **Interpretability and explainability** (constructs) — *measured_by*
  - [HookMoE: A learnable performance compensation strategy of Mixture-of-Experts forLLMinference acceleration](https://aclanthology.org/2025.emnlp-main.1611.pdf)
