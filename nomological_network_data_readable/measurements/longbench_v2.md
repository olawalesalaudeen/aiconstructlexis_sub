# LongBench v2
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, LongBench v2 is characterized as a benchmark for evaluating model capabilities in long-context scenarios. It is explicitly used to measure constructs such as "Long-context understanding" and "Information retrieval," with papers positioning it as an instrument for assessing "deep long-context comprehension and reasoning." The benchmark is consistently described as consisting of multi-choice tasks, with one source specifying it contains 503 questions and both sources noting that context lengths range from 8K to 2M words. One paper details its broad scope, listing six task categories: single- and multi-document QA, long in-context learning, long dialogue history understanding, code repository understanding, and long structured data understanding. In terms of evaluation, one study uses LongBench v2 to measure both performance via accuracy and efficiency via throughput in tokens per second. Another paper notes that the benchmark is "recognized for its broad scope and difficulty."

## Sources

**[RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf)**
> A benchmark of multi-choice tasks across long context lengths, used here to assess long-context performance and efficiency.

## Relationships

### → LongBench v2
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  - [Graph World Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25p/feng25p.pdf)
- **Long-context reasoning** (constructs) — *measured_by*
  - [Zero-shot Multimodal Document Retrieval via Cross-modal Question Generation](https://aclanthology.org/2025.emnlp-main.1325.pdf)
