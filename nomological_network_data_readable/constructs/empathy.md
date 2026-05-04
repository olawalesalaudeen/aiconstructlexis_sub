# Empathy
**Type:** Construct  
**Referenced in:** 25 papers  
**Also known as:** Emotional support, Empathic concern, Personal distress, Perspective-taking  

## State of the Field

Across the surveyed literature, empathy is most commonly defined as a model's tendency to exhibit emotion changes that align with human feelings in specific situations. However, definitions vary widely, with other work framing it as the ability to understand and share another's feelings, often within specific applications like therapeutic dialogue or providing advice that "resonates empathetically with the given situation" (TRANSIENTTABLES: EvaluatingLLMs’ Reasoning on Temporally Evolving Semi-structured Tables). Some definitions highlight cognitive components like "perspective-taking," while others focus on affective outputs such as providing "emotional support" and compassion. One paper explicitly notes this definitional diversity, stating that "Conceptual operationalizations of empathy in NLP are varied" and can be broken down into facets like "empathic concern" and "personal distress" (OntologyRAG-Q: Resource Development and Benchmarking for Retrieval-Augmented Question Answering in Qur’anic Tafsir). To measure this construct, researchers operationalize empathy using both automated and human-centric methods. The provided papers show that empathy is evaluated using "LLM-as-a-judge" protocols, including G-Eval, as well as through "Human evaluation" by experts. Empathy is also studied in relation to other constructs, with one paper identifying it as a "main factor" for "Helpfulness."

## Sources

**[Apathetic or Empathetic? Evaluating LLMs' Emotional Alignments with Humans](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0049c3f9c53fb06f674ae66c2cf2376-Paper-Conference.pdf)**
> The tendency of a model to exhibit emotion changes that match the feelings humans would experience in specific situations.

**[SDPO: Segment-Level Direct Preference Optimization for Social Agents](https://aclanthology.org/2025.acl-long.608.pdf) (as "Emotional support")**
> The ability to provide comfort, encouragement, and understanding to a user experiencing emotional distress.

**[OntologyRAG-Q: Resource Development and Benchmarking for Retrieval-Augmented Question Answering in Qur’anic Tafsir](https://aclanthology.org/2025.emnlp-main.785.pdf) (as "Empathic concern")**
> A component of empathy characterized by other-oriented feelings of sympathy and compassion for a person in distress.

**[OntologyRAG-Q: Resource Development and Benchmarking for Retrieval-Augmented Question Answering in Qur’anic Tafsir](https://aclanthology.org/2025.emnlp-main.785.pdf) (as "Personal distress")**
> A component of empathy characterized by self-oriented, aversive feelings in response to another's suffering.

**[Merger-as-a-Stealer: Stealing TargetedPIIfrom AlignedLLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.296.pdf) (as "Perspective-taking")**
> The cognitive ability to understand a situation from an alternative point of view, which is critical for interpreting complex toxic language involving sarcasm or adopted personas.

## Relationships

### Empathy →
- **LLM-as-a-judge** (measurements) — *measured_by*
  > We adopt a three-dimensional scoring system for AI therapists, evaluating them on empathy, logical coherence, and guidance. (Section 4.2)
  - [Analyzing (In)Abilities ofSAEs via Formal Languages](https://aclanthology.org/2025.naacl-long.250.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > Expert Evaluation: Five psychologists evaluated responses generated for 100 videos using a 1-to-5 Likert scale (1 = poor, 5 = exceptional). We utilized the same 3 aforementioned criteria. (Section 5)
  - [Controlled Generation for Private Synthetic Text](https://aclanthology.org/2025.emnlp-main.1664.pdf)
- **G-Eval** (measurements) — *measured_by*
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.652.pdf)

### Associated with
- **Helpfulness** (constructs)
  > Wang and Torres (2022) collected helpful and unhelpful advice from Reddit and analyzed that the main factor is ‘empathy’, consistent with our findings in Figure 4. (Section 2)
  - [TRANSIENTTABLES: EvaluatingLLMs’ Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.333.pdf)
