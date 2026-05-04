# Noise robustness
**Type:** Construct  
**Referenced in:** 23 papers  
**Also known as:** Robustness to noisy labels, Robustness to noisy textual descriptions, Susceptibility to noisy information, Resilience to noise, Robustness to noise, Noise Sensitivity, Noise resistance, Reader robustness to noise, Robustness to label noise, Robustness to random noise, Noise sensitivity, Noise-tolerance  

## State of the Field

Across the surveyed literature, noise robustness is most commonly defined as a model's ability to maintain performance when faced with corrupted inputs or irrelevant, distracting information in its context. This latter framing is particularly prevalent in studies of retrieval-augmented generation (RAG), where some papers note that "reader robustness to noise—rather than retriever quality alone—determines downstream effectiveness" (RAGGED: Towards Informed Design of Scalable and Stable RAG Systems). A second, frequently discussed form of this construct concerns robustness to imperfections in the training data, such as corrupted labels, noisy textual supervision, or errors in self-generated data used for self-improvement. A few papers offer more specific definitions, describing resilience to noise introduced during the training process itself (e.g., from DP-SGD), tolerance to noisy preference data, or the stability of internal mechanisms like attention weights. The construct is operationalized in several ways, including by introducing synthetic noise, as one study does by adding "5% synthetic label noise into the training data" and evaluating on MNLI and CivilComments-WILDS (The MaleCEOand the Female Assistant...). Other measurement approaches involve using specialized datasets like RobustHP, which contains pairs from ASR corpora in noisy scenarios, or standard benchmarks like CIFAR-10. Noise robustness is studied in relation to information retrieval, and some work suggests it influences both scalability and safety.

## Sources

**[Large Language Models are Efficient Learners of Noise-Robust Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/13f80f05afe56daf8b65fc4384ab6d09-Paper-Conference.pdf)**
> The ability of the model to maintain performance when processing inputs that are corrupted or derived from noisy sources.

**[Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf) (as "Robustness to noisy labels")**
> The degree to which model performance degrades minimally when training labels are corrupted or mislabeled.

**[Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf) (as "Robustness to noisy textual descriptions")**
> The degree to which a model maintains compositional performance when captions or textual supervision are noisy.

**[TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/16ba99f25a235f1100a4014d71d34ad8-Paper-Conference.pdf) (as "Susceptibility to noisy information")**
> The degree to which a model's performance is degraded by the presence of irrelevant, distracting, or misleading information in the input.

**[From Evidence to Belief: ABayesian Epistemology Approach to Language Models](https://aclanthology.org/2025.naacl-long.532.pdf) (as "Resilience to noise")**
> The latent property of a model to maintain performance and generate coherent output despite the introduction of noise during training, such as from DP-SGD.

**[The MaleCEOand the Female Assistant: Evaluation and Mitigation of Gender Biases in Text-To-Image Generation of Dual Subjects](https://aclanthology.org/2025.acl-long.450.pdf) (as "Robustness to noise")**
> The resilience of a model's performance in the presence of synthetic label noise in the training data, indicating stability in learning despite data imperfections.

**[RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Noise Sensitivity")**
> The latent tendency of the generator to incorporate incorrect information from retrieved chunks, whether relevant or irrelevant.

**[Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf) (as "Noise resistance")**
> The model's latent ability to maintain performance and generate correct answers when provided with irrelevant or distracting information.

**[RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf) (as "Noise sensitivity")**
> The disposition of a model to have its performance degrade when presented with irrelevant or distracting content in the retrieved context.

**[RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf) (as "Reader robustness to noise")**
> The latent ability of a reader model to maintain performance when exposed to irrelevant or distracting retrieved content, distinguishing useful information from noise.

**[Self-Improving Transformers Overcome Easy-to-Hard and Length Generalization Challenges](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25d/lee25d.pdf) (as "Robustness to label noise")**
> The model's ability to maintain performance and continue the self-improvement process even when trained on self-generated data that contains a certain amount of errors or inaccuracies.

**[ROPO: Robust Preference Optimization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25d/liang25d.pdf) (as "Noise-tolerance")**
> A property of a training process or loss function where the presence of noisy preference data does not significantly degrade the model's learning and final performance.

**[Curse of High Dimensionality Issue in Transformer for Long Context Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cr/zhang25cr.pdf) (as "Robustness to random noise")**
> The ability of a model's attention mechanism to maintain stable output distributions when subjected to random perturbations in attention weights, reducing sensitivity to noise.

## Relationships

### Noise robustness →
- **CIFAR-10** (measurements) — *measured_by*
  - [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf)
- **Stability** (constructs) — *causes*
  - [RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf)
- **Scalability** (constructs) — *causes*
  - [RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf)

### Associated with
- **Robustness** (constructs)
  - [ROPO: Robust Preference Optimization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25d/liang25d.pdf)
