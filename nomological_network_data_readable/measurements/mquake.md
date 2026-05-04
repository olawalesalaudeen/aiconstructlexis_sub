# MQUAKE
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** MQuAKE  

## State of the Field

Across the provided literature, MQUAKE is consistently defined as a benchmark for evaluating knowledge editing in language models. The benchmark's task format is centered on multi-hop question answering, where models are required to reason over facts that have been edited. One paper specifies that MQUAKE "considers different numbers of hops (from 2 to 4) and different positions of the knowledge used in the multi-hop questions" ("Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis"). The most prevalent use of MQUAKE is to measure both `Complex reasoning` and `Multi-hop question answering`. A smaller set of studies also employs the benchmark to assess other capabilities, such as `Counterfactual reasoning` and `Faithfulness`.

## Sources

**[AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)**
> A benchmark for evaluating model editing on multi-hop knowledge questions.

**[Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf) (as "MQuAKE")**
> Multi-hop knowledge editing benchmark that evaluates models on question-answering tasks requiring reasoning over edited facts, with versions varying in hop count and temporal knowledge.

## Relationships

### → MQUAKE
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [From Capabilities to Performance: Evaluating Key Functional Properties ofLLMArchitectures in Penetration Testing](https://aclanthology.org/2025.emnlp-main.803.pdf)
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  - [MQuAKE-Remastered: Multi-Hop Knowledge Editing Can Only Be Advanced with Reliable Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/f782860c2a5d8f675b0066522b8c2cf2-Paper-Conference.pdf)
- **Counterfactual reasoning** (constructs) — *measured_by*
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
