# ALFRED
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** ALFRed  

## State of the Field

Across the provided literature, ALFRED is consistently characterized as a benchmark or dataset for evaluating embodied agents in simulated household environments, which are identified as both the AI2-THOR simulator and Unity. The prevailing usage is as a "household planning benchmark" with human-annotated, language-specified tasks that involve object manipulation and state changes like "heating, cooling, and cleaning." Papers operationalize evaluation on ALFRED by measuring an agent's planning and execution capabilities, with one study specifying that "planning performance" is measured "using the task success rates" based on goal condition satisfaction. The benchmark is explicitly used to measure constructs such as `3D perception` and `Safety`. This connection to 3D is further illustrated by one paper that curates a "new 3D evaluation test set" from ALFRED. A less common framing focuses on its application to "long-horizon embodied tasks" and adopts its "task decomposition method" for experimental setups.

## Sources

**[Learning Grounded Action Abstractions from Language](https://proceedings.iclr.cc/paper_files/paper/2024/file/99dec5837aae1a7459960c6121b9e3b8-Paper-Conference.pdf)**
> Household planning benchmark with human-annotated, formally verifiable tasks in a simulated Unity environment, involving object manipulation and state changes such as heating, cooling, and cleaning.

**[MLLM as Retriever: Interactively Learning Multimodal Retrieval for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e447acb68f57e29234bc0eb19896f11-Paper-Conference.pdf) (as "ALFRed")**
> An AI2-THOR-based benchmark for long-horizon embodied tasks, whose task decomposition method is adopted in the paper's experimental setup.

## Relationships

### → ALFRED
- **Robustness** (constructs) — *measured_by*
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **3D perception** (constructs) — *measured_by*
  - [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf)
