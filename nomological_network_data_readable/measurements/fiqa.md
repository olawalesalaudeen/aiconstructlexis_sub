# FiQA
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, FiQA is consistently characterized as a dataset, frequently cited as part of the BEIR benchmark. The most prevalent use of FiQA is to evaluate models on information retrieval and question answering tasks, specifically within the financial domain. Papers most commonly describe it as a benchmark for `financial question answering` and as a `single-hop retrieval benchmark`. One paper notes that its corpus is composed of "human-written responses to the search queries in the dataset" ("Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers"). A smaller line of work also uses FiQA to measure `sentiment analysis`, where models predict sentiments in financial texts. In terms of operationalization, one study reports using the ROUGE-L metric for downstream evaluation with FiQA, while another uses it to generate and assess adversarial passages in corpus-poisoning experiments.

## Sources

**[Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)**
> A BEIR dataset used as a single-hop retrieval benchmark where passages are human-written responses to search queries.

## Relationships

### → FiQA
- **Sentiment analysis** (behaviors tasks) — *measured_by*
  > In the financial domain, we consider (1) the sentiment analysis task FiQA (Xie et al., 2023) where LLMs predict sentiments categorized as ’positive’, ’neutral’, or ’negative’ in financial texts.
  - [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf)
- **Financial question answering** (behaviors tasks) — *measured_by*
  > “FiQA (Maia et al., 2018), Financial QA”
  - [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf)
