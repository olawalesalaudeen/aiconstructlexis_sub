# Model collapse
**Type:** Construct  
**Referenced in:** 29 papers  
**Also known as:** Representation collapse, Behavior collapse, Neural collapse, Representational collapse, Within-class variability collapse, Mode collapse, Catastrophic collapse, Log-likelihood collapse  

## State of the Field

The term "Model collapse" is used across the literature to describe several distinct but related phenomena involving performance degradation in language models. The most prevalent usage refers to a latent degradation caused by training on synthetic, model-generated data, which leads to "worsening generalization and failure to improve with more data" (Strong Model Collapse). A distinct but common framing focuses on internal model states, with variants like "representation collapse" describing the degradation of features during fine-tuning or the increasing similarity of hidden states in deeper layers. Another line of work investigates "neural collapse," a geometric phenomenon where last-layer representations adopt a simplified structure during training. Other specific variants are also discussed, including "behavior collapse" (converging on a degenerate strategy) and "mode collapse" (in knowledge distillation). The construct is operationalized and measured through performance on benchmarks such as MNIST, BabiStories, and HelpSteer2, with one study quantifying a form of it via cosine similarity between layer inputs. Across papers, model collapse is frequently linked to a decrease in generalization and is studied alongside concepts like output diversity and semantic drift. While most papers frame collapse as a negative outcome that can cause misinformation generation, the specific phenomenon of neural collapse is sometimes reported to promote fairness.

## Sources

**[Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)**
> A latent degradation in model performance caused by training on synthetic data, characterized by worsening generalization and failure to improve with more data.

**[LiNeS: Post-training Layer Scaling Prevents Forgetting and Enhances Model Merging](https://proceedings.iclr.cc/paper_files/paper/2025/file/43ae0b566b802b2d00e525b672794b82-Paper-Conference.pdf) (as "Representation collapse")**
> The distortion and degradation of general, pre-trained feature representations within a model during the process of fine-tuning on a specific downstream task.

**[Training Language Models to Self-Correct via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf) (as "Behavior collapse")**
> A tendency for training to converge on a degenerate non-correcting strategy, such as making no meaningful edits on later attempts.

**[Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf) (as "Neural collapse")**
> A learning phenomenon in deep neural networks where last-layer representations and classifier weights adopt a specific, simplified geometric structure during the terminal phase of training.

**[Transformers need glasses! Information over-squashing in language tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1d35561c4a4a0e0b6012b2af531e149-Paper-Conference.pdf) (as "Representational collapse")**
> A phenomenon where distinct input sequences produce arbitrarily close final-token representations, making them indistinguishable to the model, especially with low-precision arithmetic.

**[Linguistic Collapse: Neural Collapse in (Large) Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f88cc8930b47a45ec4733123bf3039b9-Paper-Conference.pdf) (as "Within-class variability collapse")**
> The reduction of dispersion among representations belonging to the same class, so that same-class embeddings become tightly clustered around their class mean.

**[TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf) (as "Mode collapse")**
> An observable failure mode in knowledge distillation where a student model's output distribution becomes overly focused on only the dominant modes of the teacher's distribution, ignoring less frequent but potentially important information.

**[Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf) (as "Catastrophic collapse")**
> A failure mode in training where model performance sharply deteriorates after an initial improvement, often linked to unstable optimization dynamics in preference learning.

**[Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf) (as "Log-likelihood collapse")**
> The rapid decrease of the log-probabilities assigned to both preferred and dispreferred responses from the training data, often observed in certain offline RLHF methods.

## Relationships

### Model collapse →
- **Generalization** (constructs) — *causes*
  > Consequently, the model’s ability to generalize to real-world data is compromised, as it increasingly relies on the distorted distribution provided by prior AI generations rather than learning accurate representations of the real world. (Section 1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **Token copying** (behaviors tasks) — *causes*
  - [Transformers need glasses! Information over-squashing in language tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1d35561c4a4a0e0b6012b2af531e149-Paper-Conference.pdf)
- **Misinformation generation** (behaviors tasks) — *causes*
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **MNIST** (measurements) — *measured_by*
  > Our theoretical results are empirically confirmed with experiments in: • Toy settings, including random projections model on Gaussian data, and shallow networks fully trained on the MNIST dataset (Deng, 2012). (Section 1.1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **BabiStories** (measurements) — *measured_by*
  > Our theoretical results are empirically confirmed with experiments in: ... • Realistic setting of GPT-2 models trained on BabiStories (Zhang et al., 2024a) (Section 1.1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  - [Seq-VCR: Preventing  Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)
- **Fairness** (constructs) — *causes*
  > This observation further inspires us to explicitly enforce neural collapse to promote fairness in pretrained language models. (Section 1)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [Advancing Personalized Learning with Neural Collapse for Long-Tail Challenge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25f/hu25f.pdf)
- **HelpSteer2** (measurements) — *measured_by*
  > Fine-tuning Google’s Gemma2 models on Nvidia’s HelpSteer 2 dataset demonstrates that model collapse occurs if previous data are replaced after each model-fitting iteration (left), whereas model collapse is avoided if new synthetic data instead accumulate with previous real and synthetic data (right).
  - [Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kazdan25a/kazdan25a.pdf)

### → Model collapse
- **Generalization** (constructs) — *correlates*
  - [Linguistic Collapse: Neural Collapse in (Large) Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f88cc8930b47a45ec4733123bf3039b9-Paper-Conference.pdf)
- **Safety** (constructs) — *causes*
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **Fairness** (constructs) — *correlates*
  > we find that debiased language models exhibit collapsed alignment between token representations and word embeddings. (Abstract)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)

### Associated with
- **Output diversity** (constructs)
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Representation diversity** (constructs)
  > Representation collapse in Transformers manifests as a reduction in the diversity of internal representations across layers
  - [Seq-VCR: Preventing  Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)
- **Generation quality** (constructs)
  > “a better generator always improves performance”
  - [Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
- **Generation diversity** (constructs)
  - [Representative Language Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/peale25a/peale25a.pdf)
- **Semantic drift** (constructs)
  > “Semantic drift & Model Collapse, the idea that the influx of AI-generated text can shift the distribution and meaning of language, and lead to compounding errors”
  - [Refining Text Generation for Realistic Conversational Recommendation via Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.1457.pdf)
