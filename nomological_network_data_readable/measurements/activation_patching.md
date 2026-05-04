# Activation patching
**Type:** Measurement  
**Referenced in:** 28 papers  
**Also known as:** Cross-modal patching, Patching analysis, Patching experiment  

## State of the Field

Activation patching is predominantly described across the literature as a causal intervention technique for localizing model functions. The standard procedure involves running a model on a corrupted prompt while replacing a specific internal activation, such as an attention head or MLP layer output, with its value from a clean prompt run to observe the effect. This method is frequently referred to as "causal tracing" or "interchange intervention," and some papers frame it as a form of "causal mediation analysis." The impact of the intervention is often quantified by measuring changes in the model's output, with one study specifying the use of KL divergence to compare the patched model's predictions to a target. Based on the provided data, activation patching is used as an instrument to investigate several model behaviors, including mathematical reasoning, information extraction, and hallucination. While this general framing is common, a few papers detail more specialized applications, such as "cross-modal patching" to assess task alignment between modalities or "patching experiments" for modulus estimation. The overarching goal is to identify the causal role of specific components in a model's behavior, often with the aim of discovering a functional "circuit." One paper notes a potential methodological consideration, stating that by intervening on components independently, the technique may ignore that a circuit is a "holistic system."

## Sources

**[Function Vectors in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ae163cb8788970e53b4fd9578141139-Paper-Conference.pdf)**
> A general causal intervention technique for localizing model functions by running a model on a corrupted prompt while replacing a specific internal activation with its value from a clean prompt run. Also known as causal tracing or interchange intervention.

**[Vision-Language Models Create Cross-Modal Task Representations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25c/luo25c.pdf) (as "Cross-modal patching")**
> An intervention-based evaluation method where a task vector extracted from one modality (e.g., text) is injected into the model during processing of a query from another modality (e.g., image) to assess cross-modal task alignment.

**[(How) Can Transformers Predict Pseudo-Random Numbers?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tao25a/tao25a.pdf) (as "Patching experiment")**
> Intervention-based evaluation where features from one sequence are injected into another to test causal roles of model components in modulus estimation.

**[How Do Transformers Learn Variable Binding in Symbolic Programs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25j/wu25j.pdf) (as "Patching analysis")**
> A specific application of interchange interventions where parts of the model's hidden state, such as the residual stream or individual attention head outputs, are replaced to test their causal effect on the final output.

## Relationships

### → Activation patching
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks) — *measured_by*
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  - [ActionStudio: A Lightweight Framework for Data and Training of Large Action Models](https://aclanthology.org/2025.emnlp-main.1091.pdf)
