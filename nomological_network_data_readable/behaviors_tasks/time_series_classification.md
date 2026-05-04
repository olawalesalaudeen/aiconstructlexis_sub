# Time series classification
**Type:** Behavior  
**Referenced in:** 8 papers  
**Also known as:** Financial market movement prediction, Readmission prediction, Time-series classification, In-hospital mortality prediction, Sleep stage detection  

## State of the Field

Across the surveyed literature, time series classification is predominantly defined as the observable task of assigning a categorical label to a sequence of time-ordered data points. This behavior is instantiated across several domains, with a recurring focus on healthcare and, to a lesser extent, finance. In the clinical context, it includes tasks such as predicting patient mortality and hospital readmission from historical electronic health records, as well as classifying physiological signals into discrete sleep stages. Other documented applications include predicting financial market movements and tasks within the human activity recognition domain, which is noted as a primary source of data for this task. To operationalize and measure performance, particularly for healthcare predictions, papers use datasets such as MIMIC-III and MIMIC-IV. One study also highlights unique challenges associated with this task, such as "heterogeneous timestamp length, noisy labelling, and domain gap from different sensors" (Efficient Personalized Adaptation for Physiological Signal Foundation Model).

## Sources

**[Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf) (as "Mortality prediction")**
> The task of predicting a patient's survival status during their next hospital visit based on their historical electronic health records.

**[Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf) (as "Readmission prediction")**
> The task of predicting whether a patient will be readmitted to the hospital within a specific timeframe based on their historical electronic health records.

**[Filtered not Mixed: Filtering-Based Online Gating for Mixture of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d4c2f25bf0c33065b7d4fb9be2a9add1-Paper-Conference.pdf) (as "Financial market movement prediction")**
> A classification task to predict the directional movement of a financial market, such as 'Fall', 'Neutral', or 'Rise', based on contextual information like news and financial data.

**[Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf) (as "Time-series classification")**
> The observable task of assigning a class label to a sequence of time-ordered data points.

**[Sandcastles in the Storm: Revisiting the (Im)possibility of Strong Watermarking](https://aclanthology.org/2025.acl-long.1437.pdf)**
> The observable task of assigning a categorical label to an entire time series sequence.

**[CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25b/dai25b.pdf) (as "In-hospital mortality prediction")**
> The observable classification task of predicting whether a patient will die within a specific timeframe (e.g., 48 hours) during their hospital admission.

**[Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf) (as "Sleep stage detection")**
> Classifying segments of physiological signals into one of five sleep stages: Wake, N1, N2, N3, or REM, based on EEG, EOG, and EMG data.

## Relationships

### Time series classification →
- **MIMIC-III** (measurements) — *measured_by*
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **MIMIC-IV** (measurements) — *measured_by*
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)

### Associated with
- **Classification** (behaviors tasks)
  - [Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf)
