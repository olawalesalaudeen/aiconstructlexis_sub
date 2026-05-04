# Style transfer
**Type:** Behavior  
**Referenced in:** 10 papers  
**Also known as:** Text style transfer, Template rewriting  

## State of the Field

Across the surveyed literature, "Style transfer" is predominantly described as the task of modifying an output's style while preserving its core content or meaning. The most common application is in the linguistic domain, where it is operationalized as rewriting text to match a target style, such as that of a specific author, a different sentiment, or a different level of formality. For instance, one study uses prompts to request rewrites in a "more (or less) formal style" ("Context andPOSin Action: A Comparative Study ofChinese Homonym Disambiguation in Human and Language Models"). A more specific variant is termed "Template rewriting," where a model adapts a structured sentence to a new domain-specific style. However, a smaller set of papers applies the concept to vision, defining it as generating an image that combines the content of one source image with the artistic style of another. One paper suggests that "Prompt engineering" can be adapted to perform this task. The behavior is frequently studied alongside the construct of "Semantic preservation," reflecting the common requirement to maintain the original meaning, as well as "Linguistic quality," "Hallucination," and "Repetitive generation."

## Sources

**[Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)**
> The task of modifying the linguistic style of a model's output to match a target style, such as that of a specific author or dataset.

**[Evolving Prompts In-Context: An Open-ended, Self-replicating Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25aj/wang25aj.pdf) (as "Text style transfer")**
> The task of rewriting a given text to conform to a different style, such as sentiment, while preserving its core content.

**[Aspect-Oriented Summarization for Psychiatric Short-Term Readmission Prediction](https://aclanthology.org/2025.emnlp-main.1424.pdf) (as "Template rewriting")**
> The observable action of a generative model taking a structured template sentence as input and producing a new sentence that preserves the original meaning but matches a target linguistic style.

## Relationships

### → Style transfer
- **Prompt engineering** (behaviors tasks) — *causes*
  > VGD can also be easily adapted to style transfer. (Section 4.2)
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)

### Associated with
- **Semantic preservation** (constructs)
  - [Pareto Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf)
- **Fluency** (constructs)
  - [Reliability of Topic Modeling](https://aclanthology.org/2025.naacl-long.135.pdf)
- **Hallucination** (behaviors tasks)
  - [Reliability of Topic Modeling](https://aclanthology.org/2025.naacl-long.135.pdf)
- **Repetitive generation** (behaviors tasks)
  - [Reliability of Topic Modeling](https://aclanthology.org/2025.naacl-long.135.pdf)
