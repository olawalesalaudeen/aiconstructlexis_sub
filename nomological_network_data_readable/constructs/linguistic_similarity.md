# Linguistic similarity
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Cross-lingual sharing  

## State of the Field

Linguistic similarity is characterized in two distinct ways across the provided literature. The prevailing usage frames it as an internal property of a model, defined by the degree to which languages are represented similarly in the neural space. This is operationalized by measuring "inter-language activation similarity" or, as one paper puts it, quantifying the model's "internal linguistic spectrum based on overlapping neurons." A closely related concept, "cross-lingual sharing," similarly refers to the use of shared internal representations and parameters to process different languages, and is hypothesized to "facilitate multilingual generalization." In contrast, a smaller line of work defines linguistic similarity based on external, traditional linguistic features like "script, vocabulary, and grammatical structures." This latter perspective is used to explain observations that "languages closer in linguistic terms tend to share similar weaknesses." The construct is also noted to correlate with `Knowledge transferability`.

## Sources

**[Leveraging Text-to-Text Transformers as Classifier Chain for Few-Shot Multi-Label Classification](https://aclanthology.org/2025.emnlp-main.1369.pdf) (as "Cross-lingual sharing")**
> The degree to which a model utilizes shared internal representations and parameters to process information across different languages.

**[Leveraging Loanword Constraints for Improving Machine Translation in a Low-Resource Multilingual Context](https://aclanthology.org/2025.emnlp-main.1407.pdf)**
> The degree to which languages are represented similarly in the model's internal neural space, inferred from overlapping neuron activation patterns rather than external linguistic features.

## Relationships

### → Linguistic similarity
- **Knowledge transferability** (constructs) — *correlates*
  - [FoREST: Frame of Reference Evaluation in Spatial Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf)
