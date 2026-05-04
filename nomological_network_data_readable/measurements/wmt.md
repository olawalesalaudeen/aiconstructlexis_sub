# WMT
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, WMT is predominantly characterized as a benchmark for evaluating machine translation performance. The most common operationalization mentioned is the English-German (EnDe) translation task, with papers noting its use for both fine-tuning models and evaluation. The relationship data confirms this primary function, showing that WMT is used to measure the behavior of "Machine translation". A broader, but related, description frames WMT as one of several benchmarks that have "become central to evaluating translation quality" (A Case Against Implicit Standards...). A less common framing, found in one paper, describes WMT as a human-preference dataset for constructing contrastive instruction-response pairs. Some studies utilize WMT alongside other benchmarks to assess different capabilities, such as text summarization.

## Sources

**[DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf)**
> The Workshop on Machine Translation (WMT) benchmark, specifically the English-German (EnDe) task, is used to evaluate machine translation performance.

## Relationships

### → WMT
- **Machine translation** (behaviors tasks) — *measured_by*
  > "We supervised ﬁne-tune these models on three tasks: WMT EN→DE translation (Bojar et al., 2014), CNN/DM summarization (Hermann et al., 2015), and XSum abstractive summarization"
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
