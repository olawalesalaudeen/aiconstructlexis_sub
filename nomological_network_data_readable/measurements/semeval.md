# SemEval
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** SemEval-2016  

## State of the Field

Across the provided literature, the term "SemEval" refers to at least two distinct benchmark datasets used for different natural language processing tasks. One prevalent usage, identified as "SemEval 2010 Task 8," is described as a standard relation extraction dataset containing 19 relation types across diverse domains. Papers use this version to evaluate model capabilities in areas such as few-shot learning and generalization. A separate line of work utilizes "SemEval-2016," a benchmark for aspect-based sentiment analysis. This dataset is characterized by its content of "real user restaurant reviews" in multiple languages, including English, Spanish, and French, and is used to evaluate cross-lingual performance. In this context, SemEval is explicitly used as a measurement instrument for both aspect-based sentiment analysis and stance detection. Thus, the operationalization of SemEval is split, with some papers using it to assess relation extraction while others use a different version to evaluate sentiment and stance-related behaviors.

## Sources

**[BPP-Search: Enhancing Tree of Thought Reasoning for Mathematical Modeling Problem Solving](https://aclanthology.org/2025.acl-long.41.pdf) (as "SemEval-2016")**
> Benchmark dataset for aspect-based sentiment analysis containing restaurant reviews in multiple languages, used to evaluate cross-lingual performance in E2E-ABSA.

**[JuStRank: BenchmarkingLLMJudges for System Ranking](https://aclanthology.org/2025.acl-long.35.pdf)**
> Standard relation extraction dataset from SemEval 2010 Task 8, containing 19 relation types across diverse domains, used for evaluating few-shot learning and generalization.

## Relationships

### → SemEval
- **Stance detection** (behaviors tasks) — *measured_by*
  > We validate the effectiveness of our method through extensive experiments on the SemEval-2016, and VAST datasets, showing that MPVStance outperforms state-of-the-art models in zero-shot, few-shot, and challenging scenarios. (Section 1)
  - [The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc3ce215c378815ce0be41cb0f65d0b5-Paper-Conference.pdf)
- **Aspect-based sentiment analysis** (behaviors tasks) — *measured_by*
  - [BPP-Search: Enhancing Tree of Thought Reasoning for Mathematical Modeling Problem Solving](https://aclanthology.org/2025.acl-long.41.pdf)
