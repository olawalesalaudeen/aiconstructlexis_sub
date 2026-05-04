# BBH
**Type:** Measurement  
**Referenced in:** 58 papers  
**Also known as:** Big-Bench Hard, BigBench-Hard  

## State of the Field

Across the surveyed literature, BBH (Big-Bench Hard) is consistently defined as a benchmark derived from the BIG-Bench suite, composed of tasks selected for being challenging for language models. The most prevalent application of BBH is to measure reasoning capabilities, with papers explicitly using it to evaluate general, complex, and multi-step reasoning. Beyond this primary focus, the benchmark is also employed to assess a wide array of other constructs, including language and commonsense understanding, instruction following, and faithfulness. A smaller number of studies use it to measure more specific behaviors like locality after model editing. Operationally, BBH is most often evaluated in a "few-shot" context, with some papers specifying a "3-shot" setting and using metrics like exact match. The provided data shows that BBH is frequently used as part of a larger suite of evaluation tools, appearing alongside other benchmarks like MMLU, GSM8k, and DROP to assess general model performance.

## Sources

**[Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)**
> Big-Bench Hard benchmark consisting of challenging tasks from the BIG-Bench suite that are difficult for language models, evaluated in few-shot settings.

**[Route Sparse Autoencoder to Interpret Large Language Models](https://aclanthology.org/2025.emnlp-main.347.pdf) (as "Big-Bench Hard")**
> A subset of the Beyond the Imitation Game benchmark focusing on challenging tasks requiring multi-step reasoning, evaluated in a 3-shot setting.

**[Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf) (as "BigBench-Hard")**
> Subset of the Beyond the Imitation Game Benchmark focusing on challenging tasks that require complex reasoning.

## Relationships

### → BBH
- **Reasoning** (constructs) — *measured_by*
  > “BBH (Suzgun et al., 2022) and MMLU (Hendrycks et al., 2021) for multitask reasoning”
  - [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  > For models trained on general instruction datasets, we follow InstructEval (Chia et al., 2023) and report accuracy (%) on MMLU (Hendrycks et al., 2020), BBH (Suzgun et al., 2022), CRASS (Frohberg and Binder, 2021), DROP (Dua et al., 2019). (Section 4.2)
  - [MUFFIN: Curating Multi-Faceted Instructions for Improving Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d1a0188e18c1d74a0f8d6eb5ecede4f-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  > Finally, we select four text-only benchmarks to evaluate text-based performance: ...BBH for complex reasoning (Suzgun et al., 2023)... (Section 4.1)
  - [Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Logical deduction** (measurements) — *measured_by*
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **Prompt optimization** (behaviors tasks) — *measured_by*
  - [Large Language Models as Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/3339f19c5fcee3ad74502947a32be9e6-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
- **Symbolic reasoning** (constructs) — *measured_by*
  - [Where Are We? EvaluatingLLMPerformance onAfrican Languages](https://aclanthology.org/2025.acl-long.1573.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Algorithmic reasoning** (constructs) — *measured_by*
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [TAROT: Targeted Data Selection via Optimal Transport](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25l/feng25l.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [Compute-Constrained Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/5acb720a361eecb34ee62d356859d246-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **Disambiguation** (constructs) — *measured_by*
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *measured_by*
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Understanding** (constructs) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Locality** (constructs) — *measured_by*
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
- **OpenLLM Leaderboard** (measurements)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **LiveBench** (measurements)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
