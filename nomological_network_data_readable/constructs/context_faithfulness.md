# Context faithfulness
**Type:** Construct  
**Referenced in:** 7 papers  
**Also known as:** Contextual faithfulness, Context-faithfulness  

## State of the Field

Across the surveyed literature, context faithfulness is predominantly defined as a model's ability to generate outputs that are fully supported by, consistent with, and grounded in the provided contextual information. This is frequently framed in terms of avoiding undesirable behaviors such as making "unsupported claims," generating "irrelevant or unsupported content," or producing "hallucinations." A more specific framing, present in a subset of the papers, defines the construct as the ability to prioritize contextual information particularly when it "conflicts with the model's parametric knowledge." The construct is commonly studied in applications like "retrieval-augmented large language models (LLMs)" and "long-form question-answering (LFQA)" to build trustworthy and reliable systems. To operationalize and measure context faithfulness, researchers use counter-factual question-answering benchmarks, including NQ-Swap and CounterFact. For instance, NQ-Swap is described as offering a "challenging and complementary evaluation of a model’s ability to identify and rely on the correct evidence."

## Sources

**[Length Controlled Generation for Black-boxLLMs](https://aclanthology.org/2025.acl-long.826.pdf) (as "Contextual faithfulness")**
> The latent ability of a model to generate responses that are fully supported by and consistent with the provided contextual information, avoiding hallucinations or unsupported claims.

**[LongSafety: Evaluating Long-Context Safety of Large Language Models](https://aclanthology.org/2025.acl-long.1531.pdf) (as "Context-faithfulness")**
> The latent ability of a model to generate responses that accurately reflect the provided contextual information, especially when it conflicts with the model's parametric knowledge.

**[Joint Modeling of Entities and Discourse Relations for Coherence Assessment](https://aclanthology.org/2025.emnlp-main.1114.pdf)**
> The ability of a model to accurately ground its generated output in the provided contextual information, avoiding irrelevant or unsupported content.

## Relationships

### Context faithfulness →
- **NQ-Swap** (measurements) — *measured_by*
  > we also include two counter-factual QA benchmarks: NQ-Swap and ConfiQA, offering a more challenging and complementary evaluation of a model’s ability to identify and rely on the correct evidence. (Section 3.2)
  - [Joint Modeling of Entities and Discourse Relations for Coherence Assessment](https://aclanthology.org/2025.emnlp-main.1114.pdf)
- **CounterFact** (measurements) — *measured_by*
  - [Joint Modeling of Entities and Discourse Relations for Coherence Assessment](https://aclanthology.org/2025.emnlp-main.1114.pdf)
