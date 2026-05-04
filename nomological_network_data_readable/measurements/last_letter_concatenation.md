# Last letter concatenation
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** LLC, LastLetter, Last Letter Concatenation  

## State of the Field

Across the provided literature, Last letter concatenation is consistently framed as a benchmark task used to evaluate different forms of reasoning in language models. The task itself is a form of string manipulation where a model must "concatenate the last letters of words in a given name," as exemplified by one paper's instance of transforming "Amy Brown" into "yn". Its most prevalent application is to measure `Symbolic reasoning`, a use case supported by multiple definitions and a relationship cited across five papers. Some work also uses it to evaluate "algorithmic reasoning" and "length generalization." A less common application, found in one paper, is its use to measure `Commonsense knowledge`. The benchmark is described as both "frequently used" and a "difficult string manipulation task," with performance typically reported as accuracy on the test set.

## Sources

**[Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf) (as "LLC")**
> Last Letter Concatenation, a reasoning task and dataset where the model must concatenate the last letters of words in a given name.

**[Self-Guiding Exploration for Combinatorial Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb9120be0dcaac0aec66d2e75deb69dd-Paper-Conference.pdf) (as "LastLetter")**
> A benchmark test set used to evaluate symbolic reasoning performance.

**[Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf) (as "Last Letter Concatenation")**
> A string-manipulation benchmark used to evaluate algorithmic reasoning and length generalization in verification settings.

**[Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf)**
> A symbolic reasoning task used to test whether a model can follow letter-based transformation rules across inputs.

## Relationships

### → Last letter concatenation
- **Symbolic reasoning** (constructs) — *measured_by*
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
