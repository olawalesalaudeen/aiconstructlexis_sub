# MBPP
**Type:** Measurement  
**Referenced in:** 163 papers  
**Also known as:** MBPP(+), MBPP+, MBPP-pro  

## State of the Field

Across the surveyed literature, MBPP (Mostly Basic Python Problems) is a widely used programming benchmark for evaluating the behavior of `Code generation`. It is consistently operationalized to measure a model's ability to synthesize functionally correct Python programs from natural language descriptions, thereby assessing `Programming ability`. The benchmark is composed of what papers describe as "crowd-sourced" and "entry-level" Python problems, each accompanied by a textual description and automated test cases for verification. The exact number of problems cited varies across papers, with figures ranging from 257 in a "sanitized version" to 974 total tasks, indicating the use of different splits or versions of the dataset. Some research employs an extended version, MBPP+, which adds more test cases to "improve evaluation robustness." While its primary application is for code synthesis, a smaller set of studies uses MBPP or its variants to measure other constructs; for instance, one paper uses MBPP+ as an `Inductive reasoning` benchmark, while others link it to assessing `Algorithmic reasoning` and `Generalization`. MBPP is frequently used alongside the HumanEval benchmark to provide a broader assessment of Python coding skills.

## Sources

**[$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf)**
> MBPP is a programming benchmark used here to evaluate text-to-code generation from a textual context.

**[Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf) (as "MBPP+")**
> An extended version of the Mostly Basic Python Problems (MBPP) benchmark with additional test cases to improve evaluation robustness.

**[Training Language Models on Synthetic Edit Sequences Improves Code Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43f900f571de6c96a70d5724a0fb565-Paper-Conference.pdf) (as "MBPP(+)")**
> The Mostly Basic Python Problems (MBPP) benchmark, used to evaluate a model's ability to synthesize short Python programs from natural language descriptions.

**[Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf) (as "MBPP-pro")**
> A benchmark dataset for evaluating code generation, consisting of programming problems described in natural language.

## Relationships

### → MBPP
- **Code generation** (behaviors tasks) — *measured_by*
  > Text-to-Code (T2C): Given a textual context, the model is prompted to generate the corresponding code snippet. ... We perform 3-shot inference on the MBPP dataset (Austin et al., 2021) and report P@1. (Section 4.3)
  - [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *measured_by*
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
- **Coding** (behaviors tasks) — *measured_by*
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.585.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > Notably, Figure 8 shows significant gains in categories like MBPP (programming) and PIQA (physical commonsense reasoning), reflecting enhanced logical reasoning and problem-solving skills. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **Inductive reasoning** (constructs) — *measured_by*
  > MBPP+ (Liu et al., 2023) expands a program synthesis dataset MBPP (Austin et al., 2021) with 35x more test cases. It covers basic Python programming tasks written by humans. The abundance of test cases avails utilizing MBPP+ as an inductive reasoning dataset (Section 4.1).
  - [CORG: Generating Answers from Complex, Interrelated Contexts](https://aclanthology.org/2025.naacl-long.429.pdf)
- **Algorithmic reasoning** (constructs) — *measured_by*
  > Our experiments demonstrate that RaLU significantly outperforms existing baselines in mathematical reasoning (GSM8K, MATH) and algorithmic reasoning (HumanEval+, MBPP+), underscoring its potential to advance LLM reasoning and programming by offering enhanced accuracy and interpretability. (Abstract)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1475.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [pFedGPT: Hierarchically OptimizingLoRAAggregation Weights for Personalized FederatedGPTModels](https://aclanthology.org/2025.emnlp-main.240.pdf)
