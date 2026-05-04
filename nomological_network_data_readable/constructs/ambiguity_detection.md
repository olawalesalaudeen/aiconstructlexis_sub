# Ambiguity detection
**Type:** Construct  
**Referenced in:** 10 papers  
**Also known as:** Ambiguity identification, Ambiguity recognition, Ambiguous EDU identification  

## State of the Field

Across the provided literature, ambiguity detection is consistently framed as a latent ability of a model to recognize when an input, such as a question, statement, or discourse unit, has multiple valid interpretations or is unclear. The most prevalent operationalization of this construct is in the visual question answering domain, where it is measured by a model's capacity to ask for clarification for an ambiguous question while directly answering a clear one. For instance, studies evaluate this by mixing ambiguous and non-ambiguous questions from the ClearVQA benchmark or by measuring the rate of explicit responses that acknowledge uncertainty on benchmarks like RACQUET. Other work operationalizes this ability in text-based tasks, such as identifying ambiguous wording in summary claims or detecting unclear elementary discourse units (EDUs) within a sentence. A distinct application frames ambiguity identification as a prerequisite for exploiting loopholes, where, as one paper notes, models "explicitly identify and reason about both ambiguity and conflicting goals." The construct is also studied in relation to coreference resolution, with one paper observing a "persistent tension" where high performance on unambiguous tasks may be accompanied by lower performance in detecting ambiguity.

## Sources

**[Pre-training Distillation for Large Language Models: A Design Space Exploration](https://aclanthology.org/2025.acl-long.182.pdf)**
> The latent ability of a model to recognize when a visual question is ambiguous and requires clarification before answering.

**[DnDScore: Decontextualization and Decomposition for Factuality Verification in Long-Form Text Generation](https://aclanthology.org/2025.emnlp-main.1206.pdf) (as "Ambiguity recognition")**
> The latent ability of a model to detect when a question is referentially ambiguous due to multiple possible referents in an image and to respond appropriately by acknowledging uncertainty.

**[Analyzing and ModelingLLMResponse Lengths with Extreme Value Theory: Anchoring Effects and Hybrid Distributions](https://aclanthology.org/2025.emnlp-main.1677.pdf) (as "Ambiguity identification")**
> The latent ability to recognize when a statement or instruction has multiple possible, valid interpretations.

**[LASER: AnLLM-basedASRScoring and Evaluation Rubric](https://aclanthology.org/2025.emnlp-main.1258.pdf) (as "Ambiguous EDU identification")**
> Detecting discourse units within a sentence that are unclear or uninterpretable without additional context, typically subordinate units in discourse relations.

## Relationships

### Associated with
- **Coreference resolution** (behaviors tasks)
  > Across all prompts we observe a persistent tension: high performance in Correct-Unamb tends to be accompanied by lower performance in Detect-Ambig, and vice versa. (Section 6)
  - [A Comprehensive Framework to Operationalize Social Stereotypes for ResponsibleAIEvaluations](https://aclanthology.org/2025.emnlp-main.1527.pdf)
