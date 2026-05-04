# Sign language recognition
**Type:** Behavior  
**Referenced in:** 2 papers  
**Also known as:** Continuous sign language recognition, Isolated sign language recognition, Sign language identification  

## State of the Field

The task of classifying pre-segmented video clips of individual sign language movements into their corresponding labels.

## Sources

**[Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf) (as "Isolated sign language recognition")**
> The task of classifying pre-segmented video clips of individual sign language movements into their corresponding labels.

**[Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf) (as "Continuous sign language recognition")**
> The task of transcribing a continuous, unsegmented sign language video into a sequence of corresponding sign glosses.

**[YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf) (as "Sign language identification")**
> The task of classifying which sign language is being used in a given video input.

## Relationships

### Sign language recognition →
- **FLEURS-ASL** (measurements) — *measured_by*
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
- **How2Sign** (measurements) — *measured_by*
  > “For sign language identification, zero-shot scores mean that the model is briefly finetuned on YouTube-SL-25 rebalanced to the 4 sign languages with equal weight, and finetuned scores mean that the model is finetuned on an equally weighted mixture of the benchmarks’ training sets. We don’t finetune on FLEURS-ASL, so the finetuned langid scores are after finetuning on How2Sign.”
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)

### → Sign language recognition
- **Knowledge transfer** (constructs) — *causes*
  > We see that on both translation and lang id, sign language pretraining is substantially better than none (as in Uthus et al. [35]) and multilingual transfer helps both the higher-resource sign language (ASL) and the lower-resource sign languages within YouTube-SL-25.
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)

### Associated with
- **Sign language understanding** (constructs)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
- **Fine-grained understanding** (constructs)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
- **Understanding** (constructs)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
