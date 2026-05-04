# Action sequence generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Action sequence generation is consistently defined as the task of an agent producing an ordered series of actions to achieve a goal. However, the specific context and nature of these actions differ across the provided sources. One operationalization of this behavior occurs within game environments, where an agent must generate a "structured list of discrete actions (e.g., 'move_up', 'move_left')" to navigate from a starting position to an objective (GameTraversalBenchmark). A different framing treats it as "producing a series of API calls in a specific order to fulfill a user's query" (ShortcutsBench). In this latter context, the generation of a subsequent action is noted to depend on the history of prior actions. In both cases, the agent's task is to generate a sequence that accomplishes a specified objective, whether it is reaching a target position or satisfying a user request.

## Sources

**[GameTraversalBenchmark: Evaluating Planning Abilities Of Large Language Models Through Traversing 2D Game Maps](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852c8254bc6d904c09db9921157f59b-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The task of producing a structured list of discrete actions (e.g., 'move_up', 'move_left') for an agent to execute in an environment.
