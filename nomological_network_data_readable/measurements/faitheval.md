# FaithEval
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

FaithEval is characterized in the provided literature as an evaluation benchmark designed to measure model hallucination and faithfulness. According to its definition, it assesses model performance across "different challenging scenarios" with the goal of both measuring and ultimately reducing hallucination. The relationships show it is explicitly used to operationalize the constructs of Hallucination and Faithfulness. For example, one paper uses FaithEval in an ablation study to show that a new method "reduces hallucinations as a valuable secondary benefit" ("MadaKV: Adaptive Modality-PerceptionKVCache Eviction for Efficient Multimodal Long-Context Inference"). The benchmark is also studied alongside other assessment methods, including LLM-as-a-judge and Human evaluation.

## Sources

**[MadaKV: Adaptive Modality-PerceptionKVCache Eviction for Efficient Multimodal Long-Context Inference](https://aclanthology.org/2025.acl-long.653.pdf)**
> An evaluation benchmark designed to measure and reduce model hallucination across different challenging scenarios.

## Relationships

### → FaithEval
- **Faithfulness** (constructs) — *measured_by*
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  > As shown in Table 5, the ablation study on FaithEval (Ming et al., 2024) demonstrates that OpAmp not only enhances robustness to noisy contexts but also reduces hallucinations as a valuable secondary benefit. (Section 3.4)
  - [MadaKV: Adaptive Modality-PerceptionKVCache Eviction for Efficient Multimodal Long-Context Inference](https://aclanthology.org/2025.acl-long.653.pdf)

### Associated with
- **LLM-as-a-judge** (measurements)
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **Human evaluation** (measurements)
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
