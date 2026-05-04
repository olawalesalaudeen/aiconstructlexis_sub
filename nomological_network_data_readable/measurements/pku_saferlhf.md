# PKU-SafeRLHF
**Type:** Measurement  
**Referenced in:** 16 papers  
**Also known as:** PKU SafeRLHF  

## State of the Field

Across the surveyed literature, PKU-SafeRLHF is predominantly used as a dataset to evaluate and train large language models on safety and alignment with human preferences. The most common application is to measure `Harmlessness`, with many papers using it to assess model responses to harmful queries. A frequent secondary application is the measurement of `Helpfulness`, with several sources noting the dataset is annotated for both dimensions, enabling the study of trade-offs between them. A single paper also uses it to measure `Generalization`. The dataset is consistently described as containing prompt-response pairs, often with two responses per prompt and human preference labels indicating which is more harmful or helpful. Its content is characterized as human-curated and covering dimensions such as "insults, immorality, crime, emotional harm, and privacy" (Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis). Papers operationalize PKU-SafeRLHF in several ways: it is frequently employed as a benchmark for out-of-distribution evaluation, sometimes with "red-teaming instructions"; it is also used for model training, including safety alignment via reinforcement learning and fine-tuning. A less common but noted use is as a benchmark to evaluate the performance of "generative judges on safety-related preference judgments" (Learning LLM-as-a-Judge for Preference Alignment).

## Sources

**[Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf)**
> A dataset used for out-of-distribution evaluation of model performance on harmful queries.

**[Unmasking and Improving Data Credibility: A Study with Datasets for Training Harmless Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c3837ae3d17a91b08bf5cc19280e7fd2-Paper-Conference.pdf) (as "PKU SafeRLHF")**
> A dataset of over 300k instances with prompt-response pairs and safety labels, derived from human preferences, used for reinforcement learning with human feedback in safety alignment.

## Relationships

### → PKU-SafeRLHF
- **Harmlessness** (constructs) — *measured_by*
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > "Experimental results on the HH-RLHF and PKU-SafeRLHF datasets, evaluated using both automatic metrics and human judgments"
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH) (Bai et al., 2022), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU) (Ji et al., 2024), Reward3, UltraFeedback(UltraF) (Cui et al., 2024), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
