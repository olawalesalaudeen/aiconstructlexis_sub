# Simplicity bias
**Type:** Construct  
**Referenced in:** 3 papers  

## State of the Field

Across the surveyed literature, simplicity bias is most commonly described as a model's tendency to favor simpler functions or learning strategies, particularly early in training. This preference can compete with more complex but ultimately more effective strategies, and is discussed in the context of "breakthrough training dynamics." While this general framing is prevalent, some work offers more specific definitions based on the context of study. For example, one paper characterizes it as an "implicit inductive bias" of Transformers, where simplicity is operationalized as learning "the shortest RASP-L program which fits the training set." This view is used to conjecture which tasks Transformers are likely to length-generalize on. Another perspective explores the bias during in-context learning, defining simpler functions as "lower-frequency components" and observing a "clear bias for lower frequencies at small prompt lengths." The source of this bias is also framed differently, with some treating it as a general training phenomenon and others suggesting it arises from the pretraining distribution rather than the Transformer architecture itself.

## Sources

**[In-Context Learning through the Bayesian Prism](https://proceedings.iclr.cc/paper_files/paper/2024/file/d81cd83e7f6748af351485d73f305483-Paper-Conference.pdf)**
> The tendency of a model to favor simpler functions or learning strategies, especially early in training, which can compete with more complex but ultimately more effective strategies.
