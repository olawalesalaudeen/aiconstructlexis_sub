# Completeness
**Type:** Construct  
**Referenced in:** 25 papers  
**Also known as:** Response informativeness, Information coverage  

## State of the Field

The most prevalent definition of completeness, found across a majority of the provided papers, describes it as the extent to which a model's output includes all valid items satisfying given constraints, without omitting valid solutions. This core idea of avoiding omissions is applied in various contexts; for instance, some work describes it as providing "in-depth and in-breadth information" to address an instruction, while other research frames it as including all "key-facts" in a summary. Related framings include "Response informativeness," which refers to a RAG generator's ability to "fully utilize valuable information from retrieved documents," and "Information coverage," the ability to capture all relevant facts from a source text. A distinct, less frequent usage appears in the context of reasoning systems, where completeness is the property of being able to "find a valid proof whenever one exists." To operationalize this construct, researchers employ several measurement approaches. Completeness is frequently measured using Human evaluation, where raters score outputs on scales, as well as through automated instruments like FLASK and G-Eval. One paper quantifies it as "the fraction of ground truth answers that have such an approximate match" (KITAB). The construct is also studied in relation to behaviors such as Question answering.

## Sources

**[FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)**
> The extent to which the model retrieves all and only the items that satisfy the given constraints, without omitting valid solutions.

**[KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.459.pdf) (as "Response informativeness")**
> The latent ability of a RAG generator to fully utilize valuable information from retrieved documents to produce complete and correct answers.

**[MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning](https://aclanthology.org/2025.acl-long.1460.pdf) (as "Information coverage")**
> The ability of a model to capture and represent all relevant claims and facts from a source text in its generated output.

## Relationships

### Completeness →
- **FLASK** (measurements) — *measured_by*
  > Additionally, MoA also outperforms GPT-4 Omni in terms of insightfulness, correctness, factuality, completeness, and metacognition.
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > Each sample was scored on a 0–10 scale for: completeness (whether it covered all clinically relevant considerations), correctness (factual accuracy of reasoning and answers), and logical flow (coherence and structure of the reasoning path). (Section 5.2.1)
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **G-Eval** (measurements) — *measured_by*
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)

### Associated with
- **Question answering** (behaviors tasks)
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
