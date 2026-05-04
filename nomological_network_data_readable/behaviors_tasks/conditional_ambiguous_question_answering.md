# Conditional ambiguous question answering
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Ambiguous question answering, Conditional answer generation, Condition identification  

## State of the Field

Conditional ambiguous question answering is described as the task of answering a question whose correct interpretation depends on unstated or implicit conditions. The provided literature operationalizes this behavior as a two-part process: first, 'condition identification,' which involves extracting contextual factors that differentiate between interpretations, and second, 'conditional answer generation.' This second stage involves producing answers explicitly tied to the identified conditions, with one paper noting the output can be a "structured set of condition-answer-citation triples." The behavior is most commonly measured using the CondAmbigQA benchmark, which is presented as a framework and dataset for evaluating models on both condition identification and conditional answer generation. The ASQA benchmark is also mentioned as a measurement instrument for this behavior in one source, though no further details are provided.

## Sources

**[Effective Red-Teaming of Policy-Adherent Agents](https://aclanthology.org/2025.emnlp-main.115.pdf) (as "Ambiguous question answering")**
> The observable task of generating one or more valid answers to a query that is inherently ambiguous and allows for multiple interpretations.

**[Effective Red-Teaming of Policy-Adherent Agents](https://aclanthology.org/2025.emnlp-main.115.pdf) (as "Condition identification")**
> The observable task of extracting and summarizing the key contextual factors or constraints from provided documents that differentiate between possible interpretations of an ambiguous query.

**[Effective Red-Teaming of Policy-Adherent Agents](https://aclanthology.org/2025.emnlp-main.115.pdf) (as "Conditional answer generation")**
> Producing answers that are explicitly tied to identified conditions, ensuring responses are contextually grounded and distinguish between possible interpretations.

**[2025.emnlp-main.115.checklist](https://aclanthology.org/attachments/2025.emnlp-main.115.checklist.pdf)**
> The task of providing an answer to a question whose interpretation and correct response depend on unstated or implicit conditions.

## Relationships

### Conditional ambiguous question answering →
- **CondAmbigQA** (measurements) — *measured_by*
  > Using CondAmbigQA, we develop an experimental protocol to evaluate models on both condition identification and conditional answer generation. (Introduction)
  - [Effective Red-Teaming of Policy-Adherent Agents](https://aclanthology.org/2025.emnlp-main.115.pdf)
- **ASQA** (measurements) — *measured_by*
  - [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.56.pdf)
