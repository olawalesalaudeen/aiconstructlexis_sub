# Logit lens
**Type:** Measurement  
**Referenced in:** 24 papers  
**Also known as:** Logit Lens, Vocabulary projection  

## State of the Field

Across the surveyed literature, the Logit lens is predominantly characterized as a probing or analysis technique for interpreting the internal states of transformer models. The method's core mechanism, described consistently across papers, involves applying the model's final unembedding matrix or decoder head to the hidden states of intermediate layers, thereby projecting these representations into the vocabulary space. This projection is used to visualize or decode next-token predictions at each stage of processing, with several papers describing this as a way to see what the model is "'thinking'" layer-by-layer. A recurring point is that this analysis can be done without any extra training. A less common framing, found in one paper, refers to this technique as "vocabulary projection" and notes it is "equivalent to early exiting on the Transformer block at inference time" ('Answer, Assemble, Ace: Understanding How LMs Answer Multiple Choice Questions'). As a measurement instrument, the Logit lens is used to assess a range of phenomena, including `Mathematical reasoning`, `Hallucination`, `Faithfulness`, and `Hallucination detection`. The technique has also been adapted for different modalities, such as Vision Transformers, and is used alongside other methods like Sparse Autoencoders to inspect their features.

## Sources

**[Linearity of Relation Decoding in Transformer Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b6d7285306fe896fca9b2e9a02ff6ec-Paper-Conference.pdf) (as "Logit Lens")**
> An existing probing technique that visualizes the next-token prediction information at any layer by applying the model's final decoder head to that layer's hidden state.

**[Overthinking the Truth: Understanding how Language Models Process False Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb63841e1ad12370a34504f15c60db4f-Paper-Conference.pdf)**
> A method for decoding next-token predictions from a model's intermediate hidden states by applying the final layer's normalization and unembedding matrix, used to analyze the model's computation layer-by-layer without extra training.

**[Answer, Assemble, Ace: Understanding How LMs Answer Multiple Choice Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c248154176c08147e82c0b30961604f7-Paper-Conference.pdf) (as "Vocabulary projection")**
> An analysis technique, also known as 'logit lens', used to inspect a model's internal representations by projecting hidden states from any layer into the vocabulary space to see which tokens are being promoted.

## Relationships

### Logit lens →
- **Object localization** (behaviors tasks) — *causes*
  > Moreover, the logit lens enables spatially localizing objects within the input image. (Section 1)
  - [Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f14fb9acd243c13c95d4a490d1684ce-Paper-Conference.pdf)

### → Logit lens
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Pre-trained Large Language Models Use Fourier Features to Compute Addition](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cc8dc30e52798b27d37b795cc153310-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  - [ActionStudio: A Lightweight Framework for Data and Training of Large Action Models](https://aclanthology.org/2025.emnlp-main.1091.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [WISE: Weak-Supervision-Guided Step-by-Step Explanations for MultimodalLLMs in Image Classification](https://aclanthology.org/2025.emnlp-main.742.pdf)
- **Hallucination detection** (behaviors tasks) — *measured_by*
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)
