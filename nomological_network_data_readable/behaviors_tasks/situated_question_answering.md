# Situated question answering
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Situational question answering  

## State of the Field

Across the provided literature, 'Situated question answering' is most commonly framed as a behavior involving answering questions grounded in a 3D scene. This task requires a model to use a provided multi-modal context to answer questions about objects, their attributes, counts, and spatial relations. As one paper describes it, the model answers a "text-image interleaved question grounded in the 3D scene" ("Multi-modal Situated Reasoning in 3D Scenes"). This form of question answering is explicitly related to `Spatial reasoning`, with questions designed to target this ability in embodied agents. The behavior is operationalized and measured using the `SQA3D` benchmark. A distinct, less frequent usage appears under the name 'Situational question answering,' which is defined as responding to questions about a scenario or dilemma. This alternative framing is used to elicit personality-specific responses, such as extroversion, and is associated with the `PERSONALITYBENCH` dataset.

## Sources

**[Multi-modal Situated Reasoning in 3D Scenes](https://proceedings.neurips.cc/paper_files/paper/2024/file/feaeec8ec2d3cb131fe18517ff14ec1f-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Answering questions about objects, attributes, counts, spatial relations, affordances, room type, or descriptions using the provided 3D situation context.

**[Neuron based Personality Trait Induction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d399b67fa017f0f7670102c88507720c-Paper-Conference.pdf) (as "Situational question answering")**
> The task of responding to questions that describe a specific scenario or dilemma, often designed to elicit personality-specific responses.

## Relationships

### Situated question answering →
- **SQA3D** (measurements) — *measured_by*
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)

### Associated with
- **Spatial reasoning** (constructs)
  > Situated QA is designed with different types of questions targeting various levels of spatial reasoning ability for embodied agents.
  - [SPARTUN3D: Situated Spatial Understanding of 3D World in Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/b633e7052970b8f5aa1a69164d99e9e8-Paper-Conference.pdf)
