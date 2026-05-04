# Commonsense question answering
**Type:** Behavior  
**Referenced in:** 39 papers  

## State of the Field

Across the provided literature, commonsense question answering is consistently framed as the observable task of answering questions or completing sentences that require implicit, real-world knowledge not explicitly stated in the context. This behavior is most commonly operationalized and measured using a suite of benchmarks, with PIQA, HellaSwag, WinoGrande, and CommonsenseQA appearing frequently across studies. The format of these tasks is typically multiple-choice, though some papers also mention true/false or boolean-response questions. Evaluation is often conducted in zero-shot or few-shot settings to assess a model's general capabilities. While the dominant focus is on everyday situations, a few papers describe more specific instantiations, such as reasoning over provided facts or answering factual queries like a celebrity's birth year parity. This task is studied as a way to evaluate a model's broader commonsense understanding, as one paper notes that "answering commonsense questions correctly requires not only knowledge but also reasoning" (HFT: Half Fine-Tuning for Large Language Models).

## Sources

**[BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf)**
> The observable task of answering questions or completing sentences that require real-world, everyday knowledge, as evaluated on benchmarks like PIQA, HellaSwag, and WinoGrande.

## Relationships

### Commonsense question answering →
- **CommonsenseQA** (measurements) — *measured_by*
  > We consider nine varied downstream tasks: ... (c) general understanding (CommonSenseQA (Talmor et al., 2019), PhysicalIQA (Bisk et al., 2020))
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [MoE++: Accelerating Mixture-of-Experts Methods with Zero-Computation Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/7efe88bb4138d602e56637cfcf713654-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [Radio: Rate–Distortion Optimization for Large Language Model Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/young25b/young25b.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Radio: Rate–Distortion Optimization for Large Language Model Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/young25b/young25b.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [Path Drift in Large Reasoning Models: How First-Person Commitments Override Safety](https://aclanthology.org/2025.emnlp-main.991.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [Path Drift in Large Reasoning Models: How First-Person Commitments Override Safety](https://aclanthology.org/2025.emnlp-main.991.pdf)
- **Commonsense170k** (measurements) — *measured_by*
  - [Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bs/zhang25bs.pdf)

### Associated with
- **Commonsense reasoning** (constructs)
  - [HFT: Half Fine-Tuning for Large Language Models](https://aclanthology.org/2025.acl-long.627.pdf)
