# Stability
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** Local stability, Inference stability, Optimization stability  

## Sources

**[Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hamman25a/hamman25a.pdf) (as "Local stability")**
> A latent property reflecting the robustness of a model's prediction at a given input, determined by the average confidence and variability of predictions in its local neighborhood in the embedding space.

**[RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf)**
> The consistency of model performance around its optimal retrieval depth, indicating resilience to small variations in the number of retrieved passages.

**[Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf) (as "Inference stability")**
> The degree to which a model consistently produces high-quality outputs for a given input, measured by the variance in reward scores across multiple generations.

**[Towards Universal Offline Black-Box Optimization via Learning Language Model Embeddings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25b/tan25b.pdf) (as "Optimization stability")**
> The degree to which the optimization process produces consistent and reliable improvements in objective scores without erratic or divergent behavior, influenced by the geometric properties of the latent embedding space.

## Relationships

### Stability →
- **MMLU** (measurements) — *measured_by*
  - [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BIG-Bench** (measurements) — *measured_by*
  - [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf)

### → Stability
- **Consistency** (constructs) — *measured_by*
  - [Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hamman25a/hamman25a.pdf)
- **Noise robustness** (constructs) — *causes*
  - [RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf)

### Associated with
- **Plasticity** (constructs)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Coherence** (constructs)
  - [Guiding Medical Vision-Language Models with Diverse Visual Prompts: Framework Design and Comprehensive Exploration of Prompt Variations](https://aclanthology.org/2025.naacl-long.588.pdf)
- **In-context learning** (constructs)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
