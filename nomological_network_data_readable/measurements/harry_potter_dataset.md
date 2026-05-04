# Harry Potter dataset
**Type:** Measurement  
**Referenced in:** 3 papers  
**Also known as:** BOOKS, Books  

## State of the Field

The name "Harry Potter dataset" and its variants, such as "BOOKS", are predominantly used in the provided literature to describe a measurement instrument for evaluating LLM unlearning of copyrighted content. The dataset is built from passages of the Harry Potter book series, with one paper specifying the use of "Harry Potter and the Sorcerer’s Stone". Its primary function is to test whether a model "stops reproducing the source text" after undergoing an unlearning process. One paper describes a specific operationalization within the MUSE benchmark where the original novels constitute the "forget set" and related FanWiki materials serve as the "retain set." This structure is intended to evaluate if the model can unlearn the copyrighted text while preserving related domain knowledge. A different line of work mentions a dataset also named "Books," which is an Amazon dataset of user-item interactions used for evaluating recommendation performance, indicating a potential naming overlap for distinct instruments.

## Sources

**[Catastrophic Failure of LLM Unlearning via Quantization](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba79fb5c4fe70050752f20c90c5f07ca-Paper-Conference.pdf) (as "BOOKS")**
> A dataset within the MUSE benchmark featuring the Harry Potter series as the forget set and related FanWiki materials as the retain set.

**[Language Representations Can be What Recommenders Need: Findings and Potentials](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4bab1843c8d5a69f5abfd0824593493-Paper-Conference.pdf) (as "Books")**
> An Amazon dataset containing user-item interactions and metadata for products in the 'Books' category, used for evaluating recommendation performance.

**[LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)**
> A copyrighted-text unlearning evaluation dataset built from Harry Potter book passages used to test whether the model stops reproducing the source text.
