# Knowledge retrieval
**Type:** Behavior  
**Referenced in:** 11 papers  
**Also known as:** External knowledge retrieval  

## State of the Field

Knowledge retrieval is predominantly described as the behavior of accessing and incorporating information from external sources to support reasoning and answer generation. The definitions provided vary slightly in scope, with one framing the source broadly as documents or knowledge bases, while another specifies fetching facts and "reasoning chains" from structured knowledge graphs in response to user queries. Snippets from the literature illustrate its use in solving "multi-hop questions" through methods like "iterative-step retrievals." This behavior is operationalized and measured using several benchmarks. Specifically, the datasets MKQA and BoolQ are identified as "representative datasets of knowledge retrieval tasks," and LongBench is also used for its evaluation. Knowledge retrieval is studied in relation to several other topics, including Hallucination, Explanation generation, and Knowledge manipulation. One paper also suggests that knowledge retrieval influences knowledge transferability.

## Sources

**[Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://aclanthology.org/2025.acl-long.211.pdf) (as "External knowledge retrieval")**
> Accessing and incorporating information from external sources (e.g., documents, knowledge bases) to support reasoning and answer generation.

**[Croppable Knowledge Graph Embedding](https://aclanthology.org/2025.acl-long.580.pdf)**
> Fetching relevant medical facts, entities, and reasoning chains from structured knowledge graphs based on user queries and generated hypotheses.

## Relationships

### Knowledge retrieval →
- **LongBench** (measurements) — *measured_by*
  - [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf)
- **Knowledge transferability** (constructs) — *causes*
  - [CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf)
- **MKQA** (measurements) — *measured_by*
  > We selected MKQA (Longpre et al., 2021), BoolQ (Clark et al., 2019), and AmbigQA (Min et al., 2020) as representative datasets of knowledge retrieval tasks for the interpretability analysis. (Section 5.3)
  - [CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf)
- **BoolQ** (measurements) — *measured_by*
  > We selected MKQA (Longpre et al., 2021), BoolQ (Clark et al., 2019), and AmbigQA (Min et al., 2020) as representative datasets of knowledge retrieval tasks for the interpretability analysis. (Section 5.3)
  - [CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf)

### Associated with
- **Explanation generation** (behaviors tasks)
  - [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
- **Knowledge manipulation** (constructs)
  - [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.417.pdf)
- **RAVEL** (measurements)
  - [Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25af/huang25af.pdf)
- **MMLU** (measurements)
  - [Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25af/huang25af.pdf)
