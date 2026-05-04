# Text continuation
**Type:** Behavior  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, text continuation is consistently defined as the behavior of generating subsequent text that coherently follows an initial prompt or context. The primary variation across papers is not in this core definition, but in how the behavior is operationalized for different research goals. A prevalent application is for model evaluation, such as assessing a model's "ability to maintain predictive capability after compression" or testing for stylistic and logical consistency when generating a "suffix" that follows a "prefix" from human speech or social media posts. The behavior is also frequently employed in safety research, where it serves as a red-teaming scenario by using truncated text as input to trigger specific, sometimes toxic, model outputs. One paper describes this as a central capability, noting that "many applications depend on the model’s capacity to extend and complete text provided in the input prompt" (Curiosity-driven Red-teaming for Large Language Models). More specific operationalizations include its use in a student-teacher framework where models complete sentences from a five-token prompt, and as an intermediate step in speech generation where the continuation can be influenced by "paralinguistic cues from the prompt speech" (Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM).

## Sources

**[Curiosity-driven Red-teaming for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/56ed2bd15b66f709cd81cb1aaa0496b9-Paper-Conference.pdf)**
> Generating subsequent text following the original context based on memory slots, used to evaluate the model's ability to maintain predictive capability after compression.
