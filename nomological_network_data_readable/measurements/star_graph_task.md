# Star Graph Task
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Star graph problem, Star distribution  

## State of the Field

The Star Graph Task is a benchmark used in the provided literature to measure constructs like Pathfinding and Planning. It is consistently described as a task involving a star-shaped graph where a model must determine the path between a start and goal node. The structure is typically a central start node with several "spokes" or paths radiating outwards. While the core concept is consistent, its operationalization varies across papers. Some studies require the model to predict the entire sequence of nodes or output the full path, while another formulates it as a next-node prediction task given a partial path. The framing of the task also differs; it is described as both a "simple path finding task" and a "didactic" problem for analyzing memorization versus generalization, though one paper also refers to it as a "known-hard problem". A less common framing describes it as a "graph-generation procedure" rather than a task.

## Sources

**[The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)**
> A path-finding benchmark in which a model must predict the sequence of nodes along a path from a start node to a specified final node.

**[RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b77d5b896c321a29277524a98a50215-Paper-Conference.pdf) (as "Star graph problem")**
> A didactic planning task where a model must output the full path between two nodes in a star-shaped graph, used to analyze memorization versus generalization.

**[Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf) (as "Star distribution")**
> A graph-generation procedure in which the start vertex is at the center of a star and each spoke is a linear chain ending in the goal.

## Relationships

### → Star Graph Task
- **Pathfinding** (behaviors tasks) — *measured_by*
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
- **Planning** (constructs) — *measured_by*
  - [The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf)
