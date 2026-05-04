# HateXplain
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, HateXplain is predominantly described as a natural-language benchmark for text classification. Its primary use is to classify sentences as "normal versus hateful or offensive," a task also referred to as "toxic text classification." One paper specifies that the target label is binary, with '0' for normal sentences and '1' for those deemed hateful or offensive ("Debiasing Attention Mechanism in Transformer without Demographics"). A recurring focus is its application in evaluating model fairness and robustness, particularly in relation to demographics. The dataset is characterized as having "unwanted correlation between toxicity labels and mentions of demographics" and "demographic correlation shifts," making it a tool for assessing fairness concerning "gender-related sensitive information" and for evaluating "zero-shot robustness." A different, less frequent usage frames HateXplain as a "subjective single-label dataset" employed to contextualize multi-label research findings ("REARANK: Reasoning Re-ranking Agent via Reinforcement Learning").

## Sources

**[Debiasing Attention Mechanism in Transformer without Demographics](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f5337a39b1f6d670aad9d32debc0e5d-Paper-Conference.pdf)**
> A natural-language benchmark used here for classifying sentences as normal versus hateful or offensive while evaluating fairness with respect to gender-related sensitive information.
