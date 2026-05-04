# Relation discovery
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Concept discovery, Character relationship extraction, Argumentative relation identification  

## State of the Field

Across the provided literature, relation discovery is a behavior framed through several distinct operationalizations, all centered on identifying connections within data. One line of work defines it as the action of generating a preliminary new relation label for a test instance, using examples of known relations as demonstrations; this is presented as the first stage in a multi-step process that also includes denoising and prediction. Another application involves extracting structured information from narratives, specifically identifying "subject-predicate-object" triples to represent character interactions, a task for which models like GPT-4o-mini are used. A different context frames the behavior as "Argumentative relation identification," which focuses on identifying directed and typed relations like 'Support' or 'Attack' between components in an argument. A more abstract variant, termed "concept discovery," involves using an LLM to propose concepts that explain why certain generated responses are preferred over others based on query-response triplets. While the specific type of relation varies—from new labels and narrative triples to argumentative links and explanatory concepts—the common element across these papers is the task of identifying and labeling a relationship between entities.

## Sources

**[SlideCoder: Layout-awareRAG-enhanced Hierarchical Slide Generation from Design](https://aclanthology.org/2025.emnlp-main.459.pdf)**
> The observable action of generating a preliminary or initial new relation label for a test instance, typically based on examples of known relations.

**[FIRE: Flexible Integration of Data Quality Ratings for Effective Pretraining](https://aclanthology.org/2025.emnlp-main.736.pdf) (as "Concept discovery")**
> The process by which an LLM identifies potential concepts that differentiate preferred from rejected responses, based on batches of query-response triplets.

**[Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1204.pdf) (as "Character relationship extraction")**
> Identifying and representing subject-predicate-object triples that describe interactions, states, and roles among characters in a narrative.

**[How to Make Large Language Models Generate 100% Valid Molecules?](https://aclanthology.org/2025.emnlp-main.1351.pdf) (as "Argumentative relation identification")**
> The observable task of identifying directed, typed relations (e.g., 'Support', 'Attack') between pairs of argument components within a text.
