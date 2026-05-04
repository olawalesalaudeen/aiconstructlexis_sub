# ScienceWorld
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

Across the provided literature, ScienceWorld is consistently characterized as a textual, interactive simulation benchmark for embodied AI. The prevailing usage of this benchmark involves agents performing basic or "elementary-level scientific experiments" by navigating a simulated environment, manipulating objects, and observing outcomes. A recurring theme in its description is that the tasks are long-horizon and set in a large-action-space, demanding capabilities such as subtask decomposition, long-term memory, and instruction following. Papers use ScienceWorld to measure a range of agent capabilities, most frequently scientific experimentation and scientific reasoning, with one paper noting its aim is "to assess whether AI models can apply scientific knowledge." It is also employed to evaluate embodied planning, generalization, commonsense knowledge, and commonsense understanding. The environment is described as one for "physical interaction simulation" where agents must conduct experiments, often specified in natural language, to achieve specified goals.

## Sources

**[Policy Improvement using Language Feedback Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4d4f7cf206bb00f9a38a5b6ae92cf79a-Paper-Conference.pdf)**
> A textual simulation benchmark for basic science experiments used to evaluate instruction following in long-horizon, large-action-space settings.

## Relationships

### → ScienceWorld
- **Generalization** (constructs) — *measured_by*
  > Comprehensive studies on ScienceWorld and ALFWorld benchmarks show that our method consistently improves performance and generalization capacity, surpassing a range of baselines by a significant margin. (Summary of Contributions)
  - [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf)
- **Scientific experimentation** (behaviors tasks) — *measured_by*
  > ScienceWorld (Wang et al., 2022a) is an interactive benchmark designed for embodied science experiments. (Section 4.1)
  - [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf)
- **Scientific reasoning** (constructs) — *measured_by*
  > ScienceWorld... is an interactive benchmark designed for embodied science experiments... The aim is to assess whether AI models can apply scientific knowledge.
  - [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf)
- **Embodied planning** (behaviors tasks) — *measured_by*
  > To evaluate the effectiveness of DGAP and other baseline methods in complex embodied reasoning tasks, we employ the ScienceWorld (Wang et al., 2022) and VirtualHome (Puig et al., 2018) benchmark.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [FLEURS-ASL: IncludingAmericanSignLanguage in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.315.pdf)
