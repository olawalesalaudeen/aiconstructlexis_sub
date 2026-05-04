# Disambiguation
**Type:** Construct  
**Referenced in:** 19 papers  
**Also known as:** Ambiguity resolution, Kanji-rule compatibility, Homonym disambiguation, Word sense understanding, Entity disambiguation, Disambiguation capability, Sensitivity to sense boundaries, Disambiguation ability  

## State of the Field

Across the surveyed literature, Disambiguation is predominantly framed as a latent ability of a model to resolve ambiguity by leveraging various forms of context. The most common definitions describe this as selecting the intended sense of a word or entity from multiple possibilities using contextual, syntactic, or even visual cues. A smaller set of papers defines it more broadly as the capacity to recognize and address multiple valid interpretations of an entire query. This construct is operationalized and measured using a wide array of instruments, including general benchmarks like BBH and WinoGrande, as well as specialized datasets such as CondAmbigQA for ambiguous questions and DMDTEval for multi-domain translation. Evaluation is also conducted through human evaluation, LLM-as-a-judge methods, and custom metrics like "disambiguation accuracy." Some research compares model capabilities to human performance, with one study noting that models are "less sensitive to sense boundaries… than humans" ("ALPACAAGAINSTVICUNA: UsingLLMs to Uncover Memorization ofLLMs"). Disambiguation is studied alongside related behaviors like query rewriting and long-form text generation, and a lack of domain-specific knowledge is reported by one paper to cause failures in this ability for translation tasks.

## Sources

**[Effective Red-Teaming of Policy-Adherent Agents](https://aclanthology.org/2025.emnlp-main.115.pdf) (as "Ambiguity resolution")**
> The model's capacity to recognize multiple valid interpretations of a query and generate responses that appropriately distinguish or address them based on contextual constraints.

**[2025.emnlp-main.115.checklist](https://aclanthology.org/attachments/2025.emnlp-main.115.checklist.pdf) (as "Ambiguity handling")**
> The latent ability to cope with questions whose meaning depends on conditions or context and to avoid being misled by ambiguous wording.

**[EmpoweringGraphRAGwith Knowledge Filtering and Integration](https://aclanthology.org/2025.emnlp-main.1294.pdf) (as "Kanji-rule compatibility")**
> The model's latent understanding of which mnemonic-creation rules are semantically or visually suitable for a given kanji based on its specific structural or semantic features.

**[Creativity inLLM-based Multi-Agent Systems: A Survey](https://aclanthology.org/2025.emnlp-main.1404.pdf) (as "Homonym disambiguation")**
> The latent ability to resolve ambiguous words by selecting the intended sense from contextual and syntactic cues.

**[MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1720.pdf) (as "Word sense understanding")**
> The latent ability of a model to grasp the meaning of a word in context, beyond mere pattern matching, enabling accurate disambiguation and explanation across diverse usages.

**[Towards Author-informedNLP: Mind the Social Bias](https://aclanthology.org/2025.emnlp-main.1765.pdf) (as "Entity disambiguation")**
> The ability to distinguish between entities with similar or identical names by leveraging contextual clues and clarifying information.

**[What DidIDo Wrong? QuantifyingLLMs’ Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.74.pdf) (as "Disambiguation capability")**
> The underlying trait enabling a model to resolve ambiguous terms by leveraging multimodal context, particularly visual evidence, to select the correct translation.

**[ALPACAAGAINSTVICUNA: UsingLLMs to Uncover Memorization ofLLMs](https://aclanthology.org/2025.naacl-long.422.pdf) (as "Sensitivity to sense boundaries")**
> The extent to which a model distinguishes categorical same-sense versus different-sense contexts in a way that mirrors human judgments.

**[THREAD: Thinking Deeper with Recursive Spawning](https://aclanthology.org/2025.naacl-long.428.pdf)**
> The latent ability of a model to accurately distinguish between entities that share the same surface name but have different specific descriptors.

**[JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf) (as "Disambiguation ability")**
> The latent capacity of an LLM to correctly interpret and translate words with multiple meanings based on domain-specific context in multi-domain translation.

## Relationships

### Disambiguation →
- **BBH** (measurements) — *measured_by*
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **Multi30k** (measurements) — *measured_by*
  - [What DidIDo Wrong? QuantifyingLLMs’ Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.74.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf)
- **DMDTEval** (measurements) — *measured_by*
  > To this end, we present an evaluation and analysis of LLMs on disambiguation in multi-domain translation (DMDTEval), our systematic evaluation framework... (Abstract)
  - [JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf)
- **CondAmbigQA** (measurements) — *measured_by*
  - [Effective Red-Teaming of Policy-Adherent Agents](https://aclanthology.org/2025.emnlp-main.115.pdf)

### → Disambiguation
- **Domain knowledge** (constructs) — *causes*
  - [JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf)

### Associated with
- **Query rewriting** (behaviors tasks)
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-OnlyLLMs](https://aclanthology.org/2025.emnlp-main.482.pdf)
- **Long-form text generation** (behaviors tasks)
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-OnlyLLMs](https://aclanthology.org/2025.emnlp-main.482.pdf)
- **Prompt engineering** (behaviors tasks)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-OnlyLLMs](https://aclanthology.org/2025.emnlp-main.482.pdf)
