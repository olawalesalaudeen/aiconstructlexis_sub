# SIQA
**Type:** Measurement  
**Referenced in:** 50 papers  
**Also known as:** SOCIALIQA, Social IQA  

## State of the Field

Across the provided literature, SIQA is consistently characterized as a benchmark for evaluating commonsense reasoning, with a specific focus on social situations. The prevailing operationalization, found in most definitions, is a multiple-choice question-answering task where models must select the most likely answer regarding a social scenario. Papers state that the instrument is used to test "social commonsense reasoning," "social commonsense intelligence," and the ability to reason about "people's actions and their social implications." A less frequent framing describes its purpose more broadly as evaluating the "downstream task performance of large language models." The source snippets show that SIQA is frequently employed for evaluation as part of a suite of commonsense reasoning benchmarks that also includes HellaSwag, Winogrande, PIQA, and OpenbookQA. One paper reports a different application, using the benchmark as a basis for constructing new evaluation questions for another tool, PERSONALITYBENCH. While the canonical name is SIQA, it is also referred to as SocialIQA, SOCIALIQA, and Social IQA in the source materials.

## Sources

**[Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/725f5e8036cc08adeba4a7c3bcbc6f2c-Paper-Conference.pdf) (as "SocialIQA")**
> A benchmark dataset used to evaluate the downstream task performance of large language models.

**[Neuron based Personality Trait Induction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d399b67fa017f0f7670102c88507720c-Paper-Conference.pdf) (as "SOCIALIQA")**
> A multiple-choice question answering benchmark for social commonsense reasoning, used in this paper as a basis for constructing evaluation questions for PERSONALITYBENCH.

**[RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf) (as "Social IQA")**
> A benchmark for commonsense reasoning that involves choosing the most likely answer to questions about social situations.

**[Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)**
> The Social Interaction QA (SIQA) benchmark, which tests commonsense reasoning about social situations through multiple-choice questions.

## Relationships

### → SIQA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
- **Social reasoning** (constructs) — *measured_by*
  - [NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/db6461eaf0eaeaad1d9c4a70e4818cbd-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf)
- **Social competence** (constructs) — *measured_by*
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-ExpertsLLMs](https://aclanthology.org/2025.emnlp-main.1115.pdf)
