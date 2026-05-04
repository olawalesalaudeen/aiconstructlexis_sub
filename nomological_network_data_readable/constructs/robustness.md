# Robustness
**Type:** Construct  
**Referenced in:** 763 papers  
**Also known as:** Model robustness, Bias resistance, Hidden representation stability, Molecular stability, Unlearning Stability, Training instability, Routing stability, Feature learning stability, Multi-turn stability, Policy stability, Vision feature stability, Attention entropy stability, Recursive stability, Content safety, Temporal generalizability, Error tolerance, Response consistency, Stylistic self-consistency, Instruction sensitivity, Typo-fixing, Performance stability, Attention stabilization, Robustness to corruption, Robustness to weight perturbations, Robustness to strategic manipulation, Distributional robustness, Domain-specific robustness, Unlearning robustness, Representational robustness, Visual robustness, Cross-modal representation robustness, Robustness to data heterogeneity, Robustness to semantic perturbation, Robustness to noisy feedback, Training-time robustness, Judgment robustness, Robustness to matrix layout, Random-label robustness, Circuit robustness, Robustness to distractors, Distributional shift robustness, Pruning robustness, Distraction susceptibility, Invariance from irrelevant context, Distractibility  

## State of the Field

Robustness is a widely characterized construct in the provided literature, with the dominant framing being the stability of model performance under various forms of perturbation. The most prevalent definition, cited across a large number of papers, specifically concerns stability against variations in prompt engineering, such as changes to in-context example selection, order, and template design. Many studies operationalize this by measuring performance consistency when inputs are subjected to noise, paraphrasing, or distribution shifts; for example, one paper finds that models are "vulnerable to option position changes in MCQs" ("Large Language Models Are Not Robust Multiple Choice Selectors"). Other work evaluates robustness by testing against out-of-distribution opponents, hard negative examples, or ambiguous task specifications.

A smaller but recurring set of studies applies the concept of stability to different aspects of the model lifecycle and internal dynamics. This includes framings like "Training stability," which refers to the absence of loss spikes, and "Representational stability," defined as the consistency of token representations across different training runs. The term is also used to describe the resilience of specific features, such as the persistence of a backdoor after fine-tuning or the detectability of a watermark after text editing. In the context of model alignment, robustness is frequently discussed as the ability to maintain safe behavior against adversarial or "jailbreaking" prompts. For autonomous agents, the construct is often characterized as the capacity to reliably complete tasks in dynamic or challenging web environments.

## Sources

**[NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)**
> The degree to which a model retains its pre-learned general capabilities, such as code generation and problem-solving, after fine-tuning on a specialized task like code editing.

**[Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf) (as "Model robustness")**
> The stability of an LLM's reasoning performance across similar problems, tasks, or perturbations in task conditions.

**[FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf) (as "Bias resistance")**
> The tendency to resist being led into biased outputs when confronted with misleading guidance, biased context, or conflicting instructions.

**[Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/50be7e77b9c883144940be925b608acc-Paper-Conference.pdf) (as "Stability")**
> The property of a decoding algorithm where small perturbations to the model's logits result in only small, bounded changes to the output token probabilities.

**[AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf) (as "Hidden representation stability")**
> The degree to which the internal distribution of hidden states remains invariant after parameter editing.

**[NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3fb6c52aeb11e09053c16eabee74dd7b-Paper-Conference.pdf) (as "Molecular stability")**
> The degree to which generated molecular structures remain chemically stable and adhere to valency constraints.

**[Towards Robust and Parameter-Efficient Knowledge Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3076133f08b40607d00a8f48f6acd71c-Paper-Conference.pdf) (as "Unlearning Stability")**
> The degree to which the optimization process during unlearning avoids divergence or catastrophic forgetting of retained knowledge.

**[Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf) (as "Training stability")**
> The extent to which the learning dynamics remain controlled during training, avoiding catastrophic collapses or divergence in log-likelihoods of responses.

**[SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf) (as "Training instability")**
> A latent property of the LLM training process characterized by disruptions to learning, which can lead to performance degradation or catastrophic divergence.

**[u-$\mu$P: The Unit-Scaled Maximal Update Parametrization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e3130a164f5c724e37271b93bc76dd28-Paper-Conference.pdf) (as "Numerical stability")**
> The property of a model's training process where the floating-point representations of tensors stay within the valid range of a given numerical format, avoiding overflow or underflow.

**[MoE++: Accelerating Mixture-of-Experts Methods with Zero-Computation Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/7efe88bb4138d602e56637cfcf713654-Paper-Conference.pdf) (as "Routing stability")**
> The consistency and reliability of the expert selection mechanism across different layers and inputs.

**[u-$\mu$P: The Unit-Scaled Maximal Update Parametrization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e3130a164f5c724e37271b93bc76dd28-Paper-Conference.pdf) (as "Feature learning stability")**
> The property of a model's training dynamics where different components learn at balanced rates, avoiding situations where some parts learn too quickly or slowly relative to others.

**[SysBench: Can LLMs Follow System Message?](https://proceedings.iclr.cc/paper_files/paper/2025/file/b917f916e7eed84ffe8f5e63492b2be8-Paper-Conference.pdf) (as "Multi-turn stability")**
> The degree to which an LLM maintains adherence to system-message constraints over successive dialogue turns.

**[WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c66e1fcc9691aae706250638f36f681b-Paper-Conference.pdf) (as "Policy stability")**
> The degree to which the agent's policy avoids excessive drift across training phases while still improving on new tasks.

**[PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf) (as "Representational stability")**
> The consistency of token representations across seeds and training checkpoints, indicating how similar internal states remain under varying initial conditions.

**[Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf) (as "Vision feature stability")**
> The property of a vision encoder to produce consistent and unvarying feature representations when the semantic content of an input image remains unchanged despite mild perturbations.

**[ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf) (as "Attention entropy stability")**
> The tendency for the model's attention distribution to remain from becoming overly diffuse as context length increases.

**[A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf) (as "Recursive stability")**
> A property of a generative model in a self-consuming training loop that quantifies how much its output distribution changes in response to small perturbations in the initial real dataset across multiple generations.

**[A Survey ofQUDModels for Discourse Processing](https://aclanthology.org/2025.naacl-long.85.pdf) (as "Safety")**
> The overall property of a model to avoid generating harmful, offensive, or risky content and to align with human values.

**[A Survey ofQUDModels for Discourse Processing](https://aclanthology.org/2025.naacl-long.85.pdf) (as "Trustworthiness")**
> The broader latent quality of being reliable and safe across multiple risk dimensions, including harmfulness, bias, and other safety concerns.

**[Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf) (as "Content safety")**
> The latent tendency of an LLM to avoid unsafe, harmful, or policy-violating content in human interactions.

**[Large Language Models Share Representations of Latent Grammatical Concepts Across Typologically Diverse Languages](https://aclanthology.org/2025.naacl-long.313.pdf) (as "Temporal generalizability")**
> The ability of a classification model to maintain performance when applied to future data that may exhibit distributional shifts over time.

**[DS2-ABSA: Dual-Stream Data Synthesis with Label Refinement for Few-Shot Aspect-Based Sentiment Analysis](https://aclanthology.org/2025.acl-long.753.pdf) (as "Error tolerance")**
> The latent ability of a model to maintain performance quality despite input errors or noise, such as producing coherent summaries from imperfect transcriptions.

**[Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding](https://aclanthology.org/2025.emnlp-main.290.pdf) (as "Response consistency")**
> The degree to which a model produces structurally, lexically, and logically stable outputs across different instruction styles for the same underlying task.

**[Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding](https://aclanthology.org/2025.emnlp-main.290.pdf) (as "Stylistic self-consistency")**
> A model's ability to generate outputs that are stylistically similar to each other when responding to the same problem presented with varied instructions.

**[Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding](https://aclanthology.org/2025.emnlp-main.290.pdf) (as "Instruction sensitivity")**
> The degree to which a model's outputs and performance change when the same task is phrased with different instruction styles.

**[VisCRA: A Visual Chain Reasoning Attack for Jailbreaking Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.313.pdf) (as "Typo-fixing")**
> The latent ability of an LLM to recognize and correct typographical errors in input text by leveraging local and global contextual information to recover the intended meaning.

**[ASTRA: A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization](https://aclanthology.org/2025.emnlp-main.822.pdf) (as "Performance stability")**
> The degree to which a model's performance and internal representations remain consistent across different random initializations or between layers.

**[Tok](https://aclanthology.org/2025.emnlp-main.955.pdf) (as "Attention stabilization")**
> The latent functional role of visual tokens in early layers to absorb attention weights and stabilize attention distributions without contributing meaningful content to the task.

**[SKIM: Any-bit Quantization Pushing The Limits of Post-Training Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25c/bai25c.pdf) (as "Quantization robustness")**
> The degree to which a model maintains performance across varying bit-widths during post-training quantization, reflecting resilience to precision reduction.

**[GaussMark: A Practical Approach for Structural Watermarking of Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/block25a/block25a.pdf) (as "Robustness to corruption")**
> The degree to which a watermark remains detectable after the generated text undergoes token-level or sequence-level modifications such as insertions, deletions, substitutions, or roundtrip translation.

**[Vulnerability-Aware Alignment: Mitigating Uneven Forgetting in Harmful Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25w/chen25w.pdf) (as "Robustness to weight perturbations")**
> The model's stability and ability to maintain performance and safety alignment when its parameters are shifted, such as during the fine-tuning process.

**[De-mark: Watermark Removal in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bq/chen25bq.pdf) (as "Watermark robustness")**
> The degree to which a watermarking scheme resists reverse-engineering, removal, or manipulation by an adversary.

**[Two Tickets are Better than One: Fair and Accurate Hiring Under Strategic LLM Manipulations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cohen25a/cohen25a.pdf) (as "Robustness to strategic manipulation")**
> The ability of a hiring algorithm to maintain fairness and accuracy even when candidates strategically manipulate their application materials using LLMs of varying quality.

**[Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf) (as "Distributional robustness")**
> The stability of a model's performance, particularly its safety and compliance behaviors, when the distribution of input queries changes.

**[MedRAX: Medical Reasoning Agent for Chest X-ray](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fallahpour25a/fallahpour25a.pdf) (as "Domain-specific robustness")**
> The model's ability to maintain performance and reliability when applied to specialized, high-stakes domains like medicine.

**[Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25e/fan25e.pdf) (as "Unlearning robustness")**
> The degree to which an LLM's removal of undesired data influence resists being reversed by adversarial relearning or jailbreaking attacks.

**[Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf) (as "Representational robustness")**
> The extent to which learned audio-text representations remain reliable under variation and noise in the training or input data.

**[Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf) (as "Visual robustness")**
> The degree to which the model's predictions remain stable and accurate under degraded or distorted visual inputs, reflecting reliable integration of visual cues.

**[Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf) (as "Cross-modal representation robustness")**
> The model's robustness in integrating visual and textual information so that performance remains stable across multimodal perturbations.

**[HALoS: Hierarchical Asynchronous Local SGD over Slow Networks for Geo-Distributed Large Language Model Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25y/kim25y.pdf) (as "Robustness to data heterogeneity")**
> The ability of the training framework to maintain stable convergence and performance when workers process non-i.i.d. or highly divergent data distributions.

**[EduLLM: Leveraging Large Language Models and Framelet-Based Signed Hypergraph Neural Networks for Student Performance Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25e/li25e.pdf) (as "Robustness to semantic perturbation")**
> The stability of model performance when exposed to noise or variation in LLM-derived semantic embeddings, reflecting resilience to changes in the underlying language model or input representation.

**[Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cd/li25cd.pdf) (as "Robustness to noisy feedback")**
> The degree to which a planning system maintains performance when exposed to incorrect or misleading environmental feedback during execution.

**[Does Low Rank Adaptation Lead to Lower Robustness against Training-Time Attacks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25f/liang25f.pdf) (as "Training-time robustness")**
> The model's resistance to performance degradation caused by the presence of noisy, poisoned, or backdoor samples in its training data.

**[Aligning with Logic: Measuring, Evaluating and Improving Logical Preference Consistency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25u/liu25u.pdf) (as "Judgment robustness")**
> The degree to which an LLM's preference judgments are stable and resistant to perturbations in input formulation or reasoning path.

**[Reasoning Limitations of Multimodal Large Language Models. A case study of Bongard Problems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/malkinski25a/malkinski25a.pdf) (as "Robustness to matrix layout")**
> The degree to which performance remains stable when the arrangement, aspect ratio, or cropping of the image matrix changes.

**[Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf) (as "Random-label robustness")**
> The ability of a model to maintain in-context learning performance even when labels in the context are randomly permuted, indicating reliance on label presence rather than correct label-to-input mapping.

**[Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ak/wang25ak.pdf) (as "Circuit robustness")**
> The stability of a discovered circuit under dataset perturbations, reflected in how similar its structure remains across noisy variants of the task.

**[VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf) (as "Robustness to distractors")**
> The degree to which a model's performance remains stable when semantically similar but irrelevant frames are inserted near the target information in a video.

**[Unlocking Post-hoc Dataset Inference with Synthetic Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25q/zhao25q.pdf) (as "Distributional shift robustness")**
> The degree to which an inference procedure remains reliable when the held-out data differs slightly from the suspect data in text distribution.

**[Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25c/zhuang25c.pdf) (as "Pruning robustness")**
> The degree to which model performance remains stable when adapter parameters or layers are removed or zeroed out.

**[LLM-Based Explicit Models of Opponents for Multi-Agent Games](https://aclanthology.org/2025.naacl-long.42.pdf) (as "Distraction susceptibility")**
> The tendency of LLMs to fail in recognizing malicious intent due to cognitive overload or contextual interference caused by complex role-playing instructions.

**[MatViX: Multimodal Information Extraction from Visually Rich Articles](https://aclanthology.org/2025.naacl-long.186.pdf) (as "Invariance from irrelevant context")**
> The capacity of an agent to focus on the logical essence of a problem and resist influence from semantically irrelevant or misleading contextual information.

**[Improving Model Evaluation usingSMARTFiltering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.236.pdf) (as "Distractibility")**
> The latent tendency of retrieval-augmented LLMs to be negatively influenced by irrelevant or conflicting information from both external retrieved documents and internal parametric knowledge, impairing accurate response generation.

## Relationships

### Robustness →
- **SVAMP** (measurements) — *measured_by*
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **AdvBench** (measurements) — *measured_by*
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
- **GSM-Hard** (measurements) — *measured_by*
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMBench** (measurements) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **ImageNet-1k** (measurements) — *measured_by*
  - [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf)
- **GAIA** (measurements) — *measured_by*
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **MultiArith** (measurements) — *measured_by*
  - [MAC-Tuning:LLMMulti-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.36.pdf)
- **GRIT** (measurements) — *measured_by*
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
- **MMBench-CN** (measurements) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VQA-v2** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VirtualHome** (measurements) — *measured_by*
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **ALFRED** (measurements) — *measured_by*
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Kangaroo: Lossless Self-Speculative Decoding for Accelerating LLMs via Double Early Exiting](https://proceedings.neurips.cc/paper_files/paper/2024/file/16336d94a5ffca8de019087ab7fe403f-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf)
- **MS MARCO** (measurements) — *measured_by*
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Needle-in-a-haystack test** (measurements) — *measured_by*
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
- **AndroidWorld** (measurements) — *measured_by*
  - [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf)
- **FLASK** (measurements) — *measured_by*
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **FLAN** (measurements) — *measured_by*
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **MUSE** (measurements) — *measured_by*
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)
- **LLaVA-Bench** (measurements) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **GSM-Plus** (measurements) — *measured_by*
  - [Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **SmoothLLM** (measurements) — *measured_by*
  - [One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [DavIR: Data Selection via Implicit Reward for Large Language Models](https://aclanthology.org/2025.acl-long.453.pdf)
- **GCG attack** (measurements) — *measured_by*
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)
- **Jailbreaking** (behaviors tasks) — *causes*
  - [LLM-Based Explicit Models of Opponents for Multi-Agent Games](https://aclanthology.org/2025.naacl-long.42.pdf)
- **BANKING77** (measurements) — *measured_by*
  - [Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.19.pdf)
- **20 Newsgroups** (measurements) — *measured_by*
  - [Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.19.pdf)
- **GrailQA** (measurements) — *measured_by*
  - [Context-Aware Sentiment Forecasting viaLLM-based Multi-Perspective Role-Playing Agents](https://aclanthology.org/2025.acl-long.137.pdf)
- **HANS** (measurements) — *measured_by*
  - [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](https://aclanthology.org/2025.acl-long.1155.pdf)
- **PAWS** (measurements) — *measured_by*
  - [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](https://aclanthology.org/2025.acl-long.1155.pdf)
- **VoxEval** (measurements) — *measured_by*
  - [SimulS2S-LLM: Unlocking Simultaneous Inference of SpeechLLMs for Speech-to-Speech Translation](https://aclanthology.org/2025.acl-long.818.pdf)
- **AgentDojo** (measurements) — *measured_by*
  - [Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue](https://aclanthology.org/2025.acl-long.369.pdf)
- **AgentHarm** (measurements) — *measured_by*
  - [Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue](https://aclanthology.org/2025.acl-long.369.pdf)
- **Copy-paste attack** (measurements) — *measured_by*
  - [CER: Confidence Enhanced Reasoning inLLMs](https://aclanthology.org/2025.acl-long.391.pdf)
- **SQuAD 2.0** (measurements) — *measured_by*
  - [Jailbreaking? One Step Is Enough!](https://aclanthology.org/2025.acl-long.571.pdf)
- **Generalization** (constructs) — *causes*
  - [Promoting Ensemble Diversity with Interactive Bayesian Distributional Robustness for Fine-tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pham25b/pham25b.pdf)
- **RM-Bench** (measurements) — *measured_by*
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)
- **PWWS** (measurements) — *measured_by*
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)
- **Alignment** (constructs) — *causes*
  - [On the Robustness of Reward Models for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25d/hong25d.pdf)
- **Layer pruning** (behaviors tasks) — *measured_by*
  - [Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25c/zhuang25c.pdf)
- **Unstructured pruning** (behaviors tasks) — *measured_by*
  - [Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25c/zhuang25c.pdf)
- **EAP-IG** (measurements) — *measured_by*
  - [Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ak/wang25ak.pdf)
- **FINTRUST** (measurements) — *measured_by*
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **EvolInstruct** (measurements) — *measured_by*
  - [Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1475.pdf)
- **ShareGPT** (measurements) — *measured_by*
  - [Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1475.pdf)
- **RoDEval** (measurements) — *measured_by*
  - [2025.emnlp-main.864.checklist](https://aclanthology.org/attachments/2025.emnlp-main.864.checklist.pdf)

### → Robustness
- **Reasoning** (constructs) — *causes*
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs) — *causes*
  - [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.582.pdf)
- **Planning** (constructs) — *causes*
  - [Think while You Generate: Discrete Diffusion with Planned Denoising](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbf883a744952d4a40591271a58ab9d0-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *causes*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Disentanglement** (constructs) — *causes*
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks) — *causes*
  - [Reward-Guided Prompt Evolving in Reinforcement Learning for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25a/ye25a.pdf)
- **Critique** (behaviors tasks) — *causes*
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **Collaboration** (behaviors tasks) — *causes*
  - [Quantifying Semantic Emergence in Language Models](https://aclanthology.org/2025.acl-long.589.pdf)
- **Uncertainty quantification** (constructs) — *causes*
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *causes*
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
- **Shortcut learning** (constructs) — *causes*
  - [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.416.pdf)
- **Divergent reasoning** (constructs) — *causes*
  - [Flow of Reasoning: Training LLMs for Divergent Reasoning with Minimal Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25k/yu25k.pdf)
- **Model collapse** (constructs) — *causes*
  - [Advancing Personalized Learning with Neural Collapse for Long-Tail Challenge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25f/hu25f.pdf)
- **Invariance** (constructs) — *causes*
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
- **Backtracking** (behaviors tasks) — *causes*
  - [End-to-End Learnable Psychiatric Scale Guided Risky Post Screening for Depression Detection on Social Media](https://aclanthology.org/2025.emnlp-main.202.pdf)
- **Counterfactual reasoning** (constructs) — *causes*
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1158.pdf)

### Associated with
- **Generalization** (constructs)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Overfitting** (constructs)
  - [Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://proceedings.iclr.cc/paper_files/paper/2024/file/fbf1b3765e081251c804da7f508f3b21-Paper-Conference.pdf)
- **Trustworthiness** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Safety** (constructs)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Knowledge transferability** (constructs)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.189.pdf)
- **In-context learning** (constructs)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Adaptability** (constructs)
  - [ComLoRA: A Competitive Learning Approach for Enhancing LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/e993102e60e4484686f0bafe7ba8b8f2-Paper-Conference.pdf)
- **Adversarial robustness** (constructs)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Out-of-distribution robustness** (constructs)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **System 2 thinking** (constructs)
  - [SETLEXSEM CHALLENGE: Using Set Operations to Evaluate the Lexical and Semantic Robustness of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a12909ffd7145c41139ad66ecf20fc0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Truthfulness** (constructs)
  - [MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d9dcd4ebef57f1839d871fe7d891e91-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Financial analysis** (behaviors tasks)
  - [CausalStock: Deep End-to-end Causal Discovery for News-driven Multi-stock Movement Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/54d689d58fe54c92aee2d732fc49fca8-Paper-Conference.pdf)
- **Image restoration** (behaviors tasks)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Personalization** (constructs)
  - [Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf)
- **Visual perception** (constructs)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Causal reasoning** (constructs)
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **Multi-turn dialogue** (behaviors tasks)
  - [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf)
- **Output diversity** (constructs)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Consistency** (constructs)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Retrieval-augmented generation** (behaviors tasks)
  - [Improving Model Evaluation usingSMARTFiltering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.236.pdf)
- **In-context classification** (behaviors tasks)
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
- **Watermark spoofing** (behaviors tasks)
  - [StealthInk: A Multi-bit and Stealthy Watermark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25j/jiang25j.pdf)
- **Efficiency** (constructs)
  - [Beyond Zero Initialization: Investigating the Impact of Non-Zero Initialization on LoRA Fine-Tuning Dynamics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bm/li25bm.pdf)
- **Noise robustness** (constructs)
  - [ROPO: Robust Preference Optimization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25d/liang25d.pdf)
- **Compositional generalization** (constructs)
  - [Coarse-to-Fine Grounded Memory forLLMAgent Planning](https://aclanthology.org/2025.emnlp-main.660.pdf)
- **Error propagation** (constructs)
  - [CMHG: A Dataset and Benchmark for Headline Generation of Minority Languages inChina](https://aclanthology.org/2025.emnlp-main.623.pdf)
- **Fine-grained visual reasoning** (constructs)
  - [NESTFUL: A Benchmark for EvaluatingLLMs on Nested Sequences ofAPICalls](https://aclanthology.org/2025.emnlp-main.1703.pdf)
