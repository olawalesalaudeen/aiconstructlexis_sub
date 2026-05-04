# Fairness
**Type:** Construct  
**Referenced in:** 78 papers  
**Also known as:** Algorithmic fairness, Bias, Biasness, Equitability, Purity  

## State of the Field

Across the surveyed literature, the prevailing definition of Fairness is the degree to which a model avoids producing biased or stereotypical outputs across different social groups, aiming for an ideal state of equitable treatment. This is frequently operationalized as ensuring that model predictions are independent of sensitive attributes like gender, race, or sex. While this broad framing is common, some work adopts more specific definitions, such as achieving "counterfactual fairness" where outputs are consistent when spurious attributes are changed, or ensuring equal false positive and negative rates across demographic groups. A smaller set of papers conceptualizes it differently, for instance as "equitability" across cultures or as a moral foundation involving justice and reciprocity.

To measure this construct, researchers employ a wide range of benchmarks and tasks. The most frequently cited instruments in this set include StereoSet, CrowS-Pairs, WinoBias, and BBQ. Other measurement approaches include the Dictator Game, the BOLD dataset, and the specific behavior of stereotype recognition. Fairness is often studied in relation to other constructs like Harmlessness and Faithfulness, and is frequently contrasted with Societal bias and Stereotyping. Some research also connects it to internal model properties, with one paper suggesting that enforcing model collapse can promote fairness.

## Sources

**[Are Models Biased on Text without Gender-related Language?](https://proceedings.iclr.cc/paper_files/paper/2024/file/37771cc0be272368102a37f202bb88d8-Paper-Conference.pdf)**
> The degree to which a model avoids producing biased or stereotypical outputs across different social groups, representing an ideal state of equitable treatment.

**[Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf) (as "Algorithmic fairness")**
> The extent to which a model's outputs are free from systematic prejudice, particularly in sensitive applications like comparing candidates.

**[Aggregation Artifacts in Subjective Tasks Collapse Large Language Models’ Posteriors](https://aclanthology.org/2025.naacl-long.285.pdf) (as "Bias")**
> The tendency of a model to produce systematically prejudiced outputs or predictions based on demographic information rather than the primary task content.

**[Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness](https://aclanthology.org/2025.naacl-long.409.pdf) (as "Equitability")**
> The model's capability to maintain parity between its performance and a user's needs across different cultural backgrounds.

**[MILU: A Multi-taskIndic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.508.pdf) (as "Biasness")**
> The presence or absence of unfair or prejudiced content in a ToD system's responses, particularly with respect to sensitive attributes.

**[Do All Autoregressive Transformers Remember Facts the Same Way? A Cross-Architecture Analysis of Recall Mechanisms](https://aclanthology.org/2025.emnlp-main.1449.pdf) (as "Purity")**
> The latent sensitivity to physical and moral cleanliness, religious or cultural codes, and avoidance of degradation as a moral foundation in narratives.

## Relationships

### Fairness →
- **BBQ** (measurements) — *measured_by*
  - [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](https://proceedings.neurips.cc/paper_files/paper/2024/file/f5198bc255e1d5f959edd6d1d1a86fab-Paper-Conference.pdf)
- **StereoSet** (measurements) — *measured_by*
  > As measured by prior metrics from StereoSet, our model achieves a higher degree of fairness while maintaining language modeling ability with low cost12.
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
- **CrowS-Pairs** (measurements) — *measured_by*
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
- **WinoBias** (measurements) — *measured_by*
  > WinoBias Zhao et al. (2018) is an intra-sentence coreference resolution task designed to assess a system’s ability to correctly associate a gendered pronoun with an occupation in both pro-stereotypical and anti-stereotypical contexts. (Section 4.1.3)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **Winogender** (measurements) — *measured_by*
  - [Enhancing Efficiency and Exploration in Reinforcement Learning forLLMs](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **Dictator Game** (measurements) — *measured_by*
  - [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf)
- **BOLD** (measurements) — *measured_by*
  - [DCR: Quantifying Data Contamination inLLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1174.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VQA-v2** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Model collapse** (constructs) — *correlates*
  > we find that debiased language models exhibit collapsed alignment between token representations and word embeddings. (Abstract)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **SBERT** (measurements) — *measured_by*
  > "We used the SBERT (Sentence-BERT, Bidirectional Encoder Representations from Transformers) model (Reimers and Gurevych, 2019)"
  - [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.114.pdf)
- **FINTRUST** (measurements) — *measured_by*
  > we curate 15, 680 instances to evaluate LLM trustworthiness in the financial domain. We ... incorporate seven core dimensions: Truthfulness, Safety, Fairness, Robustness, Privacy, Transparency, and Knowledge Discovery. (Section 2)
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **Amazon Reviews 2023** (measurements) — *measured_by*
  - [VisBias: Measuring Explicit and Implicit Social Biases in Vision Language Models](https://aclanthology.org/2025.emnlp-main.909.pdf)
- **Stereotype recognition** (behaviors tasks) — *measured_by*
  > "To evaluate the alignment of fairness, we perform stereotype recognition task (Sun et al., 2024) based on benchmark StereoSet (Nadeem et al., 2021) with Stereotype Score (SS) and Accuracy (Acc)."
  - [Does quantization affect models’ performance on long-context tasks?](https://aclanthology.org/2025.emnlp-main.480.pdf)
- **PLLuM-Align** (measurements) — *measured_by*
  > For scalar multi-attribute rating, annotators evaluated each response on a 5-point Likert scale across seven criteria: i) truthfulness, (ii) linguistic correctness, (iii) safety, (iv) fairness, (v) conciseness, (vi) coherence & reasoning, as well as vii) helpfulness & instruction-following.
  - [REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### → Fairness
- **Model collapse** (constructs) — *causes*
  > This observation further inspires us to explicitly enforce neural collapse to promote fairness in pretrained language models. (Section 1)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks) — *causes*
  - [Position: Political Neutrality in AI Is Impossible — But Here Is How to Approximate It](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fisher25a/fisher25a.pdf)

### Associated with
- **Societal bias** (constructs)
  - [CanLLMAgents Maintain a Persona in Discourse?](https://aclanthology.org/2025.emnlp-main.1488.pdf)
- **Hallucination** (behaviors tasks)
  - [NaturalBench: Evaluating Vision-Language Models on Natural Adversarial Samples](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e69ff56d0ebff0752ff29caaddc25dd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Stereotyping** (constructs)
  - [Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Harmlessness** (constructs)
  - [Chart2Code53: A Large-Scale Diverse and Complex Dataset for Enhancing Chart-to-Code Generation](https://aclanthology.org/2025.emnlp-main.800.pdf)
- **Trustworthiness** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Error handling** (constructs)
  > While our current focus is error mitigation, by adapting the target signal with labeled inputs, MERA could steer LMs toward diverse specialised objectives (e.g., harmlessness, honesty, and fairness etc). (Section 1).
  - [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf)
- **Text summarization** (behaviors tasks)
  - [VisBias: Measuring Explicit and Implicit Social Biases in Vision Language Models](https://aclanthology.org/2025.emnlp-main.909.pdf)
- **Factual grounding** (constructs)
  - [Enhancing Efficiency and Exploration in Reinforcement Learning forLLMs](https://aclanthology.org/2025.emnlp-main.76.pdf)
