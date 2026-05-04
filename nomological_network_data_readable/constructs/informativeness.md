# Informativeness
**Type:** Construct  
**Referenced in:** 28 papers  

## State of the Field

Across the provided literature, Informativeness is a construct primarily defined by the extent to which a model's output contains relevant, detailed, and useful information. The most common framing centers on capturing all essential or key details without omission, while a subset of papers also stresses the importance of avoiding redundancy, with one study noting that an informative step "introduces new information and does not repeat or provide redundant details" ("Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment"). Some framings extend this to include the quality of the information, describing it in terms of "insightful explanations" ("Not All Adapters Matter...") or "meaningful, non-trivial, and useful insights" ("Lived Experience Not Found..."). A more specialized usage appears in the context of data augmentation, where it refers to the density of "critical training information" in a synthetic sample ("Skeletons Matter..."). The construct is commonly operationalized through human evaluation, where annotators assess generated text on Likert scales. It is also measured using automated methods, including the TruthfulQA benchmark, which has a dedicated informativeness metric, as well as the FreshWiki and QuestEval benchmarks. Additionally, several papers report using an LLM-as-a-judge approach to score outputs for informativeness. The construct is frequently studied alongside other text quality attributes like Faithfulness, Fluency, and Coherence, and is sometimes positioned as a related objective to Bias mitigation.

## Sources

**[Language Model Decoding as Direct Metrics Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf)**
> The extent to which generated text provides adequate, engaging detail in a coherent plot according to human judgment.

## Relationships

### Informativeness →
- **Human evaluation** (measurements) — *measured_by*
  > Three independent annotators are asked to review the source video and evaluate corresponding model outputs (and the human upper bound) on a 1–5 Likert scale for Faithfulness, Relevance, Informativeness, Conciseness, and Coherence (higher scores indicate better quality). (Section 7)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > In TruthfulQA, factuality is evaluated by two fine-tuned GPT-3 models, each focusing on truthfulness and informativeness (Section 4.3).
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > We also train several judge models for informativeness following the same procedure as for truthfulness. (Section 3.2.4)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **FreshWiki** (measurements) — *measured_by*
  > We conduct extensive experiments on the FreshWiki dataset and our newly constructed WikiStart dataset, demonstrating that MOG achieves state-of-the-art performance in both informativeness and verifiability. (Section 1)
  - [Tree-of-Debate: Multi-Persona Debate Trees Elicit Critical Thinking for Scientific Comparative Analysis](https://aclanthology.org/2025.acl-long.1423.pdf)
- **QuestEval** (measurements) — *measured_by*
  - [Direct Prompt Optimization with Continuous Representations](https://aclanthology.org/2025.acl-long.134.pdf)

### Associated with
- **Truthfulness** (constructs)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **Bias mitigation** (behaviors tasks)
  > From this perspective, we identify two unique objectives: (1) Informativeness—maximizing the training information available for data-scarce learning, and (2) Bias Mitigation—minimizing potential biases that may arise from limited data (Section 2.3).
  - [Skeletons Matter: Dynamic Data Augmentation for Text-to-Query](https://aclanthology.org/2025.emnlp-main.65.pdf)
