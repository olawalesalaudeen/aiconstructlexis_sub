# GrailQA
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

GrailQA is consistently described in the provided literature as a benchmark for knowledge base question answering (KBQA) over the Freebase knowledge base. Its most prevalent use is to evaluate the generalization capabilities of models, particularly semantic parsing systems. The dataset is explicitly structured to assess different generalization levels, featuring splits for I.I.D., zero-shot, and compositional settings. One source specifies that its validation and test sets contain 50% zero-shot questions, 25% compositional questions, and 25% I.I.D. questions. Beyond generalizability, GrailQA is also used to measure complex reasoning, as it contains questions requiring up to 4-hop reasoning. It is referred to as a "widely-used multi-hop KGQA benchmark," and performance improvements are reported in terms of F1 scores.

## Sources

**[Context-Aware Sentiment Forecasting viaLLM-based Multi-Perspective Role-Playing Agents](https://aclanthology.org/2025.acl-long.137.pdf)**
> Knowledge base question answering benchmark focusing on complex, compositional, and zero-shot reasoning over Freebase, used to evaluate semantic parsing systems.

## Relationships

### → GrailQA
- **Generalization** (constructs) — *measured_by*
  > We experiment on GrailQA to compare the performance on different generalization levels (preliminary in Appendix D). (Section 4.3.3)
  - [Context-Aware Sentiment Forecasting viaLLM-based Multi-Perspective Role-Playing Agents](https://aclanthology.org/2025.acl-long.137.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf)
- **Knowledge graph question answering** (behaviors tasks) — *measured_by*
  > We assess the performance of SAFE on three widely-used multi-hop KGQA benchmarks: CWQ (Talmor and Berant, 2018), WebQSP (Yih et al., 2016), and GrailQA (Gu et al., 2021) (Section 5).
  - [PreP-OCR: A Complete Pipeline for Document Image Restoration and EnhancedOCRAccuracy](https://aclanthology.org/2025.acl-long.750.pdf)
- **Data efficiency** (constructs) — *measured_by*
  - [Context-Aware Sentiment Forecasting viaLLM-based Multi-Perspective Role-Playing Agents](https://aclanthology.org/2025.acl-long.137.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Context-Aware Sentiment Forecasting viaLLM-based Multi-Perspective Role-Playing Agents](https://aclanthology.org/2025.acl-long.137.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Certainty in Uncertainty: Reasoning over Uncertain Knowledge Graphs with Statistical Guarantees](https://aclanthology.org/2025.emnlp-main.442.pdf)
- **Compositional generalization** (constructs) — *measured_by*
  - [Certainty in Uncertainty: Reasoning over Uncertain Knowledge Graphs with Statistical Guarantees](https://aclanthology.org/2025.emnlp-main.442.pdf)
