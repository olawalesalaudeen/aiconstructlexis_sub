# AndroidWorld
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** ANDROIDWORLD, Android World  

## State of the Field

AndroidWorld is predominantly characterized across the surveyed literature as an online mobile agent benchmark that operates within a dynamic Android emulator. Its primary function is to evaluate autonomous agents, and it is consistently described as containing 116 programmatic tasks across 20 real-world applications. The benchmark is used to measure several agent constructs, with papers positioning it to assess `Adaptability`, `Safety`, and `Complex reasoning`. One study highlights its utility for "finer-grained analyses of agent adaptability" ("AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents"), while another frames it as an environment "requiring multi-step reasoning that mirrors real-world scenarios" ("Phi: Preference Hijacking in Multi-modal Large Language Models at Inference Time"). Operationally, the environment is described as virtual, with one paper specifying the use of a "Pixel 6 phone simulator" ("Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction"). Evaluation is most frequently based on task success rate, determined by "the final states of the device" ("Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents"). The benchmark's design incorporates "reproducible initialization, success-checking, and teardown logic" for each task. A less common application mentioned in one paper is its use for "trajectory collection" in addition to evaluation.

## Sources

**[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf) (as "ANDROIDWORLD")**
> A dynamic Android benchmark with 116 programmatic tasks across 20 real-world apps, using reproducible initialization, success-checking, and teardown logic to assess autonomous agents.

**[Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf)**
> An online mobile agent benchmark running in Android emulators that evaluates task success rate based on the final states of the device.

**[Boosting Virtual Agent Learning and Reasoning: A Step-Wise, Multi-Dimensional, and Generalist Reward Model with Benchmark](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25b/miao25b.pdf) (as "Android World")**
> An Android virtual agent benchmark used for trajectory collection and evaluation.

## Relationships

### → AndroidWorld
- **Adaptability** (constructs) — *measured_by*
  > This approach enables ﬁner-grained analyses of agent adaptability, essential for real-world deployment. (Section 3.3)
  - [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Phi: Preference Hijacking in Multi-modal Large Language Models at Inference Time](https://aclanthology.org/2025.emnlp-main.902.pdf)
