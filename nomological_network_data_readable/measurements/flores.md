# FLORES
**Type:** Measurement  
**Referenced in:** 17 papers  
**Also known as:** Flores, FLORES+  

## State of the Field

Across the provided literature, FLORES is predominantly characterized as a benchmark dataset for evaluating machine translation quality. Its primary application, as evidenced by numerous studies, is to measure machine translation performance, often with a focus on low-resource languages. The dataset is frequently described as a "massively multilingual" and "multiway parallel" resource, with one paper noting it contains "short documents translated into 200 languages." For instance, one study uses the "FLORES devtest" to evaluate translation for specific low-resource language pairs. While the focus on machine translation is widespread, a few papers present alternative uses. One paper frames it as a dataset for "bitext mining tasks" because its sentences are "shared across several language pairs." Another study utilizes a variant, FLORES+, as an "out-of-domain dataset" specifically for the visualization of "cross-lingual alignment." The dataset also serves as a foundation for other instruments, as one paper introduces FLEURS-ASL as an "extension of FLORES".

## Sources

**[Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf)**
> A benchmark dataset for evaluating machine translation quality across many languages, particularly in low-resource settings.

**[MMTEB: Massive Multilingual Text Embedding Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0e3f908a2116ba529ad0a1530a3675-Paper-Conference.pdf) (as "Flores")**
> A dataset used in bitext mining tasks where sentences are shared across multiple language pairs.

**[From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1149.pdf) (as "FLORES+")**
> A multilingual parallel-sentence dataset used for out-of-domain visualization of cross-lingual alignment with t-SNE.

## Relationships

### → FLORES
- **Machine translation** (behaviors tasks) — *measured_by*
  > We also test eng–npi and gug translation, low-resource languages with an established evaluation set, FLORES (Costa-jussà et al., 2024) and likely a low data weight in LLMs; while not unseen, these experiments broaden our results to seen low-resource languages more generally. (Section 3.1)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)

### Associated with
- **FLEURS-ASL** (measurements)
  > In this paper, we introduce FLEURS-ASL, an extension of FLORES/FLEURS to support their ﬁrst sign language, American Sign Language. (Section 1)
  - [Examining and Adapting Time for Multilingual Classification via Mixture of Temporal Experts](https://aclanthology.org/2025.naacl-long.314.pdf)
