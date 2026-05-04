# Text editing
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Text correction, Text insertion, Sequence editing, Grammar correction, Response detoxification, Sentiment revising, Faithfulness enhancement  

## State of the Field

Across the surveyed literature, 'Text editing' is a broad category of behaviors with several distinct definitions rather than a single, unified one. A common framing defines it as generating text to complete or fill gaps in a document, operationalized through tasks like text continuation, insertion, and infilling where a model must generate text coherent with a given prefix and/or suffix. Another line of work treats text editing as a correction task, including fixing grammatical errors or rewriting "noisy surgical narration text to fix misspellings and restore intended content" (Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation). A third group of papers frames text editing in the context of model alignment, defining it through tasks such as 'response detoxification', 'sentiment revising', and 'faithfulness enhancement' to modify model outputs. This alignment-focused usage is reflected in reports that text editing can be used to improve model safety. A more distinct definition describes 'sequence editing' as the process of "repeatedly applying multiple knowledge edits to the same model" (Reasons and Solutions for the Decline in Model Performance after Editing), focusing on model updates rather than output modification. Overall, the behavior is operationalized in multiple ways: by evaluating generated text against logical and contextual constraints, by assessing the correctness of revised sentences, or by measuring changes in model properties like safety and faithfulness.

## Sources

**[Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf) (as "Text correction")**
> Rewriting noisy surgical narration text to fix misspellings and restore intended content.

**[Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf)**
> Generating continuation or insertion suggestions for a story or document while respecting contextual and logical constraints.

**[Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf) (as "Text insertion")**
> The task of generating text to fill a gap between a given prefix and suffix, ensuring coherence with both contexts.

**[Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf) (as "Text continuation")**
> The task of generating text that follows a given prefix or opening passage.

**[Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf) (as "Text infilling")**
> The task of generating text to fill in masked-out portions of a document.

**[Reasons and Solutions for the Decline in Model Performance after Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f588e59e9ae6138d3ea9e4fdaa7e040-Paper-Conference.pdf) (as "Sequence editing")**
> Repeatedly applying multiple knowledge edits to the same model over a sequence of samples.

**[BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf) (as "Grammar correction")**
> The task of identifying and correcting grammatical errors in a given sentence.

**[PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf) (as "Response detoxification")**
> The task of modifying a model's output to be harmless and safe, especially when given a malicious or toxic input prompt.

**[PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf) (as "Sentiment revising")**
> The task of altering the emotional tone of a model's generated text, such as removing negative sentiment when discussing sensitive topics.

**[PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf) (as "Faithfulness enhancement")**
> Generating outputs that are more factually grounded and less hallucinatory in response to prompts requesting information.

## Relationships

### Text editing →
- **Safety** (constructs) — *causes*
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
