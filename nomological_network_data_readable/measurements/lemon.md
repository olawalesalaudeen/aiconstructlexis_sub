# LEMON
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

LEMON is presented in the provided literature as a measurement instrument for Chinese Spelling Correction (CSC). It is consistently defined as a large-scale, multi-domain dataset featuring real-world spelling errors across seven specified sub-domains: game, encyclopedia, contract, medical care, car, novel, and news. The most prevalent use of LEMON, as indicated by the relationships, is to operationalize and measure model generalization. Specifically, papers use it to assess cross-domain generalization, with one source stating it "serves as a cross-domain dataset for evaluating the generalization capabilities." Another source notes its utility for this purpose stems from containing "longer and more complex sentences." One paper also uses it for "Evaluation" more broadly. The dataset is reportedly used to test a model's "domain correction capabilities in a zero-shot setting."

## Sources

**[Do Large Language Models have anEnglish Accent? Evaluating and Improving the Naturalness of MultilingualLLMs](https://aclanthology.org/2025.acl-long.194.pdf)**
> A large-scale, multi-domain Chinese Spelling Correction dataset featuring real-world spelling errors across seven sub-domains including game, encyclopedia, contract, medical care, car, novel, and news.

## Relationships

### → LEMON
- **Cross-domain generalization** (constructs) — *measured_by*
  - [Opt-Out: Investigating Entity-Level Unlearning for Large Language Models via Optimal Transport](https://aclanthology.org/2025.acl-long.1372.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [The Good, the Bad and the Constructive: Automatically Measuring Peer Review’s Utility for Authors](https://aclanthology.org/2025.emnlp-main.1477.pdf)
- **Generalization** (constructs) — *measured_by*
  > To further assess the generalization ability of our models, we evaluated them on the LEMON dataset, which contains longer and more complex sentences.
  - [MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis](https://aclanthology.org/2025.acl-long.678.pdf)
