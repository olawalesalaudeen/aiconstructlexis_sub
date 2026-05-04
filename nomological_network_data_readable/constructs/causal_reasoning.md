# Causal reasoning
**Type:** Construct  
**Referenced in:** 43 papers  
**Also known as:** Causal inference, Cause-and-effect reasoning, Causation understanding, Causal importance, Attribution understanding, Causal consistency, Causal concept faithfulness, Causal understanding, Causal relationship modeling, Commonsense causal reasoning  

## State of the Field

Across the provided literature, causal reasoning is most commonly defined as the ability to infer cause-and-effect relationships between events or variables. This ability is studied in various contexts, including from video observations, textual scenarios, and structured data, with a subset of work focusing on "commonsense causal reasoning" in everyday situations. A recurring theme is the distinction between this construct and the identification of mere correlations; several papers elaborate that causal reasoning involves understanding interventions and counterfactuals, with one study noting it "involves working with interventions and counterfactuals" whereas simple recall is "limited to inferring statistical correlations" ("Reasoning Elicitation in Language Models via Counterfactual Feedback"). The field operationalizes and measures this construct using a range of benchmarks, including video-based datasets like ACRE, which uses "blicket detection tests," and text-based instruments such as CREPE, XCOPA, and COPA. The literature also presents more specific framings, such as "causal consistency," which refers to the logical coherence between a model's factual and counterfactual answers. Causal reasoning is studied alongside faithfulness and language proficiency, and some work suggests it enables planning.

## Sources

**[Can Large Language Models Infer Causation from Correlation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b75a7339dfb256ee4b4bec028a6890b-Paper-Conference.pdf)**
> The ability to infer cause-and-effect relationships from observing events and object interactions in a video, such as determining which object activates a device.

**[Limits of Transformer Language Models on Learning to Compose Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e797d5139ad94fc2dc2080c09119f29-Paper-Conference.pdf) (as "Causal inference")**
> The ability to infer cause-and-effect relationships from data, identified as an area where LLMs exhibit failures.

**[OlympicArena: Benchmarking Multi-discipline Cognitive Reasoning for Superintelligent AI](https://proceedings.neurips.cc/paper_files/paper/2024/file/222d2eaf24cf8259a35d6c7130d31425-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Cause-and-effect reasoning")**
> The ability to identify and establish causal relationships between events, understanding reasons and their consequences.

**[Advancing Video Anomaly Detection: A Concise Review and a New Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3c5af1f56fc73eef1ba0f442739f5ca-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Causation understanding")**
> The ability to infer cause-and-effect relationships from contextual information, such as identifying the reasons for an anomalous event in a video.

**[Understanding Information Storage and Transfer in Multi-Modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "Causal importance")**
> The degree to which a layer or component is causally implicated in restoring or producing the correct output.

**[MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf) (as "Attribution understanding")**
> The ability to identify cause-and-effect relations in a video, including causal explanations and counting-related attribution questions.

**[Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5ec50eb177908f21f78ed0d76ed525c-Paper-Conference.pdf) (as "Causal concept faithfulness")**
> The alignment between which high-level concepts causally affect a model's answer and which of those concepts the model's explanation says were influential.

**[Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf) (as "Causal consistency")**
> The property that a model's answers to factual and counterfactual questions about the same context are logically coherent and correctly reflect the underlying causal relationships.

**[Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf) (as "Causal understanding")**
> The latent ability of a system to comprehend the underlying causal structure of an environment, distinct from reflecting mere correlations.

**[LLM Enhancers for GNNs: An Analysis from the Perspective of Causal Mechanism Identification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25o/gao25o.pdf) (as "Causal relationship modeling")**
> The latent ability of a model to capture and represent true cause-and-effect dependencies between variables in the data, as defined by a high-level causal model.

**[LLM-Human Pipeline for Cultural Grounding of Conversations](https://aclanthology.org/2025.naacl-long.49.pdf) (as "Commonsense causal reasoning")**
> The ability to reason about causality in everyday situations, playing a vital role in developing a mental model of reality.

## Relationships

### Causal reasoning →
- **COPA** (measurements) — *measured_by*
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
- **ACRE** (measurements) — *measured_by*
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **CREPE** (measurements) — *measured_by*
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **NExT-QA** (measurements) — *measured_by*
  - [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by ModellingMiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Planning** (constructs) — *causes*
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **STAR** (measurements) — *measured_by*
  - [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by ModellingMiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Coherence** (constructs) — *causes*
  - [Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.306.pdf)
- **Empathetic response generation** (behaviors tasks) — *causes*
  - [Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.306.pdf)
- **COPAL-ID** (measurements) — *measured_by*
  - [Emergent morpho-phonological representations in self-supervised speech models](https://aclanthology.org/2025.emnlp-main.1426.pdf)

### Associated with
- **Causal inference** (behaviors tasks)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
- **Counterfactual reasoning** (constructs)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
- **Video question answering** (behaviors tasks)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf)
- **Visual reasoning** (constructs)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge recall** (behaviors tasks)
  - [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5ec50eb177908f21f78ed0d76ed525c-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  - [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf)
- **Narrative understanding** (constructs)
  - [DRPruning: Efficient Large Language Model Pruning through Distributionally Robust Optimization](https://aclanthology.org/2025.acl-long.1415.pdf)
- **Structural reasoning** (constructs)
  - [Retrieval-Augmented Fine-Tuning With Preference Optimization For Visual Program Generation](https://aclanthology.org/2025.acl-long.1107.pdf)
- **Scientific question answering** (behaviors tasks)
  - [How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf)
- **Physical world understanding** (constructs)
  - [Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schulze-buschoff25a/schulze-buschoff25a.pdf)
