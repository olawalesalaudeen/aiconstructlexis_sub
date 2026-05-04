# Cultural knowledge
**Type:** Construct  
**Referenced in:** 15 papers  
**Also known as:** Understanding of Indian culture  

## State of the Field

Across the surveyed literature, "Cultural knowledge" is most commonly framed as a latent construct representing an LLM's internalized understanding of cultural norms, values, and practices. This broad definition is specified in various ways, with papers detailing knowledge of cultural artifacts like food and art, as well as societal norms, historical context, and legal frameworks. While some work treats this as a global capability, other studies focus on knowledge specific to certain regions, such as Indian, Korean, or Filipino cultures. The construct is operationalized and measured through several instruments; papers report using benchmarks like INCLUDE and Candle, as well as human evaluation, to assess it. For instance, one study notes that a portion of the KMMLU benchmark "require[s] knowledge of Korean culture for accurate resolution" (Mutual-pairing Data Augmentation for Fewshot Continual Relation Extraction). A minority perspective distinguishes this from "meta-cultural competence," arguing that current tests only show knowledge of specific cultures rather than a general ability to operate in new ones (Sneaking Syntax into Transformer Language Models with Tree Regularization). Finally, cultural knowledge is reported by one paper to influence harmful content detection.

## Sources

**[Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf)**
> The latent trait reflecting an LLM's internalized understanding of cultural norms, values, and practices, which may be accessed when contextual cues such as country or value are provided.

**[2025.emnlp-main.68.checklist](https://aclanthology.org/attachments/2025.emnlp-main.68.checklist.pdf) (as "Understanding of Indian culture")**
> The latent ability of a language model to comprehend culturally grounded content, references, and phenomena related to India across evaluation settings.

## Relationships

### Cultural knowledge →
- **Harmful content detection** (behaviors tasks) — *causes*
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)
- **INCLUDE** (measurements) — *measured_by*
  - [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf)
- **Candle** (measurements) — *measured_by*
  > Fine-tuning with CULTUREINSTRUCT outperforms the base LLMs significantly on multiple types of cultural benchmarks, including: (i) benchmarks for general cultural knowledge - CULTURALBENCH (Chiu et al., 2024), CANDLE (Nguyen et al., 2023), and ETICOR (Dwivedi et al., 2023) (Section 4.1)
  - [ManaTTSPersian: a recipe for creatingTTSdatasets for lower resource languages](https://aclanthology.org/2025.naacl-long.465.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > For the evaluator M (·) used to compute MES, we utilize GPT-4o (OpenAI et al., 2024) as a simulated evaluator and recruit real human evaluators from Prolific.
  - [Grammar Control in Dialogue Response Generation for Language Learning Chatbots](https://aclanthology.org/2025.naacl-long.496.pdf)
