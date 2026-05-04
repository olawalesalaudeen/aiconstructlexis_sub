# MAGE
**Type:** Measurement  
**Referenced in:** 3 papers  

## State of the Field

Across the provided literature, MAGE is presented with a dual identity, functioning as both a model and a dataset for AI text detection. One paper defines MAGE as a supervised fine-tuned model that classifies text as human or machine-generated through binary classification on linguistic features. In this framing, it is listed among a suite of other "prominent detectors" like GPT-Zero and Radar. In contrast, another paper refers to the "MAGE dataset," describing it as a "machine-generated text detection benchmark" composed of documents from 10 domains. This dataset is used to train and evaluate other pretrained models, such as RoBERTa and DeBERTav3, on the task of detecting machine-generated text. This application positions MAGE as an instrument for measuring a form of authorship attribution by identifying machine-generated content.

## Sources

**[MultiMed-ST: Large-scale Many-to-many Multilingual Medical Speech Translation](https://aclanthology.org/2025.emnlp-main.600.pdf)**
> A supervised fine-tuned model for AI text detection that classifies text as human or machine-generated using binary classification on linguistic features.

## Relationships

### → MAGE
- **Authorship attribution** (behaviors tasks) — *measured_by*
  > For the machine-generated text detector, we trained and evaluated three pretrained models (RoBERTa, DeBERTav3, and ModernBERT) on the MAGE dataset (Li et al., 2024), a machine-generated text detection benchmark based on documents from 10 domains.
  - [MetaFaith: Faithful Natural Language Uncertainty Expression inLLMs](https://aclanthology.org/2025.emnlp-main.1506.pdf)
