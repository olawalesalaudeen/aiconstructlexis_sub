# COPA
**Type:** Measurement  
**Referenced in:** 24 papers  

## State of the Field

Across the provided literature, COPA (Choice of Plausible Alternatives) is predominantly characterized as a benchmark for evaluating causal reasoning. The prevailing operationalization is a multiple-choice task where a model must select the more plausible cause or effect for a given premise, although one paper describes it as a sentence completion task. In line with this definition, papers most frequently use COPA to measure the constructs of "causal reasoning" and "commonsense understanding". A smaller line of work uses it to assess "causal discovery" and "causal inference". Beyond this specific focus, COPA is also treated as a general benchmark for "natural language understanding" and is widely used to evaluate "downstream task performance", often appearing in suites of benchmarks alongside HellaSwag, ARC, and BoolQ. The data also shows it is used, though less frequently, to measure constructs such as "language proficiency" and "faithfulness". Several sources also identify COPA as part of the SuperGLUE benchmark.

## Sources

**[Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)**
> The Choice of Plausible Alternatives, a benchmark for commonsense causal reasoning presented as a multiple-choice task.

## Relationships

### → COPA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
- **Causal reasoning** (constructs) — *measured_by*
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
- **Causal inference** (behaviors tasks) — *measured_by*
  - [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.622.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Evaluating Morphological Compositional Generalization in Large Language Models](https://aclanthology.org/2025.naacl-long.60.pdf)
- **Language model pre-training** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > We utilize validation sets from six benchmarks: PIQA (Bisk et al., 2020), HellaSwag (Zellers et al., 2019), ARC-E (Clark et al., 2018), ARC-C (Clark et al., 2018), COPA (Roemmele et al., 2011), Winograd (Levesque et al., 2012), and MathQA (Amini et al., 2019). (Section 4.2.3)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
