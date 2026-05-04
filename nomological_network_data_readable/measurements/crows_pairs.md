# CrowS-Pairs
**Type:** Measurement  
**Referenced in:** 16 papers  
**Also known as:** Crows-Pairs, CrowsPairs  

## State of the Field

Across the provided literature, CrowS-Pairs is consistently characterized as a dataset or benchmark designed to measure stereotypical biases in language models. Its primary operationalization involves presenting models with pairs of sentences—one more stereotypical and one less so, referred to as ‘sent more’ and ‘sent less’—and evaluating which sentence the model prefers or deems more likely. For instance, one paper provides the example pair comparing stereotypes about people from the Middle East versus Canada smelling of perfume ("Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences"). The instrument is most frequently used to measure the constructs of `Societal bias`, `Stereotyping`, and `Fairness`. A smaller set of papers also uses it to assess broader concepts like `Harmlessness` and `Human preference alignment`, with some sources categorizing it as a general "Safety" benchmark. While one definition specifies its use for "U.S. English language models," other work demonstrates its application in different languages, specifically for "evaluating stereotype generation in Spanish and Catalan" ("ONEBench to Test Them All..."). The stereotypes it assesses are noted by one source to be associated with "historically disadvantaged groups" ("CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models").

## Sources

**[Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf)**
> Dataset for measuring the presence of stereotypical biases in language models by comparing model preferences between stereotypical and anti-stereotypical sentence pairs.

**[ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf) (as "Crows-Pairs")**
> A dataset for measuring stereotypical biases in U.S. English language models by comparing sentences with stereotypical and anti-stereotypical associations.

**[Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf) (as "CrowsPairs")**
> A benchmark for measuring stereotypical biases in language models by presenting pairs of sentences, one more stereotypical than the other, and testing which the model prefers.

## Relationships

### → CrowS-Pairs
- **Stereotyping** (constructs) — *measured_by*
  - [ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
- **Fairness** (constructs) — *measured_by*
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
- **Societal bias** (constructs) — *measured_by*
  - [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Social bias** (constructs) — *measured_by*
  - [TaCoMoE](https://aclanthology.org/2025.emnlp-main.208.pdf)
