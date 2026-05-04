# MovieLens
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** Movielens  

## State of the Field

Across the provided literature, MovieLens is predominantly characterized as a benchmark dataset for recommendation systems research. The dataset is consistently defined as containing user ratings and metadata for movies. In its most common application, it is used to measure behaviors such as `Sequential recommendation` and `Prompt engineering`, particularly in the context of LLM-based recommenders. For example, one study notes its use with an "LLM4Rec model on the MovieLens and LastFM datasets" ("Unified Parameter-Efficient Unlearning for LLMs"). A less frequent framing, presented in a single paper, adapts MovieLens from the MovieLens-25M version into a multi-tabular dataset. In this alternative use case, it serves to evaluate graph construction methods on a "relation attribute prediction task" ("AutoG: Towards automatic graph construction from tabular data").

## Sources

**[Customizing Language Models with Instance-wise LoRA for Sequential Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd476d01692c508ddf1cb43c6279a704-Paper-Conference.pdf)**
> A widely used benchmark dataset in recommendation systems research, containing user ratings and metadata for movies.

**[AutoG: Towards automatic graph construction from tabular data](https://proceedings.iclr.cc/paper_files/paper/2025/file/c01dfe01b97aadc10fc16a201faa80d8-Paper-Conference.pdf) (as "Movielens")**
> A multi-tabular dataset adapted from the MovieLens-25M dataset, used to evaluate graph construction methods on a relation attribute prediction task.

## Relationships

### → MovieLens
- **Sequential recommendation** (behaviors tasks) — *measured_by*
  - [On Softmax Direct Preference Optimization for Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/30732ddb12d9faf7180f5d0e8b5b5da7-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks) — *measured_by*
  > Experimental results on the QM task, using LLaRA as the LLM4Rec model on the MovieLens and LastFM datasets. (Table 3)
  - [Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf)
