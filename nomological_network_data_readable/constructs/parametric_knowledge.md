# Parametric knowledge
**Type:** Construct  
**Referenced in:** 18 papers  
**Also known as:** In-weights learning, Open-world knowledge, Multi-task knowledge, Model knowledge, Internal knowledge, In-weight learning, In-Weights Learning  

## State of the Field

Across the surveyed literature, parametric knowledge is most commonly defined as the knowledge implicitly stored within a language model's parameters, acquired during pre-training. This framing, appearing under various names including "internal knowledge" and "model knowledge," is frequently contrasted with knowledge accessed from external sources or provided in-context; for instance, some work positions it as a "safety net when the retriever makes mistakes" (RA-DIT: Retrieval-Augmented Dual Instruction Tuning). A related line of work uses the term "in-weights learning" to emphasize the process of encoding query-response relationships into the model's weights, explicitly setting it in opposition to in-context learning. The construct is operationalized through performance on closed-book tasks where external information is withheld. Specifically, the MMLU benchmark is used to measure it, with one paper noting it "primarily assesses a model’s parametric knowledge" (Retrieval Head Mechanistically Explains Long-Context Factuality). This internal knowledge is studied alongside `memorization` and `faithfulness`. Some research suggests this knowledge is stored in the FFN layers and can be leveraged to facilitate `semantic understanding`.

## Sources

**[VDC: Versatile Data Cleanser based on Visual-Linguistic Inconsistency by Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/518046d86bbc41a0707727c38301ad8e-Paper-Conference.pdf) (as "Open-world knowledge")**
> The latent repository of general knowledge about the world that a model can draw upon to perform tasks that require information not present in the immediate input.

**[RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf)**
> The knowledge implicitly stored within the parameters of a language model, as opposed to knowledge accessed from an external source.

**[The mechanistic basis of data dependence and abrupt learning in an in-context classification task](https://proceedings.iclr.cc/paper_files/paper/2024/file/540a3bf4863672cdaebfed69fa2ce335-Paper-Conference.pdf) (as "In-weights learning")**
> The tendency of a model to encode query-response relationships in its parameters and use those learned weights rather than context examples at inference time.

**[ETHIC: Evaluating Large Language Models on Long-Context Tasks with High Information Coverage](https://aclanthology.org/2025.naacl-long.284.pdf) (as "Prior knowledge")**
> The general knowledge and task-related understanding acquired by a model during its pre-training phase, which influences its predictions independently of in-context examples.

**[Iterative Self-TuningLLMs for Enhanced Jailbreaking Capabilities](https://aclanthology.org/2025.naacl-long.298.pdf) (as "Multi-task knowledge")**
> The latent breadth of factual and domain knowledge that supports performance across many subject areas.

**[MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.25.pdf) (as "Model knowledge")**
> The latent store of factual world knowledge encoded in a model during pre-training and potentially altered during fine-tuning, which supports accurate responses in closed-book settings.

**[Probing for Arithmetic Errors in Language Models](https://aclanthology.org/2025.emnlp-main.412.pdf) (as "Internal knowledge")**
> The knowledge acquired by a large language model during its pre-training phase, which is embedded within its parameters.

**[Dual Process Learning: Controlling Use of In-Context vs. In-Weights Strategies with Weight Forgetting](https://proceedings.iclr.cc/paper_files/paper/2025/file/7db2348b5bfeca620aa7327df815adcc-Paper-Conference.pdf) (as "In-Weights Learning")**
> The latent trait where query-response relationships and memorized information are encoded directly in the model parameters after iterated observations.

**[Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf) (as "In-weight learning")**
> The ability of a model to acquire knowledge by updating its parameters during training, effectively encoding patterns from the training data into its weights.

## Relationships

### Parametric knowledge →
- **MMLU** (measurements) — *measured_by*
  > MMLU primarily assesses a model’s parametric knowledge and requires minimal reasoning, thus offering limited benefits from CoT reasoning. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Semantic understanding** (constructs) — *causes*
  > As LLMs encompass general open-world knowledge, they can be utilized for the semantic understanding of nodes’ textual content. (Section 1)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.269.pdf)

### Associated with
- **In-context learning** (constructs)
  - [The mechanistic basis of data dependence and abrupt learning in an in-context classification task](https://proceedings.iclr.cc/paper_files/paper/2024/file/540a3bf4863672cdaebfed69fa2ce335-Paper-Conference.pdf)
- **Memorization** (constructs)
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Probing for Arithmetic Errors in Language Models](https://aclanthology.org/2025.emnlp-main.412.pdf)
