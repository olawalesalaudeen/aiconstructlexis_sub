# MultiRC
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

Across the provided literature, MultiRC is consistently framed as a benchmark dataset for "Multi-Sentence Reading Comprehension." The most prevalent description characterizes it as a multiple-choice dataset where questions require reasoning over or deriving answers from multiple sentences within a text. One paper adds that questions may have multiple correct answers, and another specifies that it is evaluated with exact-match accuracy. The provided data indicates that MultiRC is used to measure two constructs: "Reading comprehension" and "Faithfulness." In practice, it is used as a task to compare the performance and efficiency of different models and methods. For example, one study notes that "Successful fine-tuning on MultiRC implies Addax can handle smaller tasks as well" ("Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models").

## Sources

**[BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)**
> Multi-Sentence Reading Comprehension, a multiple choice dataset evaluated with exact-match accuracy.

## Relationships

### → MultiRC
- **Reading comprehension** (constructs) — *measured_by*
  - [Regress, Don’t Guess: A Regression-like Loss on Number Tokens for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zausinger25a/zausinger25a.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
