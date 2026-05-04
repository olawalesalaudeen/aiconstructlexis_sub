# Event detection
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Event identification  

## State of the Field

Based on the provided data, Event detection is consistently defined as the task of identifying events within text by extracting and labeling event triggers. This process involves two primary steps: extracting trigger words from a text and then classifying those triggers into one or more predefined event types from an ontology. The resulting output is typically a structured (event type, trigger) pair. One paper also introduces the related term "Event identification," which focuses on the correctness of this process, specifically the "correct classification of event types" and the "correct identification of the trigger-event pair." To operationalize and evaluate this behavior, researchers use specific datasets as benchmarks. The provided evidence shows that Event detection is measured using the ACE dataset for the news domain and the SPEED dataset for the epidemiology domain.

## Sources

**[LILaC: Late Interacting in Layered Component Graph for Open-domain Multimodal Multihop Retrieval](https://aclanthology.org/2025.emnlp-main.1038.pdf)**
> Identifying event triggers in text and classifying them into predefined event types, producing structured outputs of (event type, trigger) pairs.

**[LILaC: Late Interacting in Layered Component Graph for Open-domain Multimodal Multihop Retrieval](https://aclanthology.org/2025.emnlp-main.1038.pdf) (as "Event identification")**
> Correctly identifying the event mention by matching both the trigger and its event type.

## Relationships

### Event detection →
- **ACE** (measurements) — *measured_by*
  > We benchmark our model across six ED datasets spanning five diverse domains, listed as: ... (3) ACE (Doddington et al., 2004)... (Experimental Setup)
  - [DiCoRe: Enhancing Zero-shot Event Detection via Divergent-ConvergentLLMReasoning](https://aclanthology.org/2025.emnlp-main.1039.pdf)
- **SPEED** (measurements) — *measured_by*
  > We benchmark our model across six ED datasets spanning five diverse domains, listed as: ... (5) SPEED (Parekh et al., 2024c)... (Experimental Setup)
  - [DiCoRe: Enhancing Zero-shot Event Detection via Divergent-ConvergentLLMReasoning](https://aclanthology.org/2025.emnlp-main.1039.pdf)
