# College Math
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, College Math is consistently described as a benchmark or dataset composed of college-level mathematics problems. Its prevailing use is to assess advanced mathematical reasoning in language models, and it is frequently evaluated alongside other instruments like Olympiad-Bench, MATH500, and Minerva Math. The problems are characterized as "challenging" and at an "undergraduate-level," positioning the benchmark as a test of sophisticated reasoning capabilities. A smaller line of work also explicitly uses College Math to evaluate a model's generalization to more advanced and "out-of-distribution" tasks, as stated in "MARGE: Improving Math Reasoning with Guided Exploration." In practice, papers report quantitative performance on the benchmark, with one study noting a model that "exceeds o1-mini by 2.7%" and another reporting gains of "+13.64%." Overall, the data shows a consensus in using College Math to evaluate model performance on complex mathematical problems that extend beyond more standard reasoning tests.

## Sources

**[MARGE: Improving Math Reasoning with Guided Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25h/gao25h.pdf) (as "CollegeMath")**
> Dataset assessing mathematical reasoning on college-level problems, used to evaluate generalization to more advanced and out-of-distribution tasks.

**[rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)**
> Benchmark of college-level mathematics problems assessing advanced mathematical knowledge and reasoning.

## Relationships

### → College Math
- **Mathematical reasoning** (constructs) — *measured_by*
  > We also incorporate two more challenging datasets, OlympiadBench (He et al., 2024) and CollegeMath (Tang et al., 2024), to further test our model’s generalizability on out-of-distribution challenging problems.
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
