# Omni-MATH
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** Omini-MATH, OmniMath, Omni-Math  

## State of the Field

Across the provided sources, Omni-MATH is consistently characterized as a benchmark used to evaluate mathematical reasoning in large language models. The prevailing definition describes it as a comprehensive dataset covering a "broad spectrum of difficulty levels" and diverse topics. A recurring theme, particularly in several papers, is its focus on high-difficulty "olympiad-style" or "competition-level" problems. In line with this framing, the benchmark is most frequently used to measure 'Mathematical reasoning', with one source also stating it assesses 'Problem-solving' and 'Complex reasoning' capabilities. The full benchmark is reported to contain 4.4K questions and is often evaluated alongside other instruments like GSM8K, MATH, and AIME. A common practice noted in multiple papers is the use of a randomly sampled 500-question subset, sometimes referred to as Omni-MATH-500, for more efficient assessment.

## Sources

**[OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)**
> Omni-MATH is a mathematics benchmark covering a broad spectrum of difficulty levels for evaluating math reasoning models.

**[AnRe: Analogical Replay for Temporal Knowledge Graph Forecasting](https://aclanthology.org/2025.acl-long.232.pdf) (as "Omini-MATH")**
> Mathematical reasoning dataset from which 500 randomly sampled questions were used to evaluate model performance efficiently.

**[Beyond Similarity: A Gradient-based Graph Method for Instruction Tuning Data Selection](https://aclanthology.org/2025.acl-long.1190.pdf) (as "OmniMath")**
> A comprehensive mathematical reasoning benchmark covering diverse topics and difficulty levels, including olympiad-style problems.

**[RBench: Graduate-level Multi-disciplinary Benchmarks for LLM & MLLM Complex Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25r/guo25r.pdf) (as "Omni-Math")**
> A benchmark focused on employing mathematical olympiad challenges to evaluate mathematical reasoning.

## Relationships

### → Omni-MATH
- **Mathematical reasoning** (constructs) — *measured_by*
  > We evaluate our models on a set of common benchmarks that consists of GSM8K (1.3K examples), MATH (5K examples), AMC 2023 (40 examples), AIME 2024 (30 examples), and Omni-MATH (4.4K examples) ... These datasets cover a broad spectrum of difficulty levels, ranging from grade school mathematics to advanced competition problems.
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > We introduce Omni-Math, a universal Olympiad-level mathematical benchmark with over 33 sub-domains and diverse difficulty levels, posing new challenges to the problem solving and complex reasoning capability of LLMs. (Section 1)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
