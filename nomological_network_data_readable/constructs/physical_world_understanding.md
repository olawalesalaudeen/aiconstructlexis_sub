# Physical world understanding
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Physical reasoning, Physics-based dynamics understanding, Physical object property understanding, Physical object relationship understanding, Physical scene understanding, Intuitive physics, Physical dynamics understanding, Physical awareness  

## State of the Field

Across the surveyed literature, physical world understanding is predominantly framed as a model's latent ability to perceive, interpret, and predict events governed by physical principles, based on sensory inputs. While various terms like 'physical reasoning', 'intuitive physics', and 'physical awareness' are used, they converge on the core idea of reasoning about object properties, relationships, and dynamics. One line of work offers a more structured view, decomposing the construct into understanding physical object properties like mass and stiffness, object relationships involving spatial positions, scene context such as viewpoints, and physics-based dynamics like collisions. The field operationalizes this construct through evaluation on specialized benchmarks, with one paper introducing PhysBench as a tool to “evaluate VLMs’ physical world understanding capability.” Other approaches measure this ability by assessing a model's capacity to reason about 4D dynamic scenes from video or, as one paper proposes, by teaching 'physical awareness' through auditory cues, which are described as containing 'fine-grained physical cues.' This construct is studied in relation to spatial reasoning, particularly concerning the evaluation of object positions and scene viewpoints. Furthermore, it is positioned as a capability that enables downstream behaviors like robotic manipulation and is presented as a 'fundamental challenge in embodied AI.'

## Sources

**[Compositional 4D Dynamic Scenes Understanding with Physics Priors for Video Question Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea06e6e9e80f1c3d382317fff67041ac-Paper-Conference.pdf) (as "Physical reasoning")**
> The ability to apply principles of physics to explain observed events, infer object properties, and simulate future outcomes in a given scene.

**[PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf)**
> The ability to perceive, interpret, and predict the properties and dynamics of objects and environments based on visual cues and core physical principles.

**[PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf) (as "Physical object property understanding")**
> The latent capacity to infer intrinsic physical attributes of objects such as mass, size, density, stiffness, elasticity, and plasticity.

**[PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf) (as "Physical object relationship understanding")**
> The ability to evaluate the spatial and motion-based relationships between objects, including their relative or absolute positions and movements.

**[PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf) (as "Physical scene understanding")**
> The latent capacity to interpret environmental factors in a scene, including light sources, viewpoints, temperature, and related contextual cues.

**[PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf) (as "Physics-based dynamics understanding")**
> The latent capacity to anticipate physical events and outcomes governed by dynamics such as collisions, throwing, fluid behavior, and explosions.

**[Core Knowledge Deficits in Multi-Modal Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25p/li25p.pdf) (as "Intuitive physics")**
> Intuitions about how physical objects interact according to basic laws in the physical world.

**[Teaching Physical Awareness to LLMs through Sounds](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ca/wang25ca.pdf) (as "Physical awareness")**
> The latent ability of a model to understand and meaningfully interact with the physical world by interpreting real-world physical phenomena.

**[UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25w/zhang25w.pdf) (as "Physical dynamics understanding")**
> The latent capacity to model and predict how objects and agents move and interact over time in the physical world, inferred from visual and action sequences.

## Relationships

### Physical world understanding →
- **Robotic manipulation** (behaviors tasks) — *causes*
  - [PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf)

### Associated with
- **Spatial reasoning** (constructs)
  > “Physical Object Relationships: Evaluation of spatial relationships involving objects’ relative or absolute positions and motions.”
  - [PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf)
- **Causal reasoning** (constructs)
  - [Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schulze-buschoff25a/schulze-buschoff25a.pdf)
