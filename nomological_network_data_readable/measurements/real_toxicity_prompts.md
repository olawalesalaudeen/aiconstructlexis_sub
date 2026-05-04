# Real-Toxicity-Prompts
**Type:** Measurement  
**Referenced in:** 3 papers  
**Also known as:** RealToxicPrompts  

## State of the Field

Across the provided literature, Real-Toxicity-Prompts is a dataset predominantly used to measure the construct of `Harmlessness` in language models. It is also used, though less frequently, to assess `Safety` and the behavior of `Harmful content generation`. The dataset is consistently defined as a collection of prompts for toxicity assessment, with one paper noting it contains 100,000 prompts. There are slightly different characterizations of the prompts themselves: one common description is that they are "naturally occurring prompts collected for toxicity assessment." A more specific framing, found in other work, describes them as "seemingly benign or neutral inputs" designed to "induce LLMs to generate harmful content." For evaluation, at least one paper specifies that the toxicity of model responses is measured using PerspectiveAPI. One definition also suggests the dataset can be adapted to assess sentiment and counterfactual fairness under gendered inputs, although its primary application in this set of papers is toxicity.

## Sources

**[Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference](https://aclanthology.org/2025.acl-long.128.pdf)**
> A dataset containing 100,000 prompts used to evaluate toxicity in language models, subsetted and adapted for assessing sentiment, toxicity, and counterfactual fairness under gendered inputs.

**[FCMR: Robust Evaluation of Financial Cross-Modal Multi-Hop Reasoning](https://aclanthology.org/2025.acl-long.1139.pdf) (as "RealToxicPrompts")**
> A dataset of seemingly benign or neutral prompts designed to induce large language models to generate toxic or harmful content.

**[Exploiting Contextual Knowledge inLLMs through𝒱-usable Information based Layer Enhancement](https://aclanthology.org/2025.acl-long.1532.pdf) (as "RealToxicityPrompts")**
> Toxicity assessment dataset containing naturally occurring prompts designed to elicit toxic completions, evaluated using PerspectiveAPI for Expected Maximum Toxicity and Toxicity Probability.
