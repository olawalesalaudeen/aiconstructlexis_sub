# Parity checking
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Parity  

## State of the Field

Parity checking is presented in the provided literature as a task for models involving binary sequences. The most direct definition describes it as the task of "Producing the parity result for a binary input sequence" ("Looped Transformers for Length Generalization"). This involves checking the parity of an entire binary string. A different paper describes a specific variant, simply named "Parity," which is framed as a "trivial task" ("Selective Attention Improves Transformer"). In this particular operationalization, the model's output is designed to be "only a function of the last two tokens" because "intermediate results are stored every other token." Thus, while the core concept involves parity, the provided sources describe different task setups with varying levels of complexity.

## Sources

**[Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf) (as "Parity")**
> A trivial task where the model's output is only a function of the last two tokens, with intermediate results stored every other token.

**[Looped Transformers for Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf)**
> Producing the parity result for a binary input sequence.
