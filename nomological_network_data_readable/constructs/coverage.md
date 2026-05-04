# Coverage
**Type:** Construct  
**Referenced in:** 12 papers  

## State of the Field

Across the provided literature, 'Coverage' is a multifaceted construct with several distinct definitions, most of which relate to some form of representativeness. The most frequently cited definition frames it as a statistical property of a language model, specifically measuring the probability mass it assigns to the optimal or arg-max response for a given prompt. Other work defines it more contextually, such as the extent to which offline preference data represents a policy's support in reinforcement learning, or the degree to which a condensed dataset includes "diverse and previously underrepresented patterns" from an original dataset. A separate line of work treats it as a quality of information extraction, referring to the capture of all verifiable information from a source text. The construct is operationalized and measured through several methods, most commonly `Human evaluation`, where annotators may rate whether a response "comprehensively addresses all components of questions asked" or count the number of source references covered. Papers also report using `Human annotation study` and `LLM-based evaluation` to measure it, and the construct is studied in relation to `Reward overoptimization`.

## Sources

**[Self-Improvement in Language Models: The Sharpening Mechanism](https://proceedings.iclr.cc/paper_files/paper/2025/file/bee8c2bc757f6bbc3efd7cf1b979f0c9-Paper-Conference.pdf)**
> A statistical property of a base model measuring how much probability mass it assigns to the optimal or arg-max response for a given prompt, on average.

## Relationships

### Coverage →
- **Human evaluation** (measurements) — *measured_by*
  > After each conversation, participants rate the model’s responses on a 5-point scale ... across five criteria ...: (4) Coverage: Response comprehensively addresses all components of questions asked, including sub-questions. (Section 3.2.3)
  - [TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Human annotation study** (measurements) — *measured_by*
  - [PIC: Unlocking Long-Form Text Generation Capabilities of Large Language Models via PositionIDCompression](https://aclanthology.org/2025.acl-long.348.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [Introducing Spotlight: A Novel Approach for Generating Captivating Key Information from Documents](https://aclanthology.org/2025.emnlp-main.1797.pdf)

### Associated with
- **Reward overoptimization** (constructs)
  - [Correcting the Mythos of KL-Regularization: Direct Alignment without Overoptimization via Chi-Squared Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e785d64baa2cde06c69d9b7a14636ef2-Paper-Conference.pdf)
