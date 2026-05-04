# World Values Survey
**Type:** Measurement  
**Referenced in:** 10 papers  
**Also known as:** World Values Survey (WVS)  

## State of the Field

The World Values Survey (WVS) is consistently described across the provided literature as a large-scale, global survey of human values, covering social, political, religious, and cultural beliefs. A prevalent application of the WVS is as a source of "seed data" or "seed questions" for generating culture-specific question-answer pairs for large language models. For instance, one study notes, "We use the World Values Survey (WVS) as seed data" ("CultureLLM: Incorporating Cultural Differences into Large Language Models"). Another common use is as a direct evaluation instrument for assessing LLMs. In this capacity, the WVS is used to measure constructs such as `Cultural alignment` and `Human preference alignment`. This evaluation is operationalized by comparing LLM responses to the ground-truth human survey data to assess the alignment of the model's value representations. Papers frequently specify using "Wave 7" of the survey, which covers 57 countries and includes data from over 129,000 human respondents. Researchers often select a subset of questions for their experiments, with one paper utilizing 260 questions and another filtering down to 206.

## Sources

**[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)**
> A cross-national survey used here as seed data for culture-specific question-answer pairs about social, political, religious, and cultural values.

**[CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf) (as "World Values Survey (WVS)")**
> A global research project and survey that explores people’s beliefs and values worldwide, used in this paper as a source of seed questions for data generation.

## Relationships

### → World Values Survey
- **Cultural alignment** (constructs) — *measured_by*
  - [Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://aclanthology.org/2025.naacl-long.350.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [QFrCoLA: aQuebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.7.pdf)
