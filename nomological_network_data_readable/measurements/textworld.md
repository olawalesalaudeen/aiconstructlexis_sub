# TextWorld
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

TextWorld is consistently described as a benchmark for agents operating in text-based games, though its purpose is framed in slightly different ways. One common definition presents it as a general sandbox for training and evaluating reinforcement learning agents in discrete domains. A more specific, and also common, framing describes it as a "classic text-based agent benchmark" for evaluating particular agent capabilities within interactive fiction games. Across the provided literature, TextWorld is used to measure a range of these capabilities. It is frequently used to evaluate an agent's `Planning`, `Commonsense understanding`, and `Memorization`, with one paper noting its use for tasks requiring "long-horizon memory." Additionally, it is used to assess `Navigation`, where an agent must "explore mazes and interact with everyday objects through natural language."

## Sources

**[Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)**
> A text-based agent benchmark for evaluating capabilities like planning, commonsense reasoning, and exploration in interactive fiction games.

## Relationships

### → TextWorld
- **Planning** (constructs) — *measured_by*
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
- **Navigation** (behaviors tasks) — *measured_by*
  > In each game, the agent needs to complete the task while navigating a maze of different rooms
  - [BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0b1515be276f6ba82b4f2b25e50bef0-Paper-Conference.pdf)
- **Memory** (constructs) — *measured_by*
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
