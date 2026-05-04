# Watermark detection
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Watermark decoding  

## State of the Field

Across the surveyed literature, Watermark detection is predominantly characterized as the process of determining whether a given text sequence contains a hidden watermark. The most common operationalization of this behavior is a statistical test, where an algorithm makes a "calibrated decision" by comparing a calculated statistic against a threshold (Provable Robust Watermarking for AI-Generated Text). Specific methods mentioned for this test include calculating a z-score, counting token membership in a "green list," or averaging token-level watermark logits. A less frequent approach involves using a trained neural network that "functions as a discriminator" to classify the text (An Unforgeable Publicly Verifiable Watermark for Large Language Models). The goal is consistently framed as a binary classification, outputting whether the text is watermarked or not. This is often positioned as the "inverse problem of watermark embedding," inferring if a text originates from a marked or unmarked distribution (Unbiased Watermark for Large Language Models). A distinct framing, referred to as "watermark decoding" in one paper, focuses not on presence/absence but on extracting an embedded binary code from the text.

## Sources

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)**
> Determining whether a text contains a watermark signal from its token-level watermark logits.

**[Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf) (as "Watermark decoding")**
> The process of extracting the embedded binary watermark code from a text using a trained classifier applied to segmented text.
