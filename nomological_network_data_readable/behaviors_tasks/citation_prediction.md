# Citation prediction
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Citation attribution  

## State of the Field

The behavior of citation prediction is framed in at least two distinct ways across the provided literature. One line of work, using the term "citation attribution," defines the task as identifying the title of a paper that is already referenced within a given scientific text excerpt. This is operationalized by asking a language model to act as a "research assistant" that, when given a text excerpt, must correctly identify the title of the paper being cited. A second framing, using the term "citation prediction," describes the task as predicting which previous papers from a candidate set a new query paper will cite. In this view, the goal is to predict future citations for an "emerging new paper" from a "set of previous papers," a task one paper describes as a "critical problem." While both conceptualizations involve linking text to specific papers, the former focuses on resolving an existing reference, whereas the latter focuses on forecasting which references a new paper will include.

## Sources

**[CiteME: Can Language Models Accurately Cite Scientific Claims?](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef47f7b768e1a012e3d995ac8d8fac7-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Citation attribution")**
> Identifying the title of the paper referenced by a scientific text excerpt.

**[HLM-Cite: Hybrid Language Model Workflow for Text-based Scientific Citation Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/5635925cf9d2274f338eb0dd5971e845-Paper-Conference.pdf)**
> The observable task of identifying which previous papers from a candidate set a new query paper will cite.
