# Entity linking
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Entity grounding  

## State of the Field

Across the provided literature, 'Entity linking' is used to describe at least two distinct behaviors. One conceptualization frames it as a text-based task of mapping entity mentions to a formal knowledge base. For instance, in a clinical context, it is defined as the process of linking disease mentions to standardized ICD codes, where the objective is to "assign a set of unique ICD codes to the latest patient appointment based on textual diagnosis conclusion" ("M-ABSA: A Multilingual Dataset for Aspect-Based Sentiment Analysis"). This process is reported to use semantic similarity with dictionary entries. A different line of work presents a multimodal version of this task, termed 'entity grounding', which involves linking a textual entity mention to its corresponding visual region in an image. This is distinguished from 'visual grounding' by the observation that entity grounding often uses a "brief entity name, which contain less semantic information" ("SciRIFF: A Resource to Enhance Language Model Instruction-Following over Scientific Literature"). The same work notes the use of multi-step Chain-of-Thought reasoning to perform this grounding task.

## Sources

**[M-ABSA: A Multilingual Dataset for Aspect-Based Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.129.pdf)**
> The observable process of mapping disease mentions in clinical text to standardized ICD codes from a formal hierarchy.

**[SciRIFF: A Resource to Enhance Language Model Instruction-Following over Scientific Literature](https://aclanthology.org/2025.emnlp-main.311.pdf) (as "Entity grounding")**
> The task of linking a textual entity mention to its corresponding visual region in an accompanying image.
