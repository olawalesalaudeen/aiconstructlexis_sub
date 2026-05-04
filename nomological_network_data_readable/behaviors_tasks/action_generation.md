# Action generation
**Type:** Behavior  
**Referenced in:** 12 papers  
**Also known as:** Action-to-reaction generation, Executable action generation  

## State of the Field

Across the surveyed literature, action generation is most commonly defined as the behavior of producing a structured output that specifies an action to be taken, such as 'click' or 'type text', along with its parameters. This behavior is operationalized in diverse settings, including GUI interaction where the output is a structured object, navigation tasks where an agent generates its next control action, and embodied robotics where models produce sequences of low-level actions autoregressively. A frequent focus is on generating not just single actions but sequences of *executable* actions required to complete a task, particularly in web environments. The distinction between valid and invalid actions is noted, with one paper highlighting that models may generate non-executable outputs like "attempting to retrieve objects from a closed container" ('CiteEval: Principle-Driven Citation Evaluation for Source Attribution'). A more specialized framing, 'action-to-reaction generation', is described in one paper as the task of generating human reaction motions in response to observed actions without text prompts. Regarding evaluation, the quality of generated actions is sometimes measured using `Human evaluation` via user studies. Furthermore, one study suggests that the action generation stage can be manipulated to cause `Harmful content generation` in the form of privacy leakage.

## Sources

**[Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)**
> Producing a structured output that specifies an action to be taken (e.g., 'click', 'type text') and its associated parameters, such as position or value.

**[Think Then React: Towards Unconstrained Action-to-Reaction Motion Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea0b28cbbd0cbc45ec4ac38e92da9cb2-Paper-Conference.pdf) (as "Action-to-reaction generation")**
> The observable task of generating a sequence of human reaction motions in response to an input sequence of human action motions without explicit text prompts.

**[CiteEval: Principle-Driven Citation Evaluation for Source Attribution](https://aclanthology.org/2025.acl-long.1575.pdf) (as "Executable action generation")**
> Producing actions that are valid and can be successfully executed within the environment, as opposed to invalid or nonsensical actions.

**[AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25m/xu25m.pdf) (as "Action sequence generation")**
> Producing a sequence of executable actions to complete a website task from the current state and user request.

## Relationships

### Action generation →
- **Human evaluation** (measurements) — *measured_by*
  > To further evaluate our model qualitatively, we conduct a user study on TTR vs. the latest SOTA method ReGenNet, and the results are shown in Figure 7 (Section 4.7).
  - [Think Then React: Towards Unconstrained Action-to-Reaction Motion Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea0b28cbbd0cbc45ec4ac38e92da9cb2-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *causes*
  > "we propose the approach to relax the opacity constraint by setting α to a low, non-zero value to affect the action generation stage, termed as Relaxed-EIA"
  - [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)
