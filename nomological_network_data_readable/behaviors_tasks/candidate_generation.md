# Candidate generation
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Statement generation  

## State of the Field

Across the surveyed literature, 'Candidate generation' is a behavior framed in several distinct ways, generally involving the production of a set of potential items for a subsequent task. The most prevalent usage defines it as producing potential matches for a given input, such as generating alternative reasoning steps or solution paths. For example, one paper operationalizes this as "generating multiple potential continuations for each active hypothesis" to explore diverse solution trajectories ("DEL-ToM: Inference-Time Scaling for Theory-of-Mind Reasoning via Dynamic Epistemic Logic"). In the context of `Schema linking`, this behavior is operationalized as producing "a set of potential matches from the target schema" using both semantic retrieval and reasoning-based methods ("Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching"). A distinct framing, termed "Statement generation," defines the behavior as generating candidate statements under a cost or length constraint for later selection, where it is treated as an "approximate solver for an optimization task" ("Generative Social Choice: The Next Generation"). While the specific items being generated differ—ranging from schema attributes and reasoning steps to statements—the shared characteristic is the creation of a candidate set for a downstream selection or matching process.

## Sources

**[Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)**
> Producing a set of potential target attributes that may correspond to a given source attribute, using either semantic retrieval or reasoning-based methods.

**[Generative Social Choice: The Next Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boehmer25a/boehmer25a.pdf) (as "Statement generation")**
> Generating candidate statements under a cost or length constraint for later selection into a slate.

## Relationships

### Associated with
- **Schema linking** (behaviors tasks)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
