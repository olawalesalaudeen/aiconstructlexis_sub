# BARTScore
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** BART Score  

## State of the Field

Across the provided literature, BARTScore is predominantly characterized as a model-based evaluation metric used to assess the quality of generated text. Its core mechanism, as described in multiple papers, involves leveraging a pre-trained BART model to calculate a score based on generation probability, such as the conditional or average likelihood of the output text. The most common application described is as an automated procedure for comparing generated chain-of-thought rationales against "manually created golden references." Papers use BARTScore to operationalize several constructs, including general `Output quality`, `Faithfulness`, and `Coherence`, with one study using it to measure "semantic coherence" in argument structures. It is applied to evaluate tasks such as `Text summarization` and question answering. While most sources treat it as a reference-based metric, one paper notes its use "without human annotations," and another describes its function as providing "pseudo ground-truth" for output quality. In evaluation contexts, BARTScore is frequently studied alongside other metrics like BERTScore, BLEURT, and human judgments.

## Sources

**[A Picture is Worth A Thousand Numbers: EnablingLLMs Reason about Time Series via Visualization](https://aclanthology.org/2025.naacl-long.384.pdf)**
> An automated evaluation procedure used to compare generated chain-of-thought rationales against manually created golden references.

**[TokenSkip: Controllable Chain-of-Thought Compression inLLMs](https://aclanthology.org/2025.emnlp-main.166.pdf) (as "BART Score")**
> A reference-based metric that uses the probability assigned by a BART model to the output given the input as a proxy for quality, used here as pseudo ground-truth for summarization and QA.

## Relationships

### → BARTScore
- **Response quality** (constructs) — *measured_by*
  - [Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing](https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf)
- **Reasoning faithfulness** (constructs) — *measured_by*
  - [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.184.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [A Picture is Worth A Thousand Numbers: EnablingLLMs Reason about Time Series via Visualization](https://aclanthology.org/2025.naacl-long.384.pdf)

### Associated with
- **LLM-as-a-judge** (measurements)
  - [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.576.pdf)
- **BERTScore** (measurements)
  > It has been shown that BARTScore outperforms other metrics such as BERTScore and BLEURT (Yuan et al., 2021) (Section 3.1).
  - [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.576.pdf)
- **BLEURT** (measurements)
  - [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.576.pdf)
