# Autonomous task solving
**Type:** Behavior  
**Referenced in:** 15 papers  
**Also known as:** Cross-application task completion, Cross-app task execution, Task execution, Household activity completion, Web task completion, Single-app task execution, Software application manipulation, Open-ended task solving  

## State of the Field

Across the surveyed literature, 'Autonomous task solving' refers to an agent's ability to complete user-specified goals through interaction with a digital or simulated environment. The specific context of this behavior varies widely across studies. A common focus is on web environments, where it is framed as 'Web task completion' involving a sequence of browser actions on real websites. Other work operationalizes it as 'Software application manipulation' on desktops or as tasks on mobile devices, which are sometimes distinguished between 'Single-app' and 'Cross-app task execution'. A separate line of inquiry examines this behavior in simulated settings, such as 'Household activity completion' or 'Open-ended task solving'. The definitions also differ in the complexity of the process, with some framing it as an iterative loop of planning and tool use, while others emphasize the need for 'coordinated agent interaction' or 'collective reasoning' for more complex goals. This focus on complexity is explicitly studied in mobile contexts, where tasks are divided based on whether they occur within a single application or require 'switching between multiple apps'. This behavior is operationalized and measured in different ways depending on the context; for instance, the `Minecraft` environment is used in one study to evaluate 'open-ended task solving'. One paper also proposes that `Understanding` is a prerequisite for this behavior.

## Sources

**[AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf) (as "Cross-application task completion")**
> The observable performance on tasks that require navigating and interacting with multiple distinct software applications to achieve a single goal.

**[SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf) (as "Cross-app task execution")**
> Completing a task that requires switching between multiple applications and coordinating actions across them.

**[Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)**
> Completing downstream tasks through coordinated agent interaction rather than a single isolated response.

**[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://proceedings.iclr.cc/paper_files/paper/2025/file/75c37811e830bf029584b1c6fac17726-Paper-Conference.pdf) (as "Task execution")**
> Carrying out an accepted predicted task through interaction with tools and the environment.

**[CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf) (as "Household activity completion")**
> The execution of common domestic tasks within a simulated environment, defined by the satisfaction of a set of specified goals or predicates.

**[ToolGen: Unified Tool Retrieval and Calling via Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b646bdebeb87dfafe2c6f77a63b564e1-Paper-Conference.pdf) (as "Task completion")**
> Completing complex user instructions by iteratively planning, selecting tools, generating parameters, and producing a final answer.

**[EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf) (as "Web task completion")**
> Executing a sequence of browser actions to accomplish a user task on a real website.

**[SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf) (as "Single-app task execution")**
> Completing a task within one mobile application by performing the required sequence of UI actions.

**[Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf) (as "Software application manipulation")**
> Using desktop applications to perform everyday tasks such as browsing, email, editing, and office workflows.

**[FOUNDER: Grounding Foundation Models in World Models for Open-Ended Embodied Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ee/wang25ee.pdf) (as "Open-ended task solving")**
> The observable performance of an agent in accomplishing a wide range of tasks specified in human-intuitive formats like text or video, without task-specific rewards.

## Relationships

### Autonomous task solving →
- **Minecraft** (measurements) — *measured_by*
  - [FOUNDER: Grounding Foundation Models in World Models for Open-Ended Embodied Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ee/wang25ee.pdf)

### → Autonomous task solving
- **Understanding** (constructs) — *causes*
  - [Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://proceedings.iclr.cc/paper_files/paper/2025/file/75c37811e830bf029584b1c6fac17726-Paper-Conference.pdf)
