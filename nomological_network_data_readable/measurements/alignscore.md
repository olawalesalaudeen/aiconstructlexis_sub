# AlignScore
**Type:** Measurement  
**Referenced in:** 15 papers  
**Also known as:** ALIGNSCORE  

## State of the Field

Across the surveyed literature, AlignScore is predominantly described as a model-based evaluation procedure for assessing text alignment between a generated text and a source passage. It is frequently used to operationalize and measure constructs like `Faithfulness` and, most commonly, "factual consistency" in the context of behaviors like `Text summarization` and `Paraphrase generation`. Several sources specify its underlying mechanism, describing it as an NLI-based or "trained entailment metric" that is based on a fine-tuned RoBERTa-large model. This procedure yields a continuous score, typically from 0 to 1, indicating the degree of correspondence or entailment. While the most prevalent usage is as an evaluation metric, a smaller line of work also employs AlignScore as a "verifier model" in fact-checking or as a quality filter, for instance by accepting only generations with a score above a certain threshold. The definitions are largely consistent, with the most common one being a general text-alignment procedure, while a few papers offer a more specific framing of it as an NLI-based metric for summarization.

## Sources

**[A Picture is Worth A Thousand Numbers: EnablingLLMs Reason about Time Series via Visualization](https://aclanthology.org/2025.naacl-long.384.pdf)**
> A model-based text-alignment evaluation procedure used to assess how well generated answers align with reference passages.

**[COVE:COntext andVEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.103.pdf) (as "ALIGNSCORE")**
> An NLI-based metric that computes an aggregated inference score between a source article and a generated summary to evaluate factual consistency.

## Relationships

### → AlignScore
- **Factuality** (constructs) — *measured_by*
  - [Ethical Concern Identification inNLP: A Corpus ofACLAnthology Ethics Statements](https://aclanthology.org/2025.naacl-long.581.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [SafeKey: Amplifying Aha-Moment Insights for Safety Reasoning](https://aclanthology.org/2025.emnlp-main.1292.pdf)
- **Paraphrase generation** (behaviors tasks) — *measured_by*
  > • Consistency →AlignScore (Zha et al., 2023) : the authors train a information alignment model on 7 well-established tasks including paraphrasing and summarization. (Section 3.2)
  - [A Picture is Worth A Thousand Numbers: EnablingLLMs Reason about Time Series via Visualization](https://aclanthology.org/2025.naacl-long.384.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [A Picture is Worth A Thousand Numbers: EnablingLLMs Reason about Time Series via Visualization](https://aclanthology.org/2025.naacl-long.384.pdf)
