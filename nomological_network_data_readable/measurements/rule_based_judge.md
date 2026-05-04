# Rule-based judge
**Type:** Measurement  
**Referenced in:** 3 papers  
**Also known as:** Rule-based Judge, Rule-based judgment  

## State of the Field

The 'Rule-based judge' is consistently described across the provided literature as an evaluation procedure used to assess the behavior of 'Jailbreaking'. The method is operationalized as a heuristic that applies predefined rules to a model's output to determine if a jailbreak attack was successful. One paper specifies this mechanism as a "keyword matching approach to judge if there are any rejected words in the response" ('ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs'). This evaluation is characterized as operating "without semantic understanding" ('Does Refusal Training in LLMs Generalize to the Past Tense?'). In some contexts, it is used alongside other evaluation methods, such as "Llama-Guard-2 judgment" ('ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs'). Multiple sources refer to this as a "simple rule-based judge from Zou et al. (2023)".

## Sources

**[Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)**
> A rule-based evaluation procedure from prior work used to assess whether a response constitutes a jailbreak.

**[Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf) (as "Rule-based Judge")**
> A heuristic evaluation procedure that uses predefined rules to detect jailbreaks without semantic understanding.

**[ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf) (as "Rule-based judgment")**
> An evaluation method that uses keyword matching to determine if a model's response contains specific rejected words, thereby judging if a jailbreak attack was successful.

## Relationships

### → Rule-based judge
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf)
