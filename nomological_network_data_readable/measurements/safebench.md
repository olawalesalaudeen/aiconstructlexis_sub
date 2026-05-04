# SafeBench
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, SafeBench is consistently presented as a benchmark for evaluating the safety of Vision-Language Models (VLMs) and Multimodal Large Language Models (MLLMs). It is defined as comprising 500 malicious questions organized into 10 categories that are based on AI usage policies. Papers use SafeBench to operationalize and assess several safety-related behaviors in these models. A prevalent application is to evaluate the defense capabilities of MLLMs against jailbreak attacks. It is also used to measure a model's ability to perceive multimodal risks, specifically in the context of `Harmfulness detection`. The content of the benchmark is described as consisting of "images and text queries where the text itself is harmful" (PakBBQ: A Culturally Adapted Bias Benchmark forQA). One study refers to it as one of several "established benchmarks" for VLM safety.

## Sources

**[“Yes, MyLoRD.” Guiding Language Model Extraction with Locality Reinforced Distillation](https://aclanthology.org/2025.acl-long.74.pdf)**
> A benchmark for evaluating VLM safety, comprising 500 malicious questions organized into 10 categories based on AI usage policies.

## Relationships

### → SafeBench
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  > Hades and Safebench consist of images and text queries where the text itself is harmful.
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
