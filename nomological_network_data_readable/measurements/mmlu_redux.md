# MMLU-redux
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** MMLU-Redux  

## State of the Field

Across the provided literature, MMLU-redux is predominantly characterized as a benchmark for evaluating a model's general knowledge and reasoning. It is frequently operationalized as a multiple-choice question answering task, with several papers specifying its use as a "zero-shot variant of MMLU" that can be evaluated with methods like "zero-shot CoT". The benchmark is consistently described as a manually re-annotated subset of the original MMLU, intended to correct issues such as "errors in ground truth answers and question clarity". However, the sources present conflicting information regarding its size, with one paper describing it as "a subset of 3000 manually re-annotated questions across 30 MMLU subjects" and another as a "subset of 5,700 manually re-annotated questions across all 57 MMLU subjects". In terms of what it measures, MMLU-redux is most commonly used to assess `Commonsense knowledge`, though it is also applied to evaluate `Mathematical reasoning` and broader language understanding. A smaller line of work also uses the benchmark to assess "sycophancy in factual contexts" or studies it in relation to `Safety`.

## Sources

**[As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)**
> A benchmark used to evaluate a model's language understanding and knowledge across a wide range of subjects.

**[Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/be06e3802e9411381feece79b4d960c1-Paper-Conference.pdf) (as "MMLU-Redux")**
> MMLU-Redux, a zero-shot variant of MMLU used as an evaluation benchmark for general knowledge and reasoning.

## Relationships

### → MMLU-redux
- **Commonsense knowledge** (constructs) — *measured_by*
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Fann or Flop: A Multigenre, Multiera Benchmark forArabic Poetry Understanding inLLMs](https://aclanthology.org/2025.emnlp-main.1024.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Representation Shattering in Transformers: A Synthetic Study with Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nishi25a/nishi25a.pdf)
