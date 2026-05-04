# MMMU-Pro
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

MMMU-Pro is consistently characterized across the provided literature as a challenging benchmark for evaluating the advanced, professional-level capabilities of Vision Language Models. Its most common application is to measure `multimodal reasoning` and `multimodal understanding`, with one paper stating it is designed to "assess a model’s true multimodal understanding and reasoning capabilities across a wide range of academic disciplines." A smaller set of papers also uses MMMU-Pro to evaluate the construct of `Faithfulness`. The benchmark is described as an "advanced version of MMMU" that focuses on complex knowledge and reasoning tasks, incorporating a vision component that requires a deep understanding of images. To increase difficulty, it employs "stricter evaluation settings," such as a 10-option multiple-choice format, which is intended to assess robustness in complex reasoning. In practice, models are evaluated for accuracy on the benchmark, and it is often used to report state-of-the-art performance improvements alongside other multimodal benchmarks like MathVista and MathVerse.

## Sources

**[ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)**
> A challenging benchmark used to evaluate the advanced, professional-level capabilities of Vision Language Models.

## Relationships

### → MMMU-Pro
- **General capabilities** (constructs) — *measured_by*
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > MMMU-Pro is designed to more accurately and rigorously assess a model’s true multimodal understanding and reasoning capabilities across a wide range of academic disciplines. (Section 1)
  - [CART: A Generative Cross-Modal Retrieval Framework With Coarse-To-Fine Semantic Modeling](https://aclanthology.org/2025.acl-long.736.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  > Experiments demonstrate that training MLLMs on our dataset not only significantly improves reasoning capabilities, achieving state-of-the-art performance on benchmarks such as MathVerse (+8.1%), MMMU-Pro (+7%), and MuirBench (+13.3%) (Section 1).
  - [CART: A Generative Cross-Modal Retrieval Framework With Coarse-To-Fine Semantic Modeling](https://aclanthology.org/2025.acl-long.736.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Thinking Out Loud: Do Reasoning Models Know When They’re Right?](https://aclanthology.org/2025.emnlp-main.74.pdf)
