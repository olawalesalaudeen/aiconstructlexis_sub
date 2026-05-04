# P(True)
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided sources, P(True) is consistently characterized as a prompt-based method for detecting errors in large language model outputs. The technique operates by prompting an LLM to perform a self-critique or self-assessment of its own response's correctness. The probability of the model outputting the token 'True' during this process is then used as a 'correctness score' or 'confidence score'. The purpose of this method is described both for general error detection and more specifically for hallucination detection. One source positions P(True) as a 'representative' of a broader class of prompt-based self-assessment methods.

## Sources

**[Beyond Sequences: Two-dimensional Representation and Dependency Encoding for Code Generation](https://aclanthology.org/2025.acl-long.309.pdf)**
> A prompt-based hallucination detection method that uses a simple template to elicit model self-assessment of response correctness.
