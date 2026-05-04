# In-context prediction
**Type:** Behavior  
**Referenced in:** 5 papers  

## State of the Field

Based on the provided data, in-context prediction is defined as the observable task of a model generating a prediction for a new test example. This prediction is based on a set of context examples, also referred to as training examples, that are provided directly within the input prompt. The process is operationalized as an algorithm that takes these context examples as input and then predicts the outcome for a new test example. One paper illustrates this with a specific sequence where the model receives pairs of inputs and their corresponding function outputs, (x1, g(x1), ..., xn, g(xn)), followed by a new test input, xt, and is tasked with predicting g(xt). In this particular instantiation, the function to be learned from the context is a linear function.

## Sources

**[Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf)**
> The observable task of generating a prediction for a new test example based on a set of context examples provided in the input prompt.
