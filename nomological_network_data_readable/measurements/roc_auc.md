# ROC-AUC
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** AUC  

## State of the Field

Across the provided literature, ROC-AUC, also referred to as AUROC or AUC, is consistently defined as the area under the receiver operating characteristic curve. It is broadly used as a metric to evaluate the performance of binary classification and detection tasks. The most prevalent application in this set of papers is in the domain of watermarking, where it is used to measure the detection performance of a watermark, evaluate its strength after attacks, and assess the overall efficacy of watermarking methods. A second common use is for error and falsehood detection; for instance, it is used to operationalize "Hallucination detection" and to evaluate "claim-level fact-checking," where one paper specifies that "nonfactual claims represent a positive class." The metric is also applied more generally to evaluate "error detection performance." Papers report specific quantitative results, such as achieving "near-perfect detection (98.8% AUC)" in one watermarking study.

## Sources

**[Cascading Large Language Models for Salient Event Graph Generation](https://aclanthology.org/2025.naacl-long.113.pdf)**
> Area under the receiver operating characteristic curve, used to evaluate binary classification performance in claim-level fact-checking with nonfactual claims as the positive class.

**[BeSimulator: A Large Language Model Powered Text-based Behavior Simulator](https://aclanthology.org/2025.emnlp-main.238.pdf) (as "AUROC")**
> Area under the receiver operating characteristic curve, used as the evaluation metric for error detection performance.

**[FedMABench: Benchmarking MobileGUIAgents on Decentralized Heterogeneous User Data](https://aclanthology.org/2025.emnlp-main.1342.pdf) (as "AUC")**
> Area under the ROC curve, used to measure detection performance of the watermark across attacked and unattacked conditions.
