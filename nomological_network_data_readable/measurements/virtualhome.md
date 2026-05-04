# VirtualHome
**Type:** Measurement  
**Referenced in:** 15 papers  

## State of the Field

Across the provided literature, VirtualHome is consistently described as a simulated 3D household environment used as a benchmark for embodied agents. It is widely used to evaluate an agent's capabilities in task planning and execution, specifically measuring constructs such as `Embodied planning`, `Sequential decision-making`, and `Generalization`. Other papers in this set also use it to assess `Cross-domain generalization`, `Data efficiency`, `Decision-making`, and `Safety`. The benchmark operationalizes these constructs by requiring an agent to complete complex, multi-step household activities in a "fully furnished household with various rich objects." Agents interact with the environment through a defined set of actions, including "pick up," "open," "close," "switch on," "put down," and "find," to determine if their generated plans are executable. While most sources frame it as a general task planning environment, a few papers offer more specific descriptions; for instance, one paper characterizes it as an "interactive simulator for modeling... human-agent collaboration." Another source notes that the benchmark offers "long-horizon... and multi-agent tasks" but also points out that it "lacks time delays."

## Sources

**[LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf)**
> VirtualHome is an embodied environment benchmark used to evaluate whether generated plans translate into executable household action programs.

## Relationships

### → VirtualHome
- **Generalization** (constructs) — *measured_by*
  > For the last two crossover tests, TWOSOME agent trained in Food Preparation is tested in Entertainment and TWOSOME trained in Entertainment is tested in Food Preparation. (Figure 6)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **Data efficiency** (constructs) — *measured_by*
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **Decision-making** (constructs) — *measured_by*
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **Sequential decision-making** (constructs) — *measured_by*
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **Embodied planning** (behaviors tasks) — *measured_by*
  > To evaluate the effectiveness of DGAP and other baseline methods in complex embodied reasoning tasks, we employ the ScienceWorld (Wang et al., 2022) and VirtualHome (Puig et al., 2018) benchmark.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **Cross-domain generalization** (constructs) — *measured_by*
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
