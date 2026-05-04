# Pathfinding
**Type:** Behavior  
**Referenced in:** 19 papers  
**Also known as:** Shortest path finding, Shortest path prediction, Shortest path identification, Graph path finding, Route finding, Graph navigation, Knowledge graph navigation, Spatial pathfinding, Path planning, Trajectory planning, Motion planning, Route planning, Path finding, Hamilton path finding  

## State of the Field

Across the provided literature, Pathfinding is predominantly characterized as the behavior of generating a sequence of steps to connect a starting point to a goal, with two main framings. The most prevalent operationalization involves tasks on abstract graphs, commonly focusing on finding the 'shortest path' between two nodes in a weighted graph by generating the exact sequence of nodes or constituent edges. Other graph-based variations include determining if any path exists ('Graph navigation'), traversing a knowledge graph, or finding a 'Hamilton path' that visits every node exactly once. A second common framing treats Pathfinding as spatial navigation or planning, such as 'route finding' in a grid world, solving mazes, or generating actions for an agent to obey constraints. In some robotics-focused work, this extends to 'motion planning' or 'trajectory planning' in 3D space. The behavior is measured using instruments like the `Star Graph Task` and `Human evaluation`. Pathfinding is studied as a form of `Graph reasoning` and is also reported to be driven by the construct of `Spatial reasoning`.

## Sources

**[Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf) (as "Shortest path finding")**
> The task of identifying the path with the minimum total weight between two specified nodes in a weighted, undirected graph.

**[GOFA: A Generative One-For-All Model for Joint Graph Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/652c104b5b0652a03684efeaf805463b-Paper-Conference.pdf) (as "Shortest path prediction")**
> The observable task of identifying and generating the shortest path(s) and their distance between two specified nodes in a graph.

**[ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf) (as "Shortest path identification")**
> Generating the exact sequence of nodes representing the shortest path between two nodes in a graph structure.

**[Beyond Autoregression: Discrete Diffusion for Complex Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1b3d1e2cf53bb28cabd801bd58b3521-Paper-Conference.pdf) (as "Graph path finding")**
> Given a graph-like input with start and goal nodes, the model outputs the constituent edges of the correct path.

**[Enhancing Graph Of Thought: Enhancing Prompts with LLM Rationales and Dynamic Temperature Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/c87245c9e8882bc1b6d4ec343d430e71-Paper-Conference.pdf) (as "Route finding")**
> Producing a valid path from a start location to a destination while obeying constraints in a grid world.

**[Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)**
> Solving navigation tasks by generating a sequence of actions or coordinates to reach a goal location from a start point.

**[Position: We Need An Algorithmic Understanding of Generative AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eberle25a/eberle25a.pdf) (as "Graph navigation")**
> The observable behavior of determining whether a path exists between nodes in a graph structure, given a textual description of connections.

**[Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf) (as "Knowledge graph navigation")**
> The observable task of traversing and reasoning over a knowledge graph to find information or relationships.

**[2025.emnlp-main.1714.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1714.checklist.pdf) (as "Spatial pathfinding")**
> The observable task of finding a route between points in a synthetic spatial environment based on a series of factual statements.

**[GAMap: Zero-Shot Object Goal Navigation with Multi-Scale Geometric-Affordance Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/459d93dad139eb084c365d40a57eada3-Paper-Conference.pdf) (as "Path planning")**
> The process of computing a sequence of actions or a trajectory for an agent to follow to travel from its current position to a designated goal location.

**[SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf) (as "Trajectory planning")**
> The task of generating a sequence of 3D movements or paths for an object or robot end-effector to achieve a goal state.

**[SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf) (as "Motion planning")**
> The process of determining a sequence of movements or waypoints for an object to achieve a goal, based on a high-level task description.

**[Mind's Eye of LLMs: Visualization-of-Thought Elicits Spatial Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/a45296e83b19f656392e0130d9e53cb1-Paper-Conference.pdf) (as "Route planning")**
> A sub-task of visual navigation where the model must generate the complete sequence of directional moves to travel from a starting point to a destination.

**[The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf) (as "Path finding")**
> The task of generating a sequence of nodes that constitutes a valid path from a starting node to a target node within a given graph structure.

**[GITA: Graph to Visual and Textual Integration for Vision-Language Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/00295cede6e1600d344b5cd6d9fd4640-Paper-Conference.pdf) (as "Hamilton path finding")**
> Finding a path in an undirected graph that visits every node exactly once.

## Relationships

### Pathfinding →
- **Star Graph Task** (measurements) — *measured_by*
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)

### → Pathfinding
- **Spatial reasoning** (constructs) — *causes*
  - [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)

### Associated with
- **Graph reasoning** (constructs)
  > We define the length-2 path problem on a graph, and use it as a means to understand other graph reasoning tasks such as graph connectivity, shortest path, and cycle detection. (Section 3.2)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
