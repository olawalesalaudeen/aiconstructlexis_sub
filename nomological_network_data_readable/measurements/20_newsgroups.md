# 20 Newsgroups
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** 20NG, 20NewsGroups  

## State of the Field

Across the provided literature, 20 Newsgroups is consistently characterized as a dataset for text classification and document understanding. It is defined as consisting of approximately 20,000 newsgroup documents partitioned across 20 different newsgroups. The dataset is used to measure several behaviors and constructs, including `Text classification`, `Natural language understanding`, and `Safety`. Researchers operationalize the dataset in various ways, such as for fine-tuning models and evaluating performance and robustness, particularly in federated learning scenarios with data heterogeneity. The categorical structure of the dataset is also leveraged; for example, one study uses it to define in-domain tasks by isolating specific categories, such as using "articles from the computer science categories" for news generation. Other applications include its use in experiments on bias reduction strategies for binary text classification.

## Sources

**[Shh, don't say that! Domain Certification in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/27befed4547edcb4bdeacef9472cadee-Paper-Conference.pdf) (as "20NG")**
> The 20 Newsgroups dataset, used here to define the in-domain task of computer science news generation and the out-of-domain set from its other categories.

**[Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.19.pdf)**
> A dataset for text classification based on newsgroup posts, used to evaluate model performance and robustness in federated learning scenarios.

**[Instance-Selection-Inspired Undersampling Strategies for Bias Reduction in Small and Large Language Models for Binary Text Classification](https://aclanthology.org/2025.acl-long.459.pdf) (as "20NewsGroups")**
> A dataset for document understanding and classification, consisting of approximately 20,000 newsgroup documents partitioned across 20 different newsgroups.

## Relationships

### → 20 Newsgroups
- **Text classification** (behaviors tasks) — *measured_by*
  - [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.19.pdf)
