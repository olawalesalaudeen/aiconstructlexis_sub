# Zero-shot generalization
**Type:** Construct  
**Referenced in:** 38 papers  
**Also known as:** Zero-shot generalizability, Zero-shot transfer  

## State of the Field

Across the surveyed literature, the prevailing framing of Zero-shot generalization is a model's ability to perform effectively on unseen tasks or data without any task-specific training, fine-tuning, or in-context examples. The concept of "unseen" is applied broadly to new datasets, instructions, objects, schemas, and constraints, with studies examining generalization to "unseen vision contexts" ("Vision-Language Foundation Models as Effective Robot Imitators") or performance on "new policies and new prompting tasks" ("SafeWatch..."). The definitions consistently state that the model must rely on its pre-trained knowledge and task instructions alone; one paper notes that the "primary motivation of instruction-tuning is to permit zero-shot adaptation to new tasks via natural language" ("Evaluating the Zero-shot Robustness of Instruction-tuned Language Models"). While "Zero-shot generalization" is the most common term, a smaller set of papers use variants like "Zero-shot learning" or "Zero-shot transfer" for this capacity in specific domains such as clinical entity extraction or dialogue understanding. To operationalize this construct, researchers measure model performance on benchmark datasets not seen during training; the provided data shows it is measured using FreebaseQA, CommonsenseQA, and MedQA for "zero-shot transfer experiments". Another method of quantification involves comparing performance between seen and unseen labels, where a smaller gap indicates better generalization ("GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction").

## Sources

**[Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)**
> The ability of a pre-trained model to perform well on unseen target datasets without exposure to their training history.

**[SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model with Transparent Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/beac6bfb7eac3d651307c16ac747df01-Paper-Conference.pdf) (as "Zero-shot generalizability")**
> The model's ability to perform effectively on new, unseen tasks, policies, or data categories without any specific fine-tuning on them.

**[Benchmarking Failures in Tool-Augmented Language Models](https://aclanthology.org/2025.naacl-long.150.pdf) (as "Zero-shot learning")**
> The capacity to perform clinical entity extraction without task-specific training examples for the target setting.

**[CAST: Corpus-Aware Self-similarity Enhanced Topic modelling](https://aclanthology.org/2025.naacl-long.387.pdf) (as "Zero-shot transfer")**
> The ability to perform dialogue understanding tasks without task-specific fine-tuning or training on the target domains.

## Relationships

### Zero-shot generalization →
- **WikiText** (measurements) — *measured_by*
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
- **AG News** (measurements) — *measured_by*
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
- **ScienceQA** (measurements) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **Penn Treebank (PTB)** (measurements) — *measured_by*
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **lm1b** (measurements) — *measured_by*
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **PubMed** (measurements) — *measured_by*
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **Arxiv** (measurements) — *measured_by*
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **MM-Vet** (measurements) — *measured_by*
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **VizWiz** (measurements) — *measured_by*
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **POPE** (measurements) — *measured_by*
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **GSM** (measurements) — *measured_by*
  - [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf)
- **FreebaseQA** (measurements) — *measured_by*
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  > To evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three unseen KGQA datasets: FreebaseQA (Jiang et al., 2019), CSQA (Talmor et al., 2019) and MedQA (Jin et al., 2021). (Section 5.4)
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **MedQA** (measurements) — *measured_by*
  > To evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three unseen KGQA datasets: FreebaseQA (Jiang et al., 2019), CSQA (Talmor et al., 2019) and MedQA (Jin et al., 2021). (Section 5.4)
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **GrailQA** (measurements) — *measured_by*
  - [Certainty in Uncertainty: Reasoning over Uncertain Knowledge Graphs with Statistical Guarantees](https://aclanthology.org/2025.emnlp-main.442.pdf)

### → Zero-shot generalization
- **Instruction following** (constructs) — *causes*
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **Compositionality** (constructs) — *causes*
  - [Human-Object Interaction Detection Collaborated with Large Relation-driven Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a54def490213ee10631b991c5acc6b5-Paper-Conference.pdf)

### Associated with
- **Cross-domain generalization** (constructs)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.513.pdf)
