# Few-shot generalization
**Type:** Construct  
**Referenced in:** 3 papers  

## State of the Field

Across the provided literature, few-shot generalization is consistently defined as a model's capacity to perform effectively on new tasks or in unseen scenarios when given only a very limited number of examples. This capability is typically assessed in what are described as "few-shot scenarios" or "low-resource scenarios." While the core concept is shared, definitions vary in their specificity; some frame it broadly as generalizing to new tasks, while others describe a more specific underlying mechanism. For example, one line of work defines it as leveraging "debiased domain-level abstractions rather than surface-level patterns," while another describes it as the ability to "infer and apply general rules or properties" from the few examples provided. One paper notes that this involves models being able to "extrapolate from provided examples to infer related properties that are not explicitly mentioned" (LLM-grounded Video Diffusion Models). This construct is observed in a variety of behaviors, with one source listing "translation, question-answering, cloze tasks, and reasoning" as tasks where large language models demonstrate this capability (NOLA: Compressing LoRA using Linear Combination of Random Basis).

## Sources

**[BayesPrompt: Prompting Large-Scale Pre-Trained Language Models on Few-shot Inference via Debiased Domain Abstraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/5fcfda9e2a28c62f1ba54bcfa09ebdbc-Paper-Conference.pdf)**
> The capacity of a model to generalize effectively from very limited training examples by leveraging debiased domain-level abstractions rather than surface-level patterns.
