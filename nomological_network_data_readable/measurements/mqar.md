# MQAR
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided sources, MQAR (Multi-Query Associative Recall) is consistently defined as a benchmark task designed to evaluate a model's ability to perform associative recall. The literature states that it is used to measure constructs such as `Knowledge recall` and `Factuality`. The task's objective is to assess a model's capacity to retrieve values associated with specific keys from a given context. One definition elaborates that this context contains "multiple key-value pairs and distractors" ("Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity"). Regarding its operationalization, one study notes that "The MQAR task involves training a small-parameter model from scratch using a specific dataset" ("Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions"). The papers position MQAR as one of the available tasks for evaluating a model's associative recall capabilities.

## Sources

**[Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)**
> The Multi-Query Associative Recall task, a benchmark designed to assess a model's ability to retrieve values associated with keys from a context.

## Relationships

### → MQAR
- **Knowledge recall** (behaviors tasks) — *measured_by*
  > The model’s recall capability is assessed using the MQAR Task (See Appendix D.7), as described in Arora et al. (2024a). (Figure 1)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
- **Recall** (constructs) — *measured_by*
  - [Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf)
