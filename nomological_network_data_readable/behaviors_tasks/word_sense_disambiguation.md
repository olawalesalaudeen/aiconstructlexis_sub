# Word sense disambiguation
**Type:** Behavior  
**Referenced in:** 24 papers  
**Also known as:** Sense labeling, Word-sense association, Homonym disambiguation, Pun interpretation, Polysemy disambiguation, Sense-aware task performance, Charge disambiguation, Lexical disambiguation, Pronoun disambiguation  

## State of the Field

Across the surveyed literature, word sense disambiguation is most commonly framed as the task of determining whether a word is used with the same sense in two different sentences. This binary judgment format, also referred to as polysemy disambiguation, is frequently operationalized using the Word in Context (WiC) task formulation. A different line of work defines the task as selecting the correct meaning for a word from a predefined inventory, a process also called 'sense labeling'. To measure this behavior, researchers employ a range of datasets, including WiC, SemEval-2007 for validation, and WinoGrande for the specific sub-task of pronoun disambiguation. The datasets 42D and HardEN are also used to evaluate performance in diverse or out-of-distribution contexts. The general concept is applied to specialized domains, including 'lexical disambiguation' in translation, 'charge disambiguation' in legal text, and 'pun interpretation' to distinguish literal and figurative meanings. The behavior is also studied in relation to 'Zero-shot cross-lingual transfer' and 'Knowledge forgetting'.

## Sources

**[Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf)**
> Determining whether a target word is used with the same sense in two different sentences.

**[Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.45.pdf) (as "Sense labeling")**
> The task of assigning a specific sense label from a predefined inventory to a polysemous word within a given sentence from a corpus.

**[2025.emnlp-main.1404.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1404.checklist.pdf) (as "Homonym disambiguation")**
> The task of identifying the correct meaning of a word that has the same spelling or pronunciation as another word but a different meaning, based on its context.

**[Synth-SBDH: A Synthetic Dataset of Social and Behavioral Determinants of Health for Clinical Text](https://aclanthology.org/2025.emnlp-main.1419.pdf) (as "Pun interpretation")**
> The observable task of associating each word in an identified pun pair with its correct meaning or sense in the given context.

**[Synth-SBDH: A Synthetic Dataset of Social and Behavioral Determinants of Health for Clinical Text](https://aclanthology.org/2025.emnlp-main.1419.pdf) (as "Word-sense association")**
> Linking a word to its correct meaning in context, particularly distinguishing between literal and figurative senses in puns.

**[FoREST: Frame of Reference Evaluation in Spatial Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf) (as "Polysemy disambiguation")**
> Producing a binary judgment on whether a polysemous word is used in the same sense across two different sentences.

**[2025.emnlp-main.1773.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1773.checklist.pdf) (as "Sense-aware task performance")**
> The observable behavior of correctly interpreting and processing text by disambiguating the meaning of words based on their context.

**[Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.188.pdf) (as "Charge disambiguation")**
> Distinguishing between similar criminal charges by analyzing differences in their four-element structures.

**[JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf) (as "Lexical disambiguation")**
> Selecting the correct translation of a word with multiple meanings based on domain context during translation.

**[Latent Inter-User Difference Modeling forLLMPersonalization](https://aclanthology.org/2025.emnlp-main.537.pdf) (as "Pronoun disambiguation")**
> The task of correctly identifying the antecedent of a pronoun in a sentence, often requiring commonsense understanding.

## Relationships

### Word sense disambiguation →
- **WiC** (measurements) — *measured_by*
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  > Winogrande (Sakaguchi et al., 2021), a large-scale adversarial dataset for testing pronoun disambiguation through commonsense reasoning; (Section 4.1)
  - [Latent Inter-User Difference Modeling forLLMPersonalization](https://aclanthology.org/2025.emnlp-main.537.pdf)
- **SemEval-2007** (measurements) — *measured_by*
  > Concretely, we replace the original SemCor training set with our silver datasets and use SemEval-2007 (Pradhan et al., 2007) as the validation set. (Section 3.3)
  - [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.45.pdf)
- **42D** (measurements) — *measured_by*
  > General-domain test sets: includes 42D and HardEN. These sets are designed to challenge models in diverse, unfamiliar, or out-of-distribution contexts. (Section 4.1)
  - [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.45.pdf)
- **HardEN** (measurements) — *measured_by*
  > General-domain test sets: includes 42D and HardEN. These sets are designed to challenge models in diverse, unfamiliar, or out-of-distribution contexts. (Section 4.1)
  - [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.45.pdf)

### Associated with
- **Zero-shot cross-lingual transfer** (behaviors tasks)
  > “Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks”
  - [2025.emnlp-main.1773.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1773.checklist.pdf)
- **Knowledge forgetting** (constructs)
  - [MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1720.pdf)
