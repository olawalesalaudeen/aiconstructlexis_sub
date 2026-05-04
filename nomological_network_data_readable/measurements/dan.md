# DAN
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, DAN is used to assess the safety of large language models in the context of jailbreaking. There is a slight variation in its framing: some work describes it as a "benchmark collection of jailbreak-enhanced instructions," while other work characterizes it more specifically as a "well-known jailbreaking prompt" named "Do Anything Now." Papers use DAN to evaluate a model's "resilience against diverse jailbreak attacks" and to measure "Backdoor vulnerability." One study operationalizes this by employing a specific version, DAN 13.0, as a baseline method intended to "override AI safety restrictions and elicit biased responses." This positions DAN as an instrument for both attempting to bypass safety features and for benchmarking a model's robustness against such attempts.

## Sources

**[ChineseSafetyQA: A Safety Short-form Factuality Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.733.pdf)**
> A benchmark collection of jailbreak-enhanced instructions used to evaluate a model's resilience against diverse jailbreak attacks.

## Relationships

### → DAN
- **Backdoor vulnerability** (constructs) — *measured_by*
  - [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf)
