# Text completion
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Sentence continuation  

## State of the Field

Across the provided literature, text completion is a behavior consistently defined as generating text to extend a given context, such as a prompt or sentence. The concept appears under related names like 'text continuation,' which emphasizes producing a 'coherent extension,' and 'sentence continuation,' which focuses on the most plausible next sentence to test coherence. The behavior is operationalized and measured using several benchmarks, including WikiText-103, GSM8k, and FineWeb. While often framed as a purely generative task, a notable variation involves a discriminative format where a model 'selects the better continuation between two options.' The task is also applied to specific domains, such as completing sentences from Wikipedia or fiction, to study model properties like 'disparities of sentiment and toxicity' or 'variation in the topics introduced'.

## Sources

**[ELABORATION: A Comprehensive Benchmark on Human-LLMCompetitive Programming](https://aclanthology.org/2025.acl-long.5.pdf)**
> The task of generating text to continue a given prompt or sentence.

**[InSerter: Speech Instruction Following with Unsupervised Interleaved Pre-training](https://aclanthology.org/2025.acl-long.883.pdf) (as "Text continuation")**
> Generating a coherent extension of a given text that remains contextually appropriate and consistent with the original content.

**[CoachMe: Decoding Sport Elements with a Reference-Based Coaching Instruction Generation Model](https://aclanthology.org/2025.acl-long.1414.pdf) (as "Sentence continuation")**
> Generating or selecting the most plausible next sentence in a coherent text passage, testing local and global coherence.

## Relationships

### Text completion →
- **WikiText-103** (measurements) — *measured_by*
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **FineWeb** (measurements) — *measured_by*
  - [Improving Dialogue State Tracking through Combinatorial Search for In-Context Examples](https://aclanthology.org/2025.acl-long.1394.pdf)
