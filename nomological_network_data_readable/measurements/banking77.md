# BANKING77
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** BANKING, Banking-77, Banking77, Bank77  

## State of the Field

BANKING77 is predominantly characterized as a dataset for intent classification within the customer banking domain. Most definitions specify that it contains online banking queries organized into 77 fine-grained intent classes. The instrument is primarily used to measure `Intention recognition` and `Text classification`, with papers frequently applying it to evaluate "fine-grained intent detection" and "domain-specific language understanding." Researchers also employ it to assess model performance in specific contexts, such as under "in-context learning settings," with one paper noting it is part of a set of benchmarks "specifically designed for ICL tasks," and in federated learning scenarios with data heterogeneity. A less common framing uses the dataset for `intent discovery`, aiming to "discover unknown intents in user utterances." Beyond these applications, BANKING77 is also reported as a tool for measuring `Safety` and `Commonsense knowledge`.

## Sources

**[Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.19.pdf)**
> A dataset for intent classification, used in this paper to evaluate model performance under various simulated data heterogeneity settings in a federated learning context.

**[CCHall: A Novel Benchmark for Joint Cross-Lingual and Cross-Modal Hallucinations Detection in Large Language Models](https://aclanthology.org/2025.acl-long.1486.pdf) (as "BANKING")**
> Intent classification dataset focused on customer banking queries, used to evaluate fine-grained intent detection in real-world domains.

**[Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](https://aclanthology.org/2025.acl-long.1542.pdf) (as "Banking-77")**
> A customer service intent classification dataset in the banking domain with 77 intent classes, used to evaluate domain-specific language understanding.

**[MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf) (as "Banking77")**
> Intent classification dataset in the banking domain with 77 classes, used to evaluate fine-grained classification under in-context learning settings.

**[QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.241.pdf) (as "Bank77")**
> A dataset for intent discovery, aiming to identify unknown intents within user utterances.

## Relationships

### → BANKING77
- **Robustness** (constructs) — *measured_by*
  - [Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.19.pdf)
- **Intention recognition** (behaviors tasks) — *measured_by*
  - [Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing](https://aclanthology.org/2025.emnlp-main.1.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  - [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.385.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
