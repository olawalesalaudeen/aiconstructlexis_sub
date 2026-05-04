# Out-of-distribution generalization
**Type:** Construct  
**Referenced in:** 56 papers  
**Also known as:** Domain generalization, Out-of-distribution generalisation, Out-of-Distribution Generalization, OOD generalization, Out-of-domain generalization, Open-set generalization, Domain generalizability, Cross-category generalization, Policy transferability, Out-of-distribution prediction  

## State of the Field

Across the surveyed literature, out-of-distribution (OOD) generalization is most commonly defined as a model's ability to maintain performance on data drawn from distributions, domains, or environments not seen during training. This concept appears under various names, including "domain generalization" and "out-of-domain generalization," all pointing to the same core capacity for performance transfer to novel contexts. The construct is frequently framed as requiring more than simple pattern matching, with one paper describing it as a need for "truly structural generalization rather than partial memorization" ("Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers"). While most definitions treat it as a latent ability, a minority framing presents "out-of-distribution prediction" as the observable performance itself. The prevailing method for operationalizing this construct is to evaluate models on held-out test sets that have an explicit distributional shift from the training data. For instance, studies measure OOD generalization by testing a summarization model on the `CNN/DailyMail` dataset after training on a different corpus, or by evaluating a planning model on `Blocksworld` problems with longer plan lengths than those in the training set. Other benchmarks used to assess this construct include `AlpacaEval v1.0`, `SHP`, and `IMDb`. Out-of-distribution generalization is frequently studied in relation to "in-context learning", "output diversity", and is often contrasted with "memorization". Some work also reports that it is influenced by constructs such as "compositionality" and "GUI understanding".

## Sources

**[Nemesis: Normalizing the Soft-prompt Vectors of Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/010c855df402b443e0c16e5b7434e74c-Paper-Conference.pdf) (as "Domain generalization")**
> The ability of a vision-language model to maintain or transfer performance from a source domain (e.g., ImageNet) to unseen or shifted target domains (e.g., ImageNet-V2, ImageNet-Sketch).

**[Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)**
> The model's ability to perform well on test data drawn from environments or distributions not seen during training, by leveraging contextual information to adapt dynamically.

**[Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf) (as "Out-of-distribution generalisation")**
> The ability of a model to maintain performance on inputs drawn from a different distribution than its training data.

**[Competition Dynamics Shape Algorithmic Phases of In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a635abfdd007c9a698410c8bbe5ebc33-Paper-Conference.pdf) (as "Out-of-Distribution Generalization")**
> The latent capacity to perform accurately on data distributions not encountered during training.

**[Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf) (as "OOD generalization")**
> The ability to perform well on formalization problems drawn from distributions different from the training or in-domain benchmark data.

**[When is Task Vector Provably Effective for Model Editing? A Generalization Analysis of Nonlinear Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb23cf87a9e04d7677b73c47acd060ef-Paper-Conference.pdf) (as "Out-of-domain generalization")**
> The ability to perform effectively on new tasks or data distributions that were not seen during fine-tuning, achieved by forming a linear combination of existing task vectors.

**[DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.388.pdf) (as "Open-set generalization")**
> The latent ability to recognize and process multimodal entities that were not present during training, leveraging broad multimodal knowledge.

**[Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention](https://aclanthology.org/2025.acl-long.271.pdf) (as "Domain generalizability")**
> The ability of a model to maintain or improve performance when applied to unseen domains or datasets different from its training domain.

**[Towards Objective Fine-tuning: HowLLMs’ Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.723.pdf) (as "Cross-category generalization")**
> The ability of a model to extract aspect-action pairs in sustainability categories not seen during training, reflecting robustness to intra-domain distribution shifts.

**[LAQuer: Localized Attribution Queries in Content-grounded Generation](https://aclanthology.org/2025.acl-long.747.pdf) (as "Policy transferability")**
> The extent to which a model's learned strategies can be successfully applied to new, unseen domains or scenarios.

**[Can a Single Model Master Both Multi-turn Conversations and Tool Use?CoALM: A Unified Conversational Agentic Language Model](https://aclanthology.org/2025.acl-long.606.pdf) (as "Cross-domain generalization")**
> The latent ability of a model to maintain performance when applied to document types or domains not seen during training, despite differences in layout, fonts, templates, and background.

**[Can Transformers Do Enumerative Geometry?](https://proceedings.iclr.cc/paper_files/paper/2025/file/aee2f03ecb2b2c1ea55a43946b651cfd-Paper-Conference.pdf) (as "Out-of-distribution prediction")**
> The observable performance of the model when tested on data from a different distribution than the training data, such as higher genera or unseen numbers of marked points.

## Relationships

### Out-of-distribution generalization →
- **CNN/DailyMail** (measurements) — *measured_by*
  > For summarisation, the ID test set is the original TL;DR test set from (Stiennon et al., 2022), and the OOD test set is the CNN/DailyMail test set, a dataset of news articles and corresponding summaries (Nallapati et al., 2016). This tests the ability of the model to have learnt the more general skill of summarisation and to apply it in a very different domain. (Section 5.1)
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Blocksworld** (measurements) — *measured_by*
  > reports our results on Blocksworld (BW) that studies out-of-distribution generalization to longer plan lengths. (Section 4.1)
  - [Improving Large Language Model Planning with Action Sequence Similarity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b18c6549c77411d92e645027a25838a8-Paper-Conference.pdf)
- **SHP** (measurements) — *measured_by*
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **IMDb** (measurements) — *measured_by*
  - [Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention](https://aclanthology.org/2025.acl-long.271.pdf)

### → Out-of-distribution generalization
- **In-context learning** (constructs) — *causes*
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Compositionality** (constructs) — *causes*
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **GUI understanding** (constructs) — *causes*
  > omitting the pre-training stage significantly degrades performance... These results highlight the critical importance of the data infrastructure for grounding data synthesis; with this infrastructure in place, we can easily improve OOD downstream performance simply by scaling the pre-training corpus. (Section 5.3)
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)

### Associated with
- **In-context learning** (constructs)
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
- **Output diversity** (constructs)
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Memorization** (constructs)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
