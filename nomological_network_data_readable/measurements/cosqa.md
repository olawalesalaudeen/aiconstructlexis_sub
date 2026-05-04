# CoSQA
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** CosQA  

## State of the Field

CoSQA is a dataset used for model evaluation, with two distinct framings present in the provided literature. The most common usage, found across multiple papers, describes CoSQA as a benchmark for natural-language-to-code semantic search, where models are evaluated on their ability to retrieve relevant code from natural-language queries. One paper in this vein specifies that it is designed to evaluate "the alignment between code and intent expressed in natural language" ("Hierarchical Bracketing Encodings for Dependency Parsing as Tagging"). A different framing, from a single paper, characterizes it as a "code-oriented question answering dataset" used to assess a model's ability to "understand and reason about code semantics" ("At Which Training Stage Does Code Data Help LLMs Reasoning?"). This paper explicitly states its use is "to test the model performance on the code question-answering task." Across descriptions, the dataset is noted to contain "natural language-code pairs." Several sources also mention its use alongside other code search benchmarks like AdvTest and CodeSearchNet.

## Sources

**[At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf) (as "CosQA")**
> A code-oriented question answering dataset containing natural language-code pairs, used to evaluate a model’s ability to understand and reason about code semantics.

**[CODE REPRESENTATION LEARNING AT SCALE](https://proceedings.iclr.cc/paper_files/paper/2024/file/cfbba5249393100ada0bfb37557d2fd9-Paper-Conference.pdf)**
> A benchmark for natural-language-to-code semantic search using natural-language queries to retrieve relevant code.
