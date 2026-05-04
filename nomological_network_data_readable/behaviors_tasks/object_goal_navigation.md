# Object goal navigation
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Object navigation, Multi-object navigation  

## State of the Field

Across the provided literature, Object goal navigation is consistently defined as a task where an embodied agent explores a new or unknown environment to locate a target object of a specified category. A recurring condition is that the target object is not directly or initially visible, requiring the agent to search efficiently. One paper describes this as a "fundamental problem in a wide range of robotic tasks" ("SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation"). While the primary framing involves finding a single object, a variant called "Multi-object navigation" is also described, in which the agent's goal is to find a "list of specified object categories" ("MO-DDN: A Coarse-to-Fine Attribute-based Exploration Agent for Multi-Object Demand-driven Navigation"). Another specified sub-task is Zero-Shot Object Goal Navigation (ZS-OGN), where the agent must navigate to a target object in an environment that have both "never been encountered before" during any training phase ("GAMap: Zero-Shot Object Goal Navigation with Multi-Scale Geometric-Affordance Guidance"). The provided data describes the task's objective and constraints but does not specify the particular benchmarks or evaluation metrics used to operationalize it.

## Sources

**[GAMap: Zero-Shot Object Goal Navigation with Multi-Scale Geometric-Affordance Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/459d93dad139eb084c365d40a57eada3-Paper-Conference.pdf)**
> The task of an embodied agent exploring an environment to find a target object of a specified category that is not initially visible.

**[SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation](https://proceedings.neurips.cc/paper_files/paper/2024/file/098491b37deebbe6c007e69815729e09-Paper-Conference.pdf) (as "Object navigation")**
> The task of an agent moving through an unknown environment to find an object specified by its category.

**[MO-DDN: A Coarse-to-Fine Attribute-based Exploration Agent for Multi-Object Demand-driven Navigation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7565f036ceb20a2c74d341bfaa9fffad-Paper-Conference.pdf) (as "Multi-object navigation")**
> A navigation task where the agent must find a list of specified object categories.
