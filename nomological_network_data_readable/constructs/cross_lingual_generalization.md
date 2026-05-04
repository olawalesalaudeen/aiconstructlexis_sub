# Cross-lingual generalization
**Type:** Construct  
**Referenced in:** 31 papers  
**Also known as:** Cross-language generalization, Cross-lingual adaptability, Cross-lingual understanding, General multilingual utility, Cross-lingual knowledge transfer, Cross-lingual transfer, Language generalization, Crosslingual transfer  

## State of the Field

Across the surveyed literature, "Cross-lingual generalization" is most commonly defined as a multilingual model's ability to transfer knowledge from high-resource to low-resource or unseen languages. This concept appears under several related names, including "cross-lingual transfer" and "multilingual generalization," all pointing to the capacity to perform tasks in a target language without extensive direct training. Several papers attribute this capability to the model developing "aligned multilingual semantic spaces" or "shared representations," resulting in a "close resemblance between the hidden representation of instructions in two languages" (Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages). This construct is operationalized by observing a model's performance on tasks like applying hallucination mitigation to new language pairs in a zero-shot setting or performing named entity recognition in a low-resource language after training on a high-resource one.

A smaller line of work uses the term "cross-language generalization" to refer to a distinct phenomenon: the transfer of problem-solving performance across different programming languages. Other papers offer more specific framings, such as "cross-lingual adaptability," which focuses on adjusting to a target language's patterns, and "cross-lingual understanding," which concerns preserving meaning when responding in a different language. While there is evidence for the construct, one paper notes that how models develop the shared representations that enable this transfer is "not well understood" (CanLLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation onAIResearch Papers).

## Sources

**[Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e9034dd5420660d86c8c360c35a895e-Paper-Conference.pdf)**
> The latent ability of a multilingual model to transfer knowledge from high-resource to low-resource languages, particularly when linguistic and data conditions differ significantly.

**[SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf) (as "Cross-language generalization")**
> The degree to which a software-engineering system transfers its problem-solving performance across programming languages and language-specific codebases.

**[Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1551c01d7a3d0bf21e2518331e9f7074-Paper-Conference.pdf) (as "Multilingual generalization")**
> The model's ability to perform effectively on languages, particularly low-resource ones, without being explicitly or extensively trained on them.

**[Flipping Knowledge Distillation: Leveraging Small Models’ Expertise to EnhanceLLMs in Text Matching](https://aclanthology.org/2025.acl-long.1082.pdf) (as "Cross-lingual understanding")**
> The latent ability of a model to understand and respond to questions in a language different from its training dominant language while preserving meaning and accuracy.

**[Are We in theAI-Generated Text World Already? Quantifying and MonitoringAIGTon Social Media](https://aclanthology.org/2025.acl-long.1121.pdf) (as "Cross-lingual adaptability")**
> The latent ability of a model to transfer knowledge and skills from English to a target language, adjusting to language-specific patterns while retaining universal linguistic principles.

**[CoE: A Clue of Emotion Framework for Emotion Recognition in Conversations](https://aclanthology.org/2025.acl-long.1149.pdf) (as "General multilingual utility")**
> The model's overall effectiveness and performance on a wide range of non-safety-related tasks across multiple languages.

**[Leveraging Dual Process Theory in Language Agent Framework for Real-time Simultaneous Human-AICollaboration](https://aclanthology.org/2025.acl-long.207.pdf) (as "Cross-lingual knowledge transfer")**
> The ability of a model trained primarily on one language (e.g., English) to effectively perform tasks in other languages by leveraging aligned token representations.

**[L4Q: Parameter Efficient Quantization-Aware Fine-Tuning on Large Language Models](https://aclanthology.org/2025.acl-long.100.pdf) (as "Cross-lingual transfer")**
> The capacity of a model to leverage knowledge acquired in one language (e.g., English) to enhance performance in another language (e.g., Arabic) during pre-training and inference.

**[TheAIGap: How Socioeconomic Status Affects Language Technology Interactions](https://aclanthology.org/2025.acl-long.915.pdf) (as "Language generalization")**
> The degree to which a model's discourse representations are aligned across different languages, enabling performance on multilingual tasks without language-specific adaptation.

**[CanLLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation onAIResearch Papers](https://aclanthology.org/2025.acl-long.1010.pdf) (as "Crosslingual transfer")**
> The ability of a multilingual model to apply knowledge learned from one language to improve performance or enable capabilities in another language.
