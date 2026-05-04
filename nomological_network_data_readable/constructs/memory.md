# Memory
**Type:** Construct  
**Referenced in:** 23 papers  
**Also known as:** Memory capacity, Long-term context retention, Episodic memory, Long-term memory retention, Information retention  

## State of the Field

Across the surveyed work, Memory is most commonly defined as a model's ability to store, retain, and access information over long sequences or multi-turn interactions. The prevailing usage frames it as the capacity to "incorporate and retain relevant long-range interaction history when selecting the next action" (AgentBoard...), often in relation to architectural features like attention mechanisms or recurrent states. This construct is operationalized and measured through `Information retrieval` tasks, with failures characterized as an "inability to retrieve and reason over relevant pieces of information present in their input" (Dynamic Evaluation with Cognitive Reasoning for Multi-turn Safety of Large Language Models). Several papers specify different forms, with `Long-term memory` being a recurring theme for extended tasks and dialogues, while a smaller line of work investigates `Episodic memory` for recalling specific, grounded events distinct from general knowledge. A less frequent framing treats memory as the recall of factual knowledge from the model's parameters, or "parametric memory," independent of retaining contextual information. Memory is also reported to cause `Knowledge integration` and is studied in relation to `Information extraction`.

## Sources

**[Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf) (as "Memory capacity")**
> The latent ability of a model to store and access information over a sequence, which can be implicitly increased by architectural features.

**[AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The capacity to incorporate and retain relevant long-range interaction history when selecting the next action.

**[Training Free Exponential Context Extension via Cascading KV Cache](https://proceedings.iclr.cc/paper_files/paper/2025/file/19a567abaec3990cb40d7a013556fecd-Paper-Conference.pdf) (as "Context retention")**
> The model's ability to maintain and access information from earlier parts of a long sequence for use in later predictions.

**[Streaming Video Question-Answering with In-context Video KV-Cache Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/67a9b444cbcd647572c88194619f72d5-Paper-Conference.pdf) (as "Long-term context retention")**
> The model's ability to preserve and access relevant information from earlier parts of a long video stream to answer questions posed later.

**[Episodic Memories Generation and Evaluation Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ff013b7e372ba5b790352ccd6908f03-Paper-Conference.pdf) (as "Episodic memory")**
> The cognitive ability to recall specific, personally experienced events that are grounded in a particular time and place.

**[Language Models can Categorize System Inputs for Performance Analysis](https://aclanthology.org/2025.naacl-long.318.pdf) (as "Long-term memory")**
> The capacity to retain and utilize relevant information across extended or multi-step financial tasks, supporting coherent and contextually consistent reasoning.

**[Dynamic Evaluation with Cognitive Reasoning for Multi-turn Safety of Large Language Models](https://aclanthology.org/2025.acl-long.964.pdf) (as "Long-term memory retention")**
> The latent ability of an LLM to retain and recall relevant information from prior interactions over extended sequences of dialogue, despite intervening irrelevant content.

**[Image Difference Captioning via Adversarial Preference Optimization](https://aclanthology.org/2025.emnlp-main.1714.pdf) (as "Information retention")**
> The capacity to store and access relevant facts within a long context, distinct from the ability to reason over them in sequence.

## Relationships

### Memory →
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf)
- **TextWorld** (measurements) — *measured_by*
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
