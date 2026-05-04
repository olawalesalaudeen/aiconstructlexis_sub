# Feedback generation
**Type:** Behavior  
**Referenced in:** 10 papers  

## State of the Field

Across the surveyed literature, feedback generation is most commonly defined as a model's behavior of producing a rationale to explain why a particular score was assigned to a response, with one paper describing this as "analogous to Chain-of-Thoughts (CoT)" in evaluation. This behavior is operationalized in several distinct contexts, particularly in code generation, where a model is prompted to output a "short explanation of why the code failed" based on the faulty program and an error message. In this domain, feedback generation is studied alongside `Code debugging` and `Self-reflection`, and is reported to influence `Code improvement`. A different line of work frames this behavior as generating rationales about model responses for social alignment, with one study positing that this capability "is a prerequisite for... Realignment." Other documented applications include producing diagnostic insights to refine prompts and delivering personalized educational feedback that "pinpoints strengths and addresses weaknesses."

## Sources

**[Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)**
> Producing a rationale explaining why a particular score was assigned to a model response, analogous to chain-of-thought reasoning in evaluation.

## Relationships

### Feedback generation →
- **Code improvement** (behaviors tasks) — *causes*
  - [Generating CAD Code with Vision-Language Models for 3D Designs](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf)

### Associated with
- **Critique** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Code debugging** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
