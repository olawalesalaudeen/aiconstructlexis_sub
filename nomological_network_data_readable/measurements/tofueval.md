# TofuEval
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, TofuEval is consistently described as a dataset or benchmark for evaluating factual consistency, primarily in the context of dialogue summarization. It is used by researchers to measure the construct of `Faithfulness` and to assess performance on `Text summarization` and `Meeting summarization` tasks. A recurring theme is its design as a "topic-focused" benchmark, with several papers highlighting its specific emphasis on evaluating summarization of "marginal or secondary topics." One source characterizes it as a "more challenging benchmark" for this reason, while another notes it targets "factual alignment under topic shifts." The dataset is reported to be composed of annotated subsets of MediaSum and MeetingBank, covering both news and dialogue domains. One paper specifies that these annotations include "human-annotated sentence-level faithfulness judgments and critiques" (Palette of Language Models: A Solver for Controlled Text Generation).

## Sources

**[AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios](https://aclanthology.org/2025.naacl-long.258.pdf)**
> A dataset for evaluating factual consistency in dialogue summarization.

## Relationships

### → TofuEval
- **Faithfulness** (constructs) — *measured_by*
  - [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.498.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Ethical Concern Identification inNLP: A Corpus ofACLAnthology Ethics Statements](https://aclanthology.org/2025.naacl-long.581.pdf)
- **Meeting summarization** (behaviors tasks) — *measured_by*
  > Among these, CREAM (Gong et al., 2024), MESA (Kirstein et al., 2025b), and TofuEval (Tang et al., 2024) stand out as one of the few frameworks specifically developed for meeting and dialogue summarization, targeting long-context summarizations and dialogue-based meeting summarizations.
  - [Frequency & Compositionality in Emergent Communication](https://aclanthology.org/2025.emnlp-main.1388.pdf)
