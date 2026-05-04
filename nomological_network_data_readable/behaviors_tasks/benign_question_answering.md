# Benign question answering
**Type:** Behavior  
**Referenced in:** 3 papers  

## State of the Field

Based on the available literature, benign question answering is defined as the task of responding helpfully and accurately to standard, non-adversarial user questions. This behavior is primarily used to evaluate whether model defense mechanisms inadvertently degrade performance on normal queries, specifically by checking if they cause a model to refuse to answer "benign prompts." The task is operationalized and measured using the TriviaQA dataset, which is described as a "normal question-answering dataset for reading comprehension." As detailed in "Protecting Your LLMs with Information Bottleneck," performance on this behavior is quantified using a metric called the Benign Answering Rate (BAR).

## Sources

**[Protecting Your LLMs with Information Bottleneck](https://proceedings.neurips.cc/paper_files/paper/2024/file/34a1fc7890141f1ada3d8bc6199cce07-Paper-Conference.pdf)**
> The task of responding helpfully and accurately to standard, non-adversarial user questions.

## Relationships

### Benign question answering →
- **TriviaQA** (measurements) — *measured_by*
  - [Protecting Your LLMs with Information Bottleneck](https://proceedings.neurips.cc/paper_files/paper/2024/file/34a1fc7890141f1ada3d8bc6199cce07-Paper-Conference.pdf)
