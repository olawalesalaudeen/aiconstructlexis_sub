# Contradiction detection
**Type:** Behavior  
**Referenced in:** 10 papers  
**Also known as:** Document-level self-contradiction detection, Contradiction identification, Conflict detection, Logical contradiction, Answer conflict detection, Corpus-level inconsistency detection  

## State of the Field

Across the provided literature, contradiction detection is a behavior focused on identifying logical inconsistencies between textual assertions. The most prevalent framing involves detecting contradictions within a single source, such as identifying "mutually inconsistent statements within the same report" (D-CoDe: Scaling Image-PretrainedVLMs to Video via Dynamic Compression and Question Decomposition) or internal inconsistencies in a multi-sentence document. Another common approach is to identify contradictions between different sources, such as between a piece of evidence and a testimony, or between facts within a larger corpus. A more specialized application defines it as detecting semantic differences in model responses to the same question across multiple languages to find "locale-sensitive" questions (Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness). The behavior is operationalized in various ways, including as a "multiple-choice format" task for selecting a contradictory pair and as a "binary classification task over atomic facts." The stated purpose of this detection is often to ensure "textual coherence and reliability" (MovieCORE:COgnitiveREasoning in Movies), with identified contradictions sometimes being classified as "Severe Errors" or used to trigger resolution processes. The provided data also indicates that contradiction detection is studied in relation to knowledge conflict resolution.

## Sources

**[MovieCORE:COgnitiveREasoning in Movies](https://aclanthology.org/2025.emnlp-main.67.pdf) (as "Document-level self-contradiction detection")**
> The task of identifying whether a multi-sentence document contains any internal contradictions.

**[Foot-In-The-Door: A Multi-turn Jailbreak forLLMs](https://aclanthology.org/2025.emnlp-main.101.pdf) (as "Contradiction identification")**
> The observable task of selecting a pair of testimony and evidence that logically contradict each other based on narrative context.

**[End-to-End Learnable Psychiatric Scale Guided Risky Post Screening for Depression Detection on Social Media](https://aclanthology.org/2025.emnlp-main.202.pdf) (as "Conflict detection")**
> Observably identifying logical inconsistencies between assertions, either within a single agent or across the multi-agent system.

**[D-CoDe: Scaling Image-PretrainedVLMs to Video via Dynamic Compression and Question Decomposition](https://aclanthology.org/2025.emnlp-main.598.pdf) (as "Logical contradiction")**
> Including mutually inconsistent statements within the same report, such as asserting both the presence and absence of a finding.

**[Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness](https://aclanthology.org/2025.emnlp-main.1466.pdf) (as "Answer conflict detection")**
> Identifying cases where model responses differ semantically across languages for the same question, indicating potential locale sensitivity.

**[Towards Author-informedNLP: Mind the Social Bias](https://aclanthology.org/2025.emnlp-main.1765.pdf) (as "Corpus-level inconsistency detection")**
> The task of identifying, for a given fact from a corpus, whether there exists at least one other fact within the same corpus that contradicts it.

## Relationships

### Associated with
- **Knowledge conflict resolution** (constructs)
  - [Measuring Data Diversity for Instruction Tuning: A Systematic Analysis and A Reliable Metric](https://aclanthology.org/2025.acl-long.909.pdf)
