# ROUGE
**Type:** Measurement  
**Referenced in:** 20 papers  

## State of the Field

Across the provided sources, ROUGE is consistently characterized as a set of metrics for evaluating text generation by measuring n-gram overlap between a generated output and a reference text. The most frequently cited variants, often used in combination, are ROUGE-1, ROUGE-2, and ROUGE-L. While the underlying mechanism of n-gram comparison is universally described, the specific quality it is purported to measure varies. The most common application is to assess general "content similarity" or, as one paper states, "reconstruction performance" ("Textual Unlearning Gives a False Sense of Unlearning"). Other work uses it more specifically to measure "lexical similarity," noting that a "higher ROUGE-L score indicates greater lexical similarity" ("PoisonedParrot..."). A distinct framing appears in one study that employs ROUGE for "semantic coverage evaluation" in abstract writing and review composition tasks ("POINTS-Reader..."). In its most direct description, it is simply referred to as a "word-based metric" ("VisDoM...").

## Sources

**[Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.290.pdf)**
> A set of text generation metrics (ROUGE-1, ROUGE-2, ROUGE-L) that measure n-gram overlap between generated and reference texts to assess content similarity.
