# Sensitivity
**Type:** Construct  
**Referenced in:** 7 papers  

## State of the Field

The prevailing usage of "Sensitivity" in the provided literature characterizes it as a construct of model instability, defined as the degree to which an LLM's predicted class distribution changes across semantically equivalent rephrasings of a prompt. This framing, which one paper notes "does not require access to ground truth labels," is operationalized by measuring how much a model's prediction varies under these rephrasings, with one study calculating it as "normalized entropy." This form of sensitivity is empirically evaluated through text classification tasks on benchmarks including TREC and DBPedia. However, several alternative definitions appear in the data. A smaller line of work treats sensitivity as a property of evaluation metrics, specifically their capacity to detect "small degradations or specific error types" in simplified text. Another paper defines it as a property of a sequence classification function, counting the number of input subsets that can be individually changed to alter the output, thereby estimating word importance. A fourth, more formal definition from a single paper describes sensitivity at the bit-level, measuring how many "Hamming neighbors have the opposite output" to gauge a function's learning difficulty. The construct is also noted as being related to "Faithfulness," though the nature of this relationship is not specified in the provided evidence.

## Sources

**[Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)**
> The degree to which an LLM's predicted class distribution changes across semantically equivalent rephrasings of the prompt, reflecting its instability to input variations independent of ground truth.

## Relationships

### Sensitivity →
- **Text classification** (behaviors tasks) — *measured_by*
  > We perform an empirical comparison of these metrics on text classification tasks, using them as guideline for understanding failure modes of the LLM. (Section 1)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **TREC** (measurements) — *measured_by*
  > In Figure 3 (bottom), we plot the sensitivity Sτ for each class and prompting strategy (Llama3). Consistently with the example of Section 1, we see that on TREC the classes Description, Entity, and Number are the ones with the highest sensitivity. (Section 5)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **DBPedia** (measurements) — *measured_by*
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **PRMBENCH** (measurements) — *measured_by*
  - [Language Constrained Multimodal Hyper Adapter For Many-to-Many Multimodal Summarization](https://aclanthology.org/2025.acl-long.1230.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
