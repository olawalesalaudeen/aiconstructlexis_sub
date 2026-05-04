# Out-of-distribution detection
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** OOD detection  

## State of the Field

Across the provided literature, out-of-distribution (OOD) detection is consistently defined as the task of identifying input samples that originate from a data distribution different from the one a model was trained on. The most common operationalization described is assigning a higher uncertainty score to OOD samples compared to in-distribution (ID) ones. In this context, OOD detection is framed as a "key benchmark for assessing the performance of uncertainty-aware methods" ("Calibrating LLMs with Information-Theoretic Evidential Deep Learning"). This behavior is measured by training a model on an ID dataset and then evaluating its ability to identify samples from designated OOD datasets. For example, studies use ARC-Challenge and ARC-Easy as OOD datasets after training on OBQA, or use SVHN after training on CIFAR100-LT. Another measurement approach involves using an out-of-distribution language, such as evaluating on Samoan translations of the TQA dataset. A model's capacity for OOD detection is reported to be influenced by its visual interpretation abilities, with one paper stating that "high interpretability of visual features contributes to stronger OoDD capabilities."

## Sources

**[Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)**
> The observable task of identifying whether a given input sample comes from a different data distribution than the one the model was trained on, typically by assigning it a higher uncertainty score.

**[Adapting Multi-modal Large Language Model to Concept Drift From Pre-training Onwards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e25d87b8a42ee3f0d5b3ef741ca13031-Paper-Conference.pdf) (as "OOD detection")**
> The task of identifying input samples that do not belong to the training distribution.

## Relationships

### Out-of-distribution detection →
- **ARC-Challenge** (measurements) — *measured_by*
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **SVHN** (measurements) — *measured_by*
  > The model is trained on CIFAR100-LT Krizhevsky & Hinton (2009) with an imbalance ratio of 100, and validated on external OOD datasets including SVHN Netzer et al. (2011), Places365 Zhou et al. (2017), LSUN Yu et al., iSUN Xu et al. and Texture Cimpoi et al. (2014). (Section 3)
  - [Adapting Multi-modal Large Language Model to Concept Drift From Pre-training Onwards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e25d87b8a42ee3f0d5b3ef741ca13031-Paper-Conference.pdf)
- **TQA** (measurements) — *measured_by*
  > We then repeat the experiment with the statements translated into Samoan, an out-of-distribution language for TQA (Kembhavi et al., 2017).
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)

### → Out-of-distribution detection
- **Visual interpretation** (constructs) — *causes*
  > We found that one of the reasons for this discrepancy is the insufficient image interpretation capabilities of these models, which limits their ability to accurately distinguish between ID and OoD inputs. (Section 1)
  - [Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf)
- **Uncertainty estimation** (constructs) — *causes*
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
