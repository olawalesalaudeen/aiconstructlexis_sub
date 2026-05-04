# Detectability
**Type:** Construct  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, Detectability is framed in two primary ways, with a focus on watermarking being more prevalent. A general usage defines it as the extent to which machine-generated text can be distinguished from human text by automated systems, where one study finds that “Personalization reduces the detectability of generated disinformation.” The more common framing, however, treats Detectability as the ability of a watermarking scheme to be reliably identified, operationalized through statistical testing with a known key. In this context, it is often evaluated as a core property of a watermarking method, with some work noting a trade-off where methods might “sacrifice detectability to maintain quality.” Furthermore, for watermarks, Detectability is studied alongside Robustness and stability, with the expectation that watermarks should “remain detectable after common token- and sequence-level corruptions are applied.”

## Sources

**[Efficient and Accurate Prompt Optimization: the Benefit of Memory in Exemplar-Guided Reflection](https://aclanthology.org/2025.acl-long.38.pdf)**
> The extent to which machine-generated text can be distinguished from human-written text by automated detection systems, influenced by factors such as content personalization and model output characteristics.

**[GaussMark: A Practical Approach for Structural Watermarking of Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/block25a/block25a.pdf) (as "Watermark detectability")**
> The latent ability of a watermarking scheme to be reliably identified through statistical testing, given knowledge of the watermark key, while maintaining low false positive rates.
