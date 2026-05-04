# Instruction fine-tuning
**Type:** Behavior  
**Referenced in:** 38 papers  
**Also known as:** Fine-tuning, Cross-lingual adaptation, Speech-to-speech instruction following, Continual instruction tuning, Instruction tuning, Sequential knowledge editing, Sequential editing, Visual instruction tuning, Instruction-tuning, Continued pretraining, Language model fine-tuning, Supervised fine-tuning  

## State of the Field

Across the surveyed literature, instruction fine-tuning is most commonly described as the process of adapting a pre-trained language model to better follow user commands by training it on a dataset of instructions and their desired outputs. This is frequently situated within the broader context of supervised fine-tuning, which involves updating a model on a labeled, task-specific dataset to improve performance on specific objectives. The provided data also details several specialized applications of this behavior, such as 'continual instruction tuning' for sequential tasks, 'visual instruction tuning' for multimodal inputs, and 'speech-to-speech instruction following' for spoken interactions. The effectiveness of instruction fine-tuning is operationalized and measured through a wide array of evaluation benchmarks, including general language understanding suites like GLUE, multitask evaluations like MMLU, mathematical reasoning datasets such as GSM8k and MATH, and commonsense reasoning tasks like PIQA and SocialIQA. This behavior is studied in relation to several other concepts, including methods for parameter efficiency, and is also linked to model properties like faithfulness, knowledge retention, and convergence. Some papers report that the process can influence other model behaviors, suggesting it may cause catastrophic forgetting and is related to a model's editability.

## Sources

**[SLTrain: a sparse plus low rank approach for parameter and memory efficient pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/d63cf0622eed012a17fe88fced64dcb8-Paper-Conference.pdf) (as "Fine-tuning")**
> Updating a pretrained model on downstream tasks to improve performance on specific objectives.

**[Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf) (as "Continual instruction tuning")**
> Sequentially fine-tuning a language model on a stream of instruction-following tasks.

**[Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf) (as "Instruction tuning")**
> The process of fine-tuning a large language model on a dataset of instructions and demonstrations to improve its ability to follow user commands.

**[Hierarchical Autoregressive Transformers: Combining Byte- and Word-Level Processing for Robust, Adaptable Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f69eee2fafab3743a3d2ae5981c949f-Paper-Conference.pdf) (as "Cross-lingual adaptation")**
> Improving performance on a new language during continued pretraining while preserving performance on the original language.

**[LLaMA-Omni: Seamless Speech Interaction with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf) (as "Speech-to-speech instruction following")**
> Responding to spoken instructions with both text and spoken outputs that satisfy the user's request.

**[MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf) (as "Sequential editing")**
> The task of continuously updating a model with multiple, sequential pieces of knowledge and evaluating its ability to retain earlier edits.

**[AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf) (as "Sequential knowledge editing")**
> The observable process of applying a series of targeted updates to a model's parameters to modify its stored knowledge over time.

**[Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf) (as "Visual instruction tuning")**
> Following multimodal instructions that combine language and vision inputs to produce appropriate responses.

**[A Systematic Analysis of Base Model Choice for Reward Modeling](https://aclanthology.org/2025.emnlp-main.9.pdf) (as "Instruction-tuning")**
> Adapting a language model to better follow task instructions by training it on a collection of instruction-response pairs.

**[Exploring the Hidden Capacity ofLLMs for One-Step Text Generation](https://aclanthology.org/2025.emnlp-main.1166.pdf) (as "Continued pretraining")**
> The process of further training a pretrained model on a large corpus of text to enhance its general language modeling capabilities.

**[COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf) (as "Language model fine-tuning")**
> The task of adapting a pre-trained language model to a specific downstream task or domain using a smaller, task-specific dataset.

**[Adam-mini: Use Fewer Learning Rates To Gain More](https://proceedings.iclr.cc/paper_files/paper/2025/file/45ae878717399e6f62d57c65f052cd46-Paper-Conference.pdf) (as "Supervised fine-tuning")**
> The process of adapting a pre-trained language model to a specific downstream task using a labeled dataset.

## Relationships

### Instruction fine-tuning →
- **GLUE** (measurements) — *measured_by*
  - [On the Optimization Landscape of Low Rank Adaptation Methods for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c34262c35aa5f8c1a091822cbb2020c2-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **MATH** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [TAROT: Targeted Data Selection via Optimal Transport](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25l/feng25l.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf)
- **SVAMP** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **NumGLUE** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf)
- **SIQA** (measurements) — *measured_by*
  - [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *causes*
  - [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf)
- **SlimPajama** (measurements) — *measured_by*
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **Commonsense170k** (measurements) — *measured_by*
  - [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf)
- **Super-Natural Instructions** (measurements) — *measured_by*
  - [PEARL: Towards Permutation-Resilient LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fad8e1915f66161581bb127ccf01092e-Paper-Conference.pdf)
- **Editability** (constructs) — *causes*
  - [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf)

### Associated with
- **LoRA** (measurements)
  - [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf)
- **Geometric reasoning** (constructs)
  - [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf)
- **Parameter efficiency** (constructs)
  - [Efficient Learning with Sine-Activated Low-Rank Matrices](https://proceedings.iclr.cc/paper_files/paper/2025/file/112d8e0c7563de6e3408b49a09b4d8a3-Paper-Conference.pdf)
- **Knowledge retention** (constructs)
  - [Identification of Multiple Logical Interpretations in Counter-Arguments](https://aclanthology.org/2025.emnlp-main.327.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [ChainEdit: Propagating Ripple Effects inLLMKnowledge Editing through Logical Rule-Guided Chains](https://aclanthology.org/2025.acl-long.666.pdf)
- **Data quality** (constructs)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **Convergence** (constructs)
  - [Synthetic Text Generation for Training Large Language Models via Gradient Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nguyen25c/nguyen25c.pdf)
