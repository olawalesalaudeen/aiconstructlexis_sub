# RACE
**Type:** Measurement  
**Referenced in:** 42 papers  

## State of the Field

Across the surveyed literature, RACE is consistently described as a reading comprehension benchmark derived from English exams for middle and high school students. The dataset is most frequently used to measure the constructs of `Reading comprehension` and `Language understanding`. It operationalizes this measurement through passage-based, multiple-choice questions. While this general framing is prevalent, different papers emphasize distinct facets of the abilities it assesses. For instance, one paper uses it to evaluate "factual QA", while another targets "reading reasoning capabilities". A more specific characterization appears in one study that describes RACE as a "'needle-in-a-haystack' task" for evaluating `long-context processing` and `logical reasoning`. In addition to these reasoning and comprehension tasks, the benchmark is also used in at least one case to evaluate `Text generation`.

## Sources

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)**
> Reading Comprehension dataset collected from English exams for middle and high school students, assessing reasoning and understanding ability through passage-based multiple-choice questions.

## Relationships

### → RACE
- **Reading comprehension** (constructs) — *measured_by*
  > “we define five fundamental LLM capabilities, namely Mathematical Reasoning, Reading Comprehension, Commonsense Reasoning, Scientific Reasoning, and Professional Expertise”
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > RACE is a reading comprehension benchmark introduced in Lai et al. (2017) collected from English examinations of middle and high school students. (Section 3)
  - [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [How Humans andLLMs Organize Conceptual Knowledge: Exploring Subordinate Categories inItalian](https://aclanthology.org/2025.acl-long.225.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > This suggests that the state space architecture effectively enhances logical reasoning capabilities without compromising long-text processing efficiency. (Section 4.5)
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
