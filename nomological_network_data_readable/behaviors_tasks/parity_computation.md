# Parity computation
**Type:** Behavior  
**Referenced in:** 3 papers  

## State of the Field

In the provided literature, parity computation is characterized as a behavior involving boolean variables. The task is defined as calculating the sum modulo 2 of a tuple of these variables. It is operationalized as a training task where a model must compute the parity of the sum of a given set of variables. For example, one source illustrates this with a prompt requiring the model to calculate `(X2 + X3 + X1) % 2` and provide the correct output. The available data comes from a single study and does not connect this behavior to any specific benchmarks or other constructs.

## Sources

**[Connecting the Dots: LLMs can Infer and Verbalize Latent Structure from Disparate Training Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe489a28a54583ee802b8e2955c024c2-Paper-Conference.pdf)**
> Calculating the sum modulo 2 of a tuple of boolean variables.
