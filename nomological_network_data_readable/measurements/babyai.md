# BabyAI
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Based on the provided literature, BabyAI is a procedurally-generated, partially-observable 2D gridworld environment designed to evaluate agent capabilities. Its primary application is assessing performance on tasks specified by textual or visual goals. The capabilities most frequently measured using this instrument are navigation and object manipulation, with one source noting that agents are tested on "five different types of navigation tasks." Additionally, papers use BabyAI to measure other constructs, including decision-making, embodied planning, and commonsense knowledge. The environment is described as operating across multiple modalities. For instance, one study highlights its use in enabling foundation models to succeed with "visual observations zero-shot" ("Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models").

## Sources

**[Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)**
> A procedurally-generated, partially-observable 2D gridworld environment used to evaluate agent capabilities on tasks specified by textual or visual goals, such as navigation and object manipulation.

## Relationships

### → BabyAI
- **Navigation** (behaviors tasks) — *measured_by*
  > Agents are tested across five different types of navigation tasks, see Appendix A.
  - [Grounding Multimodal Large Language Models in Actions](https://proceedings.neurips.cc/paper_files/paper/2024/file/2406694fd7bc7e7bf257446a14f9ea63-Paper-Conference.pdf)
- **Decision-making** (constructs) — *measured_by*
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **Embodied planning** (behaviors tasks) — *measured_by*
  - [TunableLLM-based Proactive Recommendation Agent](https://aclanthology.org/2025.acl-long.945.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [The Synergy of LLMs & RL Unlocks Offline Learning of Generalizable Language-Conditioned Policies with Low-fidelity Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pouplin25a/pouplin25a.pdf)
