# Wino
**Type:** Measurement  
**Referenced in:** 3 papers  

## State of the Field

Across the provided sources, Wino is consistently characterized as a benchmark designed to evaluate commonsense reasoning. The definitions specify that it is based on the Winograd Schema Challenge and operationalizes this evaluation through pronoun resolution problems. The most prevalent application of Wino in this dataset is to measure `Commonsense understanding`, a use cited across multiple papers. A smaller number of sources also employ it to assess `Language understanding` and `Faithfulness`. In practice, Wino is frequently included as one component in a broader suite of datasets to evaluate general `Downstream task performance`. As evidence from one paper shows, it is often listed alongside other benchmarks like ARC, BoolQ, and HellaSwag to measure the "downstream task accuracy" of models.

## Sources

**[Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf) (as "Winograd")**
> The Winograd Schema Challenge, a benchmark for commonsense reasoning via pronoun resolution problems.

**[Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bs/zhang25bs.pdf)**
> A benchmark based on the Winograd Schema Challenge, designed to test commonsense reasoning through pronoun resolution problems.

## Relationships

### → Wino
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bs/zhang25bs.pdf)
