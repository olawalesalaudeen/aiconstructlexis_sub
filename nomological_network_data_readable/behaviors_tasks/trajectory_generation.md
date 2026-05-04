# Trajectory generation
**Type:** Behavior  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, trajectory generation is consistently described as the production of a sequence of states, actions, or poses over time, though its specific application varies across different research contexts. One framing treats this behavior as a rehearsal mechanism in decision-making, where an agent generates "imagined states, actions, and rewards" to form an "imaginary dataset" based on retrieved knowledge ("Policy Learning from Tutorial Books via Understanding, Rehearsing and Introspecting"). In the domain of physical navigation, the behavior is operationalized more concretely as producing a sequence of future waypoints, for example, using a "hierarchical trajectory decoder" to generate a UAV's next target pose ("Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology"). A third usage appears in the context of modeling dynamic systems, where the goal is to generate "new, plausible state sequences (trajectories) that conform to the underlying dynamics provided in the context" ("Zebra: In-Context Generative Pretraining for Solving Parametric PDEs"). In this setting, the behavior is evaluated by assessing if the model "effectively generates faithful trajectory distributions that closely match the real simulated trajectory distribution."

## Sources

**[Policy Learning from Tutorial Books via Understanding, Rehearsing and Introspecting](https://proceedings.neurips.cc/paper_files/paper/2024/file/21cf8411ed825614e00006a1d9aab7e4-Paper-Conference.pdf)**
> The observable production of sequences of imagined states, actions, and rewards based on retrieved knowledge.
