# Long-term memory
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** Episodic memory, Long-term memory retention  

## State of the Field

Across the provided literature, long-term memory is most commonly defined as a model's capacity to retain and utilize information across extended interactions or multi-step tasks to support coherent reasoning. This construct is frequently discussed in the context of dialogue systems, where its stated purpose is to "create consistent and human-like conversations" (MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration). Failures of long-term memory are described as a model's inability "to connect distant parts of the text" or its failure to "retrieve and reason over relevant pieces of information" during a sequence of interactions. While this is the prevailing view, a smaller set of papers uses more specific framings, such as "episodic memory," which distinguishes storing sequence-level information from generalized world knowledge, and "long-term memory retention," which highlights the ability to recall information despite "intervening irrelevant content." The construct is studied in contexts like "multi-step financial tasks" and dialogues requiring reasoning over a sequence of instructions. Some work also contrasts model capabilities with the "dynamic and interconnected nature of human long-term memory" (From RAG to Memory: Non-Parametric Continual Learning for Large Language Models).

## Sources

**[Language Models can Categorize System Inputs for Performance Analysis](https://aclanthology.org/2025.naacl-long.318.pdf)**
> The capacity to retain and utilize relevant information across extended or multi-step financial tasks, supporting coherent and contextually consistent reasoning.

**[Segment-Based Attention Masking forGPTs](https://aclanthology.org/2025.acl-long.948.pdf) (as "Episodic memory")**
> The ability of a model to store and retrieve specific, sequence-level information, distinct from its generalized world knowledge.

**[Dynamic Evaluation with Cognitive Reasoning for Multi-turn Safety of Large Language Models](https://aclanthology.org/2025.acl-long.964.pdf) (as "Long-term memory retention")**
> The latent ability of an LLM to retain and recall relevant information from prior interactions over extended sequences of dialogue, despite intervening irrelevant content.

## Relationships

### Long-term memory →
- **Knowledge integration** (constructs) — *causes*
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)

### Associated with
- **Information extraction** (behaviors tasks)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
