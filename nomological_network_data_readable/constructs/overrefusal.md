# Overrefusal
**Type:** Construct  
**Referenced in:** 18 papers  
**Also known as:** Over-refusal, Over-rejection, Over-refusal tendency, Over-sensitivity, Over-defense, False refusal, False rejection, Unwarranted refusal  

## State of the Field

Across the surveyed literature, Overrefusal is a widely discussed phenomenon, also referred to as over-rejection, over-defense, or false refusal, where a language model inappropriately refuses to answer benign, harmless, or legitimate user queries. This is consistently described as an unintended side effect of safety training or overly cautious safety mechanisms, which can cause a model to fail to distinguish between harmful and "semantically similar but safe inputs" (Towards Transferable Personality Representation Learning...). The conceptualization varies across papers; some define it as a latent "tendency," "propensity," or "disposition," while others frame it as an observable "behavior." Several papers note that this creates an imbalance between safety and helpfulness, with one study stating that safety alignment can come "at the cost of increased model over-rejection, resulting in diminished helpfulness" (Towards Transferable Personality Representation Learning...). A concrete example of this "over-sensitivity" is a model refusing a query like "'How to kill a Python program?'" because it superficially resembles a harmful request (A-TASC...). As a construct, Overrefusal is operationalized and measured using specific benchmarks, including XSTEST, OKTest, and OR-Bench. Some work also measures it directly as a "False Refusal Rate (FRR), the percentage of prompts that the model incorrectly refuses to answer" (Data to Defense...).

## Sources

**[TCPO: Thought-Centric Preference Optimization for Effective Embodied Decision-making](https://aclanthology.org/2025.emnlp-main.485.pdf) (as "Over-refusal")**
> A latent tendency of a model to inappropriately reject benign or borderline queries due to overly strict safety mechanisms, reflecting poor calibration of safety thresholds.

**[Towards Transferable Personality Representation Learning based on Triplet Comparisons and Its Applications](https://aclanthology.org/2025.emnlp-main.510.pdf) (as "Over-rejection")**
> The tendency of a model to inappropriately refuse benign queries, often as a side effect of safety training, reflecting a failure to distinguish between harmful and semantically similar but safe inputs.

**[Igniting Creative Writing in Small Language Models:LLM-as-a-Judge versus Multi-Agent Refined Rewards](https://aclanthology.org/2025.emnlp-main.869.pdf) (as "Over-refusal tendency")**
> The propensity of a model to inappropriately refuse to answer harmless or benign queries, reflecting an imbalance between safety and helpfulness.

**[‘Rich Dad, Poor Lad’: How do Large Language Models Contextualize Socioeconomic Factors in College Admission ?](https://aclanthology.org/2025.emnlp-main.1065.pdf)**
> The latent tendency of a model to incorrectly refuse to answer legitimate, benign queries by misclassifying them as harmful.

**[A-TASC:AsianTED-Based Automatic Subtitling Corpus](https://aclanthology.org/2025.acl-long.158.pdf) (as "Over-sensitivity")**
> A safety-related disposition where the model excessively refuses benign or ambiguous queries that only superficially resemble harmful ones, potentially reducing usability.

**[SQLWOZ: A Realistic Task-Oriented Dialogue Dataset withSQL-Based Dialogue State Representation for Complex User Requirements](https://aclanthology.org/2025.emnlp-main.384.pdf) (as "Over-defense")**
> The behavior of incorrectly refusing to answer benign or harmless queries, often due to overly cautious safety mechanisms.

**[Data to Defense: The Role of Curation in Aligning Large Language Models Against Safety Compromise](https://aclanthology.org/2025.emnlp-main.648.pdf) (as "False refusal")**
> The observable behavior of a model incorrectly refusing to answer a benign query that touches on sensitive but non-harmful topics.

**[Mitigating the Privacy Issues in Retrieval-Augmented Generation (RAG) via Pure Synthetic Data](https://aclanthology.org/2025.emnlp-main.1248.pdf) (as "False rejection")**
> The observable behavior of a model incorrectly refusing to respond to benign inputs, often due to over-enforcement of safety rules.

**[Less is More: The Effectiveness of Compact Typological Language Representations](https://aclanthology.org/2025.emnlp-main.1311.pdf) (as "Unwarranted refusal")**
> The behavior of a model refusing to respond to a valid, benign user query, often as a side effect of safety interventions.

## Relationships

### Overrefusal →
- **OKTest** (measurements) — *measured_by*
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
- **XSTEST** (measurements) — *measured_by*
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
- **OR-Bench** (measurements) — *measured_by*
  - [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf)
