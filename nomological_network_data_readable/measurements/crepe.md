# CREPE
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** Crepe  

## State of the Field

The term CREPE is used inconsistently across the provided literature, referring to at least two distinct benchmarks with different evaluation goals. The most prevalent usage is as a benchmark for evaluating compositional reasoning in vision-language models. In this context, CREPE is used to measure constructs such as `Compositionality` and `Compositional reasoning`. One paper specifies this benchmark's full name as the "Compositionally-hard E-commerce Product Extrapolation (CREPE) benchmark" and notes that it "focuses on systematicity... and productivity." A separate line of work defines CREPE as a "causal reasoning evaluation dataset" for identifying cause-effect relationships in natural language, and it is used in this context to measure `Language proficiency`. Additionally, a single paper introduces a completely different instrument also named CREPE, an acronym for "Rapid Chest X-ray Report Evaluation by Predicting Multi-category Error Counts," which is a regression-based metric for clinical reports. Thus, while the name appears in multiple contexts, its most common application in the surveyed work is for assessing the compositional abilities of models.

## Sources

**[Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)**
> Causal reasoning evaluation dataset that tests models on identifying cause-effect relationships in natural language.

**[ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Crepe")**
> A compositional reasoning benchmark inspired by cognitive science literature and used to test systematicity and productivity.

## Relationships

### → CREPE
- **Causal reasoning** (constructs) — *measured_by*
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **Compositionality** (constructs) — *measured_by*
  > We evaluate on the CREPE benchmark (Ma et al., 2023) that focuses on systematicity (Fodor & Pylyshyn, 1988) and productivity (von Humboldt et al., 1988; Chomsky, 1956). (Section 2.3)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Compositional reasoning** (constructs) — *measured_by*
  - [ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf)
