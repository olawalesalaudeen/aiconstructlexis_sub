# Task adaptation
**Type:** Construct  
**Referenced in:** 3 papers  
**Also known as:** Task-specific adaptation, Task adaptability  

## State of the Field

Across the provided literature, "Task adaptation" is a construct framed in two distinct ways, primarily differing on whether the adaptation occurs during fine-tuning or at inference time. The more prevalent usage treats it as a latent ability of a model to adjust its internal state for a specific downstream task via fine-tuning. Within this framing, one paper conceptualizes it as adjustments to "task-specific directions (TSDs)" in the weight space that "undergo significant changes when fine-tuning" (DiplomacyAgent: DoLLMs Balance Interests and Ethical Principles in International Events?). A related definition describes it as the model's ability to adjust its "neuronal representations" to capture new input patterns, particularly in the "orthogonal complementary subspace" relative to pre-trained weights (Can Large Language Models Tackle Graph Partitioning?). In contrast, a different line of work defines task adaptation as a property of modifying an LLM's behavior at inference time. This approach is described as a "lightweight solution" that relies on "Inference-Time Intervention" by injecting vectors rather than performing parameter updates (Pragmatic Inference Chain (PIC) ImprovingLLMs’ Reasoning of Authentic Implicit Toxic Language).

## Sources

**[Pragmatic Inference Chain (PIC) ImprovingLLMs’ Reasoning of Authentic Implicit Toxic Language](https://aclanthology.org/2025.emnlp-main.297.pdf)**
> The latent property of adapting an LLM’s behavior at inference time to a task using injected vectors rather than parameter updates.

**[DiplomacyAgent: DoLLMs Balance Interests and Ethical Principles in International Events?](https://aclanthology.org/2025.emnlp-main.694.pdf) (as "Task-specific adaptation")**
> The latent ability of a model to adjust its parameters effectively for a particular downstream task while preserving general capabilities from pretraining.

**[Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.793.pdf) (as "Task adaptability")**
> The latent ability of a model to adjust its neuronal representations to capture task-specific input patterns introduced during fine-tuning, particularly in the orthogonal subspace relative to pre-trained weights.
