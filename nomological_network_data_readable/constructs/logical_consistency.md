# Logical consistency
**Type:** Construct  
**Referenced in:** 33 papers  
**Also known as:** Logical robustness, Logical coherence  

## State of the Field

Across the surveyed literature, logical consistency is a widely discussed property of language models, predominantly defined as the absence of internal contradictions in generated outputs. This concept appears under several names, including "logical coherence" and "logical robustness," all pointing to the quality of being logically structured and free from self-contradiction. The most common framing applies to the internal coherence of a single output, such as ensuring the absence of "discrepancies within the plot, character development, or themes of a generated summary" (BooookScore: A systematic exploration of book-length summarization in the era of LLMs) or maintaining a reasoning process "without any contradiction" (FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets). A more formal line of work operationalizes this concept through adherence to propositional logic, assessing whether a model's responses to "logically equivalent or related queries, such as a statement and its negation," are semantically opposite (Logical Consistency of Large Language Models in Fact-Checking). This perspective is extended in some work to evaluate consistency across a model's "beliefs or probability assignments across a set of logically related statements" (ToW: Thoughts of Words Improve Reasoning in Large Language Models). Other papers define logical consistency in relation to specific task constraints, such as an agent producing "invariant decisions across equivalent representations of the same problem" (MatViX: Multimodal Information Extraction from Visually Rich Articles), or a model's generated code adhering to "explicit rules and conditions specified in domain knowledge documents" (ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation). For example, in Natural Language Inference, it is measured by checking if a model's predictions on "atomic NLI and defeasible NLI sub-problems" align with its overall prediction (No Simple Answer to Data Complexity: An Examination of Instance-Level Complexity Metrics for Classification Tasks). Thus, while the core idea of non-contradiction is stable, its operationalization varies, ranging from narrative coherence and reasoning chain integrity to formal logical equivalence and adherence to external knowledge.

## Sources

**[FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf) (as "Logical robustness")**
> The degree to which a response remains logically consistent and generally applicable throughout its reasoning process without contradictions.

**[BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)**
> The absence of internal contradictions or discrepancies within the plot, character development, or themes of a generated summary.

**[MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Logical coherence")**
> The quality of a model's generated output being logically structured, consistent, and free from contradictions.

## Relationships

### Logical consistency →
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.38.pdf)
- **SNLI** (measurements) — *measured_by*
  - [No Simple Answer to Data Complexity: An Examination of Instance-Level Complexity Metrics for Classification Tasks](https://aclanthology.org/2025.naacl-long.130.pdf)

### Associated with
- **Factuality** (constructs)
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  - [Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ds/zhang25ds.pdf)
- **Self-consistency** (measurements)
  - [MS-RAG: Simple and Effective Multi-Semantic Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1152.pdf)
