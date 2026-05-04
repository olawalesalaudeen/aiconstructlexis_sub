# ANLI
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

Across the provided literature, ANLI is consistently characterized as a benchmark dataset for Adversarial Natural Language Inference (NLI). A recurring theme is its creation through an "iterative, adversarial human-and-model-in-the-loop process," with one paper noting its "primary aim" is "to make SoTA models fail." The dataset is used to measure both `Natural language inference` and `Commonsense understanding`. Some papers also position it as a tool for testing "robust reasoning" and evaluating "Open-domain Reasoning." In practice, ANLI is employed as a classification benchmark for model evaluation, often alongside other datasets like GLUE and SQuAD. One study specifies the use of its "challenging subsets ANLI-A2 and ANLI-A3" for its evaluation. The prevailing usage of ANLI is as a challenging, adversarially constructed instrument to assess model capabilities in NLI and related reasoning tasks.

## Sources

**[Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf)**
> Adversarial Natural Language Inference, included as a classification benchmark in the expanded evaluation set.

## Relationships

### → ANLI
- **Natural language inference** (behaviors tasks) — *measured_by*
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [AutoPSV: Automated Process-Supervised Verifier](https://proceedings.neurips.cc/paper_files/paper/2024/file/9246aa822579d9b29a140ecdac36ad60-Paper-Conference.pdf)
