# Meaning preservation
**Type:** Construct  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, meaning preservation is consistently defined as the degree to which a generated text retains the semantic or factual content of an original source. This construct is primarily discussed in the context of evaluating text generation tasks such as simplification, paraphrasing, and rewriting, where it serves as a central quality criterion. Several papers frame it in relation to other text properties, noting that it is "often lacking correlation with simplicity" ("On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena") or that it should not be sacrificed for goals like ease of translation, as one paper states, "We do not want rewrites that are easier to translate at the expense of changing the original meaning" ("KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy"). This tension is further highlighted by the mention of BETS, a metric described as "a balanced score between meaning preservation and text simplification" ("TheTIPof the Iceberg: Revealing a Hidden Class of Task-in-Prompt Adversarial Attacks onLLMs"). The field operationalizes and measures this construct in several ways, including the use of a "reading comprehension task" to assess simplification systems and specific evaluation tools like ParaPLUIE for complex rewriting cases. The overarching goal is to ensure that generated outputs, such as "simplified rewrites... still largely preserve the original meaning" ("KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy").

## Sources

**[KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)**
> The degree to which a model retains the original semantic content of the source text when generating a simplified or paraphrased version.

## Relationships

### Meaning preservation →
- **Human evaluation** (measurements) — *measured_by*
  - [VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf)
- **XCOMET** (measurements) — *measured_by*
  - [KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)
- **QuestEval** (measurements) — *measured_by*
  - [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.327.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.327.pdf)
