# Arena-Hard-Auto
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** Arena-Hard-Auto-v0.1  

## State of the Field

Across the provided sources, Arena-Hard-Auto is consistently characterized as an automated benchmark that uses a strong LLM as a judge to evaluate model performance on challenging prompts. The most common definition describes its mechanism as conducting pairwise comparisons against a baseline model, using a Likert scale and chain-of-thought prompting to score outputs. Papers use this instrument to measure several concepts, most frequently to evaluate "human preference to models’ generations," but also to assess commonsense knowledge. A specific version, Arena-Hard-Auto-v0.1, is described as being designed to assess chat and instruction-following capabilities using 500 complex prompts. This benchmark is frequently listed alongside other LLM-judge instruments like MT-Bench and AlpacaEval. It is explicitly positioned as an automated replication of the LMSYS Chatbot Arena, with one source reporting that its v0.1 version achieves "89% agreement with human rankings" from the original arena.

## Sources

**[Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)**
> A popular LLM-judge benchmark that conducts pairwise comparisons against a baseline model, using a Likert scale and chain-of-thought prompting to score outputs.

**[Predicting Through Generation: Why Generation Is Better for Prediction](https://aclanthology.org/2025.acl-long.1304.pdf) (as "Arena-Hard-Auto-v0.1")**
> Automated evaluation that uses an LLM to judge model responses to 500 complex prompts, replicating LMSYS Chatbot Arena with 89% agreement with human rankings, designed to assess chat and instruction-following capabilities.

## Relationships

### Arena-Hard-Auto →
- **LMSYS Chatbot Arena** (measurements) — *correlates*
  - [From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf)

### → Arena-Hard-Auto
- **Instruction following** (constructs) — *measured_by*
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  > Thus we adopt MT-Bench (Zheng et al., 2023), AlpacaEval (Li et al., 2023b), and Arena-Hard-Auto (Li et al., 2024b) to evaluate human preference to models’ generations. (Section 3.2)
  - [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.52.pdf)
