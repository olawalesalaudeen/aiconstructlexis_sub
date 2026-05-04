# Text simplification
**Type:** Behavior  
**Referenced in:** 10 papers  
**Also known as:** Claim simplification, Sentence decomposition, Sentence simplification, Lexical simplification  

## State of the Field

Across the surveyed literature, text simplification is most commonly defined as the behavior of revising text to reduce its complexity and enhance readability, with most definitions stipulating that the original meaning should be preserved. This behavior is operationalized through several distinct actions, including lexical simplification (replacing complex words), sentence decomposition (breaking down complex syntactic structures), and shortening sentences. While 'text simplification' is the general term, a few papers focus on more granular versions of this task, such as 'claim simplification' for easier verification of assertions or 'sentence simplification' which converts compound-complex sentences into simpler forms. One paper operationalizes sentence simplification using 'hybrid chain-of-thought and few-shot prompting,' while another notes that lexical simplification can be guided by LCP scores. This behavior is frequently studied for its downstream effects; papers report that it causes improvements in `Readability`, `Translation quality`, and `Information extraction`. Although often presented as a beneficial process, one study suggests that a model's tendency to simplify can be a drawback in certain contexts, noting it as a 'possible reason that GPT-4 achieves low scores on lexical evaluation' in a specialized task.

## Sources

**[From Redundancy to Relevance: Information Flow inLVLMs Across Reasoning Tasks](https://aclanthology.org/2025.naacl-long.116.pdf)**
> An observable behavior where a model revises text in a way that reduces its complexity or increases its readability, which may be contrary to the goals of a specialized task like patent revision.

**[Self-Critique and Refinement for Faithful Natural Language Explanations](https://aclanthology.org/2025.emnlp-main.428.pdf) (as "Claim simplification")**
> The task of breaking down complex assertions into simpler, more easily verifiable components.

**[Complex Numerical Reasoning with Numerical Semantic Pre-training Framework](https://aclanthology.org/2025.emnlp-main.783.pdf) (as "Sentence decomposition")**
> The process of breaking down syntactically complex, compound, or compound-complex sentences into simpler, more easily parsable forms.

**[Complex Numerical Reasoning with Numerical Semantic Pre-training Framework](https://aclanthology.org/2025.emnlp-main.783.pdf) (as "Sentence simplification")**
> The task of converting sentences with complex syntactic structures (complex, compound, compound-complex) into one or more simple sentences.

**[“Feels Feminine to Me”: Understanding Perceived Gendered Style through Human Annotations](https://aclanthology.org/2025.emnlp-main.1603.pdf) (as "Lexical simplification")**
> The observable task of replacing complex words in a text with simpler alternatives while preserving the original meaning.

## Relationships

### Text simplification →
- **Translation quality** (constructs) — *causes*
  > Simplification with TOWER-INSTRUCT distinguishes itself by improving translation quality based on XCOMET(s, t, r) scores and maintaining it according to the METRICX(t, r) scores. (§4.1)
  - [KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)
- **Readability** (constructs) — *causes*
  > This refinement greatly improves the readability of documents, making them more accessible to diverse audiences... (Section 1)
  - [KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)
- **Information extraction** (behaviors tasks) — *causes*
  > Ablation studies demonstrate that integrating coreference and decomposition increases recall on rare relations by over 20%. (Abstract)
  - [Complex Numerical Reasoning with Numerical Semantic Pre-training Framework](https://aclanthology.org/2025.emnlp-main.783.pdf)
