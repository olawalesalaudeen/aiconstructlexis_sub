# NFCorpus
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** NFCORPUS  

## State of the Field

Across the provided literature, NFCorpus is consistently characterized as a dataset for information retrieval (IR). The prevailing usage is to measure the behavior of `Information retrieval`, though one paper also uses it to evaluate `Fact-seeking question answering` on domain-specific questions. A more specific framing, found in one paper, defines it as a "medical information retrieval dataset" containing "professional academic terms" that can pose challenges for semantic processing. Beyond standard evaluation, a distinct line of work uses NFCorpus in the context of security, where it serves to "generate and evaluate adversarial passages in... corpus-poisoning experiments." It is also employed as an evaluation dataset for query generation. One study highlights a particular feature of the dataset, noting that it "shows the highest unseen query term ratio" among the datasets considered ("AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence").

## Sources

**[AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.334.pdf)**
> A retrieval dataset used to generate and evaluate adversarial passages in the corpus-poisoning experiments.

**[MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf) (as "NFCORPUS")**
> Medical information retrieval dataset used to evaluate performance on domain-specific factual questions involving single entities.

## Relationships

### → NFCorpus
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **Factual question answering** (behaviors tasks) — *measured_by*
  - [MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf)
