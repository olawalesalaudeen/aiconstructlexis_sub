# GAIA
**Type:** Measurement  
**Referenced in:** 9 papers  

## State of the Field

Across the provided literature, GAIA is consistently characterized as a benchmark or dataset designed to evaluate the capabilities of general AI assistants. It is most frequently used to assess an agent's proficiency in tool use, multimodal understanding, and information-seeking behaviors like web browsing and file reading. The benchmark's tasks are also described as evaluating a range of other competencies, including reasoning, coding, and document understanding. Reflecting this broad scope, papers report using GAIA to measure constructs such as `Tool use`, `Multimodal understanding`, `Web navigation`, `Generalization`, `Commonsense knowledge`, and `Safety`. Operationally, GAIA is described as a collection of human-designed questions, with sources citing either 446 tasks with 109 files or 466 annotated questions. As one paper states, it "evaluates agents’ general task-solving skills, covering different real-world scenarios" ("OpenHands: An Open Platform for AI Software Developers as Generalist Agents"). The prevailing usage of GAIA is as a multi-faceted evaluation instrument for complex, real-world agentic tasks.

## Sources

**[Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf)**
> GAIA is a multi-modal benchmark with 446 tasks and 109 files used to evaluate document understanding, web surfing, logic reasoning, and answer summarization.

## Relationships

### → GAIA
- **Reasoning** (constructs) — *measured_by*
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *measured_by*
  > We evaluate MaAS on six public benchmarks covering three domains: ... and (3) tool use, GAIA (Mialon et al., 2023) (Section 4.1).
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **Web navigation** (behaviors tasks) — *measured_by*
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > "We validated OSCAR’s effectiveness and generalizability across diverse benchmarks involving both desktop and smartphone OS environments. On the GAIA (Mialon et al., 2023) benchmark, OSCAR outperformed previous methods"
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > It requires various agent capabilities, including reasoning, multi-modal understanding, web browsing, and coding. (§4.4)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
