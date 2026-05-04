# WebShop
**Type:** Measurement  
**Referenced in:** 28 papers  
**Also known as:** Webshop  

## State of the Field

Across the provided literature, WebShop is consistently characterized as a benchmark environment that simulates an online shopping website. It is widely used to evaluate an agent's ability to follow a natural language user instruction to find and purchase a specific item. This task requires the agent to perform a series of interactions, commonly described as navigating the site, searching, and using "search and click actions" to select product attributes under specified constraints. Papers use WebShop to measure several agent capabilities, most frequently decision-making and web navigation, but also problem-solving and commonsense knowledge. The simulated environment is noted for containing "over a million real-world products" and presenting agents with "large action spaces." Performance is operationalized through a scoring system, with some sources describing it as "dense final rewards from 0 to 1" based on how well the purchased item matches the user's specifications for attributes, options, and price.

## Sources

**[Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf)**
> A benchmark environment that simulates an online shopping website, where an agent must navigate, search, and select product attributes to find and purchase a specific item based on a user instruction.

**[AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf) (as "Webshop")**
> A benchmark for evaluating LLM agents on web-based shopping tasks.

## Relationships

### → WebShop
- **Web navigation** (behaviors tasks) — *measured_by*
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
- **Decision-making** (constructs) — *measured_by*
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
- **Web shopping** (behaviors tasks) — *measured_by*
  - [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > We assess the effectiveness of our proposed FOA framework through comparisons with representative SOTA methods on a judicious mix of tasks that require a variety of reasoning, planning, and general problem-solving skills.
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)

### Associated with
- **AgentBench** (measurements)
  - [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf)
