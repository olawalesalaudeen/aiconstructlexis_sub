# Watermark detectability
**Type:** Construct  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, Watermark detectability is consistently defined as the capacity of a detection system to identify a statistical signal embedded within model-generated text. The prevailing definition describes it as the degree to which this identification is successful, with one paper further specifying it as a "latent ability" inferred from "statistical patterns in token selection" ("LoSiA: Efficient High-Rank Fine-Tuning via Subnet Localization and Optimization"). A recurring theme is the connection between detectability and robustness, with one definition explicitly including the ability to identify watermarks "even in the presence of tokenization inconsistencies or adversarial attacks" ("Arena-lite: Efficient and Reliable Large Language Model Evaluation via Tournament-Based Direct Comparisons"). This emphasis on robustness is echoed in another paper's conclusion that a particular method "enhances both detectability and robustness against adversarial modifications" ("Arena-lite..."). To operationalize this construct, one study reports that the "AUROC value is employed to simulate detectability in real-world scenarios" ("Arena-lite..."). The evaluation of detectability is mentioned in the context of specific tasks, such as machine translation and protein generation.

## Sources

**[A Watermark for Order-Agnostic Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ce8e3434c7b486bbddff9745b2a1722-Paper-Conference.pdf)**
> The degree to which a statistical signal embedded in model-generated text can be successfully identified by a detection algorithm.

**[Arena-lite: Efficient and Reliable Large Language Model Evaluation via Tournament-Based Direct Comparisons](https://aclanthology.org/2025.emnlp-main.361.pdf) (as "Detectability")**
> The ability of a watermark detection system to correctly identify LLM-generated text as watermarked, even in the presence of tokenization inconsistencies or adversarial attacks.
