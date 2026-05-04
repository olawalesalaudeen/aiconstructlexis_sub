# Sentiment steering
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Sentiment expression, Sentiment generation  

## State of the Field

Sentiment steering is consistently described across the provided sources as the task of generating text that conveys a specific, controlled emotional tone. The definitions, using terms like "sentiment generation" and "sentiment expression," converge on the idea of producing text, such as movie reviews, with a designated positive or negative sentiment. This behavior is operationalized and measured in a few ways within the surveyed literature. For instance, one paper describes the task in the context of the IMDb dataset, where the objective is to generate reviews that balance positive sentiment with conciseness. Another study demonstrates controlling this behavior by directly manipulating sentiment features to increase or decrease the expression of positive and negative tones. The SST-5 benchmark is also cited as a measurement instrument for this task.

## Sources

**[MPO: An Efficient Post-Processing Framework for Mixing Diverse Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25af/wang25af.pdf) (as "Sentiment generation")**
> The task of generating text, such as movie reviews, that exhibits a specific emotional tone like positive sentiment.

**[Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf) (as "Sentiment expression")**
> The generation of text that conveys a specific emotional tone, such as positive or negative sentiment.

## Relationships

### Sentiment steering →
- **SST-5** (measurements) — *measured_by*
  - [On Synthetic Data Strategies for Domain-Specific Generative Retrieval](https://aclanthology.org/2025.acl-long.393.pdf)
