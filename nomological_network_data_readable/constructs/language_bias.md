# Language bias
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** Anglocentric bias, Language-dependent effectiveness, Cross-lingual fairness  

## State of the Field

Across the provided literature, 'Language bias' is used to describe two distinct phenomena. The prevailing usage frames it as inequitable performance across different natural languages in multilingual models, where it is also referred to as 'Anglocentric bias' or 'language-dependent effectiveness'. This is commonly observed as a performance gap between high-resource languages like English and non-Western languages. One paper operationalizes this by quantifying it as "the performance drop when switching from bilingual to multilingual evaluation" ('AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents'). Another characterization describes it as a model's tendency to map sentences from the same language closer together in its embedding space, regardless of semantic similarity. A separate line of work defines 'Language bias' in the context of vision-language models (LVLMs) as a modality issue, where models "‘ignore’ visual inputs and generate text responses solely based on text inputs" ('Do It Yourself (DIY): Modifying Images for Poems in a Zero-Shot Setting Using Weighted Prompt Manipulation'). This form of bias is reported to cause or be "closely related to" `Hallucination`. The construct is also measured by the `ScienceQA-IMG` benchmark, though the specific method is not detailed. Thus, the term's application in this set of papers is split between cross-lingual performance equity and modality preference within vision-language models.

## Sources

**[An Empirical Study of Iterative Refinements for Non-autoregressive Translation](https://aclanthology.org/2025.acl-long.1444.pdf) (as "Cross-lingual fairness")**
> The degree to which model performance and computational efficiency are equitable across different languages, mitigating biases introduced by static tokenization.

**[RePanda: Pandas-powered Tabular Verification and Reasoning](https://aclanthology.org/2025.acl-long.1550.pdf) (as "Anglocentric bias")**
> A systemic tendency for model performance, particularly in style-sensitive tasks like translation, to be higher for English and Western languages compared to non-Western languages.

**[ConsistencyChecker: Tree-based Evaluation ofLLMGeneralization Capabilities](https://aclanthology.org/2025.acl-long.1586.pdf) (as "Language-dependent effectiveness")**
> The systematic variation in a model's performance that is attributable to the specific natural language it is operating on, often observed as a performance gap between high-resource and lower-resource languages.

**[AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://aclanthology.org/2025.acl-long.108.pdf)**
> The tendency of a multilingual model to prefer certain languages or language pairs, for instance by mapping sentences from the same language closer together in the embedding space regardless of semantic similarity.

## Relationships

### Language bias →
- **Hallucination** (behaviors tasks) — *causes*
  > LVLMs suffer from hallucinations caused by language bias, which neglects images while over-relying on text. (Abstract)
  - [Do It Yourself (DIY): Modifying Images for Poems in a Zero-Shot Setting Using Weighted Prompt Manipulation](https://aclanthology.org/2025.emnlp-main.995.pdf)
- **ScienceQA-IMG** (measurements) — *measured_by*
  - [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  > These findings provide statistical evidence that language bias is closely related to hallucinations in LVLMs.
  - [Contrastive Prompting Enhances Sentence Embeddings inLLMs through Inference-Time Steering](https://aclanthology.org/2025.acl-long.175.pdf)
