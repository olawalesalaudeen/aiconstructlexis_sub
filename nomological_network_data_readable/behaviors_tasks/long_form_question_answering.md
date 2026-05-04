# Long-form question answering
**Type:** Behavior  
**Referenced in:** 13 papers  

## State of the Field

Across the surveyed literature, long-form question answering (LFQA) is most commonly defined as the task of generating extended, paragraph-length responses to open-ended questions, a process that often requires information synthesis and contextual coherence. While this general definition is prevalent, some papers frame the task more specifically, such as generating answers from retrieved evidence in a retrieval-augmented setting, synthesizing responses from tabular data, or answering questions based on information within long documents. The field operationalizes and measures this behavior using a variety of benchmarks. The ELI5 dataset appears frequently as an instrument for this task, described as being for "complex QA with paragraph-length responses." Other benchmarks are used to assess more specific capabilities within LFQA, including TruthfulQA for evaluating truthful generation, LaMP-QA for personalized answer generation, and UNCLE for measuring uncertainty expression. Beyond being a standalone task, LFQA serves as an evaluation setting in studies on topics like watermarking and controlling for specific stylistic attributes like quoting.

## Sources

**[DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.191.pdf)**
> Generating extended, paragraph-length responses to open-ended questions, often requiring synthesis of information and contextual coherence.

## Relationships

### Long-form question answering →
- **ELI5** (measurements) — *measured_by*
  > We utilize two popular datasets for the task of long-form QA, including: ... 2) ELI5, which is a dataset for complex QA with paragraph-length responses... (Section 4)
  - [LLM4DistReconfig: A Fine-tuned Large Language Model for Power Distribution Network Reconfiguration](https://aclanthology.org/2025.naacl-long.209.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > To assess long-form generation capabilities, we utilized TruthfulQA (Lin et al., 2022), which requires the model to produce truthful answers when faced with questions to elicit false or misleading responses. (Section 4)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
- **LaMP-QA** (measurements) — *measured_by*
  > We address this gap by introducing LaMP-QA—a benchmark designed for evaluating personalized long-form answer generation.
  - [2025.emnlp-main.60.checklist](https://aclanthology.org/attachments/2025.emnlp-main.60.checklist.pdf)
- **UNCLE** (measurements) — *measured_by*
  > we first introduce UNCLE, a benchmark designed to evaluate uncertainty expression in both long- and short-form question answering (QA). (Abstract)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1543.pdf)
