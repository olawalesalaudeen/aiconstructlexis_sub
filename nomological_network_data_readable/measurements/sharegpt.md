# ShareGPT
**Type:** Measurement  
**Referenced in:** 20 papers  

## State of the Field

Across the provided literature, ShareGPT is consistently defined as a dataset of real-world, user-shared conversations with ChatGPT, collected from the website sharegpt.com. The prevailing use of this dataset falls into two main categories: model training and evaluation. Several papers employ it for supervised fine-tuning (SFT) or general instruction tuning, with one study using "10,000 instruction-response pairs" for this purpose (DataMan: Data Manager for Pre-training Large Language Models). As an evaluation instrument, its application is varied; it is used to source authentic user queries, to benchmark the performance of LLM serving systems, and to assess model capabilities. Specifically, ShareGPT is used to measure `Dialogue`, `Commonsense knowledge`, and `Safety`. It is also explicitly used to evaluate "instruction-following capabilities" alongside other prompt sets covering general reasoning and mathematical problem-solving (A Triple-View Framework for Fine-Grained Emotion Classification with Clustering-Guided Contrastive Learning). A smaller line of work uses the dataset in experiments to study phenomena like alignment drift.

## Sources

**[DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)**
> A dataset of user-shared conversations with ChatGPT, used here for instruction fine-tuning and evaluation.

## Relationships

### → ShareGPT
- **Instruction following** (constructs) — *measured_by*
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.227.pdf)
- **Dialogue** (behaviors tasks) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1475.pdf)

### Associated with
- **HelpSteer2** (measurements)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
