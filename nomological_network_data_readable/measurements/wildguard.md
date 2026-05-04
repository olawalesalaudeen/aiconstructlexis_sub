# WildGuard
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** WildGuardTest  

## State of the Field

Across the provided literature, the term 'WildGuard' refers to two distinct but related measurement instruments: a dataset of prompts and a classifier-based evaluation procedure, with the latter being the more prevalent usage. In its most common framing, WildGuard is a classifier or harmfulness detection model used as an external safety evaluator. It is operationalized to automatically judge model outputs, either by classifying them as compliance or refusal to a harmful query or by assigning a "harmfulness probability" to a response, as one paper notes. A smaller set of papers refers to 'WildGuardTest,' an evaluation dataset containing prompts designed to assess model safety and "moderation robustness" ('SafetyAnalyst...'). The composition of this dataset is described with some variation; one source states it contains 863 harmful persuasion prompts and 862 safe prompts, while another characterizes it as having "960 vanilla and 796 adversarial prompts" ('SafetyAnalyst...'). Both the dataset and the classifier are used to evaluate model safety, and the instrument is cited as a measure for the construct of 'Content moderation'.

## Sources

**[Beyond Mere Token Analysis: A Hypergraph Metric Space Framework for Defending Against Socially Engineered LLM Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/18699b47bb4abf5f92b0b73266b3ffc8-Paper-Conference.pdf) (as "WildGuardTest")**
> An evaluation dataset consisting of 1725 prompts, with 863 harmful persuasion prompts and 862 safe prompts.

**[Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)**
> WildGuard, a classifier-based evaluation procedure used to judge whether model responses fully comply with harmful test queries.

## Relationships

### → WildGuard
- **Content moderation** (behaviors tasks) — *measured_by*
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf)
