# FineWeb
**Type:** Measurement  
**Referenced in:** 11 papers  

## State of the Field

Across the provided literature, FineWeb is consistently characterized as a web-text corpus, with some sources describing it as a "high-quality LLM pretraining dataset" composed of "deduplicated English web documents." The most prevalent application of FineWeb is for evaluation. It is used to measure model performance on tasks like `Text completion` and `Data reconstruction`, and is also used as a dataset to evaluate a model's `Generalization`. Some work specifically uses it to evaluate the negative log-likelihood of language models. Beyond evaluation, FineWeb serves as a source for generating new data; one study synthesizes prompts from it, while another samples 10,000 examples to create a new dataset. A more specific application appears in a study that uses the corpus for "analyzing bilinear transformer feature interactions at different model sizes," training models referred to as "'fw-small' and 'fw-medium'" for this purpose.

## Sources

**[Bilinear MLPs enable weight-based mechanistic interpretability](https://proceedings.iclr.cc/paper_files/paper/2025/file/7504142a20a3e1fe9dd7de42f475828c-Paper-Conference.pdf)**
> A web-text corpus used for analyzing bilinear transformer feature interactions at different model sizes.

## Relationships

### → FineWeb
- **Text completion** (behaviors tasks) — *measured_by*
  - [Improving Dialogue State Tracking through Combinatorial Search for In-Context Examples](https://aclanthology.org/2025.acl-long.1394.pdf)
- **Data reconstruction** (behaviors tasks) — *measured_by*
  - [Improving Dialogue State Tracking through Combinatorial Search for In-Context Examples](https://aclanthology.org/2025.acl-long.1394.pdf)
- **Generalization** (constructs) — *measured_by*
  > We evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH) (Bai et al., 2022), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU) (Ji et al., 2024), Reward3, UltraFeedback(UltraF) (Cui et al., 2024), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
