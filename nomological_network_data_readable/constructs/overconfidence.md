# Overconfidence
**Type:** Construct  
**Referenced in:** 35 papers  
**Also known as:** Over-confidence, Overconfident generation, Probability overestimation  

## State of the Field

Across the surveyed literature, Overconfidence is predominantly characterized as a dispositional trait where a model's predicted confidence is systematically higher than its actual accuracy. This phenomenon is frequently noted to occur after fine-tuning, particularly on small datasets, and can be exacerbated by mechanisms like auto-regressive decoding. The construct is operationalized by comparing a model's confidence scores to its accuracy, with one study observing that "the accuracy within each bin is much lower than its corresponding confidence" ("Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs"). It is also identified through behaviors such as producing "assertive but incorrect responses" when addressing topics beyond the model's knowledge ("GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models"). While this framing is most common, a smaller body of work defines it more narrowly as "probability overestimation"—assigning excessive probability to unlikely tokens—or, in a game-theoretic context, as overlooking risks to pursue rewards. Several papers report that overconfidence can cause or promote Hallucination. The construct is also studied alongside Faithfulness, with which it appears to have a complex, potentially bidirectional causal relationship, and is a recurring topic in model Evaluation.

## Sources

**[It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf) (as "Over-confidence")**
> A latent property where the model's confidence in its predictions exceeds its actual accuracy, particularly exacerbated during auto-regressive decoding due to exposure bias.

**[Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf)**
> A dispositional trait where a model's predicted confidence is systematically higher than its actual accuracy, particularly after fine-tuning.

**[INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf) (as "Overconfident generation")**
> A latent tendency of a model to produce highly confident but incorrect outputs, particularly in cases where multiple consistent hallucinations are generated, evading standard consistency checks.

**[Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf) (as "Probability overestimation")**
> The model's tendency to assign excessive probability to tokens that should have a true probability of zero or near-zero.

## Relationships

### Overconfidence →
- **Faithfulness** (constructs) — *causes*
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  > Overconfidence on Unknown Knowledge LLMs often show overconfidence when addressing topics beyond their knowledge, delivering assertive but incorrect responses. ... LLMs perform poorly on unfamiliar topics while maintaining high confidence (Agarwal et al., 2023; Deng et al., 2024). (Section 3.2)
  - [LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios](https://aclanthology.org/2025.acl-long.804.pdf)

### → Overconfidence
- **Factuality** (constructs) — *causes*
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Prior knowledge** (constructs) — *causes*
  - [P](https://aclanthology.org/2025.acl-long.722.pdf)

### Associated with
- **Evaluation** (behaviors tasks)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Faithfulness** (constructs)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **Confidence calibration** (constructs)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
