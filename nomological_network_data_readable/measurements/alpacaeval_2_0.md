# AlpacaEval 2.0
**Type:** Measurement  
**Referenced in:** 109 papers  
**Also known as:** AlpacaEval2, AlpacaEval2.0, AlpacaEval-2, Alpaca Eval V2, Alpaca Eval 2.0, Alpaca Eval 2, Alpaca-Eval-2, AlpacaEval-V2, AlpacaEvalv2, Alpaca-Eval V2, AlpacaEval v2.0  

## State of the Field

Across the provided literature, AlpacaEval 2.0 is consistently characterized as an automatic evaluation framework or benchmark for assessing language models. Its prevailing operationalization involves using a strong LLM, most commonly a version of GPT-4, as a judge to perform pairwise comparisons of a model's generated response against a reference output, often from a baseline model like GPT-4 itself. The primary metric reported is a win rate, and a frequently mentioned feature is the "Length-Controlled Win Rate," which some papers describe as an innovation to mitigate length-based biases in evaluation. The most common application of AlpacaEval 2.0 is to measure a model's instruction following ability, a purpose cited in a large volume of the provided papers. It is also frequently used to evaluate human preference alignment, conversational ability, and helpfulness. A smaller number of studies use the benchmark to assess more specific behaviors such as question answering, mathematical reasoning, and code generation. Several sources specify that the evaluation is conducted on a set of 805 instructions.

## Sources

**[Online Iterative Reinforcement Learning from Human Feedback with General Preference Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf) (as "AlpacaEval2")**
> AlpacaEval2 is an evaluation framework that uses strong LLMs like GPT-4 as judges to assess model performance on a set of prompts, providing a simulated human preference evaluation.

**[SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf) (as "AlpacaEval 2")**
> An automatic evaluator of instruction-following models that uses pairwise comparisons to assess chat response quality against a baseline model.

**[3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf) (as "AlpacaEval2.0")**
> An evaluation framework that uses GPT-4 to judge instruction-following responses against a reference model.

**[RRM:  Robust Reward Model Training Mitigates Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf) (as "AlpacaEval-2")**
> An automatic evaluation suite for assessing the performance of instruction-following language models, which includes a length-controlled win-rate metric.

**[Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)**
> An evaluation benchmark that assesses a model's question-answering performance by comparing its responses on a set of instructions against a reference model like GPT-4.

**[MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ddab70bf41ffe5d423840644d3357f4-Paper-Conference.pdf) (as "Alpaca Eval V2")**
> An evaluation set used to compare fine-tuned instruction-following models on response quality via GPT-4 judgments.

**[Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf) (as "Alpaca Eval 2.0")**
> A benchmark used here as an in-domain evaluation of instruction-following, with pairwise head-to-head judgments by GPT-4-turbo.

**[OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf) (as "Alpaca Eval 2")**
> A benchmark for evaluating a model's ability to follow instructions.

**[The Impossibility of FairLLMs](https://aclanthology.org/2025.acl-long.6.pdf) (as "Alpaca-Eval-2")**
> An updated version of Alpaca-Eval that evaluates model responses using GPT-4 with improved criteria and task coverage, focusing on conversation quality.

**[Can Large Language Models Detect Errors in Long Chain-of-Thought Reasoning?](https://aclanthology.org/2025.acl-long.906.pdf) (as "AlpacaEval-V2")**
> A text-only human preference alignment benchmark used to evaluate language alignment in LLMs and MLLMs.

**[TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1091.pdf) (as "AlpacaEvalv2")**
> Human-preference benchmark that evaluates model responses through pairwise comparisons, measuring overall helpfulness and coherence in open-ended dialogue.

**[Probing for Arithmetic Errors in Language Models](https://aclanthology.org/2025.emnlp-main.412.pdf) (as "Alpaca-Eval V2")**
> An automatic evaluation system for instruction-following language models that uses GPT-4-Turbo to judge responses and introduces Length-Controlled Win Rates to reduce length-based biases.

**[PERSEVAL: A Framework for Perspectivist Classification Evaluation](https://aclanthology.org/2025.emnlp-main.1138.pdf) (as "AlpacaEval v2.0")**
> An automatic, LLM-based evaluator for assessing the quality of a model's responses to a set of instructions, comparing them against a reference model's outputs.

## Relationships

### → AlpacaEval 2.0
- **Instruction following** (constructs) — *measured_by*
  > We also evaluate instruction-tuned model, Vicuna-v1.5 (Zheng et al., 2023), with AlpacaEval 2.0 (Dubois et al., 2024), which is an automatic evaluation tool for instruction-following tasks.
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  > “Extensive experiments on widely used real-world benchmarks, including MT-Bench, AlpacaEval 2, and 10 key benchmarks of the Open LLM Leaderboard”
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > Helpfulness is measured using AlpacaEval 2.0 (Alpaca) (Dubois et al., 2024a; Li et al., 2023; Dubois et al., 2024b).
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
- **Conversational ability** (constructs) — *measured_by*
  > Both benchmarks evaluate the models’ versatile conversational abilities across a diverse set of queries. (Section 4)
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > For question answering, we use AlpacaEval 2.0 (Li et al., 2023b; Dubois et al., 2024a;b) to assess model performance on 805 instructions. (Section 7.1)
  - [The Best of Both Worlds: Bridging Quality and Diversity in Data Selection with Bipartite Graph](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ac/wu25ac.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To understand the effect of α on model generalization, we measure the AE2 performance of various models with changing α. (Section 4.2. Results)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  > To test our hypothesis, we break down the prompts in Alpaca Eval 2.0 (Li et al., 2023) into different categories. ... We select four representative tasks: two are objective tasks that can be verified: mathematical reasoning or calculation (Math) and Coding...
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
- **Code generation** (behaviors tasks) — *measured_by*
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
- **Creative writing** (behaviors tasks) — *measured_by*
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)

### Associated with
- **LLM-as-a-judge** (measurements)
  > In this benchmark, GPT-4-Preview-1106 serves as both the baseline model and the evaluator for the other models.
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
- **Verbosity bias** (constructs)
  - [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf)
