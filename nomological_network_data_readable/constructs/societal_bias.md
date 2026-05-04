# Societal bias
**Type:** Construct  
**Referenced in:** 17 papers  
**Also known as:** Cultural bias, Demographic bias, English-centric bias, Gender bias, Implicit demographic bias, Intergroup empathy bias, Intersectional bias, Religious bias, Sexual orientation bias, Stereotype bias  

## State of the Field

Across the surveyed literature, societal bias is predominantly framed as a latent tendency for models to reproduce skewed, stereotypical, or harmful representations of social and demographic groups, a phenomenon most definitions attribute to prejudices within the training data. The concept is multifaceted, with papers specifying various forms such as demographic, stereotype, gender, cultural, and intersectional bias. The source of this bias is consistently linked to imbalances in training corpora, such as the overrepresentation of English content causing an "English-centric bias," or, as one paper notes, models acting as "'time capsules,' capturing and reflecting evolving societal biases present in literature" (MergeME: Model Merging Techniques for Homogeneous and HeterogeneousMoEs). Operationally, this construct is measured by observing systematic variations in model outputs across different social attributes; for instance, one study on "implicit demographic bias" identified a "'default persona' bias toward middle-aged, able-bodied, native-born, Caucasian, atheistic males" (ACCESS: A Benchmark for Abstract Causal Event Discovery and Reasoning). Another common operationalization involves calculating the frequency with which a model agrees with stereotypical statements. A wide array of measurement instruments are used to assess this construct, with BBQ and CrowS-Pairs appearing most frequently in this dataset, followed by StereoSet and WinoBias. Other cited benchmarks include BIG-Bench, BOLD, and GlobalOpinionQA. Societal bias is frequently studied alongside related constructs such as fairness, harmlessness, and cultural understanding.

## Sources

**[ACCESS: A Benchmark for Abstract Causal Event Discovery and Reasoning](https://aclanthology.org/2025.naacl-long.50.pdf) (as "Implicit demographic bias")**
> The degree to which an LLM's responses vary systematically across demographic identities in ways that reflect unconscious societal biases, inferred from variability in semantic content and response quality.

**[Mixture of Multimodal Adapters for Sentiment Analysis](https://aclanthology.org/2025.naacl-long.91.pdf) (as "Demographic bias")**
> A latent tendency of the model to generate outputs that favor or disfavor individuals based on demographic attributes such as gender, race, age, or socioeconomic status, reflecting underlying societal stereotypes or imbalances in training data.

**[Mixture of Multimodal Adapters for Sentiment Analysis](https://aclanthology.org/2025.naacl-long.91.pdf) (as "Stereotype bias")**
> The latent tendency of the model to agree with or reproduce socially harmful stereotypes related to protected attributes such as gender, race, religion, or disability, even when not explicitly prompted.

**[MergeME: Model Merging Techniques for Homogeneous and HeterogeneousMoEs](https://aclanthology.org/2025.naacl-long.118.pdf) (as "Gender bias")**
> The latent tendency of a model to systematically associate clinical reasoning or language use with gendered stereotypes, independent of clinical relevance.

**[MergeME: Model Merging Techniques for Homogeneous and HeterogeneousMoEs](https://aclanthology.org/2025.naacl-long.118.pdf)**
> The latent tendency of a model to reproduce skewed representations of demographic groups that reflect historical or cultural prejudices present in its training data.

**[MergeME: Model Merging Techniques for Homogeneous and HeterogeneousMoEs](https://aclanthology.org/2025.naacl-long.118.pdf) (as "Sexual orientation bias")**
> A latent, systematic skew in the model's representations related to sexual orientation, influencing its portrayal of different relationship types and identities.

**[MergeME: Model Merging Techniques for Homogeneous and HeterogeneousMoEs](https://aclanthology.org/2025.naacl-long.118.pdf) (as "Religious bias")**
> A latent, systematic skew in the model's representations related to religion, influencing its association of religious groups with positive or negative actions and stereotypes.

**[DreamSync: Aligning Text-to-Image Generation with Image Understanding Feedback](https://aclanthology.org/2025.naacl-long.305.pdf) (as "Social bias")**
> A tendency for model outputs to vary systematically with social attributes in ways that can produce harmful or stereotypical differences across groups.

**[DreamSync: Aligning Text-to-Image Generation with Image Understanding Feedback](https://aclanthology.org/2025.naacl-long.305.pdf) (as "Intersectional bias")**
> A form of social bias that arises from the interaction of multiple social attributes, such as the combination of race and gender or physical characteristics and gender.

**[Grammar Control in Dialogue Response Generation for Language Learning Chatbots](https://aclanthology.org/2025.naacl-long.496.pdf) (as "Cultural bias")**
> The tendency of a model to favor certain cultural perspectives—particularly Western ones—over others, reflecting an imbalance in cultural representation and understanding.

**[Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf) (as "English-centric bias")**
> A model's disposition to perform better on English tasks and contexts due to being trained on disproportionately English-dominated datasets.

**[ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.611.pdf) (as "Intergroup empathy bias")**
> The latent tendency to empathize less with out-group members relative to in-group members, which is inferred from differences in predicted emotion intensity.

## Relationships

### Societal bias →
- **CrowS-Pairs** (measurements) — *measured_by*
  - [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BIG-Bench** (measurements) — *measured_by*
  - [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BBQ** (measurements) — *measured_by*
  - [Friend or Foe? A Computational Investigation of Semantic FalseFriends acrossRomance Languages](https://aclanthology.org/2025.emnlp-main.774.pdf)
- **GlobalOpinionQA** (measurements) — *measured_by*
  > GlobalOpinionQA (Durmus et al., 2024) uses multiple-choice questions to assess the opinions stated by a model relative to aggregated population opinions from different countries. The goal is to identify model bias in representing diverse viewpoints. (Section 3)
  - [Mixture of Multimodal Adapters for Sentiment Analysis](https://aclanthology.org/2025.naacl-long.91.pdf)
- **CoBia** (measurements) — *measured_by*
  - [Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.84.pdf)
- **BOLD** (measurements) — *measured_by*
  - [Friend or Foe? A Computational Investigation of Semantic FalseFriends acrossRomance Languages](https://aclanthology.org/2025.emnlp-main.774.pdf)

### Associated with
- **Fairness** (constructs)
  - [CanLLMAgents Maintain a Persona in Discourse?](https://aclanthology.org/2025.emnlp-main.1488.pdf)
- **Cultural understanding** (constructs)
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
- **Multilingual ability** (constructs)
  - [Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf)
