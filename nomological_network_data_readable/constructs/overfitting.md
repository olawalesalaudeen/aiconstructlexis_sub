# Overfitting
**Type:** Construct  
**Referenced in:** 26 papers  
**Also known as:** Overadaptation, Catastrophic overtraining, Benchmark overfitting  

## State of the Field

Across the surveyed literature, the prevailing definition of Overfitting is a phenomenon where a model learns its training data too closely, capturing noise and specific artifacts, which harms its ability to generalize to new data. This can involve learning superficial details like "formatting details, exact wording, and text length" ("NEFTune: Noisy Embeddings Improve Instruction Finetuning"). While this general framing is common, a smaller body of work introduces more specific variants, such as "benchmark overfitting," where models exploit patterns in evaluation data, and "overadaptation," a form of overfitting during fine-tuning that results in the loss of pretrained knowledge. One paper also describes "catastrophic overtraining," where excessive pre-training harms post-training performance.

As a construct, overfitting is most directly operationalized by observing a "U-curve" where validation loss increases while training loss continues to decrease. It is also assessed by measuring performance on out-of-domain data splits. The literature indicates that performance on a range of benchmarks, including HumanEval, MMLU, HellaSwag, WinoGrande, and BoolQ, is used in the context of studying overfitting.

Overfitting is consistently positioned as being inversely related to generalization, with multiple papers stating that it causes a decline in generalization capability. It is also linked to memorization, with one study defining it as a model "memorizing the full context at the expense of using capacity to learn statistics of subcontext" ("Understanding Transformers via N-Gram Statistics"). The concept is also studied alongside knowledge forgetting and catastrophic forgetting.

## Sources

**[Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)**
> The phenomenon where a model learns the training data too closely, capturing noise and specific artifacts, which harms its ability to generalize to new data.

**[Understanding Overadaptation in Supervised Fine-Tuning: The Role of Ensemble Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25d/hao25d.pdf) (as "Overadaptation")**
> The latent tendency of a fine-tuned model to overfit to downstream task data, resulting in degraded generalization and loss of pretrained knowledge, analogous to harmful overfitting in statistical learning.

**[Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf) (as "Catastrophic overtraining")**
> The phenomenon where extending pre-training beyond a certain token budget results in decreased model performance after subsequent modifications such as fine-tuning, due to increased sensitivity to parameter changes.

**[Continuous-Time Attention:PDE-Guided Mechanisms for Long-Sequence Transformers](https://aclanthology.org/2025.emnlp-main.1098.pdf) (as "Benchmark overfitting")**
> A model's tendency to rely on superficial cues, specific phrasing, or structural patterns within a benchmark's prompts, leading to high scores that do not reflect true, generalizable capabilities.

## Relationships

### Overfitting →
- **Generalization** (constructs) — *causes*
  > Over-personalization can lead to overfitting, reducing generalizability (Abstract).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs) — *causes*
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **SocialIQA** (measurements) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **PIQA** (measurements) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **MMLU** (measurements) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)

### → Overfitting
- **Memorization** (constructs) — *causes*
  > This result suggests that some of the reason for overﬁtting is due to partial memorization of the test set. (Section 5.4)
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *causes*
  > Injecting pretraining data has a regularizing effect that reduces overfitting and forgetting. (Figure 1 caption)
  - [Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bethune25a/bethune25a.pdf)

### Associated with
- **Generalization** (constructs)
  > This indicated less overfitting and better generalization when NEFTune is used. (Section 5.1)
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://proceedings.iclr.cc/paper_files/paper/2024/file/fbf1b3765e081251c804da7f508f3b21-Paper-Conference.pdf)
- **Pre-training data detection** (behaviors tasks)
  > A common view is that the effectiveness of TDD is closely tied to the level of training-data memorization or overfitting exhibited by the target model during training (Yeom et al., 2018; Long et al., 2018).
  - [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf)
- **HumanEval** (measurements)
  > This indicates some level of overfitting to HUMANEVAL.
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs)
  - [Understanding Overadaptation in Supervised Fine-Tuning: The Role of Ensemble Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25d/hao25d.pdf)
