# L-Eval
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** L-eval  

## State of the Field

Across the provided literature, L-Eval is predominantly characterized as a benchmark designed to assess the long-context capabilities of large language models. Papers use L-Eval to measure several related constructs, most commonly `Long-context processing` and `Long-context understanding`, with one paper also using it to evaluate `Long-form text generation`. The benchmark is consistently described as an evaluation suite composed of closed-ended tasks with varying input lengths, specifically multiple-choice and true/false question answering. One study specifies that its evaluation uses four particular closed-ended tasks from L-Eval: TOFEL, QuALITY, Coursera, and SFiction. In practice, L-Eval is often studied alongside other long-context benchmarks, including LongBench and LooGLE. A less common framing, found in one paper, describes L-Eval as a benchmark for "long-text and reasoning-oriented evaluations" used for comparative purposes with another benchmark, CS-Bench. The prevailing usage, therefore, positions L-Eval as an instrument for evaluating how LLMs handle long contexts, operationalized through a set of closed-ended question-answering tasks.

## Sources

**[CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf) (as "L-eval")**
> L-eval is a benchmark used for comparing CS-Bench with long-text and reasoning-oriented evaluations.

**[Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)**
> L-Eval is a benchmark designed to assess the long-context capabilities of LLMs, featuring closed-ended tasks such as multiple-choice and true/false question answering.

## Relationships

### → L-Eval
- **Long-context understanding** (constructs) — *measured_by*
  > “LongBench, L-eval and LooGLE serve as multitask benchmarks, providing a comprehensive evaluation of long-context understanding”
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
