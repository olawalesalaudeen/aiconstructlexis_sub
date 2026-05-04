# Response aggregation
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Answer aggregation, Response fusion  

## State of the Field

Across the provided literature, response aggregation is consistently framed as the process of combining multiple answers or candidate responses into a single, improved final output. The stated goal is to produce a more reliable, higher-quality, or coherent response than any individual input. This behavior is operationalized in several ways, from selecting the most plausible answer among candidates to using a dedicated LLM as a 'Fuser' to generate a new, combined response. Some papers describe more complex implementations that involve specific sub-processes, such as "semantic conflict detection and weighted information fusion" to synthesize outputs from multiple experts ("KABB: Knowledge-Aware Bayesian Bandits for Dynamic Expert Coordination in Multi-Agent Systems"). The inputs for aggregation are described as coming from various sources, including different reasoning paths, sub-questions, or multiple expert models. Response aggregation is also studied in relation to response ranking, with one paper noting the effectiveness of using rankers before the aggregation or 'fuser' step.

## Sources

**[Similarity = Value? Consultation Value-Assessment and Alignment for Personalized Search](https://aclanthology.org/2025.emnlp-main.499.pdf) (as "Answer aggregation")**
> The process of combining answers derived from multiple sources or reasoning paths to produce a single, more reliable final answer.

**[An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf) (as "Response fusion")**
> The act of combining multiple candidate responses into a single, higher-quality output using an LLM.

**[KABB: Knowledge-Aware Bayesian Bandits for Dynamic Expert Coordination in Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aa/zhang25aa.pdf)**
> The process of synthesizing outputs from multiple selected experts into a single coherent final response, including conflict detection and weighted fusion.

## Relationships

### Associated with
- **Response ranking** (behaviors tasks)
  > Scaling the diversity of inference-time techniques included also bolsters task performance across the explored tasks, with critics and rankers before fusers being particularly effective (Figure 4; Figure 11).
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
