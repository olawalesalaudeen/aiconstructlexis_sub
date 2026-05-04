# Chart question answering
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Chart-based question answering, Flowchart question answering, Figure question answering  

## State of the Field

Across the provided literature, chart question answering is consistently defined as the task of generating answers to natural language questions based on information presented in a visual chart or figure. The process involves a model analyzing a visual input, such as a chart, alongside a textual prompt to generate a response, which can be numerical, categorical, or textual. While the general term is prevalent, some papers use more specific variants like 'figure question answering' or 'flowchart question answering'. The flowchart-focused variant, for instance, is explicitly used to "assess geometric understanding, spatial reasoning, and logical capabilities" (The Role of Outgoing Connection Heterogeneity in Feedforward Layers of Large Language Models). To evaluate this behavior, researchers in this set of papers use measurement instruments such as the ChartQA benchmark. As one paper formally defines the task, "CQA is a task that involves providing an answer A to a natural language question Q, based on the information contained in a chart C" (LegalSearchLM: Rethinking Legal Case Retrieval as Legal Elements Generation).

## Sources

**[Semantic Inversion, Identical Replies: Revisiting Negation Blindness in Large Language Models](https://aclanthology.org/2025.emnlp-main.1089.pdf) (as "Chart-based question answering")**
> Generating textual responses to questions by analyzing a visual chart and its underlying data.

**[The Role of Outgoing Connection Heterogeneity in Feedforward Layers of Large Language Models](https://aclanthology.org/2025.emnlp-main.1144.pdf) (as "Flowchart question answering")**
> Generating natural language answers to questions about the content, logic, or process flow of a given flowchart image.

**[LegalSearchLM: Rethinking Legal Case Retrieval as Legal Elements Generation](https://aclanthology.org/2025.emnlp-main.226.pdf)**
> Generating answers to natural language questions based on information presented in a chart, including numerical, categorical, or textual responses.

**[SmartBench: Is YourLLMTruly a GoodChinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.195.pdf) (as "Figure question answering")**
> Answering questions about information contained in a figure.

## Relationships

### Chart question answering →
- **ChartQA** (measurements) — *measured_by*
  - [ShouldIShare this Translation? Evaluating Quality Feedback for User Reliance on Machine Translation](https://aclanthology.org/2025.emnlp-main.607.pdf)
