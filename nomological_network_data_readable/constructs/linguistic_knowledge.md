# Linguistic knowledge
**Type:** Construct  
**Referenced in:** 10 papers  
**Also known as:** Derivational knowledge, Morphological knowledge, Pragmatic knowledge, Semantic knowledge, Syntactic knowledge, Frame semantics encoding, Frame-semantic knowledge  

## State of the Field

Across the surveyed literature, Linguistic knowledge is predominantly framed as a latent, structured understanding of language intrinsically represented within large language models. The most common conceptualization breaks this construct down into distinct components: morphology (word structure), syntax (grammatical structure), semantics (meaning), and pragmatics (contextual interpretation). This framework is further refined in some work to include more specific types, such as derivational knowledge, which concerns word formation, and frame-semantic knowledge, which involves understanding structured conceptual scenarios. While this hierarchical view is prevalent, a few papers define the construct in more specific contexts, such as the "internalized language information that supports generating or aligning textual outputs from sign language inputs" or as proficiency in spoken language. To measure this latent construct, researchers operationalize it using specific benchmarks; the provided data shows that Linguistic knowledge is measured by BLiMP. Specific facets of this knowledge are also probed through targeted tasks, such as evaluating a model's ability to segment words to assess morphological knowledge. Some work presents findings as "strong evidence that LLMs possess genuine linguistic knowledge" as an intrinsic property.

## Sources

**[Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)**
> The internalized language information that supports generating or aligning textual outputs from sign language inputs.

**[Type-Less yet Type-Aware Inductive Link Prediction with Pretrained Language Models](https://aclanthology.org/2025.emnlp-main.1384.pdf) (as "Morphological knowledge")**
> The underlying understanding of word formation rules, including the ability to decompose words into meaningful morphemes and assign their grammatical functions.

**[2025.emnlp-main.1384.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1384.checklist.pdf) (as "Derivational knowledge")**
> The latent understanding of how words are formed from base words through morphological processes like affixation.

**[Scaling Up Temporal Domain Generalization via Temporal Experts Averaging](https://aclanthology.org/2025.emnlp-main.1433.pdf) (as "Pragmatic knowledge")**
> The model's internal representation of how context influences the interpretation of meaning, including politeness, discourse, and speaker intent.

**[Scaling Up Temporal Domain Generalization via Temporal Experts Averaging](https://aclanthology.org/2025.emnlp-main.1433.pdf) (as "Semantic knowledge")**
> The model's internal representation of meaning at the word, phrase, and sentence level.

**[Scaling Up Temporal Domain Generalization via Temporal Experts Averaging](https://aclanthology.org/2025.emnlp-main.1433.pdf) (as "Syntactic knowledge")**
> The latent representation of grammatical structure and sentence-level form, including constructions like passive voice, relative clauses, and coordination.

**[FISTAPruner: Layer-wise Post-training Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.1499.pdf) (as "Frame-semantic knowledge")**
> The latent ability of a model to understand and represent meaning through structured conceptual scenarios (frames) and their associated roles.

**[2025.emnlp-main.1499.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1499.checklist.pdf) (as "Frame semantics encoding")**
> The latent ability of a model to implicitly represent structured predicate-argument relationships (frames) as defined in linguistic theory, such that these can be decoded from its internal representations.

## Relationships

### Linguistic knowledge →
- **BLiMP** (measurements) — *measured_by*
  > As a control, we evaluate TopoLM's performance on linguistic knowledge (BLiMP), downstream task (GLUE), and brain alignment benchmarks (Brain-Score), compared to the non-topographic baseline model.
  - [TopoLM: brain-like spatio-functional organization in a topographic language model](https://proceedings.iclr.cc/paper_files/paper/2025/file/4f7f521c08b5e0cd9931e74fa353b59b-Paper-Conference.pdf)
