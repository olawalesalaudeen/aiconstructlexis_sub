# Anomaly detection
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Anomaly Detection, Abnormal detection  

## State of the Field

Across the provided literature, anomaly detection is a behavior defined in several distinct ways depending on the application domain. The most frequent framing involves identifying irregularities within sequences of events. One line of work operationalizes this as a "time-series prediction task" where the goal is to predict "whether a sequence of log events indicates abnormal system behavior" ("RuAG: Learned-rule-augmented Generation for Large Language Models"). A related but more specific operationalization involves identifying a single "out-of-place element" in a sequence where one event's type has been randomly replaced ("LAST SToP for Modeling Asynchronous Time Series"). A different application, termed "Abnormal detection," defines the task as classifying entire "EEG records as clinically normal or abnormal" ("NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals"). Thus, while the general concept involves identifying what is abnormal, its measurement varies from predicting system-level behavior in logs to locating a single incorrect event or classifying a complete biomedical recording.

## Sources

**[RuAG: Learned-rule-augmented Generation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d7e8991f75f3e5af14edf7aebb5be5e-Paper-Conference.pdf) (as "Anomaly Detection")**
> Predicting whether a sequence of log events indicates abnormal system behavior.

**[NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf) (as "Abnormal detection")**
> Classifying EEG records as clinically normal or abnormal.

**[LAST SToP for Modeling Asynchronous Time Series](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25a/gupta25a.pdf)**
> Identifying an out-of-place event in a sequence when one event type has been replaced.
