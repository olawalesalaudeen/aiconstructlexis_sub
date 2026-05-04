# RM-Bench
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

RM-Bench is consistently described as a benchmark for evaluating reward models. The prevailing usage across the provided literature is to assess a model's sensitivity to subtle variations in content, operationalized through the use of "preference pairs with subtle differences." One common framing states that the benchmark measures a reward model's "resistance to style biases," while another specifies it is designed to correlate with downstream performance on chat, math, code, and safety tasks. In practice, papers use RM-Bench to measure the constructs of `Safety` and `Faithfulness`. One study notes a specific metric called "'Hard Acc'" associated with its evaluation. The benchmark is also explicitly contrasted with `RewardBench`, with one paper claiming it "achieves higher correlation against actual use cases," and is also related to `HumanEvalPack`.

## Sources

**[CanLLMWatermarks Robustly Prevent Unauthorized Knowledge Distillation?](https://aclanthology.org/2025.acl-long.649.pdf)**
> A benchmark that evaluates reward models by assessing their sensitivity to subtle content variations and resistance to style biases.

## Relationships

### → RM-Bench
- **Factuality** (constructs) — *measured_by*
  - [Quantifying Lexical Semantic Shift via Unbalanced Optimal Transport](https://aclanthology.org/2025.acl-long.775.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)

### Associated with
- **Reward-Bench** (measurements)
  - [RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style](https://proceedings.iclr.cc/paper_files/paper/2025/file/6da1eec80095dc5937f7716db15aca4b-Paper-Conference.pdf)
- **HumanEvalPack** (measurements)
  - [RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style](https://proceedings.iclr.cc/paper_files/paper/2025/file/6da1eec80095dc5937f7716db15aca4b-Paper-Conference.pdf)
