# Misalignment
**Type:** Construct  
**Referenced in:** 5 papers  

## State of the Field

The provided literature presents two distinct framings of Misalignment. One line of work defines it as a latent, unsafe tendency within a model that can be hidden in one setting and activated in another. In this view, a "safety misalignment remains dormant in a full-precision LLM but becomes exploitable post-quantization." This form of misalignment is operationalized through its outcomes, as it is reported to cause the generation of harmful content. Alternatively, another paper treats misalignment as a model's failure to follow instructions and produce valid, actionable outputs within a specific domain. This is exemplified by a model's "deficiency in identifying essential information for constructing valid routes." Under this framing, misalignment is used as a metric to measure the performance of LLMs in outputting valid instructions. The concept is also studied in relation to other model risks, such as hallucination.

## Sources

**[Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)**
> A latent unsafe tendency in the model that can be hidden in one setting and activated in another, leading to harmful outputs.

## Relationships

### Misalignment →
- **Harmful content generation** (behaviors tasks) — *causes*
  > safety misalignment remains dormant in a full-precision LLM but becomes exploitable post-quantization... enables the generation of harmful content
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  > Discussed in Section 6 (Limitations) and Appendix A.5 (Error Analysis), where risks such as retrieval failure, hallucinations, misalignment, and layout errors are described.
  - [2025.emnlp-main.1443.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1443.checklist.pdf)
