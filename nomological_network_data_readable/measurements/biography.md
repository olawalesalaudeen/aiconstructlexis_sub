# Biography
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Biography dataset  

## State of the Field

Across the provided sources, Biography is consistently characterized as a dataset for evaluating language models. It is defined as a "fact-seeking long-form generation dataset" containing prompts or questions centered on biographical information, with its size noted as 181 prompts in one paper and 183 questions in another. The prevailing use of the dataset is to assess factuality; papers report using it to measure the construct of `Faithfulness` and to evaluate "factual consistency in narrative generation." One study specifically employs it as a test set for "out-of-domain evaluation of factuality." A different line of inquiry uses the Biography dataset to measure `Knowledge forgetting`. The tasks within the instrument are explicitly related to the behavior of `Biography generation`.

## Sources

**[Disambiguating Reference in Visually Grounded Dialogues through Joint Modeling of Textual and Multimodal Semantic Structures](https://aclanthology.org/2025.acl-long.548.pdf)**
> Fact-seeking long-form generation dataset with 181 prompts centered on biographical information, used to evaluate factual consistency in narrative generation.

**[Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf) (as "Biography dataset")**
> A test set containing questions about generating biographies, used for out-of-domain evaluation of factuality.

## Relationships

### → Biography
- **Factuality** (constructs) — *measured_by*
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs) — *measured_by*
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)

### Associated with
- **Biography generation** (behaviors tasks)
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
