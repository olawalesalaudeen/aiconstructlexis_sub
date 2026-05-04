# Repetitive generation
**Type:** Behavior  
**Referenced in:** 18 papers  
**Also known as:** Repetitive text generation, Repetition, Parroting, Repetitive actions, Redundant looping, Meaningless repetition, Content repetition, Action repetition, Token repetition  

## State of the Field

Across the surveyed literature, repetitive generation is most commonly characterized as an observable failure mode where a model produces repeating tokens, phrases, or entire utterances that degrade text quality. While most definitions focus on text, such as "meaningless repetition" of ideas or "content repetition" in code, several papers extend the concept to non-textual outputs, using terms like "parroting" or "repetitive actions" to describe repeating commands or subtasks without progress. This behavior is attributed to several factors, including "reward hacking in preference optimization," poor memory or context retention, and as a side effect of fine-tuning or excessive editing strength. For instance, one study notes that "Looping behavior and task repetition were most evident in systems with fragmented memory" ("AIP: Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt"). The provided data indicates that this behavior is operationalized and measured through `Human evaluation`. Repetitive generation is also studied in relation to other concepts such as `Reward hacking`, `Overthinking`, `Faithfulness`, and `Style transfer`.

## Sources

**[The Impact of Token Granularity on the Predictive Power of Language Model Surprisal](https://aclanthology.org/2025.acl-long.210.pdf) (as "Repetition")**
> An observable failure mode where the model generates repetitive tokens, phrases, or entire utterances that degrade the quality and meaning of the text.

**[NGQA: A Nutritional Graph Question Answering Benchmark for Personalized Health-aware Nutritional Reasoning](https://aclanthology.org/2025.acl-long.297.pdf) (as "Repetitive text generation")**
> An observable failure mode where the model produces outputs consisting of repeating words or phrases.

**[Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to EnhanceLLMReasoning](https://aclanthology.org/2025.acl-long.1203.pdf) (as "Parroting")**
> Repeating similar or nearly identical actions across multiple turns in a dialogue, resulting in low response diversity despite potential goal achievement.

**[AIP: Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt](https://aclanthology.org/2025.emnlp-main.802.pdf) (as "Redundant looping")**
> Repeating the same command or subtask without progress, due to lack of memory or awareness of prior outcomes.

**[ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming](https://aclanthology.org/2025.emnlp-main.810.pdf) (as "Repetitive actions")**
> Performing the same interaction or exploration move multiple times without progress, indicating poor memory utilization or lack of hypothesis refinement.

**[Less is More: The Effectiveness of Compact Typological Language Representations](https://aclanthology.org/2025.emnlp-main.1311.pdf)**
> Producing overly repetitive text as a failure mode after excessive editing strength.

**[NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1329.pdf) (as "Meaningless repetition")**
> The observable pattern of repeating phrases, sentences, or ideas without adding new information, often as a result of reward hacking in preference optimization.

**[EvoWiki: EvaluatingLLMs on Evolving Knowledge](https://aclanthology.org/2025.acl-long.48.pdf) (as "Content repetition")**
> The observable repetition of identical or nearly identical tokens, expressions, or comments in the generated code, such as repeated assertions or print statements.

**[LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ruoss25a/ruoss25a.pdf) (as "Action repetition")**
> The tendency of a model to output the same action repeatedly, even when inappropriate, such as holding down a fire button in a game without auto-fire.

**[Interpreting the Repeated Token Phenomenon in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yona25a/yona25a.pdf) (as "Token repetition")**
> Producing the same input token repeatedly when prompted with a repetition task.

## Relationships

### Repetitive generation →
- **Human evaluation** (measurements) — *measured_by*
  - [The Impact of Token Granularity on the Predictive Power of Language Model Surprisal](https://aclanthology.org/2025.acl-long.210.pdf)

### Associated with
- **Style transfer** (behaviors tasks)
  - [Reliability of Topic Modeling](https://aclanthology.org/2025.naacl-long.135.pdf)
- **Reward hacking** (behaviors tasks)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Overthinking** (behaviors tasks)
  - [Beyond Text: Unveiling Privacy Vulnerabilities in Multi-modal Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1260.pdf)
- **Faithfulness** (constructs)
  - [Current Semantic-change Quantification Methods Struggle with Discovery in the Wild](https://aclanthology.org/2025.emnlp-main.1792.pdf)
