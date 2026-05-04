# Self-verification
**Type:** Construct  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, Self-verification is most commonly framed as an inherent or latent ability of a model to assess the correctness, validity, or quality of its own outputs and reasoning steps without external assistance. A smaller set of papers treats it as an explicit technique or procedure, where a model is prompted to re-evaluate its judgments or verify specific information, such as whether an entity matches the correct type. The construct is operationalized in several ways, including by having a model generate and execute code to validate an answer, or by generating and ranking multiple possible answers. For example, one method "applies generated codes to verify the answers and votes on different answers based on the verification results" ("Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification"). While some work points to this as an "emergent ability" ("MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts"), other findings question its reliability. One paper notes that "LLMs struggle with verification on truthfulness and reasoning correctness" and that relying on it without external feedback "may yield modest improvements or even deteriorate performance" ("CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing").

## Sources

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)**
> The inherent ability of a model to assess the correctness of its own generated solutions or reasoning steps, particularly by generating and executing code to validate an answer.
