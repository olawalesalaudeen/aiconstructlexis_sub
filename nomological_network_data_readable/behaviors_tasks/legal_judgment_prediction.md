# Legal judgment prediction
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Charge prediction, Prison term prediction  

## State of the Field

Legal judgment prediction is characterized in the surveyed literature as the task of forecasting court rulings based on case information. One paper describes its application as enabling litigants and lawyers to "forecast judgment outcomes and refine litigation strategies." The behavior is operationalized through at least two distinct sub-tasks, both specified within the context of Chinese law. These sub-tasks are "charge prediction," which involves identifying the correct legal charge and is evaluated using the F1 score, and "prison term prediction," which focuses on determining the appropriate sentence length and is measured by normalized log distance. Thus, the concept is framed both as a general forecasting problem and as a set of specific predictive tasks with defined evaluation metrics.

## Sources

**[TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.44.pdf) (as "Charge prediction")**
> Predicting the correct legal charge in a given case based on Chinese law, evaluated using F1 score.

**[TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.44.pdf) (as "Prison term prediction")**
> Predicting the appropriate prison sentence length in legal cases under Chinese law, evaluated using normalized log distance.

**[Tiny Budgets, Big Gains: Parameter Placement Strategy in Parameter Super-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.322.pdf)**
> The task of forecasting court rulings, such as whether a plaintiff's claims are supported, based on case information.
