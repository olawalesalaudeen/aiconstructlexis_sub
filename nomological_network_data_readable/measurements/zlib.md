# Zlib
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided sources, Zlib is characterized as a method for pretraining data detection, also referred to as a membership inference method. It is operationalized as a likelihood-based procedure that uses zlib compression entropy to normalize a model-derived score for a given input. The specific calculation is described in slightly different ways: one paper frames it as using the "ratio of example perplexity and zlib compression entropy," while another describes it as a "loss-calibration-based" approach that "divides the model’s loss by the zlib compression entropy of the input." The stated purpose of this normalization is to account for input complexity. In one context, Zlib is presented as a "baseline method" for its task.

## Sources

**[Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)**
> A likelihood-based detection procedure that uses the ratio of example perplexity and zlib compression entropy for pretraining data detection.
