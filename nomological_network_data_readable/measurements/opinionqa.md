# OpinionQA
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

OpinionQA is consistently described across the provided literature as a benchmark or dataset derived from public opinion surveys, specifically from Pew Research’s American Trends Panel. Its most prevalent application is to evaluate the "distributional alignment" of large language models by comparing the distribution of their responses to those of US citizens. In addition to this primary framing, the dataset is also used to measure constructs like "Representativeness" and "Personalization". A smaller line of work defines its purpose as measuring the "steerability of LLMs for specific users or social groups" or evaluating "LLM simulation of public opinion." The benchmark is structured as a multiple-choice question-answering dataset containing responses from the US population on topics such as science, politics, and health. As an operational detail, one study notes using a specific split of the data consisting of "10.5k and 15.8k training and test QA pairs across 525 users and 15 topics."

## Sources

**[FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.598.pdf)**
> A survey-based benchmark using PEW public opinion questions and demographic-group response distributions to evaluate distributional alignment.

## Relationships

### → OpinionQA
- **Representativeness** (constructs) — *measured_by*
  - [PersonalLLM: Tailoring LLMs to Individual Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/a730abbcd6cf4a371ca9545db5922442-Paper-Conference.pdf)
- **Distribution alignment** (constructs) — *measured_by*
  - [Understanding Figurative Meaning through Explainable Visual Entailment](https://aclanthology.org/2025.naacl-long.2.pdf)
- **Personalization** (constructs) — *measured_by*
  > For OpinionQA, we use a subsampled split released by Hwang et al. (2023), which consists of 10.5k and 15.8k training and test QA pairs across 525 users and 15 topics, respectively. For GlobalOpinionQA, since the dataset originally included the answer distribution by multiple respondents in the same country, we converted it to have a single answer by selecting the choice with the highest probability. It results in 920 training and 1,317 test QA pairs across 46 countries. We consider each country as a specific user. (Section 4.1)
  - [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.598.pdf)
