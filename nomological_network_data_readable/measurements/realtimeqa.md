# RealTimeQA
**Type:** Measurement  
**Referenced in:** 3 papers  
**Also known as:** REALTIME QA  

## State of the Field

Across the provided sources, RealTimeQA is consistently characterized as a question-answering benchmark or dataset focused on time-sensitive, real-time events. A primary design goal highlighted by one paper is to avoid data contamination by collecting questions after an LLM's knowledge cut-off date. In this context, it is mentioned alongside other benchmarks like FreshQA and TAQA. Another paper describes its use as a testbed for downstream tasks, specifically to evaluate zero-shot knowledge recall in continual learning settings. The dataset is specified as being in a multiple-choice question format. The benchmark's design requires periodic manual updates to maintain its currency. However, one source notes that these manual updates stopped in January 2024, creating a risk that newer models might be exposed to its data during pre-training.

## Sources

**[Binary Classifier Optimization for Large Language Model Alignment](https://aclanthology.org/2025.acl-long.94.pdf)**
> A time-sensitive question-answering benchmark developed after LLM knowledge cut-off dates to avoid data contamination, requiring periodic manual updates.

**[Probing Relative Interaction and Dynamic Calibration in Multi-modal Entity Alignment](https://aclanthology.org/2025.acl-long.1385.pdf) (as "REALTIME QA")**
> A multiple-choice question answering dataset about real-time events used to evaluate zero-shot knowledge recall in continual learning settings.
