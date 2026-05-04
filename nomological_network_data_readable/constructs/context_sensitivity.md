# Context sensitivity
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** Contextual sensitivity  

## State of the Field

Across the provided literature, context sensitivity is most commonly defined as the degree to which an LLM's generated goals adapt to an agent's current state, inventory, and environment to ensure relevance. This framing is supported by work that prompts models with environmental descriptions to generate context-aware goals. Other papers define the construct more broadly as a model's ability to adjust its outputs, such as rationales, in response to meaningful changes in the input, indicating reliance on "domain-specific and semantically important elements." The operationalization of this construct varies across studies. For instance, some researchers measure it by systematically altering parts of a prompt, like replacing country names, to investigate if a model's predictions are influenced by the specific context rather than general priors. Other work examines it in the domain of causal reasoning, where "the contextual information critically affects the outcomes of LLMs to discern causal connections." It is also studied in the context of language interpretation, where it refers to the ability to distinguish sarcasm from genuinely harmful content based on situational cues.

## Sources

**[Benchmarking Distributional Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.3.pdf)**
> The degree to which the LLM's generated goals adapt to the agent's current state, inventory, and environment, ensuring relevance and usefulness of the guidance.

**[Unlocking General Long Chain-of-Thought Reasoning Capabilities of Large Language Models via Representation Engineering](https://aclanthology.org/2025.acl-long.340.pdf) (as "Contextual sensitivity")**
> The ability of a model to adjust its outputs—especially rationales—in response to meaningful changes in the input context, indicating reliance on domain-specific and semantically important elements.
