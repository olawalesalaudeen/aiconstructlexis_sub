# MNIST
**Type:** Measurement  
**Referenced in:** 16 papers  

## State of the Field

Across the provided literature, MNIST is consistently characterized as a benchmark dataset composed of handwritten digits. Its most prevalent application is to measure and evaluate tasks related to image classification and optical character recognition. For instance, one paper notes that even advanced Vision-Language Models “struggle on simple digit recognition and counting tasks, e.g. MNIST” (UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling). Beyond these core visual tasks, a smaller set of studies uses MNIST to operationalize more abstract phenomena, such as testing a model's general perception capability or empirically confirming theoretical results on model collapse. The dataset is shown to be used in a variety of experimental contexts, including controlled finetuning, evaluating backdoor attacks, and robust hyperparameter optimization, with models ranging from multilayer perceptrons to shallow networks.

## Sources

**[Demystifying Poisoning Backdoor Attacks from a Statistical Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/4488bf8354049b1cd592b6418dc30466-Paper-Conference.pdf)**
> A classification dataset used in the paper's controlled finetuning experiments.

## Relationships

### → MNIST
- **Image classification** (behaviors tasks) — *measured_by*
  > “evaluations conducted on standard benchmark datasets, including Cars (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2018), GTSRB (Stallkamp et al., 2011), MNIST (LeCun, 1998), RESISC45 (Cheng et al., 2017), SUN397 (Xiao et al., 2016), and SVHN (Netzer et al., 2011).”
  - [Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Optical character recognition** (behaviors tasks) — *measured_by*
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Model collapse** (constructs) — *measured_by*
  > Our theoretical results are empirically confirmed with experiments in: • Toy settings, including random projections model on Gaussian data, and shallow networks fully trained on the MNIST dataset (Deng, 2012). (Section 1.1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **Perception** (constructs) — *measured_by*
  > The perception capability is tested on CIFAR-10/100 (Krizhevsky et al., 2009) and MNIST (Deng, 2012). (Section 4.1)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
