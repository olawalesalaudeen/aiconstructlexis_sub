# Long-context reasoning
**Type:** Construct  
**Referenced in:** 49 papers  
**Also known as:** Long context reasoning, Long-term reasoning, Long-range dependency capture, Long-range reasoning, Long-range interaction reasoning, Long-distance dependency capture, Long-context problem solving, Long-range dependency handling, Long-range sequential reasoning, Long-horizon reasoning, Long-context inference, Multi-needle reasoning  

## State of the Field

Across the surveyed literature, long-context reasoning is most commonly defined as a model's ability to process, understand, and synthesize information distributed across extended input sequences. A prevalent technical framing of this construct is "long-range dependency capture," which focuses on the capacity to model relationships between elements that are far apart in a sequence. A distinct line of work treats it as "long-term" or "long-horizon" reasoning, emphasizing the ability to maintain a coherent plan over multiple interaction rounds to achieve a distant goal, particularly in agentic tasks where poor performance is described as a main obstacle for developing usable agents. This construct is operationalized and measured through a variety of benchmarks. For instance, Needlebench is used to evaluate "multi-needle reasoning," a sub-task requiring the synthesis of multiple distinct facts embedded in a long context. Other instruments mentioned include NOCHA for reasoning over book-length texts, WildBench for handling extended conversation histories, as well as BABILong, RULER, and MuSR. The agent-focused variant, "long-horizon reasoning," is evaluated in environments like VirtualHome, Habitat, and Crafter. The construct is also studied in relation to Faithfulness.

## Sources

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf) (as "Long context reasoning")**
> The ability to synthesize and reason over information distributed across extended input sequences, integrating distant pieces of information to form coherent responses.

**[AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf) (as "Long-term reasoning")**
> The latent ability to maintain coherent and effective reasoning over multiple interaction rounds to achieve a distant goal.

**[Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)**
> The cognitive ability of a language model to effectively process, understand, and utilize information presented over extended sequences of text.

**[Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf) (as "Long-range dependency capture")**
> The model's capacity to model relationships and dependencies between elements that are far apart in a sequence.

**[Theoretical Foundations of Deep Selective State-Space Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6231c5f46598cfd09ff1970524e0436-Paper-Conference.pdf) (as "Long-range reasoning")**
> The ability to model and reason over long sequences of information, capturing dependencies between distant elements.

**[BehaviorGPT: Smart Agent Simulation for Autonomous Driving with Next-Patch Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9144c7c014bf4c30e88f650bef8f68dd-Paper-Conference.pdf) (as "Long-range interaction reasoning")**
> The ability to capture dependencies and interactions across extended spatial and temporal horizons in traffic trajectories.

**[InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf) (as "Long-distance dependency capture")**
> The model's ability to identify and utilize relationships between pieces of information that are far apart within a long sequence of text.

**[MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf) (as "Long-range dependency modeling")**
> The ability of a model to capture, represent, and utilize relationships between elements that are far apart in a sequence.

**[WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf) (as "Long-context problem solving")**
> The ability to handle extended conversation histories and long queries when generating useful responses.

**[Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf) (as "Long-range dependency handling")**
> The ability of a model to capture and utilize relationships between elements that are far apart in a sequence.

**[Can Large Language Models Understand Symbolic Graphics Programs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41bd71e7bf7f9fe68f1c936940fd06bd-Paper-Conference.pdf) (as "Long-range sequential reasoning")**
> The capacity to process and understand the procedural steps in a program where the order of operations significantly affects the final semantic meaning.

**[SAFE: Schema-Driven Approximate Distance Join for Efficient Knowledge Graph Querying](https://aclanthology.org/2025.emnlp-main.884.pdf) (as "Long-horizon reasoning")**
> The ability of a model to generate and maintain a coherent, multi-step plan to achieve a complex goal over an extended sequence of actions.

**[ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf) (as "Long-context inference")**
> Producing outputs while processing very long input contexts without failing as the context length grows.

**[CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf) (as "Multi-needle reasoning")**
> Performing a reasoning task that requires synthesizing information from multiple, distinct facts ('needles') embedded within a long context.

## Relationships

### Long-context reasoning →
- **RULER** (measurements) — *measured_by*
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **SCROLLS** (measurements) — *measured_by*
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
- **ZeroSCROLLS** (measurements) — *measured_by*
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **BABILong** (measurements) — *measured_by*
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
- **Needlebench** (measurements) — *measured_by*
  > "NeedleBench (Li et al., 2024a): Tests retrieval and reasoning in complex contexts through three subtasks: Single-Needle Retrieval, Multi-Needle Retrieval, and Multi-Needle Reasoning."
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
- **FLenQA** (measurements) — *measured_by*
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  - [Alignment for Efficient Tool Calling of Large Language Models](https://aclanthology.org/2025.emnlp-main.899.pdf)
- **LongBench v2** (measurements) — *measured_by*
  - [Zero-shot Multimodal Document Retrieval via Cross-modal Question Generation](https://aclanthology.org/2025.emnlp-main.1325.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **MuSiQue** (measurements) — *measured_by*
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **2WikiMultihopQA** (measurements) — *measured_by*
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)

### Associated with
- **Positional bias** (constructs)
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Complex reasoning** (behaviors tasks)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
