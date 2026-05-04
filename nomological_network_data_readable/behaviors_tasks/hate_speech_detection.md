# Hate speech detection
**Type:** Behavior  
**Referenced in:** 25 papers  
**Also known as:** Sexism detection, Hate type classification, Toxicity detection, Implicit hate speech classification, Hate speech recognition, Misogyny intensity detection, Offensive language detection, Toxicity classification, Antisemitism detection  

## State of the Field

Across the surveyed literature, hate speech detection is most commonly defined as the task of identifying and classifying text that expresses hatred or promotes violence towards individuals or groups. This behavior is also framed more broadly as "Toxicity detection," which targets rude or disrespectful content, or "Offensive language detection," which includes personal attacks and bullying. A number of papers focus on more specific subtypes, such as "Sexism detection," "Antisemitism detection," and "Misogyny intensity detection," with the latter sometimes involving the assessment of multimodal content like memes. The task's operationalization varies in granularity, from a binary classification of content as hateful or not, to a more detailed "Hate type classification" that assigns text to predefined categories like "dehumanization, derogation, animosity, threatening, and support." A recurring challenge noted in the literature is identifying subtle or indirect expressions, which is the focus of "Implicit hate speech classification" and is exemplified by the mention of "dog whistles" in one study (P2Law: Scaling Law for Post-Training After Model Pruning). To measure this behavior, researchers use benchmarks such as ToxiGen and Hateful Memes. The task is frequently situated within the broader application of "online content moderation," as noted in "Transplant Then Regenerate: A New Paradigm for Text Data Augmentation."

## Sources

**[P2Law: Scaling Law for Post-Training After Model Pruning](https://aclanthology.org/2025.acl-long.284.pdf)**
> The observable task of identifying and classifying text that expresses hatred or promotes violence towards individuals or groups based on certain characteristics.

**[Hierarchical Memory Organization forWikipedia Generation](https://aclanthology.org/2025.acl-long.1424.pdf) (as "Sexism detection")**
> Identifying language that expresses or implies discrimination based on sex, particularly in online discourse, by recognizing hostile or stereotypical content.

**[M-Wanda: Improving One-Shot Pruning for MultilingualLLMs](https://aclanthology.org/2025.emnlp-main.1370.pdf) (as "Hate type classification")**
> Assigning a text to one of several predefined hate categories, including dehumanization, derogation, animosity, threatening, and support.

**[Aspect-Oriented Summarization for Psychiatric Short-Term Readmission Prediction](https://aclanthology.org/2025.emnlp-main.1424.pdf) (as "Toxicity detection")**
> The task of identifying and classifying text that is rude, disrespectful, or likely to make someone leave a discussion.

**[Instructing Large Language Models for Low-Resource Languages: A Systematic Study forBasque](https://aclanthology.org/2025.emnlp-main.1485.pdf) (as "Implicit hate speech classification")**
> The task of classifying text containing different forms of implicit hate speech, which requires understanding subtle or indirect cues.

**[CanLLMAgents Maintain a Persona in Discourse?](https://aclanthology.org/2025.emnlp-main.1488.pdf) (as "Hate speech recognition")**
> The task of classifying a given text, such as a tweet, as containing hate speech or not.

**[ToM: Leveraging Tree-orientedMapReduce for Long-Context Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.900.pdf) (as "Misogyny intensity detection")**
> The task of assessing and assigning a level of intensity (e.g., low, moderate, high) to the misogynistic content within a meme.

**[MiLQ: BenchmarkingIRModels for Bilingual Web Search with Mixed Language Queries](https://aclanthology.org/2025.emnlp-main.1154.pdf) (as "Offensive language detection")**
> The task of identifying and classifying text content as offensive, including expressions like hate speech, personal attacks, and online bullying.

**[Current Semantic-change Quantification Methods Struggle with Discovery in the Wild](https://aclanthology.org/2025.emnlp-main.1792.pdf) (as "Antisemitism detection")**
> Classifying social media posts as antisemitic or not based on the IHRA definition, producing a label (Yes/No) and supporting rationale.

**[Unconditional Truthfulness: Learning Unconditional Uncertainty of Large Language Models](https://aclanthology.org/2025.emnlp-main.1808.pdf) (as "Toxicity classification")**
> The task of identifying and categorizing text as toxic or non-toxic at the sentence or token level.

## Relationships

### Hate speech detection →
- **ToxiGen** (measurements) — *measured_by*
  - [ImpScore: A Learnable Metric For Quantifying The Implicitness Level of Sentences](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd6bb13e78da078d8adcabbe6d9ca737-Paper-Conference.pdf)
- **Hateful Memes** (measurements) — *measured_by*
  - [VeriLocc: End-to-End Cross-Architecture Register Allocation viaLLM](https://aclanthology.org/2025.emnlp-main.1539.pdf)

### Associated with
- **Content moderation** (behaviors tasks)
  - [CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf)
- **COLD** (measurements)
  > Recent datasets such as ToxiCN (Lu et al., 2023), COLD (Deng et al., 2022), Cdial-bias (Zhou et al., 2022), SWSR (Jiang et al., 2022), and SCCD (Yang et al., 2025b) support toxicity classification but do not provide sentiment-preserving rewrites. (Section 1)
  - [Unconditional Truthfulness: Learning Unconditional Uncertainty of Large Language Models](https://aclanthology.org/2025.emnlp-main.1808.pdf)
