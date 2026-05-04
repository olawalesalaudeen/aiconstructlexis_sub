# Data leakage
**Type:** Construct  
**Referenced in:** 7 papers  
**Also known as:** Knowledge leakage, Privacy leakage, Information leakage risk, Knowledge file leakage  

## State of the Field

Across the provided literature, the most common framing of "Data leakage" is the unintentional disclosure of information by a model, though the specific type of information and mechanism of exposure vary. A prevalent view treats this as the inadvertent release of sensitive or private content, such as "confidential information embedded in its context or training data" ("Growing Through Experience: Scaling Episodic Grounding in Language Models") or "protected knowledge file data" ("MegaPairs: Massive Data Synthesis for Universal Multimodal Retrieval"). In contrast, a more specific, technical definition frames it as "data contamination," where a model exhibits an artificially high log-likelihood on a text because that corpus was part of its pre-training data ("RAG"). A smaller line of work discusses the leakage of "benchmark-specific knowledge" to a student model through processes like distillation ("Browsing Lost Unformed Recollections: A Benchmark for Tip-of-the-Tongue Search and Reasoning"). The construct is operationalized in multiple ways; some work detects it by comparing a model's log-likelihood with its benchmark performance, while other approaches use specific attack methods, such as exploiting "lower-ranked output tokens to leak sensitive information." The provided data also indicates that the `MMStar` benchmark is used as a measurement instrument for data leakage. This construct is explicitly related to `Memorization`, with one paper noting that "models do memorize some personal information and may occasionally disclose it." The scope of leakage is described as broad, with one study identifying five distinct "leakage vectors," including metadata, retrieval, and prompts ("MegaPairs: Massive Data Synthesis for Universal Multimodal Retrieval").

## Sources

**[Browsing Lost Unformed Recollections: A Benchmark for Tip-of-the-Tongue Search and Reasoning](https://aclanthology.org/2025.acl-long.407.pdf) (as "Knowledge leakage")**
> The phenomenon where benchmark-specific knowledge is transferred to a student model, often covertly through methods like distillation, even without direct training on the test set.

**[Growing Through Experience: Scaling Episodic Grounding in Language Models](https://aclanthology.org/2025.acl-long.410.pdf) (as "Privacy leakage")**
> The latent tendency of a model to inadvertently reveal confidential information embedded in its context or training data, even when not explicitly prompted to do so.

**[STUN: Structured-Then-Unstructured Pruning for ScalableMoEPruning](https://aclanthology.org/2025.acl-long.672.pdf) (as "Information leakage risk")**
> The latent potential for a tool-learning system to unintentionally disclose sensitive user or tool information to unauthorized parties as a result of its design and behavior.

**[MegaPairs: Massive Data Synthesis for Universal Multimodal Retrieval](https://aclanthology.org/2025.acl-long.936.pdf) (as "Knowledge file leakage")**
> The latent propensity of an LLM agent to expose protected knowledge file data—such as titles, content, or original files—through various system vectors, even without direct adversarial prompting.

**[RAG](https://aclanthology.org/2025.acl-long.1584.pdf)**
> The phenomenon where a model exhibits an artificially high log-likelihood on a text corpus because that corpus was included in its pre-training data.

## Relationships

### Data leakage →
- **MMStar** (measurements) — *measured_by*
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)

### Associated with
- **Memorization** (constructs)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
