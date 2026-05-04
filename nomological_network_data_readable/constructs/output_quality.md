# Output quality
**Type:** Construct  
**Referenced in:** 7 papers  
**Also known as:** Overall quality, Content quality  

## State of the Field

Across the provided literature, Output quality is consistently framed as a holistic, latent construct representing the overall effectiveness of a model's generated text. While some definitions describe it broadly in terms of correctness and coherence, others specify more granular criteria such as structure, relevance, coverage, and logical linkage. A recurring theme is the difficulty of direct assessment, with one paper noting that "Quantitatively assessing output quality is challenging" ("PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance"). Consequently, the construct is operationalized through a wide array of proxy methods. The most prevalent approaches involve using other models for evaluation, as seen with `LLM-as-a-judge`, reward models like `ArmoRM`, and automated benchmarks including `AlpacaEval`, `MT-Bench`, and `Arena-Hard`. Additionally, it is measured through performance on standard question-answering and reasoning benchmarks like `MMLU`, `BoolQ`, and `PIQA`, as well as through `Human evaluation` and automated metrics like `BARTScore`. The construct is studied alongside `Faithfulness` and `Commonsense knowledge`, and several papers report that it is influenced by methods such as `Chain-of-thought reasoning` and `Best-of-N`.

## Sources

**[UTBoost: Rigorous Evaluation of Coding Agents onSWE-Bench](https://aclanthology.org/2025.acl-long.190.pdf) (as "Overall quality")**
> A holistic latent trait reflecting the combined effectiveness of a model in generating patent claims that meet professional standards across multiple evaluation dimensions.

**[Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home](https://aclanthology.org/2025.acl-long.320.pdf) (as "Response quality")**
> The latent property of a model's generated responses reflecting their correctness, coherence, and alignment with high-quality expectations, as judged by external evaluators or reward models.

**[PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance](https://aclanthology.org/2025.acl-long.519.pdf)**
> The latent quality of a model's generated text, which is challenging to assess directly and is instead measured using proxy methods like reward models.

**[KokoroChat: AJapanese Psychological Counseling Dialogue Dataset Collected via Role-Playing by Trained Counselors](https://aclanthology.org/2025.acl-long.609.pdf) (as "Content quality")**
> The overall quality of the generated survey's text, assessed on its structure, relevance to the topic, and comprehensive coverage of key information.

## Relationships

### Output quality →
- **LLM-as-a-judge** (measurements) — *measured_by*
  > Response Quality : We measure the quality of Ri given Ii. First, we use LLM-as-a-Judge where we prompt an LM to return a discrete score between 1 and 5 that represents the quality of Ri. (Section 5.2)
  - [LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/59f278de1619bdb6b53fd04e8e0976e0-Paper-Conference.pdf)
