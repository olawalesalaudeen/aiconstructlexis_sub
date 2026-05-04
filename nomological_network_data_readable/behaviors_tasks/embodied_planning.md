# Embodied planning
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Action sequence prediction  

## State of the Field

Across the provided literature, embodied planning is predominantly defined as the task of generating a sequence of actions for an agent to execute within a simulated or physical environment. A more specific framing, termed 'action sequence prediction,' further requires that the generated action sequence aligns with a ground-truth human trajectory to be considered successful. This behavior is positioned as a complex scenario for LLM agents, studied alongside problem-solving, function calling, and tool use. To operationalize and evaluate embodied planning, researchers employ several benchmarks, including ScienceWorld, VirtualHome, and BabyAI. The evidence from one paper specifies that ScienceWorld and VirtualHome are used for 'complex embodied reasoning tasks'. The success criteria can be stringent, with one study noting that 'task-level success is achieved only if the entire sequence of steps predicted by the agent aligns with the ground-truth human trajectories' (Multi-Attribute Steering of Language Models via Targeted Intervention). The concept is also documented as being related to long-horizon planning.

## Sources

**[Benchmarking Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/adbe936993aa7cf41e45054d8b72f183-Paper-Conference.pdf)**
> The task of generating a sequence of actions for an agent to execute within a simulated or physical environment.

**[Multi-Attribute Steering of Language Models via Targeted Intervention](https://aclanthology.org/2025.acl-long.1008.pdf) (as "Action sequence prediction")**
> Generating a correct sequence of actions (element selection and operation) that aligns with the ground-truth human trajectory to achieve task success.

## Relationships

### Embodied planning →
- **ScienceWorld** (measurements) — *measured_by*
  > To evaluate the effectiveness of DGAP and other baseline methods in complex embodied reasoning tasks, we employ the ScienceWorld (Wang et al., 2022) and VirtualHome (Puig et al., 2018) benchmark.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **VirtualHome** (measurements) — *measured_by*
  > To evaluate the effectiveness of DGAP and other baseline methods in complex embodied reasoning tasks, we employ the ScienceWorld (Wang et al., 2022) and VirtualHome (Puig et al., 2018) benchmark.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **BabyAI** (measurements) — *measured_by*
  - [TunableLLM-based Proactive Recommendation Agent](https://aclanthology.org/2025.acl-long.945.pdf)

### Associated with
- **Long-horizon planning** (constructs)
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
