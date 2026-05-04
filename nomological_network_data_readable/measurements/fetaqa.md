# FeTaQA
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** FetaQA  

## State of the Field

FeTaQA is predominantly described across the literature as a benchmark for table question answering. It is widely used to measure model capabilities in `Table understanding`, with some papers also using it to evaluate `Data-to-text generation` and performance on "structured knowledge grounding tasks". Several sources characterize it as a challenging dataset because it requires generating long-form, free-form natural language answers, which average around 18 words. This task structure, as one paper notes, requires "fetching multiple entities from the table, aggregating and reasoning over these entities, and structuring the inferred information to produce a coherent answer" (CABINET: Content Relevance-based Noise Reduction for Table Question Answering). Due to its nature as an "open-ended generation task", evaluation is sometimes performed with overlap-based metrics like Sacre-BLEU. While its prevailing use is for evaluation, a smaller line of work treats FeTaQA as a "table-language dataset" that can be adapted into different training formats for other tasks, such as question generation or row summarization.

## Sources

**[CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)**
> FeTaQA, a table question answering benchmark with long-form natural-language answers that require fetching multiple entities and reasoning over them.

**[Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf) (as "FetaQA")**
> A table-language dataset adapted here into training formats for table-language interleaved learning.

## Relationships

### → FeTaQA
- **Table question answering** (behaviors tasks) — *measured_by*
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
- **Data-to-text generation** (behaviors tasks) — *measured_by*
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)

### Associated with
- **Prompt engineering** (behaviors tasks)
  > To further increase data diversity, we also adapt FetaQA (Nan et al., 2022), WikiTableQuestion (Pasupat & Liang, 2015), and ToTTo (Parikh et al., 2020) into formats suitable for training column embeddings, resulting in three adapted tasks: ③Question Generation... ④Table Titling... and ⑤Row Summarization (Section 4.2).
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)
