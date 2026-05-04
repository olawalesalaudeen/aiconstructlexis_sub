# Clone detection
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Equivalence checking, Program equivalence checking, Code compliance checking, Consistency checking  

## State of the Field

Across the provided literature, Clone detection is most commonly described as the task of determining whether two programs or code snippets are semantically or functionally equivalent. This core idea appears under several names, including "Equivalence checking" and "Program equivalence checking," with definitions specifying that two programs should "produce identical outputs for all possible inputs" or "exhibit the same functional behavior." One paper operationalizes this as a "binary classification task" to determine semantic equivalence. This behavior is used to "evaluate LLMs’ ability to reason about program semantics." A distinct and less frequent set of definitions broadens the concept of checking beyond code. For example, "Code compliance checking" is defined as evaluating if a floor plan adheres to building regulations, while "Consistency checking" involves scoring a generated fact for alignment with a knowledge graph. These latter tasks focus on adherence to external standards or knowledge bases rather than the functional equivalence between two pieces of code.

## Sources

**[Data Descriptions from Large Language Models with Influence Estimation](https://aclanthology.org/2025.emnlp-main.1718.pdf) (as "Equivalence checking")**
> Determining whether two programs produce identical outputs for all possible inputs, regardless of syntactic or structural differences.

**[2025.emnlp-main.1718.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1718.checklist.pdf) (as "Program equivalence checking")**
> Determining whether two programs exhibit the same functional behavior despite potential differences in syntax or structure.

**[LoCt-Instruct: An Automatic Pipeline for Constructing Datasets of Logical Continuous Instructions](https://aclanthology.org/2025.emnlp-main.1735.pdf)**
> The binary classification task of determining if two distinct code snippets are semantically equivalent, meaning they perform the same function.

**[HYDRA: A Multi-Head Encoder-only Architecture for Hierarchical Text Classification](https://aclanthology.org/2025.emnlp-main.473.pdf) (as "Code compliance checking")**
> Evaluating whether a generated floor plan adheres to building codes and safety regulations using retrieved standards.

**[PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.508.pdf) (as "Consistency checking")**
> Evaluating whether a generated fact aligns with the existing knowledge graph by scoring it with a pre-trained knowledge graph embedding model.
