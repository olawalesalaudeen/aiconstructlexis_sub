# Misinformation detection
**Type:** Behavior  
**Referenced in:** 11 papers  
**Also known as:** Rumor detection, Fake news detection  

## State of the Field

Across the provided sources, misinformation detection is characterized as an observable classification task focused on text. The behavior is described under several names, including "rumor detection," "fake news detection," and "misinformation detection," with definitions generally involving the identification or classification of problematic content. One paper details a specific approach to "fake news detection" where an agent "uses structured debates to identify logical and factual flaws for detection." Another framing, for "rumor detection," specifies that the task relies on a text's "content and context." To operationalize and assess this behavior, papers use specific benchmarks. The task of misinformation detection is reported to be measured by the PHEME and Weibo21 datasets. The behavior is also studied in relation to "Evaluation," consistent with its treatment as a formal task.

## Sources

**[2025.emnlp-main.407.checklist](https://aclanthology.org/attachments/2025.emnlp-main.407.checklist.pdf) (as "Rumor detection")**
> The observable task of identifying whether a given piece of text is a rumor based on its content and context.

**[From Long to Lean: Performance-aware and Adaptive Chain-of-Thought Compression via Multi-round Refinement](https://aclanthology.org/2025.emnlp-main.619.pdf) (as "Fake news detection")**
> Classifying news content as true or fake based on its textual content and supporting debate evidence.

**[2025.emnlp-main.1405.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1405.checklist.pdf)**
> The observable task of classifying a piece of text as containing or not containing misinformation.

## Relationships

### Misinformation detection →
- **PHEME** (measurements) — *measured_by*
  - [NusaAksara: A Multimodal and Multilingual Benchmark for PreservingIndonesian Indigenous Scripts](https://aclanthology.org/2025.acl-long.1378.pdf)
- **Weibo21** (measurements) — *measured_by*
  - [NusaAksara: A Multimodal and Multilingual Benchmark for PreservingIndonesian Indigenous Scripts](https://aclanthology.org/2025.acl-long.1378.pdf)

### Associated with
- **Claim verification** (behaviors tasks)
  - [B4: A Black-Box Scrubbing Attack onLLMWatermarks](https://aclanthology.org/2025.naacl-long.461.pdf)
