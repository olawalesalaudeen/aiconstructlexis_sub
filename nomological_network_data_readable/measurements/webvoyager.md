# WebVoyager
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

WebVoyager is consistently described across the provided literature as a measurement instrument, specifically a "dynamic, real-world web dataset" for evaluation. Its most common application is to measure the behavior of `Web navigation`, with some papers specifying its use for "vision-based web navigation" on real websites. It is also explicitly used to assess the construct of `Generalization`, with one definition characterizing it as an "out-of-distribution benchmark" that "covers diverse domains that are unseen in the WebArena environment." A recurring theme is its use for assessing "task completion in realistic environments," and it is also defined as a tool for evaluating `long-horizon planning`. Performance on the benchmark is reported in terms of "success rate," and it is applied to both text-only and vision-based tasks.

## Sources

**[Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/erdogan25a/erdogan25a.pdf)**
> Dynamic, real-world web dataset for evaluating long-horizon planning in web navigation, assessing task completion in realistic environments.

## Relationships

### → WebVoyager
- **Generalization** (constructs) — *measured_by*
  - [AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2c6e459b95694a24ac69c469a4ee746-Paper-Conference.pdf)
- **Web navigation** (behaviors tasks) — *measured_by*
  > “as well as a text-only state-of-the-art 81.36% success rate on WebVoyager.”
  - [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ah/zhou25ah.pdf)
