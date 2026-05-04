# Social bias
**Type:** Construct  
**Referenced in:** 134 papers  
**Also known as:** Stereotypical bias, User name bias, Western bias, Ethical bias, Cultural bias, Bias, Gender bias, Diversity bias, Implicit bias, Political stereotyping, Gender-occupation bias, Omnivore bias, Explicit bias, Culture bias, Disability bias, Demographic bias, Bias against marginalized genders, Stereotype bias  

## State of the Field

Across the surveyed literature, social bias is most commonly defined as the tendency for model outputs to reflect, perpetuate, or amplify problematic societal prejudices and stereotypes, leading to disparate treatment between social groups. This general concept is frequently specified into more granular forms, including stereotypical, demographic, cultural, political, and gender-occupation biases, with a few papers also identifying unique types such as "omnivore bias" or "user name bias." The source of this behavior is consistently attributed to problematic content within training data, which models are reported to not only mimic but also amplify. The field operationalizes and measures social bias through a variety of benchmarks, with WinoBias being frequently used for gender-occupation stereotypes, StereoSet for associations across race and religion, and BBQ for biases in question-answering contexts. Other instruments cited include BOLD for gender bias, AccessEval for disability bias, and both A-OKVQA and CVQA for measuring "Western bias" in visual understanding tasks. Some studies observe specific failure modes, such as LLM-judges exhibiting "powerful implicit biases, prioritizing style over factuality and safety." Social bias is studied alongside concepts like faithfulness and cultural alignment, and one paper reports that aligning models with human preferences can increase stereotypical bias. While most definitions center on societal harms, a less common framing defines bias more technically as the "deviation of a model's output distribution from a desired target distribution."

## Sources

**[More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf) (as "Stereotypical bias")**
> The model's tendency to generate or agree with over-generalized, disrespectful, or negative beliefs about particular demographic groups.

**[See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf) (as "Western bias")**
> A performance disparity where a vision-language model performs better on tasks involving images and annotations from Western cultures compared to those from East Asian cultures.

**[First-Person Fairness in Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/92af0c8c2664429de2bb44c2692d84ae-Paper-Conference.pdf) (as "User name bias")**
> Differences in chatbot responses that arise from the stored user's name and the demographic information associated with that name.

**[Language Model Alignment in Multilingual Trolley Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f32be3e112e151707cb12528bdfa7d5-Paper-Conference.pdf) (as "Ethical bias")**
> Systematic deviations in moral judgment that may be influenced by factors such as language or culture.

**[CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)**
> Disparate treatments between social groups exhibited by model outputs, often stemming from stereotypes encoded in training data.

**[Attributing Culture-Conditioned Generations to Pretraining Corpora](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4546b4f9e1a44ed15c253dd43307dd5-Paper-Conference.pdf) (as "Cultural bias")**
> A tendency for model generations to reflect uneven or stereotyped cultural associations, especially favoring some cultures or culturally salient symbols over others.

**[UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf) (as "Political bias")**
> The tendency of a language model to generate text that reflects a specific political leaning or viewpoint, which the paper suggests may be linked to toxicity.

**[Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf) (as "Bias")**
> The tendency of a model to produce outputs that reflect or amplify problematic societal prejudices.

**[Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf) (as "Gender bias")**
> A specific form of bias where a model's outputs systematically disadvantage or misrepresent individuals based on their gender.

**[Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf) (as "Diversity bias")**
> A tendency for an LLM judge to respond differently when demographic identity information is introduced into the content.

**[Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf) (as "Implicit bias")**
> An LLM-judge's internal, unstated preference for certain criteria over others, which influences its decisions independently of or in violation of explicit instructions.

**[CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf) (as "Stereotyping")**
> The model's propensity to associate social groups with inaccurate, oversimplified, or potentially negative generalizations.

**[Examining Alignment of Large Language Models through Representative Heuristics: the case of political stereotypes](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d53575463291ea6b5a23cf6e571f59b-Paper-Conference.pdf) (as "Political stereotyping")**
> A form of misalignment where a model generates exaggerated judgments or beliefs about political parties, often by overemphasizing characteristics associated with them.

**[What can large language models do for sustainable food?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25a/thomas25a.pdf) (as "Omnivore bias")**
> A systematic tendency for the model to favor non-vegetarian options or model preferences for them more accurately than for vegetarian options.

**[Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf) (as "Gender-occupation bias")**
> A specific form of social bias where a model systematically associates certain occupations with particular genders, often reflecting societal stereotypes.

**[Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf) (as "Explicit bias")**
> Bias that is relatively controllable and directly reportable, typically captured with direct measures.

**[Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.84.pdf) (as "Societal bias")**
> The latent tendency of an LLM to express or amplify stereotypical, demeaning, or dehumanizing associations about social groups based on attributes such as race, gender, religion, or nationality, even when safety mechanisms are in place.

**[2025.emnlp-main.1246.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1246.checklist.pdf) (as "Culture bias")**
> The latent tendency of a model to exhibit stronger implicit associations between certain cultural groups and stereotypical attributes, reflecting societal biases present in training data.

**[Crisp: Cognitive Restructuring of Negative Thoughts through Multi-turn Supportive Dialogues](https://aclanthology.org/2025.emnlp-main.1653.pdf) (as "Disability bias")**
> A latent tendency of LLMs to generate systematically less favorable, less accurate, or more stereotypical responses when queries reference disability, reflecting embedded ableist patterns in model behavior.

**[Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Demographic bias")**
> The latent tendency of a model to reflect societal or data-driven prejudices regarding demographic groups in its outputs.

**[SHARE: AnSLM-based Hierarchical ActionCorREction Assistant for Text-to-SQL](https://aclanthology.org/2025.acl-long.553.pdf) (as "Bias against marginalized genders")**
> The latent tendency to generate content that perpetuates disparities or harms against non-dominant gender identities, particularly within the LGBTQ+ community, such as denying their legitimacy or associating them with deviance.

**[ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf) (as "Stereotype bias")**
> The latent disposition of a model to generate content that perpetuates or reinforces stereotypes related to demographic factors such as race, gender, or age.

## Relationships

### Social bias →
- **BBQ** (measurements) — *measured_by*
  > Differently, BBQ (Parrish et al., 2022) focuses on identifying biases within question-answering contexts.
  - [A Theoretical Understanding of Self-Correction through In-context Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/a399456a191ca36c7c78dff367887f0a-Paper-Conference.pdf)
- **WinoBias** (measurements) — *measured_by*
  > As typical examples, WinoBias (Zhao et al., 2018) measures the gender bias in language models by identifying the dependency between output words and social groups, where such bias is further mitigated with word-embedding debiasing techniques (Bolukbasi et al., 2016).
  - [Prompting Fairness: Integrating Causality to Debias Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f26a2d143a227376dff99a279f93f99-Paper-Conference.pdf)
- **StereoSet** (measurements) — *measured_by*
  > We train the BiasUnlearn model on the StereoSet dataset, which is a large-scale dataset used to measure stereotypes in four domains: gender, profession, race, and religion.
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
- **BOLD** (measurements) — *measured_by*
  > Additionally, we further conducted an experiment where we use the BOLD dataset to analyze LM gender bias, results are shown in appendix Table 13. (Section 4.4)
  - [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  > “To measure Western bias in question answering, we use A-OKVQA and CVQA (Schwenk et al., 2022; Romero et al., 2024).”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **CVQA** (measurements) — *measured_by*
  > “To measure Western bias in question answering, we use A-OKVQA and CVQA (Schwenk et al., 2022; Romero et al., 2024).”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **CrowS-Pairs** (measurements) — *measured_by*
  - [TaCoMoE](https://aclanthology.org/2025.emnlp-main.208.pdf)
- **Winogender** (measurements) — *measured_by*
  - [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  - [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf)
- **AccessEval** (measurements) — *measured_by*
  > "we introduce AccessEval (Accessibility Evaluation), a benchmark evaluating 21 closed- and open-source LLMs across 6 real-world domains and 9 disability types using paired Neutral and Disability-Aware Queries."
  - [Crisp: Cognitive Restructuring of Negative Thoughts through Multi-turn Supportive Dialogues](https://aclanthology.org/2025.emnlp-main.1653.pdf)
- **Word association test** (measurements) — *measured_by*
  - [2025.emnlp-main.1246.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1246.checklist.pdf)
- **HESEIA** (measurements) — *measured_by*
  - [2025.emnlp-main.1275.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1275.checklist.pdf)

### → Social bias
- **Human preference alignment** (constructs) — *causes*
  > the effects on other trustworthiness aspects are negative: stereotypical bias increases by 150%... (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)

### Associated with
- **Trustworthiness** (constructs)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Stereotyping** (constructs)
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Harmlessness** (constructs)
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Visual understanding** (constructs)
  > In this work, we characterize the Western bias of VLMs in image understanding and investigate the role that language plays in this disparity. (Section 1)
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **Cultural alignment** (constructs)
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **Preference prediction** (behaviors tasks)
  > Within the vegetarian vs. non-vegetarian meal comparisons, accuracy is lower when vegetarian options are rated higher, reflecting LLMs’ omnivore bias, as LLMs more frequently prefer non-vegetarian options compared to ground truth human preferences. (Section 5.4)
  - [What can large language models do for sustainable food?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25a/thomas25a.pdf)
