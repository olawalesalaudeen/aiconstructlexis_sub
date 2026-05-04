# Translation quality
**Type:** Construct  
**Referenced in:** 12 papers  

## State of the Field

Across the provided papers, translation quality is predominantly defined as the overall excellence of a translated text, consistently encompassing dimensions such as fluency, adequacy, correctness, and meaning preservation. A few sources also describe it as the overall fidelity or effectiveness of the output, with one paper framing it as a "latent property" of a model's ability to produce good translations ("Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion"). The construct is operationalized and measured through a wide array of automated metrics and human evaluation. The most frequently cited measurement instruments include XCOMET, MetricX, AfriCOMET, BLEURT, COMETKIWI, and MQM. Human evaluation is also used to assess the construct, with annotators rating translations on criteria like fluency, understandability, and how well they preserve meaning. Translation quality is often studied in the context of trade-offs, such as balancing it with low latency. Some work reports that text simplification can improve translation quality, while other research challenges the assumption that high model probability is a reliable proxy for it.

## Sources

**[DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf)**
> The overall degree of excellence of a translated text, encompassing aspects like fluency, adequacy, and correctness, as judged by automated or human evaluation.

## Relationships

### Translation quality →
- **MQM** (measurements) — *measured_by*
  - [A Case Against Implicit Standards: Homophone Normalization in Machine Translation for Languages that use theGe’ez Script.](https://aclanthology.org/2025.emnlp-main.524.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > We conduct a manual evaluation to determine whether bilingual human annotators rate translations generated using our winning rewrite method (simplification with TOWER-INSTRUCT) as superior to the original translations. (§5.3)
  - [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.602.pdf)
- **XCOMET** (measurements) — *measured_by*
  > We additionally report the combined evaluation metric, XCOMET(s′, t′, r) to take into account of the trade-off between the two above metrics, and METRICX(t′, r) which also assesses translation quality of the rewrite but is not informed by the updated source s′. (§3.2)
  - [KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)
- **MetricX** (measurements) — *measured_by*
  - [Enhancing Large Vision-Language Models with Ultra-Detailed Image Caption Generation](https://aclanthology.org/2025.emnlp-main.1358.pdf)
- **COMETKIWI** (measurements) — *measured_by*
  - [Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages](https://aclanthology.org/2025.emnlp-main.1408.pdf)
- **AfriCOMET** (measurements) — *measured_by*
  - [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.602.pdf)
- **BLEURT** (measurements) — *measured_by*
  - [Learning from others’ mistakes: Finetuning machine translation models with span-level error annotations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25p/zhang25p.pdf)

### → Translation quality
- **Text simplification** (behaviors tasks) — *causes*
  > Simplification with TOWER-INSTRUCT distinguishes itself by improving translation quality based on XCOMET(s, t, r) scores and maintaining it according to the METRICX(t, r) scores. (§4.1)
  - [KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)

### Associated with
- **Semantic drift** (constructs)
  - [A Case Against Implicit Standards: Homophone Normalization in Machine Translation for Languages that use theGe’ez Script.](https://aclanthology.org/2025.emnlp-main.524.pdf)
