# ETHICS
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** Social Chemistry 101, ETHICS dataset, Ethics  

## State of the Field

Across the surveyed literature, ETHICS is a benchmark dataset used to evaluate language models on tasks related to ethics and morality. It is most frequently used to measure 'Ethical reasoning,' with some papers also using it to assess 'Moral reasoning' and 'Ethical decision-making.' The benchmark is consistently described as consisting of scenarios, which are variously characterized as 'morally charged' or involving 'commonsense moral recognition.' Models are typically evaluated in a zero-shot setting, tasked with making classifications such as 'wrong' or 'not wrong' based on these scenarios, with accuracy being a common metric. Some papers specify that these scenarios cover topics like justice, deontology, and virtue ethics, while others mention using specific subsets like 'Commonsense' or 'Deontology.' A specific point raised in one study is that the dataset, collected from participants in the US, Canada, and Great Britain, 'dominantly reflects a Western ethical perspective'.

## Sources

**[ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf) (as "Social Chemistry 101")**
> A dataset encompassing diverse social norms and moral judgments about everyday actions, used to evaluate morality.

**[EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf) (as "ETHICS dataset")**
> A benchmark dataset consisting of morally charged scenarios used to evaluate a model's ability to perform implicit ethical assessments.

**[CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf) (as "Ethics")**
> A zero-shot benchmark dataset used to assess model accuracy on ethical reasoning tasks.

**[More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)**
> A benchmark for evaluating machine ethics, including a 'Commonsense' subset with scenario-based moral recognition tasks.

## Relationships

### → ETHICS
- **Ethical reasoning** (constructs) — *measured_by*
  - [ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
- **Ethical decision-making** (constructs) — *measured_by*
  - [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
- **Moral reasoning** (constructs) — *measured_by*
  > We evaluate models on four moral reasoning benchmarks with varying normative demands: Value Kaleidoscope (VK) (Sorensen et al., 2024), UniMoral (Kumar and Jurgens, 2025), ETHICS (Deontology) (Hendrycks et al., 2020), and MoralCoT (Jacovi et al., 2024). (Section 4)
  - [FLUIDQA: A Multilingual Benchmark for Figurative Language Usage in Dialogue acrossEnglish,Chinese, andKorean](https://aclanthology.org/2025.emnlp-main.1541.pdf)

### Associated with
- **Helpfulness** (constructs)
  - [TRANSIENTTABLES: EvaluatingLLMs’ Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.333.pdf)
