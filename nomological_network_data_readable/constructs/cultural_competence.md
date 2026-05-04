# Cultural competence
**Type:** Construct  
**Referenced in:** 17 papers  
**Also known as:** Cultural competency, Cultural sensitivity, Meta-cultural competence, Cultural authenticity, Cultural literacy  

## State of the Field

Across the surveyed literature, the construct of cultural competence is most frequently framed as an LLM's ability to understand, respect, and appropriately navigate diverse cultural contexts to avoid generating offensive or alienating content. This dominant view is captured by the widely used terms 'Cultural competence' and 'Cultural sensitivity', with one paper noting that effective interaction is 'contingent on outputs that are culturally relevant' ('How to MakeLLMs Forget...'). A smaller set of studies offers more specialized definitions, such as 'Cultural literacy,' which is operationalized as a model's recall of 'culturally embedded facts' ('FLRC...'), and 'Cultural authenticity,' which measures how well generated stories reflect specified sociocultural contexts. A distinct, higher-level framing is 'Meta-cultural competence,' defined not as cultural knowledge itself, but as the latent ability to 'spot cultural differences and learn about a new culture quickly and efficiently' ('Sneaking Syntax...'). Papers operationalize this construct using both `Human evaluation` and `LLM-as-a-judge` methods, with one study using GPT-4 for assessment. The construct is evaluated in specific tasks like interpreting non-verbal gestures, where models have been found to exhibit 'strong US-centric biases' ('iNews...'). Some work suggests that cultural competence is not a 'generalizable objective' and depends on the interplay between the model, probing language, and cultural context.

## Sources

**[A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.388.pdf) (as "Cultural sensitivity")**
> The ability of an LLM to acknowledge and respect differences in cultural values, communication styles, and practices to avoid generating offensive or alienating content.

**[A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.388.pdf)**
> The overall capability of an LLM to understand and appropriately navigate diverse cultural contexts, enhanced through culturally-informed training.

**[Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.408.pdf) (as "Meta-cultural competence")**
> The latent ability of an LLM or AI system to recognize cultural variation, detect when it lacks knowledge about a new culture, and adapt its responses through efficient learning and interaction strategies.

**[Grammar Control in Dialogue Response Generation for Language Learning Chatbots](https://aclanthology.org/2025.naacl-long.496.pdf) (as "Cultural competency")**
> The degree to which an LLM can accurately capture culturally nuanced knowledge across different cultural groups and prompt conditions.

**[Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment inLLMs](https://aclanthology.org/2025.emnlp-main.3.pdf) (as "Cultural authenticity")**
> The degree to which generated stories reflect the sociocultural characteristics specified in the prompt in a way that matches the intended cultural context.

**[FLRC: Fine-grained Low-Rank Compressor for EfficientLLMInference](https://aclanthology.org/2025.emnlp-main.756.pdf) (as "Cultural literacy")**
> The shared body of translinguistic cultural and factual knowledge specific to a community or nation, which is essential for effective communication and understanding within that context.

## Relationships

### Cultural competence →
- **Human evaluation** (measurements) — *measured_by*
  - [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.388.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > "To evaluate our model’s performance in these dimensions, we conduct an assessment using GPT-4 on the full test data"
  - [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.388.pdf)
