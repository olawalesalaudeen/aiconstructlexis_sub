# Spurious correlations
**Type:** Construct  
**Referenced in:** 3 papers  

## State of the Field

In the provided literature, spurious correlations are characterized as non-robust patterns that models learn from training data instead of generalizable, ground-truth concepts. One framing defines these as "input-output regularities that fit the observed data but arise from sampling noise" (Learning from Teaching Regularization...). A closely related perspective, termed "shortcut learning," describes this as the tendency of neural networks to learn "simple, superficial statistical correlations" to achieve good performance on a training set, rather than more complex underlying concepts (Co-occurrence is not Factual Association...). This behavior is described as being common in neural networks and is attributed to their tendency to learn simple features first. The provided data does not specify how this construct is operationalized or measured.

## Sources

**[Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf)**
> Input-output regularities that fit the observed data but arise from sampling noise rather than the underlying ground truth.

**[Co-occurrence is not Factual Association in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/775226eaa2a36c543e2bd6cc9eae1b6a-Paper-Conference.pdf) (as "Shortcut learning")**
> The tendency of a neural network to learn simple, superficial statistical correlations in the training data instead of more complex and robust underlying concepts.
