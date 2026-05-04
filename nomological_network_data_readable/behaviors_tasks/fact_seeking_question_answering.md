# Fact-seeking question answering
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Factoid question answering, Fact-based question answering  

## State of the Field

Across the provided literature, "Fact-seeking question answering" is consistently defined as the task of answering questions that require objective, verifiable, and specific factual information. Papers use slightly different but related terms like "Factual," "Factoid," and "Fact-based" question answering to describe this behavior, which typically involves generating short, precise responses about entities, dates, or locations. As one paper exemplifies, this includes questions like "‘In which year was the Eiffel Tower built?’" ("Procedural Environment Generation for Tool-Use Agents"). This behavior is operationalized and measured using a range of question-answering benchmarks. The most frequently cited instruments in this set are TriviaQA and Natural Questions. TriviaQA is described as a dataset for testing the "retrieval of world knowledge," and both are used for what some papers term "factoid QA tasks." Other benchmarks used to evaluate this behavior include HotpotQA, SQuAD v1.1, NFCorpus, and SimpleQA, with the latter being explicitly called a "representative benchmark for factual QA" ("VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search"). While often concerning general knowledge, some work applies this task to specific domains, such as factual queries grounded in a Polish context.

## Sources

**[MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf) (as "Factual question answering")**
> The task of answering questions by extracting specific, factual information from a given text.

**[Procedural Environment Generation for Tool-Use Agents](https://aclanthology.org/2025.emnlp-main.937.pdf)**
> The task in which an LLM answers questions that ask for objective, verifiable information such as dates, locations, or entities, typically with short and precise responses.

**[Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf) (as "Factoid question answering")**
> The task of answering questions that have a single, concise factual answer, often requiring the retrieval of a few targeted facts.

**[REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf) (as "Fact-based question answering")**
> The observable generation of answers to factual queries, particularly those grounded in Polish context and knowledge.

## Relationships

### Fact-seeking question answering →
- **TriviaQA** (measurements) — *measured_by*
  > TriviaQA (5-shot) (Joshi et al., 2017), a factual question-answering dataset compiled by trivia enthusiasts to test retrieval of world knowledge. (Section 4.1)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **HotpotQA** (measurements) — *measured_by*
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
