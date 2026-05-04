# Coreference resolution
**Type:** Behavior  
**Referenced in:** 43 papers  
**Also known as:** Pronoun resolution, Co-reference resolution, Pronoun reference resolution, Reference resolution, Anaphora resolution, Argument alignment, Event composition  

## State of the Field

Across the provided literature, coreference resolution is most commonly described as the behavior of identifying which expressions in a text, particularly pronouns, refer to the same real-world entity. A prevalent focus is on linking gendered pronouns to their antecedent professions in Winograd-style sentences, often to study model biases. This behavior is most frequently operationalized and measured using commonsense reasoning benchmarks, with WinoGrande being the most widely cited instrument, followed by WSC and WinoBias. Other datasets mentioned for its evaluation include OntoNotes, MT-Bench, TACT, and XWinograd. While most definitions center on pronoun resolution, a few papers use related terms like "Anaphora resolution" for multi-turn conversations or introduce more complex cross-document tasks like "Argument alignment". Coreference resolution is frequently studied alongside `Stereotyping`, as one paper notes that it can make "gender biases in neural models... visible". A smaller set of papers also suggests that this capability influences other behaviors like `Question answering`, `Text summarization`, and `Information extraction`.

## Sources

**[Are Bert Family Good Instruction Followers?  A Study on Their Potential And Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a13eb0c08247364066e8d86551c3090-Paper-Conference.pdf)**
> The observable behavior of linking gendered pronouns to their correct antecedent profession in Winograd-style sentences, particularly in stereotypical versus anti-stereotypical contexts.

**[metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf) (as "Pronoun resolution")**
> The observable task of correctly identifying the antecedent of a pronoun in a sentence, which requires contextual understanding.

**[Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf) (as "Co-reference resolution")**
> The task of determining which noun phrases or entities in a text refer to the same real-world entity, specifically resolving a pronoun to an occupation.

**[Retrieval-augmentedGUIAgents with Generative Guidelines](https://aclanthology.org/2025.emnlp-main.903.pdf) (as "Pronoun reference resolution")**
> Correctly identifying and resolving ambiguous personal pronouns in spoken utterances by leveraging contextual cues from surrounding sentences.

**[Sketch-of-Thought: EfficientLLMReasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1237.pdf) (as "Reference resolution")**
> Identifying the correct referent of pronouns or noun phrases within a text.

**[We Need to Measure Data Diversity inNLP— Better and Broader](https://aclanthology.org/2025.emnlp-main.446.pdf) (as "Anaphora resolution")**
> The general task of determining the referent of an anaphoric expression, such as a pronoun.

**[DivScore: Zero-Shot Detection ofLLM-Generated Text in Specialized Domains](https://aclanthology.org/2025.emnlp-main.972.pdf) (as "Argument alignment")**
> The observable process of matching arguments from different documents to the same underlying referent by evaluating semantic compatibility and coreference cues.

**[DivScore: Zero-Shot Detection ofLLM-Generated Text in Specialized Domains](https://aclanthology.org/2025.emnlp-main.972.pdf) (as "Event composition")**
> The observable process of clustering document-level events into cross-document event clusters and aligning their arguments through iterative reasoning.

## Relationships

### Coreference resolution →
- **WinoGrande** (measurements) — *measured_by*
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **WSC** (measurements) — *measured_by*
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **WinoBias** (measurements) — *measured_by*
  > WinoBias Zhao et al. (2018) present the dataset containing a WinoGrad scheme (Levesque et al., 2011) examples. ... The task is to identify the coreference link between the pronouns and the correct professional. (Section 2.3)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TACT** (measurements) — *measured_by*
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question answering** (behaviors tasks) — *causes*
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *causes*
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *causes*
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **OntoNotes** (measurements) — *measured_by*
  > Evaluation is conducted on five datasets: WikiHop (multi-hop QA), TriviaQA (open QA), OntoNotes (coreference resolution), Hyperpartisan News Detection (long document classification), and HotpotQA (distractor setting, joint F1).
  - [CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.474.pdf)
- **Information extraction** (behaviors tasks) — *causes*
  > Ablation studies demonstrate that integrating coreference and decomposition increases recall on rare relations by over 20%. (Abstract)
  - [Complex Numerical Reasoning with Numerical Semantic Pre-training Framework](https://aclanthology.org/2025.emnlp-main.783.pdf)
- **XWinograd** (measurements) — *measured_by*
  - [Emergent morpho-phonological representations in self-supervised speech models](https://aclanthology.org/2025.emnlp-main.1426.pdf)

### Associated with
- **Stereotyping** (constructs)
  > As noted by Davis and van Schijndel (2020), gender biases in neural models can be made visible in coreference resolution. (Section 4)
  - [A Comprehensive Framework to Operationalize Social Stereotypes for ResponsibleAIEvaluations](https://aclanthology.org/2025.emnlp-main.1527.pdf)
- **Textual reasoning** (behaviors tasks)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Ambiguity detection** (constructs)
  > Across all prompts we observe a persistent tension: high performance in Correct-Unamb tends to be accompanied by lower performance in Detect-Ambig, and vice versa. (Section 6)
  - [A Comprehensive Framework to Operationalize Social Stereotypes for ResponsibleAIEvaluations](https://aclanthology.org/2025.emnlp-main.1527.pdf)
