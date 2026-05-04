# Error propagation
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Error accumulation  

## State of the Field

Across the provided literature, "Error propagation" is conceptualized in two distinct contexts: as an internal failure mode in sequential reasoning and as a communication breakdown in multi-agent systems. The first framing, also termed "Error accumulation," describes the tendency for mistakes in early reasoning steps to compound and lead to an incorrect final answer. This effect is reported to be exacerbated as reasoning chains grow longer, with one paper noting that "the accumulation of intermediate mistakes increasingly undermines final output accuracy" ("Improving Reasoning Capabilities..."). In this context, the construct is operationalized through evaluation on benchmarks like ARES, which is used to detect propagated errors in long reasoning chains. Furthermore, the absence of mechanisms like Backtracking is reported to worsen error propagation by preventing the correction of early missteps. A second line of work defines error propagation in multi-agent systems, where it refers to erroneous information from one agent spreading through a communication network to negatively influence the system's output. This perspective is concerned with network topology, with denser communication structures being described as "more susceptible to error spreading" ("CMHG..."). Within this multi-agent framing, error propagation is also studied in relation to the concept of Safety.

## Sources

**[Improving Reasoning Capabilities in Small Models through Mixture-of-layers Distillation with Stepwise Attention on Key Information](https://aclanthology.org/2025.emnlp-main.251.pdf) (as "Error accumulation")**
> The tendency for mistakes made in early steps of a sequential reasoning process to propagate and compound, leading to an incorrect final answer.

**[CMHG: A Dataset and Benchmark for Headline Generation of Minority Languages inChina](https://aclanthology.org/2025.emnlp-main.623.pdf)**
> The tendency for erroneous information from one agent to spread through the communication network and negatively influence the final output of the multi-agent system.

## Relationships

### Error propagation →
- **ARES** (measurements) — *measured_by*
  > "ARES achieves state-of-the-art performance across four benchmarks ... and demonstrates superior robustness on very long synthetic reasoning chains, where it excels at detecting propagated errors"
  - [Avoidance Decoding for Diverse Multi-Branch Story Generation](https://aclanthology.org/2025.emnlp-main.382.pdf)

### → Error propagation
- **Backtracking** (behaviors tasks) — *causes*
  > The performance drop highlights the importance of backtracking in mitigating error propagation, where an early misstep without backtracking cannot be corrected, resulting in deteriorated performance. (Section 5.3)
  - [End-to-End Learnable Psychiatric Scale Guided Risky Post Screening for Depression Detection on Social Media](https://aclanthology.org/2025.emnlp-main.202.pdf)

### Associated with
- **Robustness** (constructs)
  - [CMHG: A Dataset and Benchmark for Headline Generation of Minority Languages inChina](https://aclanthology.org/2025.emnlp-main.623.pdf)
