# Mind2Web
**Type:** Measurement  
**Referenced in:** 16 papers  

## State of the Field

Across the surveyed literature, Mind2Web is consistently characterized as a benchmark or dataset for evaluating agents on real-world web navigation tasks. It is frequently described as containing human demonstrations of complex, multi-step tasks based on language instructions across a wide range of open-domain websites, with several sources noting it contains over 2,000 instructions. The most prevalent application of Mind2Web is to measure an agent's `Web navigation` capabilities, with a recurring emphasis on assessing generalization across different tasks, websites, and domains. It is also used to evaluate more specific behaviors, including `Action prediction`, `Planning`, and, in one instance, agent `Adaptability`. Performance on the benchmark is commonly operationalized using metrics such as "step success rate" and "element accuracy," with some work also reporting "action F1" and "task-level success rate." While most papers treat it as an evaluation tool, some frame it as an "ofﬂine task planning evaluation" or use it as a data source from which to collect agent trajectories. A minority framing from one paper conceptualizes its tasks as "dynamic how-to question[s]".

## Sources

**[A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)**
> Real-world web navigation benchmark containing human demonstrations across open-domain websites, assessing generalization across tasks, websites, and domains using step success rate and element accuracy.

## Relationships

### → Mind2Web
- **Web navigation** (behaviors tasks) — *measured_by*
  > “We employ Mind2Web (Deng et al., 2023) to train and evaluate the agent’s capability of performing complex instructions on real-world websites.”
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
- **Action prediction** (behaviors tasks) — *measured_by*
  > “In the action prediction tasks, we transfer WebGUM finetuned for MiniWoB++ with 401K dataset into real-world Mind2Web”
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
- **Planning** (constructs) — *measured_by*
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
- **Adaptability** (constructs) — *measured_by*
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
