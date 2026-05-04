# ConflictQA
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** ConflictQA+  

## State of the Field

Across the provided literature, ConflictQA is predominantly characterized as a benchmark dataset used for "contradiction checking" and evaluating how models handle conflicting information. Most descriptions specify that each sample contains a question, "correct aligned evidence," and "ChatGPT-generated contradictory evidence." A related framing, found in one paper, describes the dataset as containing "counterfactual contexts" instead. One study notes that the questions are sourced from PopQA. The dataset also has a documented extension, ConflictQA+, which was constructed to further evaluate LLM performance under more complex conditions. This extension augments the original set by adding "distracting, ambiguous, and duplicated contexts." Collectively, the papers use ConflictQA and its extension to assess model performance when presented with conflicting, unhelpful, or ambiguous information.

## Sources

**[Entity Decomposition with Filtering: A Zero-Shot Clinical Named Entity Recognition Framework](https://aclanthology.org/2025.naacl-long.151.pdf)**
> A dataset used for contradiction checking, containing questions, correct aligned evidence, and ChatGPT-generated contradictory evidence.

**[THREAD: Thinking Deeper with Recursive Spawning](https://aclanthology.org/2025.naacl-long.428.pdf) (as "ConflictQA+")**
> An extension of the ConflictQA dataset, constructed to evaluate LLM performance by adding distracting, ambiguous, and duplicated contexts to the original set of counterfactual contexts.
