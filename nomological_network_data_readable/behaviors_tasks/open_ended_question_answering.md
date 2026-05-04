# Open-ended question answering
**Type:** Behavior  
**Referenced in:** 26 papers  
**Also known as:** Open-ended answer generation, Free-form question answering, Free-text response generation  

## State of the Field

Across the provided literature, open-ended question answering is most commonly defined as the task of generating comprehensive, detailed, and human-like responses to questions that do not have a predefined or fixed set of possible answers. This framing is frequently contrasted with close-ended formats like multiple-choice questions. Some definitions specify the context, such as generating free-form answers from video or its use in "LLM-as-a-judge" evaluations. The questions associated with this task are often described as lacking a single definitive answer, requiring information synthesis, or involving topics where "a range of valid answers from multiple perspectives exists" (CodeSCM: Causal Analysis for Multi-Modal Code Generation). This behavior is operationalized and measured using a wide variety of benchmarks. These include general knowledge datasets like `TriviaQA` and `Natural Questions`, specialized benchmarks for controversial topics like `ConflictingQA`, and multimodal instruments such as `LLaVA-Bench-in-the-Wild` and `LLaVA-Med`. The task is also studied in relation to other concepts like `Faithfulness` and `Visual question answering`.

## Sources

**[ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://proceedings.iclr.cc/paper_files/paper/2024/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf)**
> The task of providing comprehensive, detailed, and human-like responses to questions that do not have a predefined or fixed set of possible answers.

**[CausalChaos! Dataset for Comprehensive Causal Action Question Answering Over Longer Causal Chains Grounded in Dynamic Visual Scenes](https://proceedings.neurips.cc/paper_files/paper/2024/file/a89558069b44ae56ee0daf1f32aae1f6-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Open-ended answer generation")**
> The task of generating a free-form natural language answer to a question based on a video, without being provided a set of options.

**[Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26d4fbaf7dfa115f1d4b3f104e26bce-Paper-Conference.pdf) (as "Free-form question answering")**
> Generating answers to questions without restricted formats or multiple-choice constraints.

**[Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf) (as "Free-text response generation")**
> Generating open-ended textual answers to questions without predefined options, used in LLM-as-a-judge evaluations.

## Relationships

### Open-ended question answering →
- **TriviaQA** (measurements) — *measured_by*
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **FairEval** (measurements) — *measured_by*
  > We evaluate ChatEval on two benchmarks, FairEval and Topical-Chat which represent the categories of open-ended question answer and dialogue response generation, respectively. (Section 3)
  - [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://proceedings.iclr.cc/paper_files/paper/2024/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf)
- **AmbigNQ** (measurements) — *measured_by*
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **EHRNoteQA** (measurements) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [LongReward: Improving Long-context Large Language Models withAIFeedback](https://aclanthology.org/2025.acl-long.188.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing](https://aclanthology.org/2025.acl-long.625.pdf)
- **SciQ** (measurements) — *measured_by*
  - [LongReward: Improving Long-context Large Language Models withAIFeedback](https://aclanthology.org/2025.acl-long.188.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
- **ConflictingQA** (measurements) — *measured_by*
  > To measure the semantic diversity of LLMs’ outputs before and after alignment, we chose two datasets containing open-ended questions where a range of valid answers from multiple perspectives exists. CONFLICTINGQA (Wan et al., 2024) consists of short questions on controversial topics. (Section 2.2)
  - [CodeSCM: Causal Analysis for Multi-Modal Code Generation](https://aclanthology.org/2025.naacl-long.346.pdf)
- **WikiQA** (measurements) — *measured_by*
  - [LongReward: Improving Long-context Large Language Models withAIFeedback](https://aclanthology.org/2025.acl-long.188.pdf)
- **LLaVA-Bench-in-the-Wild** (measurements) — *measured_by*
  > we mainly used LLaVA v1.5 (Liu et al., 2024a) and LLaVA NeXT (Liu et al., 2024b) in 7B and 13B sizes and evaluated them on the LLaVA-Bench COCO and LLaVA-Bench Wild (Liu et al., 2023) datasets to assess open-ended generation quality.
  - [Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oh25a/oh25a.pdf)
- **LLaVA-Med** (measurements) — *measured_by*
  > we adopt LLaVA-Med instruction dataset (Li et al., 2024) as a domain-specific open-ended benchmark on the medical images and corresponding questions. (Section 5)
  - [Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oh25a/oh25a.pdf)

### Associated with
- **Truthfulness** (constructs)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  - [VRSBench: A Versatile Vision-Language Benchmark Dataset for Remote Sensing Image Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/05b7f821234f66b78f99e7803fffa78a-Paper-Datasets_and_Benchmarks_Track.pdf)
