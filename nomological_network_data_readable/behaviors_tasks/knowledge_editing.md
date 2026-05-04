# Knowledge editing
**Type:** Behavior  
**Referenced in:** 24 papers  
**Also known as:** Knowledge injection, Knowledge erasure, Domain-specific knowledge unlearning, Knowledge update, User-specific editing, Visual entity editing, Visual semantic editing, Model editing, Targeted knowledge removal, Knowledge refinement, Factual knowledge updating  

## State of the Field

Knowledge editing is most commonly framed as the process of updating a model's stored factual or commonsense knowledge by modifying a small number of its parameters, often to correct "incorrect or outdated knowledge" efficiently. A recurring objective across the literature is to perform these updates surgically, ensuring that unrelated knowledge is preserved. While most definitions center on direct parameter modification, a smaller line of work explores editing "without modifying model weights, relying solely on forward passes". The scope of this behavior is broad, encompassing specific actions like "knowledge update" (adding new facts), "knowledge erasure" (removing facts), and even "domain-specific knowledge unlearning". The concept also extends beyond text to include "visual entity editing" and "user-specific editing". To operationalize and measure this behavior, researchers employ a range of benchmarks, with zs-RE, CounterFact, WikiDatacounterfact, WikiDatarecent, and WikiBio being frequently used. The quality of an edit is also assessed based on associated properties such as "Locality" (preserving unrelated knowledge) and "Portability," which one paper defines as ensuring "relevant knowledge... should be updated as well."

## Sources

**[Reasons and Solutions for the Decline in Model Performance after Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f588e59e9ae6138d3ea9e4fdaa7e040-Paper-Conference.pdf)**
> Updating a model's stored factual or commonsense knowledge by modifying a small number of parameters.

**[Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf) (as "Knowledge injection")**
> Incorporating external facts or references into generated responses during inference.

**[Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf) (as "Domain-specific knowledge unlearning")**
> Removing or suppressing knowledge associated with a target subject domain while leaving other domains relatively intact.

**[Knowledge Localization: Mission Not Accomplished? Enter Query Localization!](https://proceedings.iclr.cc/paper_files/paper/2025/file/48adb34f7ee39177c4c23a8e4253a492-Paper-Conference.pdf) (as "Knowledge erasure")**
> The observable outcome of a model ceasing to produce a specific fact in response to relevant queries after its parameters have been modified.

**[Knowledge Localization: Mission Not Accomplished? Enter Query Localization!](https://proceedings.iclr.cc/paper_files/paper/2025/file/48adb34f7ee39177c4c23a8e4253a492-Paper-Conference.pdf) (as "Knowledge update")**
> The observable outcome of a model producing a new, updated fact in response to relevant queries after its parameters have been modified to replace an old fact.

**[MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf) (as "Visual entity editing")**
> The observable task of modifying a model's knowledge about a specific visual entity, such as updating its attributes or associated facts.

**[MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf) (as "Visual semantic editing")**
> The observable task of modifying a model's understanding of complex visual semantics, such as actions, body gestures, or object relationships.

**[MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf) (as "User-specific editing")**
> The observable task of incorporating new, personalized user information into a model, such as details about owned items or personal relationships.

**[Efficient Model Editing with Task-Localized Sparse Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96f5de31e8e3d19cbcd3a7397b8dce57-Paper-Conference.pdf) (as "Model editing")**
> The general practice of modifying a pre-trained model's parameters to add, remove, or alter its knowledge and capabilities in a targeted manner.

**[Rethinking LLM Unlearning Objectives: A Gradient Perspective and Go Beyond](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad307ab459fb93163248a0a56959307-Paper-Conference.pdf) (as "Targeted knowledge removal")**
> The observable behavior of a model failing to reproduce or respond correctly to information designated for unlearning.

**[NeSyC: A Neuro-symbolic Continual Learner For Complex Embodied Tasks in Open Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/d569e4655e2835e3d38310b67c5ad646-Paper-Conference.pdf) (as "Knowledge refinement")**
> Re-entering the reformulation phase to update generalized knowledge after failures or detected inconsistencies.

**[Identification of Multiple Logical Interpretations in Counter-Arguments](https://aclanthology.org/2025.emnlp-main.327.pdf) (as "Factual knowledge updating")**
> The observable process of modifying model parameters to reflect new factual associations in the form of subject-relation-object triples, such as updating "Beats Music is owned by Apple."

## Relationships

### Knowledge editing →
- **zs-RE** (measurements) — *measured_by*
  > "We adopted two representative benchmarks in the field of model editing: Counterfact(Meng et al., 2022) and ZsRE(Levy et al., 2017)." (Section 4.1) and "we adopt the metrics for evaluating knowledge updating ability: Efficacy (efficiency success) and Generalization (paraphrase success)" (Section 4.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **CounterFact** (measurements) — *measured_by*
  - [Implicit Values Embedded in How Humans andLLMs Complete Subjective Everyday Tasks](https://aclanthology.org/2025.emnlp-main.848.pdf)
- **WikiDatacounterfact** (measurements) — *measured_by*
  > "We select three datasets including knowledge insertion and knowledge modification in our experiments: WikiDatacounterfact (Cohen et al., 2024), WikiDatarecent (Cohen et al., 2024) and ZsRE (Levy et al., 2017)."
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **WikiDatarecent** (measurements) — *measured_by*
  > "We select three datasets including knowledge insertion and knowledge modification in our experiments: WikiDatacounterfact (Cohen et al., 2024), WikiDatarecent (Cohen et al., 2024) and ZsRE (Levy et al., 2017)."
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **WikiBio** (measurements) — *measured_by*
  > we edit different kinds of knowledge: WikiDatarecent, WikiDatacounterfact (Cohen et al., 2024), WikiBio (Hartvigsen et al., 2024), ConvSent (Mitchell et al., 2022), and ZsRE (Yao et al., 2023). (Section 3.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > Using the MMLU Pro (Wang et al., 2024) benchmark taxonomy, which divides question-answer sets into 14 distinct domains, we investigated the effects of domain-specific knowledge unlearning on MMLU (Hendrycks et al., 2021).
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)

### Associated with
- **Locality** (constructs)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **Generality** (constructs)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **Portability** (constructs)
  > Knowledge editing seeks to maximize the chance of an LLM responding with y given x, while satisfying the following additional criteria at the same time...: (2) Portability: relevant knowledge such as the first lady of United States should be updated as well. (Section 2.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **Linguistic quality** (constructs)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
