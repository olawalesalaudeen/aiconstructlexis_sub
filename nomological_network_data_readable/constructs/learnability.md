# Learnability
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Domain learnability  

## State of the Field

Across the provided literature, learnability is most commonly defined as a property of a task or data distribution that determines how efficiently a model can learn to solve it from examples. One paper specifies this concept as "domain learnability," referring to the "latent ease" with which a downstream domain is learned during continual pre-training ("D-CPT Law: Domain-specific Continual Pre-Training Scaling Law for Large Language Models"). A more granular framing, present in one study, defines learnability at the level of a single datum, operationalizing it as the "relative reduction in loss on that data point after a fine-tuning step" ("Toward Automatic Discovery of a Canine Phonetic Alphabet"). This paper proposes the DavIR algorithm to provide an exact measurement of this property, noting its close relation to the implicit reward model in Direct Preference Optimization (DPO). The concept is also studied alongside and contrasted with expressive power; one paper makes a clear distinction, stating that a model's expressivity "does not address the learnability objective" ("How Far Can Transformers Reason? The Globality Barrier and Inductive Scratchpad").

## Sources

**[How Far Can Transformers Reason? The Globality Barrier and Inductive Scratchpad](https://proceedings.neurips.cc/paper_files/paper/2024/file/3107e4bdb658c79053d7ef59cbc804dd-Paper-Conference.pdf)**
> The property of a task or distribution that determines whether a model can efficiently learn to solve it from examples.

**[D-CPT Law: Domain-specific Continual Pre-Training Scaling Law for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4628e9fbd3002a554923642f74d5d6b-Paper-Conference.pdf) (as "Domain learnability")**
> The latent ease with which a specific downstream domain can be learned by the model under continual pre-training.

## Relationships

### Associated with
- **Expressive power** (constructs)
  - [How Far Can Transformers Reason? The Globality Barrier and Inductive Scratchpad](https://proceedings.neurips.cc/paper_files/paper/2024/file/3107e4bdb658c79053d7ef59cbc804dd-Paper-Conference.pdf)
