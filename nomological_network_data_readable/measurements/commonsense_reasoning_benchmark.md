# Commonsense reasoning benchmark
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** Commonsense Reasoning benchmark, Commonsense Benchmark  

## State of the Field

Across the provided literature, the "Commonsense reasoning benchmark" is consistently defined as a composite evaluation suite used to assess language models. The benchmark is uniformly specified as comprising eight sub-tasks: BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-e, ARC-c, and OBQA. Its primary stated purpose is to measure a model's "Commonsense understanding" or its ability for "reasoning about everyday situations." Operationally, the benchmark utilizes "predefined training and testing datasets," with one paper noting a procedure of combined training across the sub-tasks followed by individual test evaluation. In addition to its direct function, the benchmark also serves as a performance evaluation context for studies on other topics. For example, one paper uses model accuracy on this benchmark to compare the "Memory efficiency" of different fine-tuning methods. The available data thus portrays this instrument as a multi-task tool for measuring commonsense abilities, whose performance scores are also used to contextualize findings about other model properties.

## Sources

**[RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf) (as "Commonsense Reasoning benchmark")**
> A collection of eight sub-tasks (BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-e, ARC-c, OBQA) used to evaluate language models on reasoning about everyday situations, with combined training and individual test evaluation.

**[From Weight-Based to State-Based Fine-Tuning: Further Memory Reduction on LoRA with Parallel Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25au/zhang25au.pdf) (as "Commonsense Benchmark")**
> A composite evaluation suite assessing model performance on multiple tasks requiring commonsense reasoning, including BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-e, ARC-c, and OBQA.

## Relationships

### → Commonsense reasoning benchmark
- **Commonsense reasoning** (constructs) — *measured_by*
  - [From Outcomes to Processes: GuidingPRMLearning fromORMfor Inference-Time Alignment](https://aclanthology.org/2025.acl-long.947.pdf)
- **Memory efficiency** (constructs) — *measured_by*
  > For the 7B model, the hybrid approach of Control(UD)+LoRA(QKV) outperforms DoRA in both accuracy and efficiency. With an average score of 80.0, it surpasses DoRA while significantly reducing 21G less memory... (Section 5.3)
  - [From Weight-Based to State-Based Fine-Tuning: Further Memory Reduction on LoRA with Parallel Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25au/zhang25au.pdf)
