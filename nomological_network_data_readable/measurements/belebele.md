# Belebele
**Type:** Measurement  
**Referenced in:** 17 papers  
**Also known as:** BELEBELE  

## State of the Field

Across the provided literature, Belebele is consistently described as a multilingual benchmark designed to evaluate reading comprehension. The prevailing operationalization of the task involves multiple-choice questions based on short passages, with one paper noting that its passages are sourced from the FLORES-200 dataset. Papers use this instrument to measure a range of capabilities, most frequently reading comprehension, machine reading comprehension, and language understanding. It is also used to assess question answering, multilingual ability, and text generation in a prompted question-answering context. A recurring feature is its broad linguistic coverage, with multiple sources specifying it spans 122 language variants or language-dialect combinations. The benchmark is noted to include low-resource languages and specific dialects, such as Moroccan and Egyptian. In practice, researchers are shown to employ Belebele in few-shot evaluation settings, with two papers specifically mentioning five-shot prompting.

## Sources

**[Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf) (as "BELEBELE")**
> A multilingual reading comprehension benchmark used to assess a model's basic language understanding across many languages.

**[Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)**
> A multilingual benchmark for evaluating reading comprehension via multiple-choice questions based on short passages.

## Relationships

### → Belebele
- **Reading comprehension** (constructs) — *measured_by*
  - [CoRAC: Integrating SelectiveAPIDocument Retrieval with Question Semantic Intent for Code Question Answering](https://aclanthology.org/2025.naacl-long.629.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > We evaluate understanding capabilities using MMLU (Hendrycks et al., 2021), HellaSwag (Zellers et al., 2019), and Belebele (Bandarkar et al., 2024) benchmarks, each adapted to both EGY and MOR dialects. (Section 4.1)
  - [Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **Multilingual ability** (constructs) — *measured_by*
  - [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://aclanthology.org/2025.acl-long.1406.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > "We use the following datasets: ARC challenge (Clark et al., 2018), HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2020), CommonSense QA (Talmor et al., 2018) and Belebele (Bandarkar et al., 2023)."
  - [Neutral residues: revisiting adapters for model extension](https://raw.githubusercontent.com/mlresearch/v267/main/assets/talla25a/talla25a.pdf)
- **Machine reading comprehension** (behaviors tasks) — *measured_by*
  > To evaluate the generalization of bridge selection beyond the BLI task, we further evaluate cross-lingual Machine Reading Comprehension (MRC) using the Belebele dataset (Bandarkar et al., 2024). (Section 4.1)
  - [AFRIDOC-MT: Document-levelMTCorpus forAfrican Languages](https://aclanthology.org/2025.emnlp-main.1414.pdf)
