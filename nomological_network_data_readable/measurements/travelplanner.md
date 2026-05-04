# Travelplanner
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** TravelPlanner  

## State of the Field

Across the provided literature, Travelplanner is predominantly described as a benchmark used to evaluate the construct of `Planning` in LLM agents, with one paper also specifying its use for measuring `Long-horizon planning`. The central task within this benchmark requires an agent to generate a travel plan or itinerary that satisfies multiple, complex user-specified constraints. These constraints are characterized as both "commonsense and hard constraints" and can involve details like "flights, accommodations, and other travel arrangements." Several papers frame this as a "real-world" planning task, and one source specifies its scope as "U.S. domestic travel planning." The benchmark is described as providing a "rich sandbox environment" with "tools for accessing nearly four million data records" to support the agent's process. While most sources refer to it as a benchmark, one paper describes it as the "TravelPlanner dataset." The task is presented as challenging, with one study noting that LLMs are generally "not capable of handling multi-constraint tasks" and that a top model achieved only a "10% success rate."

## Sources

**[AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)**
> A benchmark for evaluating LLM agents on travel-planning tasks.

**[Interactive Speculative Planning: Enhance Agent Efficiency through Co-design of System and User Interface](https://proceedings.iclr.cc/paper_files/paper/2025/file/25458943db16e0f78f748ca5bc34fff6-Paper-Conference.pdf) (as "TravelPlanner")**
> A benchmark for evaluating travel planning agents, providing a sandbox environment with tools for accessing travel data and a set of curated planning intents with constraints.

## Relationships

### → Travelplanner
- **Planning** (constructs) — *measured_by*
  - [FLEURS-ASL: IncludingAmericanSignLanguage in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.315.pdf)
- **Long-horizon planning** (constructs) — *measured_by*
  - [Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.93.pdf)
