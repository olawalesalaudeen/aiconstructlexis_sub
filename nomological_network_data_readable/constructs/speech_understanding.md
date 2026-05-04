# Speech understanding
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** Spatial speech understanding  

## State of the Field

Across the surveyed literature, the prevailing definition of speech understanding is a model's latent ability to interpret the semantic content of spoken language from audio, encompassing comprehension of words and context across varied conditions like noise and accents. Some papers expand this definition to include the capacity for following spoken instructions and processing mixed-modal inputs. A more specialized variant, "spatial speech understanding," is described in one paper as the ability to comprehend speech in conjunction with its spatial origins, such as speaker direction, for applications in wearable devices. The construct is operationalized and measured using specific benchmarks, with papers citing AudioBench and SUPERB as evaluation instruments. One paper explicitly links the construct to a concrete task, stating, "To measure the understanding ability... we verified the accuracy of ASR on different evaluation sets" (Freeze-Omni...). This demonstrates that performance on Automatic Speech Recognition is used as a direct measure of understanding. The construct is also studied alongside related concepts such as spoken question answering and instruction following.

## Sources

**[Iterative Self-TuningLLMs for Enhanced Jailbreaking Capabilities](https://aclanthology.org/2025.naacl-long.298.pdf)**
> The latent ability of a model to interpret the semantic content of spoken language in audio, including comprehension of words, phrases, and context across diverse conditions such as accents, noise, and length.

**[SING: Spatial Context in Large Language Model for Next-Gen Wearables](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mishra25a/mishra25a.pdf) (as "Spatial speech understanding")**
> The latent ability of a model to process and comprehend spoken language in conjunction with its spatial origins, such as the direction of the speaker.

## Relationships

### Speech understanding →
- **SUPERB** (measurements) — *measured_by*
  - [SIFT-50M: A Large-Scale Multilingual Dataset for Speech Instruction Fine-Tuning](https://aclanthology.org/2025.acl-long.682.pdf)

### → Speech understanding
- **AudioBench** (measurements) — *measured_by*
  - [SVD-LLMV2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.218.pdf)

### Associated with
- **Speech recognition** (behaviors tasks)
  - [SVD-LLMV2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.218.pdf)
- **Spoken question answering** (behaviors tasks)
  - [SVD-LLMV2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.218.pdf)
- **Instruction following** (constructs)
  - [SVD-LLMV2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.218.pdf)
