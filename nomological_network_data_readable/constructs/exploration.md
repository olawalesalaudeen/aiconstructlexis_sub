# Exploration
**Type:** Construct  
**Referenced in:** 21 papers  
**Also known as:** Exploration capability, Exploitation, Exploration ability, Self-exploration, Action exploration, Codebase exploration  

## State of the Field

Across the surveyed literature, 'Exploration' is predominantly framed in two ways: as a process of searching a solution space for diverse reasoning paths, or as an observable behavior of an agent navigating a physical or digital environment. The most common usage describes exploration as the process of searching broadly to discover varied solutions, defined as a model's latent ability or tendency to generate diverse reasoning paths. This form of exploration is operationalized by evaluating the diversity of model outputs, where metrics like Pass@k are used to indicate a model's "ability to explore diverse reasoning paths" (MARGE: Improving Math Reasoning with Guided Exploration). A separate line of work treats exploration as the observable behavior of an agent actively searching an environment to locate objects, visit new states, or gather information, particularly in embodied or interactive tasks. The concept is also applied in more specialized contexts, such as 'codebase exploration' for navigating code repositories and 'action exploration' for trying different actions in a search process. Exploration is frequently contrasted with 'exploitation,' which is defined as refining known solutions, and some methods aim to "balance exploration and exploitation" (SFS: Smarter Code Space Search improves LLM Inference Scaling). Finally, some work suggests that exploration is enhanced by capabilities like 'Language understanding' and 'Commonsense understanding' and is studied in relation to 'Active information gathering'.

## Sources

**[Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf) (as "Exploration capability")**
> The latent ability of an agent to discover useful states and solution paths in environments that require systematic search over long horizons.

**[SFS: Smarter Code Space Search improves LLM Inference Scaling](https://proceedings.iclr.cc/paper_files/paper/2025/file/387982dbf23d9975c7fc45813dd3dabc-Paper-Conference.pdf)**
> The process of searching broadly across a solution space to discover varied and potentially novel solutions, rather than focusing only on refining existing ones.

**[SFS: Smarter Code Space Search improves LLM Inference Scaling](https://proceedings.iclr.cc/paper_files/paper/2025/file/387982dbf23d9975c7fc45813dd3dabc-Paper-Conference.pdf) (as "Exploitation")**
> The process of refining and improving upon known, promising solutions by leveraging feedback and prior search experience to intensify the search in a local region.

**[MARGE: Improving Math Reasoning with Guided Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25h/gao25h.pdf) (as "Exploration ability")**
> The tendency of a model to generate diverse reasoning paths and cover more of the solution space when producing multiple candidate answers.

**[Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf) (as "Self-exploration")**
> The latent ability of a model to identify flaws in its reasoning and generate alternative solution paths without external intervention.

**[Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf) (as "Action exploration")**
> The behavior of selecting and trying out different actions within a search or learning process to discover their outcomes and potential rewards.

**[OrcaLoca: An LLM Agent Framework for Software Issue Localization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25x/yu25x.pdf) (as "Codebase exploration")**
> The observable process of an agent navigating and searching through a code repository to gather context and identify relevant code entities.

## Relationships

### → Exploration
- **Language understanding** (behaviors tasks) — *causes*
  - [Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs) — *causes*
  - [Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf)

### Associated with
- **Active information gathering** (behaviors tasks)
  - [B-STaR: Monitoring and Balancing Exploration and Exploitation in Self-Taught Reasoners](https://proceedings.iclr.cc/paper_files/paper/2025/file/c8db30c6f024a3f667232ed7ba5b6d47-Paper-Conference.pdf)
