# LOSS
**Type:** Measurement  
**Referenced in:** 3 papers  

## State of the Field

Based on the provided data, LOSS is presented as a baseline membership inference attack. The method is defined as a technique for classifying data membership by calculating the average next-token loss across a sequence. As detailed in "Confounding Factors in Relating Model Performance to Morphology," this approach involves computing this average loss and then classifying a sequence as a member of the training data if the resulting score is below a specified threshold (τ). The paper attributes this technique to Yeom et al. (2018).

## Sources

**[Confounding Factors in Relating Model Performance to Morphology](https://aclanthology.org/2025.emnlp-main.370.pdf)**
> A baseline membership inference attack that classifies membership based on average next-token loss across a sequence.
