# Task success
**Type:** Behavior  
**Referenced in:** 9 papers  
**Also known as:** Success classification, Passing unit tests, Completing subjective everyday tasks  

## State of the Field

Across the provided literature, 'Task success' is a multifaceted behavior defined and measured in various ways depending on the application domain. A prevalent framing treats it as an objectively verifiable outcome, such as generated code 'passing unit tests' or an agent accomplishing a user's goal from an initial instruction. This is often quantified using metrics like 'test computational accuracy (TCA)' or the 'Fraction of user tasks solved'. Other work defines it in the context of interactive scenarios, like achieving the goal of a 'dialogue game'. A distinct line of inquiry considers success in open-ended contexts, defining it as 'Completing subjective everyday tasks' which lack a single correct answer. The measurement of this behavior is correspondingly diverse, operationalized using benchmarks like WebArena and Android-in-the-Wild for agentic tasks. For more complex evaluations, an LLM-as-a-judge approach is used, and one study describes a model making a binary 'success or mistake' judgment based on visual and dialog evidence. Regarding factors that influence this behavior, one paper hypothesizes that reducing ambiguity 'should lead to improved code accuracy'.

## Sources

**[(iii) Neuron interference.](https://aclanthology.org/2025.emnlp-main.53.pdf) (as "Task completion")**
> The observable outcome where an LLM agent successfully accomplishes the user's intended goal as defined by the initial instruction.

**[TVQACML: Benchmarking Text-Centric Visual Question Answering in MultilingualChinese Minority Languages](https://aclanthology.org/2025.emnlp-main.706.pdf) (as "Success classification")**
> The observable behavior of making a binary decision (success or mistake) about whether a procedural task has been completed, based on a procedural text and visual evidence gathered through dialog.

**[Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?](https://aclanthology.org/2025.emnlp-main.1517.pdf)**
> Achieving the goal of a dialogue game, such as correctly guessing a target word or completing a collaborative objective.

**[Addressing Tokenization Inconsistency in Steganography and Watermarking Based on Large Language Models](https://aclanthology.org/2025.emnlp-main.362.pdf) (as "Passing unit tests")**
> The observable outcome where generated code, when executed against a set of predefined test cases, produces the expected outputs for all cases.

**[2025.emnlp-main.847.checklist](https://aclanthology.org/attachments/2025.emnlp-main.847.checklist.pdf) (as "Completing subjective everyday tasks")**
> The observable action of generating a response or solution for open-ended, real-world scenarios that lack a single, objectively correct answer.

## Relationships

### → Task success
- **Ambiguity** (constructs) — *causes*
  > Based on our definition of ambiguity, we hypothesize that ambiguity reduction should lead to improved code accuracy. (Section 1)
  - [DPED: Multi-Layer Noise Distillation for Privacy-Preserving Text Embeddings](https://aclanthology.org/2025.emnlp-main.1283.pdf)
