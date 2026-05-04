# WMT16
**Type:** Measurement  
**Referenced in:** 10 papers  
**Also known as:** WMT-2016, WMT-16  

## State of the Field

WMT16 is predominantly characterized as a machine translation benchmark dataset with two distinct applications in the provided literature. The most prevalent usage is for evaluating the performance of machine-generated text detection systems, particularly in a cross-lingual context. In this capacity, its English and German splits are frequently used to assess "cross-lingual detection performance" and "text detection evasion." For example, one study notes its selection to "evaluate performance in German" (DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text). A separate line of work uses WMT16 to directly evaluate machine translation capabilities. These studies operationalize it for tasks like English-to-Romanian translation, using it for fine-tuning or, as one paper states, to "distill the pre-trained mBART students for the downstream task of translation" (Improving Language Model Distillation through Hidden State Matching). Across these applications, WMT16 is explicitly used to measure the behavior of `Machine translation` and is also listed as a measure for `Multilingual ability`.

## Sources

**[DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/d4ce6738e84876aa79f13c8bc8b7c5eb-Paper-Conference.pdf)**
> Machine translation dataset in English and German used to evaluate cross-lingual detection performance.

**[Humanizing the Machine: Proxy Attacks to Mislead LLM Detectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab1ee157f7804a13f980414b644a9460-Paper-Conference.pdf) (as "WMT-2016")**
> A machine translation benchmark dataset used here for cross-language evaluation of text detection evasion.

**[Scaling Laws for Downstream Task Performance in Machine Translation](https://proceedings.iclr.cc/paper_files/paper/2025/file/dce0ad3bd4981fea9a5a5a274a2256d9-Paper-Conference.pdf) (as "WMT-16")**
> A machine translation benchmark/task suite used here for English-to-Romanian fine-tuning evaluation.

## Relationships

### → WMT16
- **Machine translation** (behaviors tasks) — *measured_by*
  > We distill the pre-trained mBART students for the downstream task of translation from English to Romanian using the WMT16 dataset (Bojar et al., 2016). (Section 3.2)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **Multilingual ability** (constructs) — *measured_by*
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
