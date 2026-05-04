# How2Sign
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, How2Sign is consistently characterized as a large-scale dataset and benchmark for American Sign Language (ASL). Its most prevalent application is to measure the behavior of sign language translation, specifically from ASL to English. Multiple sources state that the "SLT task is conducted on... How2Sign," and it is described as a standard benchmark for this purpose. The dataset's content is specified as being collected from "instructional videos" or focusing on the domain of "'how to' instructional videos." One source provides more granular details, noting it includes "35,191 samples with a vocabulary of 16K English words." A less common application is in the context of sign language recognition, where one paper reports using the dataset's training set to finetune models for language identification tasks. How2Sign is frequently mentioned alongside other datasets such as CSL-Daily and PHOENIX14T.

## Sources

**[Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)**
> A large-scale American Sign Language (ASL) dataset collected from instructional videos, used as a benchmark for evaluating sign language translation.

## Relationships

### → How2Sign
- **Sign language translation** (behaviors tasks) — *measured_by*
  > SLT task is conducted on the CSL-Daily, How2Sign (Duarte et al., 2021), and OpenASL (Shi et al., 2022) datasets. (Section 4.2)
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
- **Sign language recognition** (behaviors tasks) — *measured_by*
  > “For sign language identification, zero-shot scores mean that the model is briefly finetuned on YouTube-SL-25 rebalanced to the 4 sign languages with equal weight, and finetuned scores mean that the model is finetuned on an equally weighted mixture of the benchmarks’ training sets. We don’t finetune on FLEURS-ASL, so the finetuned langid scores are after finetuning on How2Sign.”
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
