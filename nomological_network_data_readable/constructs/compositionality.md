# Compositionality
**Type:** Construct  
**Referenced in:** 55 papers  
**Also known as:** Composition, Composability, Symbolic composition, Skill composition, Compositional capability, Compositional generalisation, Compositional capabilities  

## State of the Field

Across the surveyed literature, Compositionality is most commonly framed as a model's ability to combine simpler elements—such as subproblems, concepts, or linguistic units—to solve more complex problems or generate complex meanings. While this is the prevailing usage, a distinct concept termed 'Composability' also appears, referring to the ability to combine model components like parameters or interventions without additional training. Other related framings include 'skill composition,' which focuses on combining reasoning steps, and 'compositional generalization,' which emphasizes handling novel combinations of known elements. Researchers operationalize and measure this construct using several benchmarks, with papers in this set citing the use of CREPE, SugarCrepe, and WINOGROUND. A recurring theme is that current models often exhibit deficiencies in this area; as one study notes, a "‘compositionality gap’ remains as models scale in size," and another finds that "LMMs lack compositional ability." The construct is studied alongside other concepts including semantic understanding, faithfulness, and inductive reasoning. A smaller body of work applies the concept to specific domains, such as defining 'composition' as the generation of coherent song structures or the decomposition of drug editing tasks. Some papers also propose that compositionality influences outcomes like out-of-distribution and multilingual generalization.

## Sources

**[Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)**
> The degree to which a model can combine simpler subproblems into correct solutions for more complex problems as difficulty increases.

**[SongCreator: Lyrics-based Universal Song Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/92a7a03e1c716970848a4a86cc8243ee-Paper-Conference.pdf) (as "Composition")**
> The ability to generate musically coherent vocal content and song structure from conditioning inputs such as lyrics or prompts.

**[3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf) (as "Composability")**
> The ability to combine model parameters or components trained on distinct tasks to create new, multitask capabilities without requiring additional training.

**[Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf) (as "Symbolic composition")**
> The latent ability to compose multiple distinct concepts together using symbolic code, uniquely equipped in induction models.

**[Evaluating Contextualized Representations of (Spanish) Ambiguous Words: A New Lexical Resource and Empirical Analysis](https://aclanthology.org/2025.naacl-long.423.pdf) (as "Skill composition")**
> The ability to combine multiple atomic operations or reasoning steps into a coherent solution for a complex task, reflecting compositional generalization in problem-solving.

**[Hierarchical Planning for Complex Tasks with Knowledge Graph-RAG and Symbolic Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/petruzzellis25a/petruzzellis25a.pdf) (as "Compositional capability")**
> The ability of a model to construct complex plans by combining simpler, reusable components (e.g., macro actions) in a structured and coherent way, reflecting systematic generalization across tasks.

**[Transplant Then Regenerate: A New Paradigm for Text Data Augmentation](https://aclanthology.org/2025.emnlp-main.703.pdf) (as "Compositional generalisation")**
> The latent ability of a model to recognise and correctly interpret novel combinations of known linguistic elements (e.g., targets and hateful expressions) that were not observed together during training.

**[Read to Hear: A Zero-Shot Pronunciation Assessment Using Textual Descriptions andLLMs](https://aclanthology.org/2025.emnlp-main.135.pdf) (as "Compositional generalization")**
> The ability to extend compositional reasoning skills to new, unseen combinations of objects, attributes, and relations.

**[Cache-Efficient Posterior Sampling for Reinforcement Learning withLLM-Derived Priors Across Discrete and Continuous Domains](https://aclanthology.org/2025.emnlp-main.561.pdf) (as "Compositional capabilities")**
> The ability to combine simpler computational or linguistic elements to form more complex structures and meanings.

## Relationships

### Compositionality →
- **CREPE** (measurements) — *measured_by*
  > We evaluate on the CREPE benchmark (Ma et al., 2023) that focuses on systematicity (Fodor & Pylyshyn, 1988) and productivity (von Humboldt et al., 1988; Chomsky, 1956). (Section 2.3)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **SugarCrepe** (measurements) — *measured_by*
  > Empirical results on four compositionality benchmarks, Winoground, EqBench, ColorSwap, and SugarCrepe, in seven different open-source VLMs with varying sizes, demonstrate that COCO-Tree significantly improves compositional generalization by 5-10% over baselines. (Abstract)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **WINOGROUND** (measurements) — *measured_by*
  - [EfficientQAT: Efficient Quantization-Aware Training for Large Language Models](https://aclanthology.org/2025.acl-long.499.pdf)
- **Out-of-distribution generalization** (constructs) — *causes*
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *causes*
  - [Human-Object Interaction Detection Collaborated with Large Relation-driven Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a54def490213ee10631b991c5acc6b5-Paper-Conference.pdf)
- **Sentiment analysis** (behaviors tasks) — *measured_by*
  > Two tasks that assess different aspects of compositional generalisation are used in the paper: Inverse Dictionary Modelling (IDM) for word-level composition and Sentiment Classification (SC) for phrase-level structure. (Section 4.1)
  - [ASTRA: A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization](https://aclanthology.org/2025.emnlp-main.822.pdf)

### → Compositionality
- **Adaptability** (constructs) — *causes*
  > By focusing on this principled parameterization, our approach mitigates the risk of overfitting, drastically reduces computational demands, and allows for inherent compositionality. (Section 1)
  - [Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf)

### Associated with
- **Semantic understanding** (constructs)
  > This indicates that compositionality alone might not be sufficient to fully understand semantic and lexical alterations. (Abstract)
  - [SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Task decomposition** (behaviors tasks)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
- **Inductive reasoning** (constructs)
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **Editability** (constructs)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
- **ARC** (measurements)
  > Therefore, we regard ARC tasks as complex compositions of atomic operations for evaluation. (Section 4.2)
  - [Evaluating Contextualized Representations of (Spanish) Ambiguous Words: A New Lexical Resource and Empirical Analysis](https://aclanthology.org/2025.naacl-long.423.pdf)
