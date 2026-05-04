# SPIDER-Realistic
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Spider-Realistic  

## State of the Field

Across the provided sources, SPIDER-Realistic is consistently described as a measurement instrument derived from the SPIDER benchmark. Its defining feature, as noted in all definitions, is the removal of "explicitly mentioned column names" from the natural language questions. This modification is intended to "simulate more realistic question settings" and "better reflect real-world scenarios" for text-to-SQL tasks. One paper specifies that this benchmark is derived from the "SPIDER development set" ("ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL"). It is also presented alongside other Spider-derived benchmarks like Spider-DK and Spider-Syn, which make different modifications to the original dataset ("EPO: Explicit Policy Optimization for Strategic Reasoning inLLMs via Reinforcement Learning"). Therefore, SPIDER-Realistic is used to evaluate text-to-SQL systems in a setting that more closely mirrors practical use cases where users may not know or use exact schema names in their queries.

## Sources

**[ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)**
> A SPIDER-derived benchmark that removes explicit column-name mentions to simulate more realistic question settings.

**[EPO: Explicit Policy Optimization for Strategic Reasoning inLLMs via Reinforcement Learning](https://aclanthology.org/2025.acl-long.748.pdf) (as "Spider-Realistic")**
> A variant of the Spider benchmark where explicitly mentioned column names are removed from the questions to better reflect real-world scenarios.
