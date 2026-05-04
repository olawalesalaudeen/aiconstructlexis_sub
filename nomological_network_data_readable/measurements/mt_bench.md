# MT-Bench
**Type:** Measurement  
**Referenced in:** 240 papers  
**Also known as:** MT Bench, MT-BENCH, MT-bench, MTBench  

## State of the Field

Across the provided literature, MT-Bench is consistently described as a benchmark designed to evaluate large language models, with a primary focus on their multi-turn conversational and instruction-following capabilities. A defining and near-universal feature of its operationalization is the use of a strong LLM, most frequently GPT-4, as an automated judge to score model responses. The evaluation process typically involves generating responses to a predefined set of open-ended questions—most sources cite a set of 80 multi-turn questions—which are then graded by the judge, often on a 1-to-10 scale. The most prevalent application of MT-Bench is to measure a model's `instruction following` ability, and it is also commonly used to assess related constructs such as `conversational ability`, `helpfulness`, and `human preference alignment`. The benchmark's questions are described as spanning a wide range of domains; as one paper notes, it evaluates models on dimensions like "writing, roleplay, coding, mathematics, reasoning, STEM, and humanities" ("WildChat: 1M ChatGPT Interaction Logs in the Wild"). Papers also use MT-Bench to evaluate broader capabilities like `generalization`, `commonsense knowledge`, and `faithfulness`. A less common but present use case involves employing MT-Bench for meta-evaluation, where it serves to assess the performance of other LLM-based evaluators. Overall, the data shows MT-Bench is a widely used instrument for assessing the quality of chat-focused and instruction-tuned models through LLM-judged, open-ended, multi-turn interactions.

## Sources

**[#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf)**
> MT-Bench is a benchmark that uses strong LLMs like GPT-4 to evaluate the multi-turn conversational and instruction-following capabilities of other models.

**[Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf) (as "MT-bench")**
> GPT-4-based evaluation benchmark for large language models that assesses generation quality through open-ended questions in multi-turn conversations and instruction-following tasks.

**[Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) (as "MT Bench")**
> A benchmark for evaluating LLMs across diverse instruction-following tasks, used here to assess evaluator models' correlation with human and GPT-4 judgments.

**[The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf) (as "MT-BENCH")**
> An automatic benchmark featuring challenging one-turn and multi-turn reasoning and instruction-following examples, where model responses are graded by GPT-4 on a scale from 1 to 10.

**[Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf) (as "MTBench")**
> A benchmark used to evaluate model responses on instruction-following or chat-style tasks under different decoding methods.

## Relationships

### → MT-Bench
- **Instruction following** (constructs) — *measured_by*
  > We evaluate finetuned models on MT-Bench (Zheng et al., 2023), by generating model responses to a pre-defined set of 80 multi-turn questions and subsequently evaluating these using GPT-4 (OpenAI, 2023). (Section 4.3)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Conversational ability** (constructs) — *measured_by*
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
- **Dialogue** (behaviors tasks) — *measured_by*
  > "We evaluated our multi-model speculative system in SpecBench(Xia et al., 2024), across multiple tasks including multi-turn conversation, translation, summarization, question answering, mathematical reasoning, and retrieval-augmented generation, employing the MT-bench (Zheng et al., 2023)"
  - [Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/6091f2bb355e960600f62566ac0e2862-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf)
- **Multi-turn dialogue** (behaviors tasks) — *measured_by*
  > To further validate the improvements of ICON2 in overall capabilities and multi-turn dialogue, we conducted evaluations on MT-Bench, with the results shown in Table 2 (Section 4.3).
  - [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **Dialogue generation** (behaviors tasks) — *measured_by*
  > We evaluate its performance on dialogue (Zheng et al., 2023), math (Cobbe et al., 2021) and coding (Chen et al., 2021) following Wang et al. (2024d)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **Scientific reasoning** (constructs) — *measured_by*
  > “The second benchmark, MT-Bench (Zheng et al., 2024), consists of 80 multi-turn dialogues spanning various domains, including writing, roleplay, reasoning, math, coding, extraction, STEM, and humanities.”
  - [s3: You Don’t Need That Much Data to Train a Search Agent viaRL](https://aclanthology.org/2025.emnlp-main.1096.pdf)
- **Information extraction** (behaviors tasks) — *measured_by*
  > “The second benchmark, MT-Bench (Zheng et al., 2024), consists of 80 multi-turn dialogues spanning various domains, including writing, roleplay, reasoning, math, coding, extraction, STEM, and humanities.”
  - [s3: You Don’t Need That Much Data to Train a Search Agent viaRL](https://aclanthology.org/2025.emnlp-main.1096.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coreference resolution** (behaviors tasks) — *measured_by*
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coding** (behaviors tasks) — *measured_by*
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **Verbosity** (constructs) — *measured_by*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Kangaroo: Lossless Self-Speculative Decoding for Accelerating LLMs via Double Early Exiting](https://proceedings.neurips.cc/paper_files/paper/2024/file/16336d94a5ffca8de019087ab7fe403f-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **Fluency** (constructs) — *measured_by*
  - [Reflection-Window Decoding: Text Generation with Selective Refinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25a/tang25a.pdf)
- **Versatility** (constructs) — *measured_by*
  > These benchmarks are commonly used in the community to assess the conversational versatility of models across a diverse range of queries. (Section 8.1)
  - [AMPO: Active Multi Preference Optimization for Self-play Preference Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25c/gupta25c.pdf)
- **Open-ended question answering** (behaviors tasks) — *measured_by*
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
- **Short-context capability** (constructs) — *measured_by*
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **Open-ended instruction following** (behaviors tasks) — *measured_by*
  - [NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1329.pdf)
- **Adaptability** (constructs) — *measured_by*
  - [RouteLLM: Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
- **URIAL** (measurements) — *measured_by*
  - [Is In-Context Learning Sufficient for Instruction Following in LLMs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41623b137cd34807f56028aa9f6f84a7-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Best-of-N** (measurements) — *measured_by*
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **Coherence** (constructs) — *measured_by*
  - [Reflection-Window Decoding: Text Generation with Selective Refinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25a/tang25a.pdf)
- **Contextual understanding** (constructs) — *measured_by*
  > Contextual Understanding: the final score from MT-Bench. (Section 4.1).
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
- **Knowledge transferability** (constructs) — *measured_by*
  - [LingGym: How Far AreLLMs from Thinking Like Field Linguists?](https://aclanthology.org/2025.emnlp-main.70.pdf)

### Associated with
- **LLM-as-a-judge** (measurements)
  - [RouteLLM: Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
- **Dialogue** (behaviors tasks)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
