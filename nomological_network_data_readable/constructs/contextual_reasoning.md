# Contextual reasoning
**Type:** Construct  
**Referenced in:** 19 papers  
**Also known as:** Context-specific reasoning, Context-aware reasoning, Context reasoning  

## State of the Field

Across the surveyed literature, contextual reasoning is most commonly defined as the ability to understand instructions or situations and infer information based on functional or situational relationships, rather than literal keyword matching. This framing is applied in domains ranging from detecting objects based on "daily life requirement" instructions (Ins-DetCLIP: Aligning Detection Model to Follow Human-Language Instruction) to making "deontic judgments" about social norms (G-Safeguard: A Topology-Guided Security Lens and Treatment onLLM-based Multi-agent Systems). A related but distinct definition treats it as the capacity to use information provided exclusively in a prompt to form representations "without relying on stored factual weights" (How do Language Models Bind Entities in Context?). Other definitions specify the type of context, such as information distributed across long texts, specialized user queries, or surrounding code for vulnerability analysis. To operationalize this construct, papers report using benchmarks like LongBench, PubMedQA, and MemeReaCon, with the latter being used to evaluate the "fine-grained contextual reasoning required to understand memes" (WangchanThaiInstruct...). The construct is also presented as a capability related to natural language understanding.

## Sources

**[How do Language Models Bind Entities in Context?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9d1b7fc578c0d2d6431fc26d736ecaf3-Paper-Conference.pdf) (as "In-context reasoning")**
> The capacity to use information provided in the prompt or context to form and recall structured representations without relying on stored factual weights.

**[Ins-DetCLIP: Aligning Detection Model to Follow Human-Language Instruction](https://proceedings.iclr.cc/paper_files/paper/2024/file/accb5f309ec092a6787a1879ad5f2a5f-Paper-Conference.pdf)**
> The ability to understand the context within an instruction and infer relevant objects based on situational or functional relationships, rather than literal keyword matching.

**[STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Context-specific reasoning")**
> The latent ability to infer user interests, understand specialized field descriptions, and deduce relationships involving multiple subjects within a specific query context.

**[RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf) (as "Context-aware reasoning")**
> The ability to reason about sequences by selectively focusing on relevant context, a key feature of the Mamba architecture.

**[Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf) (as "Context reasoning")**
> The latent ability of a model to understand and draw inferences from information distributed across a long textual context.

## Relationships

### Contextual reasoning →
- **LongBench** (measurements) — *measured_by*
  > For LongBench, we use datasets from the Single-Doc QA and Multi-Doc QA categories to assess contextual reasoning.
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
- **PubMedQA** (measurements) — *measured_by*
  - [Reading between the Lines: CanLLMs Identify Cross-Cultural Communication Gaps?](https://aclanthology.org/2025.naacl-long.410.pdf)
- **MemeReaCon** (measurements) — *measured_by*
  > MemeReaCon occupies a unique position by being the first benchmark, to our knowledge, specifically constructed to evaluate the fine-grained contextual reasoning required to understand memes as they are used in online posts. (Section 2)
  - [WangchanThaiInstruct: An instruction-following Dataset for Culture-Aware, Multitask, and Multi-domain Evaluation inThai](https://aclanthology.org/2025.emnlp-main.176.pdf)

### Associated with
- **Natural language understanding** (constructs)
  > Recent advances in Large Language Models (LLMs) have demonstrated strong capabilities in natural language understanding and contextual reasoning, opening new avenues for complex tasks. (Section 1)
  - [Improving the Quality of Web-mined Parallel Corpora of Low-Resource Languages using Debiasing Heuristics](https://aclanthology.org/2025.emnlp-main.1436.pdf)
