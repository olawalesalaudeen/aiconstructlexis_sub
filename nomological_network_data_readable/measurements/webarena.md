# WebArena
**Type:** Measurement  
**Referenced in:** 19 papers  

## State of the Field

WebArena is consistently characterized across the provided literature as a benchmark and interactive environment for evaluating autonomous agents. Its most common application is to measure the behavior of `Web navigation`, assessing an agent's ability to control a browser and complete tasks based on natural language instructions. Several papers also use WebArena to measure an agent's `Generalization` capabilities, citing its inclusion of diverse websites and task types from domains like e-commerce, forums, and development platforms. The benchmark is operationalized as a set of "long-horizon, realistic web tasks" running on what are described as "live, functional websites." According to its originating paper, evaluation is based on the "functional correctness of task completions." Some sources describe it as a "highly challenging benchmark" and specify it contains 812 test examples for grounding instructions to web interactions.

## Sources

**[Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)**
> Web-based interactive environment for evaluating agents' ability to navigate and complete tasks in a simulated browser through natural language and code.

## Relationships

### → WebArena
- **Web navigation** (behaviors tasks) — *measured_by*
  > We adopt Mind2Web and WebArena for evaluation for their generalizability and resemblance of real-world web interactions. (Section 2)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To further measure the generalizability of our method, we also evaluate on other popular benchmarks such as OSWorld and relevant domains from WebArena.
  - [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c995a913bc20ca39ce2231b8973be90a-Paper-Conference.pdf)
- **Task completion** (behaviors tasks) — *measured_by*
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
