# SNLI
**Type:** Measurement  
**Referenced in:** 26 papers  

## State of the Field

Across the provided literature, SNLI (Stanford Natural Language Inference) is consistently characterized as a large-scale dataset or benchmark used to evaluate natural language inference (NLI). The benchmark operationalizes this by presenting models with sentence pairs and requiring a classification of the relationship as one of three labels: 'entailment', 'neutral', or 'contradiction'. One source specifies that the dataset was constructed using "image captions as premises paired with hypotheses elicited from crowdworkers" ('No Simple Answer to Data Complexity: An Examination of Instance-Level Complexity Metrics for Classification Tasks'). While its primary and most frequent application is measuring NLI, it is also used to assess the broader capability of 'Natural language understanding'. A smaller set of studies adapts SNLI for more specific purposes, for instance, as an out-of-domain task to measure model generalization or as a source to generate stimuli for logical inconsistency tasks. One study reports using only the 'entailment' pairs from the dataset to specifically evaluate a model's ability to compute asymmetric relationships. SNLI is frequently mentioned and used in experiments alongside other NLI benchmarks such as MNLI, QNLI, and RTE.

## Sources

**[Meaning Representations from Trajectories in Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/ac1887299ee703ba4e54f8c102161213-Paper-Conference.pdf)**
> The Stanford Natural Language Inference dataset, a large-scale corpus for evaluating textual entailment.

## Relationships

### → SNLI
- **Natural language inference** (behaviors tasks) — *measured_by*
  > We also evaluate KnOTS in the NLI setting, by merging six PEFT llama3-8B (AI, 2024) models finetuned on SNLI (Bowman et al., 2015), MNLI (Williams et al., 2018), SICK (Marelli et al., 2014), QNLI, RTE (Wang et al., 2019), and SCITAIL (Khot et al., 2018). (§ 5.2)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > Experimental results demonstrate that our ReFusion framework can significantly improve models’ understanding capability, achieving superior and robust performance. (Section 1)
  - [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We then assessed the performance of the merged LoRA on these in-domain tasks as well as on two additional out-of-domain tasks, SNLI and WNLI, to evaluate its adaptability and generalization capabilities.
  - [Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b54e0146a82945f01e69c2e3309ba925-Paper-Conference.pdf)
- **Logical consistency** (constructs) — *measured_by*
  - [No Simple Answer to Data Complexity: An Examination of Instance-Level Complexity Metrics for Classification Tasks](https://aclanthology.org/2025.naacl-long.130.pdf)
