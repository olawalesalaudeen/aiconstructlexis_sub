# Preference learning
**Type:** Behavior  
**Referenced in:** 18 papers  
**Also known as:** Preference label classification, Preference labeling, Preference selection, Preference annotation, Preference classification, Preference optimization, Preference model estimation, Pairwise discrimination learning  

## State of the Field

Across the provided literature, preference learning is most commonly framed as the task of choosing, ranking, or predicting a preferred response from a pair or set of candidates for a given prompt. This behavior is operationalized through the creation of preference datasets where an annotator, which can be a human or another LLM, labels which response is better according to a set of criteria. Performance on this task is frequently measured using metrics like "ranking accuracy" or "classification accuracy" to evaluate how well a model can predict these preference judgments. The annotations themselves can vary; one paper notes they can include "Scalar scores that indicate the fine-grained quality regarding multiple aspects, (2) Preference ranking... and (3) Textual explanations" ("Multimodal Large Language Models Make Text-to-Image Generative Models Align Better"). While most definitions focus on the act of judging preferences, a few papers define it as "preference optimization," the process of updating a model's policy to align with these judgments. Other, less frequent conceptualizations include "preference selection" to test for biases in multimodal models by using images as choices, and "pairwise discrimination learning," which frames the task as learning from differential feedback over a series of binary choices. In the provided data, preference learning is studied in relation to "Objective mismatch" and is reported by one paper to cause "Hallucination".

## Sources

**[Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf) (as "Preference label classification")**
> The task of predicting which of two given responses is more preferable for a given prompt.

**[A Critical Evaluation of AI Feedback for Aligning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/33870b3e099880cd8e705cd07173ac27-Paper-Conference.pdf) (as "Preference labeling")**
> The task of choosing a preferred response from two or more candidate completions for a given instruction, based on a set of criteria.

**[Preference Learning Algorithms Do Not Learn Preference Rankings](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8ce770a6b25e603fbff4a37f9e31edc-Paper-Conference.pdf) (as "Preference ranking")**
> The observable action of a model assigning likelihoods to a pair of responses (one preferred, one dispreferred) for a given prompt.

**[MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Preference selection")**
> The task of choosing a preferred option from a set of choices, which can be presented visually or textually, to test for inherent biases.

**[Multimodal Large Language Models Make Text-to-Image Generative Models Align Better](https://proceedings.neurips.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf) (as "Preference annotation")**
> The task of assigning scalar scores, rankings, or textual explanations to images based on specific quality aspects.

**[Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf) (as "Preference classification")**
> Predicting the preferred answer between a pair of responses based on human feedback rankings.

**[Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1646e34971facbcda3727d1dc28ab635-Paper-Conference.pdf) (as "Preference prediction")**
> The task of predicting which of two responses is more preferred by humans, typically outputting a score or probability.

**[Correcting the Mythos of KL-Regularization: Direct Alignment without Overoptimization via Chi-Squared Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e785d64baa2cde06c69d9b7a14636ef2-Paper-Conference.pdf) (as "Preference optimization")**
> Updating a language model policy to prefer responses judged better under a preference dataset or reward model.

**[Square$χ$PO: Differentially Private and Robust $χ^2$-Preference Optimization in Offline Direct Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ad/zhou25ad.pdf) (as "Preference model estimation")**
> The observable process of estimating a model of preferences from corrupted or privatized labels, using least-square regression with privacy-aware scaling.

**[Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf) (as "Pairwise discrimination learning")**
> The observable behavior of learning to select the correct option in a series of binary choices through differential feedback, such as consistently choosing A over B when reinforced for doing so.

## Relationships

### Preference learning →
- **Hallucination** (behaviors tasks) — *causes*
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)

### Associated with
- **Objective mismatch** (constructs)
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
