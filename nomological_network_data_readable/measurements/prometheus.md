# Prometheus
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, Prometheus is consistently described as an open-source, LLM-based evaluation model, or 'LLM judge,' trained to assess the outputs of other language models. A prevalent application is scoring the quality of summaries, where it is defined as using a 1-5 scale to evaluate dimensions such as interest, coherence, relevance, coverage, and diversity. However, its use extends to other tasks, with different papers adapting it for assessing translation quality, text-to-SQL generation, and scoring generated articles. This variation is reflected in its operationalization; for instance, while summarization is scored on a 1-5 scale, article evaluation is reported using a 0-5 scale with distinct criteria like relevance, breadth, depth, and novelty. Some sources refer to a specific version, 'Prometheus 2,' which is identified as a 7-billion-parameter model. Regarding its performance, one study reports it achieves 72-85% human agreement, while another notes that in a different context, it 'showed a marginally lower agreement than EX'. A more general framing, found in one paper, describes Prometheus as a tool for 'general human preference evaluation in natural language generation'.

## Sources

**[Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.548.pdf)**
> An LLM-based evaluation model used to score the quality of summaries on a 1-5 scale across dimensions like interest, coherence, relevance, coverage, and diversity.
