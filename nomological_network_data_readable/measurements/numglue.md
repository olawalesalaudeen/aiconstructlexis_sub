# NumGLUE
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, NumGLUE is consistently presented as a benchmark used to measure mathematical and numerical reasoning abilities in models. The definitions converge on describing it as a suite of tasks requiring an understanding of numerical concepts within natural language contexts. One paper specifies that the tasks it contains "fundamentally involve arithmetic formula evaluation" (Cache-Efficient Posterior Sampling for Reinforcement Learning withLLM-Derived Priors Across Discrete and Continuous Domains). In practice, multiple papers use NumGLUE to operationalize and evaluate the construct of mathematical reasoning. Its application is frequently situated alongside other mathematical reasoning datasets, with several sources mentioning it in conjunction with GSM8K and MATH.

## Sources

**[SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)**
> A suite of mathematical reasoning tasks that require understanding of numerical concepts and language.

## Relationships

### → NumGLUE
- **Mathematical reasoning** (constructs) — *measured_by*
  > Mathematic reasoning: GSM8K math problem dataset (Cobbe et al., 2021) and NumGLUE dataset (Mishra et al., 2022). (Section 4.1.1)
  - [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
