# Self-modification
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Experiential learning, Recursive self-improvement  

## State of the Field

Across the provided literature, self-modification is conceptualized as an agent's capacity to improve its performance over time by learning from its experiences. The definitions diverge on the mechanism of this improvement, with some papers focusing on learning from past events and others on the direct alteration of the agent's own code. One common framing, termed "self-improvement" or "experiential learning," involves an agent enhancing its performance without retraining. This is described as being achieved through mechanisms like "Contextual Experience Replay," where an agent replays distilled experiences in its context window, or by storing failures in memory to "generate natural language insights through self-reflection" ("Towards Comprehensive Argument Analysis in Education: Dataset, Tasks, and Method"). A different framing, presented as "self-modification" or "recursive self-improvement," describes an agent's ability to dynamically alter its own code and operational logic. In this view, an agent can "iteratively enhance its own policy and learning algorithm" or even "dynamically write[] [new code] into the runtime memory" to modify its behavior based on reasoning and feedback ("T-REG: Preference Optimization with Token-Level Reward Regularization"). While both approaches aim for performance enhancement, the former focuses on refining future actions based on memory and reflection, whereas the latter involves direct, runtime modification of the agent's underlying code.

## Sources

**[UniRAG: Unified Query Understanding Method for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.694.pdf) (as "Self-improvement")**
> The latent ability of a language agent to enhance its performance over time by learning from past task experiences without retraining.

**[Towards Comprehensive Argument Analysis in Education: Dataset, Tasks, and Method](https://aclanthology.org/2025.acl-long.697.pdf) (as "Experiential learning")**
> The capacity of a model to reflect on past failures, extract insights, and refine future planning and decision-making through accumulated experience.

**[T-REG: Preference Optimization with Token-Level Reward Regularization](https://aclanthology.org/2025.acl-long.1354.pdf) (as "Recursive self-improvement")**
> The latent ability of an agent to iteratively enhance its own policy and learning algorithm by modifying its code, leading to progressively better performance over time.

**[T-REG: Preference Optimization with Token-Level Reward Regularization](https://aclanthology.org/2025.acl-long.1354.pdf)**
> The agent's ability to dynamically alter its own code and operational logic during execution based on its reasoning and environmental feedback.
