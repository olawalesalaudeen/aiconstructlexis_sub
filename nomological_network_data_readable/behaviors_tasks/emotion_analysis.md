# Emotion analysis
**Type:** Behavior  
**Referenced in:** 9 papers  
**Also known as:** Emotion classification, Emotion recognition in conversations  

## State of the Field

Across the provided literature, emotion analysis is most frequently framed as a classification task involving the assignment of a predefined emotional label to a piece of text or an utterance. Several papers specify this task within a conversational context, where a model must determine an utterance's emotion based on the preceding dialogue history. A different line of work defines it more broadly as extracting and representing emotional connotations, particularly those found in rhetorical expressions like hyperbole and metaphor. The behavior is operationalized and measured using several datasets, including EmoryNLP, MELD, and IEMOCAP, for what is termed 'emotion classification' or 'emotion detection'. Other operationalizations involve prompting a large language model to analyze a sentence or having human participants select from a taxonomy of emotions for multimodal posts. Performance on this task is assessed using methods such as zero-shot evaluation and can be elicited through techniques like chain-of-thought prompting. The task is also studied alongside the related concept of emotion understanding.

## Sources

**[SUA: Stealthy Multimodal Large Language Model Unlearning Attack](https://aclanthology.org/2025.emnlp-main.566.pdf) (as "Emotion classification")**
> Assigning an emotional label (e.g., joy, fear, anger) to a given utterance based on its content and contextual history in a conversation.

**[How to Enable Effective Cooperation Between Humans andNLPModels: A Survey of Principles, Formalizations, and Beyond](https://aclanthology.org/2025.acl-long.23.pdf)**
> Extracting and representing the emotional connotations present in a sentence, particularly those underlying rhetorical expressions.

**[T2A-Feedback: Improving Basic Capabilities of Text-to-Audio Generation via Fine-grainedAIFeedback](https://aclanthology.org/2025.acl-long.1148.pdf) (as "Emotion recognition in conversations")**
> The task of assigning a predefined emotion label to a specific utterance within a dialogue, given the preceding conversational history.

## Relationships

### → Emotion analysis
- **Zero-shot evaluation** (measurements) — *measured_by*
  - [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf)
- **Chain-of-thought prompting** (measurements) — *measured_by*
  - [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf)

### Associated with
- **Emotion understanding** (constructs)
  - [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf)
