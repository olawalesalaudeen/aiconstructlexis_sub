# StereoSet
**Type:** Measurement  
**Referenced in:** 16 papers  

## State of the Field

Across the provided literature, StereoSet is consistently defined as a benchmark for measuring stereotypical and social biases in language models. It is frequently used to operationalize and evaluate constructs such as `Fairness`, `Stereotyping`, and `Social bias`. The most common description of its task format is a sentence completion or cloze task, where a model is presented with a sentence containing a gap and must choose between three options: a stereotypical, an anti-stereotypical, and a meaningless or unrelated completion. Some papers specify using only the "intrasentence subset" of the benchmark, particularly when evaluating masked language models. A less frequent framing, found in one paper, describes the instrument as using crowdsourced "Context Association Tests (CATs)". In addition to bias, papers also report using StereoSet to evaluate `Language modeling` and `Stereotype recognition`. The benchmark is reported to measure stereotypical associations across domains including gender, profession, race, and religion.

## Sources

**[Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)**
> StereoSet is a benchmark for measuring stereotypical bias using sentence completions that contrast stereotypical, anti-stereotypical, and meaningless options.

## Relationships

### → StereoSet
- **Social bias** (constructs) — *measured_by*
  > We train the BiasUnlearn model on the StereoSet dataset, which is a large-scale dataset used to measure stereotypes in four domains: gender, profession, race, and religion.
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
- **Fairness** (constructs) — *measured_by*
  > As measured by prior metrics from StereoSet, our model achieves a higher degree of fairness while maintaining language modeling ability with low cost12.
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
- **Stereotyping** (constructs) — *measured_by*
  > Both datasets [StereoSet and CrowS-Pairs] emerged during a similar timeframe, focus on measuring stereotypical bias in language models, and use comparable methods for data gathering and bias measurement, making them ideal candidates for comparative analysis. (Section 3.1)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **Sentence completion** (behaviors tasks) — *measured_by*
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > LMS is used to evaluate the language modeling abilities of models. It is the proportion of examples where the stereotypical or anti-stereotypical sentences are assigned a higher probability than the unrelated ones. (Section 4.4)
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
- **Stereotype recognition** (behaviors tasks) — *measured_by*
  - [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf)
