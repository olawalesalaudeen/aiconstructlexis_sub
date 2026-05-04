# MINT
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, MINT is consistently described as a benchmark or evaluation framework designed to assess LLM capabilities in multi-turn, interactive scenarios. Its primary function, as stated in multiple papers, is to evaluate an agent's ability to solve challenging tasks by both using tools and leveraging natural language feedback. The framework is operationalized by adapting existing datasets into feedback-rich environments, with one paper noting the use of a "GPT-4 simulated user as a teacher to guide the model in problem-solving" ('Lemur: Harmonizing Natural Language and Code for Language Agents'). The tasks within MINT are drawn from domains such as reasoning, code generation, and decision-making, with some studies focusing specifically on its coding and math problems. In practice, papers use MINT to measure constructs like `Dialogue` and `In-context learning`, with the latter being directly linked to the benchmark's emphasis on an LLM's ability to process natural language feedback. Other capabilities the benchmark is reported to assess include tool utilization and self-debugging.

## Sources

**[Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)**
> Multi-turn Interactive agent evaluation framework that adapts existing datasets into interactive, feedback-rich environments for assessing agent capabilities like tool use and self-debugging.

## Relationships

### → MINT
- **Multi-turn interaction** (behaviors tasks) — *measured_by*
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  > It is a benchmark for LLMs that measures their performance during multi-turn interaction, focusing on two particular capabilities (§2.1): ... (2) leveraging natural language feedback. (Section 1)
  - [MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf)
