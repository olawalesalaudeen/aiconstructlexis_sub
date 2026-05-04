# Minerva Math
**Type:** Measurement  
**Referenced in:** 11 papers  

## State of the Field

Across the provided literature, Minerva Math is consistently characterized as a benchmark used to evaluate the mathematical reasoning capabilities of models. The definitions describe it as both a general "math benchmark" and more specifically as a "Mathematical reasoning benchmark designed to evaluate models on a wide range of math problems." Its primary application, as evidenced by numerous papers, is to measure or assess mathematical reasoning, often as part of a larger evaluation suite that includes other benchmarks like MATH500, OlympiadBench, AIME24, and GSM8K. While its prevalent use is for general mathematical reasoning evaluation, some papers describe more targeted applications, such as using it to "assess generalization of the FANS framework" or, in combination with LiveCodeBench, "to evaluate model selection under accurate ex-ante quality estimation." The provided data shows a strong consensus on its function, with all sources framing it as an instrument for evaluating performance on challenging math problems.

## Sources

**[A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)**
> Minerva Math is a math benchmark used in combination with LiveCodeBench to evaluate model selection under accurate ex-ante quality estimation.

## Relationships

### → Minerva Math
- **Mathematical reasoning** (constructs) — *measured_by*
  > Second, to simulate a use-case where ex-ante quality estimation is accurate, we use the Math and Coder models from the QWEN-2.5 model family (Yang et al., 2024; Hui et al., 2024) and evaluate them on a combination of Minerva Math (Lewkowycz et al., 2022) and LiveCodeBench (Jain et al., 2024). (Section 5.2)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
