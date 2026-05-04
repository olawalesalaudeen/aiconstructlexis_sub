# Model similarity
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Behavior alignment, Functional similarity, Representation similarity  

## State of the Field

Across the surveyed literature, `Model similarity` is most commonly defined as the statistical resemblance between the output distributions of different language models. This perspective, independent of model architecture or size, is operationalized by estimating pairwise distances between model outputs or by inferring similarity from misclassification patterns. A different line of work conceptualizes similarity internally, defining it as `Representation similarity`—the structural alignment between models' internal representation spaces, which is measured using techniques such as SVCCA, CKA, or Jaccard similarity on learned activation dictionaries. More specialized definitions also exist, such as `Functional similarity`, which compares the outputs of different experts within a single SMoE model, and `Behavior alignment`, which measures the acceptance rate of a draft model's outputs by a target model in speculative decoding. One study suggests that factors like training data are more determinative of output similarity than model scale, noting that "models within the same family... output more similar distributions" ("Model Equality Testing: Which Model is this API Serving?"). The construct is also studied in relation to other phenomena; one paper reports an inverse correlation between `Model similarity` and the performance gains from `Weak-to-strong generalization`. Specifically, higher similarity between a weak supervisor and a student model was associated with less improvement from the training procedure.

## Sources

**[Model Equality Testing: Which Model is this API Serving?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d73234a13815fc1f9779dd17d89be9b4-Paper-Conference.pdf)**
> The degree of statistical resemblance between the output distributions of two different language models, independent of their architecture or size.

**[SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf) (as "Behavior alignment")**
> The extent to which the layer-skipping draft model produces outputs that are accepted or matched by the target LLM.

**[Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf) (as "Functional similarity")**
> The degree to which different experts in an SMoE model produce equivalent outputs given the same input, reflecting underlying redundancy in learned representations.

**[Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/leask25a/leask25a.pdf) (as "Representation similarity")**
> The degree of structural alignment or equivalence between the internal representation spaces of different neural network models.

## Relationships

### Model similarity →
- **Weak-to-strong generalization** (constructs) — *correlates*
  > for all model combinations, similarity between the weak supervisor and initial strong student inversely correlates with the improvement obtained from weak-to-strong training (r = −0.85). (Section 4.2)
  - [Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf)
