# Attack effectiveness
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Effectiveness  

## State of the Field

Attack effectiveness is conceptualized as the capacity of an adversarial attack to induce unintended model behavior. The provided literature offers two related framings: one paper defines it more broadly as a "latent capacity of an adversarial prompt to successfully override a model's system prompt" ("TurnaboutLLM: A Deductive Reasoning Benchmark from Detective Games"), while another frames it more specifically as the ability to make a "web agent to perform a target action" ("Direct Judgement Preference Optimization"). Across these uses, the construct is consistently operationalized by measuring the success rate of an attack. This is measured as the "probability of generating the desired output" or is "inferred from patterns of attack success across multiple trials and models." For instance, one study evaluates this construct on "five popular LLM models across seven distinct task scenarios" and reports a strong correlation between "lower energy scores in adversarial prompts" and "higher ASR values" ("TurnaboutLLM: A Deductive Reasoning Benchmark from Detective Games").

## Sources

**[TurnaboutLLM: A Deductive Reasoning Benchmark from Detective Games](https://aclanthology.org/2025.emnlp-main.102.pdf)**
> The latent capacity of an adversarial prompt to successfully override a model's system prompt and induce unintended behavior, inferred from patterns of attack success across multiple trials and models.

**[Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.104.pdf) (as "Effectiveness")**
> The ability of an attack to successfully induce a web agent to perform a target action, measured by the probability of generating the desired output across prompts and monitors.
