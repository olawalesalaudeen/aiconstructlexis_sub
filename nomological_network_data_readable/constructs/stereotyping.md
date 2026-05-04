# Stereotyping
**Type:** Construct  
**Referenced in:** 26 papers  
**Also known as:** Stereotype bias, Gender stereotypical bias, Stereotypical association, Occupational gender bias, Stereotypical reasoning, Gender stereotypes, Gender bias, Stereotypes  

## State of the Field

Across the surveyed literature, "Stereotyping" is predominantly defined as a model's tendency to generate or rely on oversimplified and generalized beliefs about groups of people, with a recurring focus on gender. Many definitions describe this as associating specific occupations, roles, or characteristics with individuals based on their gender, such as models justifying behavior with statements like "'men should pay'" ("SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence"). A less common framing extends this concept to other demographic indicators like ethnicity and religion, as one study notes an LLM stereotyped "Chinatown and Little India as having higher crime rates" ("ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Thinking in Reasoning Models"). This construct is operationalized and measured through a wide array of benchmarks and tasks. The most frequently cited instruments are CrowS-Pairs and StereoSet, which are described as using "comparable methods for data gathering and bias measurement" ("UnderstandingLLMs’ Cross-Lingual Context Retrieval: How Good It Is And Where It Comes From"). Other benchmarks used to assess stereotyping include WinoBias, Winogender, BOLD, and BBQ. The construct is also observed in behaviors like coreference resolution, text generation, and machine translation, where systems may "consistently [translate] certain professions with specific genders" ("Africa Health Check: Probing Cultural Bias in MedicalLLMs"). Finally, stereotyping is studied in relation to broader concepts such as Fairness and Societal bias.

## Sources

**[ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Thinking in Reasoning Models](https://aclanthology.org/2025.emnlp-main.862.pdf)**
> The model's tendency to generate oversimplified and often inaccurate generalizations about groups of people, particularly based on demographic indicators like gender, ethnicity, or religion.

**[EMO: Embedding Model Distillation via Intra-Model Relation and Optimal Transport Alignments](https://aclanthology.org/2025.emnlp-main.386.pdf) (as "Stereotype bias")**
> The latent tendency of a model to systematically associate aesthetic judgments with demographic attributes such as gender, age, or education, even when image content is constant, reflecting inherited cognitive or societal priors.

**[UnderstandingLLMs’ Cross-Lingual Context Retrieval: How Good It Is And Where It Comes From](https://aclanthology.org/2025.emnlp-main.1162.pdf) (as "Gender stereotypical bias")**
> The tendency of a language model to associate certain characteristics, roles, or attributes with individuals based on their gender, reflecting and potentially amplifying societal stereotypes.

**[Africa Health Check: Probing Cultural Bias in MedicalLLMs](https://aclanthology.org/2025.emnlp-main.1640.pdf) (as "Occupational gender bias")**
> A model's systematic predisposition to associate specific occupations with particular genders, revealed through aggregated patterns in translation when the source text is gender-ambiguous.

**[Africa Health Check: Probing Cultural Bias in MedicalLLMs](https://aclanthology.org/2025.emnlp-main.1640.pdf) (as "Stereotypical association")**
> The tendency to link particular occupations with specific genders in ways that reflect social stereotypes rather than neutral interpretation.

**[Rapid Word Learning Through Meta In-Context Learning](https://aclanthology.org/2025.emnlp-main.1632.pdf) (as "Stereotypical reasoning")**
> The latent cognitive process by which a model preferentially selects responses that align with culturally ingrained stereotypes, particularly in gendered contexts.

**[2025.emnlp-main.1632.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1632.checklist.pdf) (as "Gender stereotypes")**
> A latent cognitive bias where a model holds oversimplified and generalized beliefs about the attributes, characteristics, or roles of individuals based on their gender.

**[SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.94.pdf) (as "Gender bias")**
> The tendency of a model to produce responses influenced by stereotypical gender roles rather than culturally appropriate norms, even when gender is irrelevant to the expected behavior.

**[SHARE: AnSLM-based Hierarchical ActionCorREction Assistant for Text-to-SQL](https://aclanthology.org/2025.acl-long.553.pdf) (as "Stereotypes")**
> The latent tendency to reproduce oversimplified and generalized beliefs about gender roles, characteristics, or abilities, such as assuming women are naturally suited for caregiving or men for leadership.

## Relationships

### Stereotyping →
- **CrowS-Pairs** (measurements) — *measured_by*
  - [ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
- **StereoSet** (measurements) — *measured_by*
  > Both datasets [StereoSet and CrowS-Pairs] emerged during a similar timeframe, focus on measuring stereotypical bias in language models, and use comparable methods for data gathering and bias measurement, making them ideal candidates for comparative analysis. (Section 3.1)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **WinoBias** (measurements) — *measured_by*
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **Winogender** (measurements) — *measured_by*
  - [SHARE: AnSLM-based Hierarchical ActionCorREction Assistant for Text-to-SQL](https://aclanthology.org/2025.acl-long.553.pdf)
- **DecodingTrust** (measurements) — *measured_by*
  - [ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **BOLD** (measurements) — *measured_by*
  - [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf)
- **BBQ** (measurements) — *measured_by*
  - [SHARE: AnSLM-based Hierarchical ActionCorREction Assistant for Text-to-SQL](https://aclanthology.org/2025.acl-long.553.pdf)

### Associated with
- **Text generation** (behaviors tasks)
  > Paper title: Job Unfair: An Investigation of Gender and Occupational Bias in Free-Form Text Completions by LLMs
  - [2025.emnlp-main.1159.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1159.checklist.pdf)
- **Coreference resolution** (behaviors tasks)
  > As noted by Davis and van Schijndel (2020), gender biases in neural models can be made visible in coreference resolution. (Section 4)
  - [A Comprehensive Framework to Operationalize Social Stereotypes for ResponsibleAIEvaluations](https://aclanthology.org/2025.emnlp-main.1527.pdf)
- **Fairness** (constructs)
  - [Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf)
- **Social bias** (constructs)
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Machine translation** (behaviors tasks)
  > Machine Translation systems have become indispensable tools for cross-linguistic communication, yet they frequently exhibit gender biases that reinforce societal stereotypes (Blodgett et al., 2020; Menis-Mastromichalakis et al., 2025). (Section 1)
  - [Africa Health Check: Probing Cultural Bias in MedicalLLMs](https://aclanthology.org/2025.emnlp-main.1640.pdf)
