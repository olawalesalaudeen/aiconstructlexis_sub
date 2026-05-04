# Robotic manipulation
**Type:** Behavior  
**Referenced in:** 27 papers  
**Also known as:** Robotic control, Visuo-motor control, Robot manipulation, Object rearrangement, Object transport, Tabletop manipulation, Low-level manipulation, Multi-step manipulation, Object sorting, Embodied robotic control, Long-horizon manipulation, Pushing, Throwing, Touching, Stacking, Pick and stack  

## State of the Field

Across the surveyed literature, robotic manipulation is predominantly characterized as the observable behavior of a robot physically interacting with objects to achieve a goal, often guided by visual and language inputs. Definitions vary in granularity, from broad descriptions like "producing control actions" to more specific tasks such as "object rearrangement," "tabletop manipulation," and "object sorting." A subset of work further breaks down the behavior into atomic actions like "pushing," "stacking," and "throwing." The complexity also ranges from "low-level manipulation," which involves controlling a robotic arm through fine-grained action vectors, to "long-horizon manipulation" requiring the execution of multi-step sequences.

To measure this behavior, researchers commonly employ simulation benchmarks. The `Meta-world` benchmark suite is a frequently cited instrument for this purpose, alongside others like `RLBench` and `MuJoCo`. These platforms operationalize manipulation through specific tasks such as "Reach-v2, Push-v2, Pick-Place-v2." Several cognitive constructs are reported to enable successful robotic manipulation, including `commonsense knowledge`, `spatial reasoning`, `instruction understanding`, and `physical world understanding`.

## Sources

**[Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf) (as "Robotic control")**
> Producing control actions in a simulated robotics environment to achieve task goals.

**[HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3bfee3bc6639c36e6e7b058db909f760-Paper-Conference.pdf) (as "Robot manipulation")**
> The observable act of a robot interacting with and physically altering its environment to achieve a specified goal.

**[Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf) (as "Visuo-motor control")**
> Producing robot action trajectories for manipulation tasks from visual and textual task inputs.

**[Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c4a7643ab90cd62320df95c873a1c6f-Paper-Conference.pdf)**
> Performing continuous control manipulation tasks such as reaching, pushing, picking, sweeping, and peg insertion.

**[EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/8ec46cecdae5407662899c5f6698cd8b-Paper-Conference.pdf) (as "Object rearrangement")**
> A complex, observable task requiring agents to move one or more objects from their initial locations to specified goal locations, often involving multiple steps and coordination.

**[LLaRA: Supercharging Robot Learning Data for Vision-Language Policy](https://proceedings.iclr.cc/paper_files/paper/2025/file/909f526db5127f8bd8158af32d9e313a-Paper-Conference.pdf) (as "Robot action generation")**
> Producing robot control actions from visual observations and task instructions, including pick-and-place and rotation decisions.

**[CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf) (as "Object transport")**
> The task of moving one or more objects from a starting location to a specified destination within a simulated environment, potentially using containers.

**[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf) (as "Tabletop manipulation")**
> The task of physically interacting with and rearranging objects on a flat surface like a table.

**[Perception in Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25r/wei25r.pdf) (as "Multi-step manipulation")**
> The execution of a sequence of actions based on visual input to achieve a specific goal.

**[DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf) (as "Object sorting")**
> The task of grasping multiple objects and placing them into designated areas based on their category.

**[EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf) (as "Low-level manipulation")**
> Controlling a robotic arm through fine-grained 7D action vectors to perform object interactions such as picking up or stacking, requiring accurate spatial and visual perception.

**[Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf) (as "Embodied robotic control")**
> Executing physical manipulation tasks (e.g., pick and place) guided by language instructions in a real or simulated environment.

**[PERIA: Perceive, Reason, Imagine, Act via Holistic Language and Vision Planning for Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6af963e891e7efa229c24a1607fa7f-Paper-Conference.pdf) (as "Long-horizon manipulation")**
> Executing multi-step robotic tabletop tasks that require completing a sequence of subtasks over extended horizons.

**[ClevrSkills: Compositional Language And Visual Reasoning in Robotics](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Pushing")**
> The action of applying force to an object to move it without grasping it.

**[ClevrSkills: Compositional Language And Visual Reasoning in Robotics](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Throwing")**
> The action of propelling an object through the air.

**[ClevrSkills: Compositional Language And Visual Reasoning in Robotics](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Touching")**
> The action of making physical contact with an object, often with controlled force.

**[ClevrSkills: Compositional Language And Visual Reasoning in Robotics](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Stacking")**
> The action of placing multiple objects on top of one another in a specified order.

**[SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf) (as "Pick and stack")**
> A robotics manipulation task where the model must generate a plan to grasp an object and place it on top of another object.

## Relationships

### Robotic manipulation →
- **Meta-world** (measurements) — *measured_by*
  - [KALM: Knowledgeable Agents by Offline Reinforcement Learning from Large Language Model Rollouts](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4cdb4090e04816422afcbb08d4badcf-Paper-Conference.pdf)

### → Robotic manipulation
- **World modeling** (constructs) — *causes*
  - [PIVOT-R: Primitive-Driven Waypoint-Aware World Model for Robotic Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6164b6e5352c139e9ddc1a98c09e4e4a-Paper-Conference.pdf)
- **Spatial reasoning** (constructs) — *causes*
  - [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)
- **Instruction understanding** (constructs) — *causes*
  - [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf)
- **Visual grounding** (constructs) — *causes*
  - [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf)
- **Physical world understanding** (constructs) — *causes*
  - [PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf)
- **Spatiotemporal reasoning** (constructs) — *causes*
  - [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf)

### Associated with
- **Instruction following** (constructs)
  - [PERIA: Perceive, Reason, Imagine, Act via Holistic Language and Vision Planning for Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6af963e891e7efa229c24a1607fa7f-Paper-Conference.pdf)
