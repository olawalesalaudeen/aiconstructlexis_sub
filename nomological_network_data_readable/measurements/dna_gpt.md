# DNA-GPT
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, DNA-GPT (Divergent N-Gram Analysis) is consistently defined as a training-free, zero-shot method for detecting machine-generated text. The procedure, as detailed in its proposing paper, involves truncating a given text, using the preceding portion to have a language model regenerate the remaining part, and then analyzing the divergence between the original and the regenerated completions. This analysis of divergence is the basis for identifying AI authorship. The method is designed to function in both black-box and white-box settings. In subsequent research, DNA-GPT is positioned as a typical training-free approach, often grouped with methods like DetectGPT, and is used as a baseline for evaluating new detection techniques. One paper notes that the reliability of its statistical metrics is dependent on the text having a sufficient token length.

## Sources

**[DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/d4ce6738e84876aa79f13c8bc8b7c5eb-Paper-Conference.pdf)**
> A zero-shot detection method based on divergence between multiple completions of a truncated passage.
