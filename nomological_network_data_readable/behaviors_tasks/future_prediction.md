# Future prediction
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Next-state prediction, Observation prediction, State transition prediction, State forecasting, Temporal prediction  

## State of the Field

Across the provided literature, future prediction is a behavior commonly defined as a model's ability to forecast a subsequent state or observation based on current information. The specific inputs for this task vary, with some papers framing it as predicting from a current state and an action, while others describe it as predicting the next step in a sequence or from general contextual information. The operationalization of this behavior also differs across studies; it can involve selecting from candidate observations, generating a textual description of the next state, producing a probabilistic forecast, or autoregressively predicting both the next state and its associated reward. For instance, one approach prompts a model to "select between 1) a pair of candidate next observations" ("On the Modeling Capabilities of Large Language Models for Sequential Decision Making"), while another requires it to generate "a textual description of the next observation" ("LLaRA: Supercharging Robot Learning Data for Vision-Language Policy"). A less common framing extends this concept to include not just forecasting future events but also reconstructing past ones, involving the generation of both images and text. In the context of this research, future prediction is studied alongside the constructs of faithfulness and commonsense understanding.

## Sources

**[On the Modeling Capabilities of Large Language Models for Sequential Decision Making](https://proceedings.iclr.cc/paper_files/paper/2025/file/368cba57d00902c752eaa9e4770bbbbe-Paper-Conference.pdf) (as "Observation prediction")**
> The observable behavior where the model selects candidate next observations given current state and action.

**[Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b594f6dd4931c4af4f12042af8d40ec-Paper-Conference.pdf) (as "Next-state prediction")**
> The task of predicting the next observation in a sequence generated from a stochastic process, such as a random walk on a graph.

**[Zero-shot Model-based Reinforcement Learning using Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf) (as "State transition prediction")**
> Autoregressively predicting the next state and reward given the current state and action.

**[DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf) (as "State forecasting")**
> The observable task of producing a probabilistic forecast for the values of unknown variables (states) based on provided contextual information.

**[LLaRA: Supercharging Robot Learning Data for Vision-Language Policy](https://proceedings.iclr.cc/paper_files/paper/2025/file/909f526db5127f8bd8158af32d9e313a-Paper-Conference.pdf)**
> The task of generating a textual description of the next observation, given a current observation and a single-step action.

**[Interleaved Scene Graphs for Interleaved Text-and-Image Generation Assessment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e0ceee9751ae8b5c6603c029e4ca42-Paper-Conference.pdf) (as "Temporal prediction")**
> The task of generating a sequence of images and text that forecasts future events or reconstructs past events based on an input.

## Relationships

### Associated with
- **Faithfulness** (constructs)
  - [DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf)
- **Commonsense understanding** (constructs)
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
