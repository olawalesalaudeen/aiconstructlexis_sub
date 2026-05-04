# HADES
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

HADES is consistently presented as a multimodal jailbreak benchmark used to evaluate model safety. The provided literature uses it to measure several related concepts, including jailbreaking, safety alignment, and harmfulness detection. According to its definition, HADES is designed to "probe safety under adversarial conditions across harmful scenarios" by using "crafted images and accompanying typography." The mechanism for this involves embedding and amplifying "malicious intent" within its multimodal samples, with one source specifying that it consists of "images and text queries where the text itself is harmful." The benchmark is described as containing 750 samples distributed across five different harmful scenarios. In practice, papers frequently evaluate models on HADES alongside other safety and jailbreak benchmarks like MM-SafetyBench and SafeBench.

## Sources

**[MAKAR: a Multi-Agent framework based Knowledge-Augmented Reasoning for Grounded Multimodal Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.312.pdf)**
> HADES is a multimodal jailbreak benchmark with crafted images and accompanying typography designed to probe safety under adversarial conditions across harmful scenarios.

## Relationships

### → HADES
- **Safety alignment** (constructs) — *measured_by*
  - [Defending LVLMs Against Vision Attacks Through Partial-Perception Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25z/zhou25z.pdf)
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  > Hades and Safebench consist of images and text queries where the text itself is harmful.
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
