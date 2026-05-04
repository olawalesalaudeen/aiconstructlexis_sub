# Hallucination
**Type:** Behavior  
**Referenced in:** 496 papers  
**Also known as:** Hallucinated response generation, Factuality hallucination, Hallucinated tool calling, Hallucinated object generation, Untruthful response generation, Soliloquizing, Hallucinatory success, Hallucinated answer generation, Hallucinated content generation, Confusion, Generating false preambles, Non-factual response generation, Hallucinated reasoning, Hallucinated geometry, Hallucinated citations, Object existence determination, Reasoning hallucinations, Reference reliability, Long-term knowledge recall, Anti-hallucination, Hallucination resistance, Cross-modal hallucination, Multimodal hallucination, Hallucination tendency  

## State of the Field

Across the surveyed literature, Hallucination is predominantly characterized as the observable behavior of a model generating factually incorrect, nonsensical, or ungrounded information not supported by its input or real-world facts. While this is the prevailing usage, a smaller line of work frames it as a latent "tendency" or "propensity" to produce such content. The concept is applied across numerous specific failure modes, including "hallucinated tool calling," "hallucinated reasoning," and "hallucinated citations." In multimodal contexts, the behavior is frequently specified as generating text inconsistent with visual or audio inputs, with common variants being "object hallucination" and "cross-modal hallucination." The field operationalizes this behavior most frequently through benchmarks for vision-language models, such as POPE, which uses yes/no questions to probe for the existence of objects, and CHAIR, which assesses ungrounded objects in image captions. For factual errors in text, it is commonly measured with benchmarks like TruthfulQA, which tests models against common misconceptions, and HaluEval, which uses synthetic data for detection. Hallucination is consistently treated as an inverse of `Faithfulness` and `Consistency` and is often described as a failure of `Visual grounding`. Some papers report that it can be caused by `Language bias` or `Multimodal misalignment`, and it is frequently studied alongside mitigation techniques like retrieval-augmented generation.

## Sources

**[Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)**
> The observable act of a model generating factually incorrect or nonsensical information that is not grounded in its input or training data.

**[Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf) (as "Misinformation generation")**
> Producing incorrect factual content as an observable failure mode linked to model collapse.

**[Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf) (as "Hallucinated response generation")**
> The observable behavior of a model producing a factually incorrect or speculative response to a question, particularly when the question's premise is not supported by the video content.

**[GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models](https://aclanthology.org/2025.acl-long.256.pdf) (as "Factuality hallucination")**
> The specific observable behavior where a model's generated output diverges from established real-world facts.

**[Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf) (as "Hallucinated tool calling")**
> The observable generation of invalid tool calls, including fabricated tools, incorrect parameters, or redundant invocations not grounded in the user input or task requirements.

**[LLMScan: Causal Scan for LLM Misbehavior Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25al/zhang25al.pdf) (as "Untruthful response generation")**
> The observable act of an LLM producing a factually incorrect answer, such as stating 'Paris' as the capital of the Roman Republic when instructed to lie.

**[Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf) (as "Hallucinated object generation")**
> The observable output of referring to objects in an image that are not actually present, as evidenced by incorrect affirmative answers or false descriptions.

**[EnIGMA: Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramovich25a/abramovich25a.pdf) (as "Soliloquizing")**
> An observable phenomenon where a language model self-generates a complete thought-action-observation loop, including a hallucinated observation, in a single response without interacting with the environment.

**[What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf) (as "Hallucinatory success")**
> Incorrectly concluding that a task has been completed when key steps remain unexecuted, often due to weak contextual memory.

**[Unveiling Internal Reasoning Modes inLLMs: A Deep Dive into Latent Reasoning vs. Factual Shortcuts with Attribute Rate Ratio](https://aclanthology.org/2025.emnlp-main.112.pdf) (as "Hallucinated content generation")**
> The observable behavior of generating factually incorrect or counterfactual statements, often as the target of a truthfulness steering intervention.

**[Ask Patients with Patience: EnablingLLMs for Human-Centric Medical Dialogue with Grounded Reasoning](https://aclanthology.org/2025.emnlp-main.143.pdf) (as "Hallucinated answer generation")**
> The process of generating factually incorrect but plausible medical answers using specific hallucination types such as misinterpretation, incomplete information, mechanism misattribution, or evidence fabrication.

**[Large Language Models as Realistic Microservice Trace Generators](https://aclanthology.org/2025.emnlp-main.5.pdf) (as "Confusion")**
> The introduction of factual errors in the simplified text that contradict the original, such as reversing the direction of a requirement (e.g., claiming the opposite of what the source states).

**[CiteBART: Learning to Generate Citations for Local Citation Recommendation](https://aclanthology.org/2025.emnlp-main.90.pdf) (as "Generating false preambles")**
> An observable error where the model generates non-existent or invalid preambles, such as library imports, for a formal code block.

**[Procedural Environment Generation for Tool-Use Agents](https://aclanthology.org/2025.emnlp-main.937.pdf) (as "Non-factual response generation")**
> The observable behavior in which an LLM produces an answer to a fact-seeking question that fails to convey the correct, verifiable fact.

**[UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1544.pdf) (as "Hallucinated reasoning")**
> Producing reasoning steps that are not supported by the input evidence, involving fabricated or incorrect justifications for outputs.

**[Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries](https://aclanthology.org/2025.emnlp-main.816.pdf) (as "Hallucinated geometry")**
> Generating confident but unfounded claims about object size, position, or visibility that are inconsistent with the actual scene structure.

**[Retrieval-Augmented Generation with Estimation of Source Reliability](https://aclanthology.org/2025.emnlp-main.1739.pdf) (as "Hallucinated citations")**
> An observable error where a model cites legal sections that are irrelevant or non-existent in its generated answer.

**[LibEvolutionEval: A Benchmark and Study for Version-Specific Code Generation](https://aclanthology.org/2025.naacl-long.349.pdf) (as "Object existence determination")**
> The model's latent capability to correctly identify whether a specified object is present or absent in a given image.

**[Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf) (as "Reasoning hallucinations")**
> The latent tendency of LLMs to generate reasoning steps in natural language that are inconsistent with the logic of generated programs, manifesting as logical errors, missing steps, or misordered connections despite seemingly correct justifications.

**[POINTS-Reader: Distillation-Free Adaptation of Vision-Language Models for Document Conversion](https://aclanthology.org/2025.emnlp-main.83.pdf) (as "Reference reliability")**
> The latent ability of a model to generate citations that correspond to real, existing academic publications with accurate metadata.

**[Context-Aware Hierarchical Taxonomy Generation for Scientific Papers viaLLM-Guided Multi-Aspect Clustering](https://aclanthology.org/2025.emnlp-main.789.pdf) (as "Long-term knowledge recall")**
> The latent ability to access and retrieve stored factual knowledge about the world, such as historical, scientific, or geographical facts, independent of the current context.

**[Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cb66be286795d71f89367d596bf78ea7-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Anti-hallucination")**
> The latent tendency to avoid generating unsupported or false content in multimodal outputs.

**[MKGL: Mastery of a Three-Word Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe03053bd2cf5b5c56de1e463bc53e1a-Paper-Conference.pdf) (as "Hallucination resistance")**
> The tendency to avoid factually incorrect or nonsensical outputs when generating or completing knowledge graph facts.

**[AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc685788a311fa35d8d41df93e288ca-Paper-Conference.pdf) (as "Cross-modal hallucination")**
> A phenomenon where a model generates outputs based on cross-interactions between modalities that are not present in the input signals, such as hearing imaginary sounds from visual cues or seeing fake events from audio cues.

**[Mitigating Modality Prior-Induced Hallucinations in Multimodal Large Language Models via Deciphering Attention Causality](https://proceedings.iclr.cc/paper_files/paper/2025/file/86fe62e3b315d2578721562d9fd1a433-Paper-Conference.pdf) (as "Multimodal hallucination")**
> A failure mode in Multimodal Large Language Models where the generated output contains information that is inconsistent with or absent from the provided multimodal inputs.

**[Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf) (as "Object hallucination")**
> The tendency of a Large Vision-Language Model to generate textual responses that are not factually aligned with the visual input, such as describing objects that are not present.

**[Routing Experts: Learning to Route Dynamic Experts in Existing Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49a4829a2ccaaa4706cc82e68c39a9c6-Paper-Conference.pdf) (as "Visual hallucination")**
> A failure mode where the model generates text describing objects, attributes, or relationships that are not present in the input image.

**[From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf) (as "Hallucination tendency")**
> The latent propensity of the model to generate factually incorrect or unsupported content, potentially encouraged by finetuning data.

## Relationships

### Hallucination →
- **POPE** (measurements) — *measured_by*
  > Moreover, POPE (Li et al., 2023d) results show our method could mitigate object hallucinations. (Section 5.2)
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
- **CHAIR** (measurements) — *measured_by*
  > CHAIR (Rohrbach et al., 2018) evaluates object hallucinations in open-ended captioning tasks (Section 4.1).
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > TruthfulQA (Lin et al., 2022) and HaluEval (Li et al., 2023) for factual reasoning and ARC-Challenge (Clark et al., 2018) for scientific reasoning (Section 4.1, Datasets).
  - [Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf)
- **MM-Hal-Bench** (measurements) — *measured_by*
  > Moreover, we conduct experiments on several hallucination benchmarks such as ... MMHal-Bench (Sun et al., 2023). (Section 4.1)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
- **HaluEval** (measurements) — *measured_by*
  > TruthfulQA (Lin et al., 2022) and HaluEval (Li et al., 2023) for factual reasoning and ARC-Challenge (Clark et al., 2018) for scientific reasoning (Section 4.1, Datasets).
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AMBER** (measurements) — *measured_by*
  > AMBER (Wang et al., 2023a) further extends POPE by evaluating not just existence but also attribute and relation hallucinations. (Section 3.2).
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **HallusionBench** (measurements) — *measured_by*
  > We evaluate our each variant of ROSS mainly on (i) hallucination: POPE (Li et al., 2023c) and HallusionBench (Guan et al., 2024) (Section 5.1)
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > The GPT-4V-aided evaluation shown in Table 4 further confirms that our method enhances both the accuracy and detailedness of the generated response, outperforming other hallucination mitigation approaches (Section 4.2).
  - [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  > “MME (Fu et al., 2023) and MMBench (Liu et al., 2023b) benchmarks are employed to assess the LVLM’s general ability.”
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
- **Object HalBench** (measurements) — *measured_by*
  > Moreover, we conduct experiments on several hallucination benchmarks such as ... Object HalBench (Yu et al., 2024a) (Section 4.1)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > Due to incomplete text annotations on the MMHal, GPT-4 couldn't reliably detect hallucinations. To make the results more reliable, we invited experts to manually annotate the data
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **SelfCheckGPT** (measurements) — *measured_by*
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **GAVIE** (measurements) — *measured_by*
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [Interpretation Meets Safety: A Survey on Interpretation Methods and Tools for ImprovingLLMSafety](https://aclanthology.org/2025.emnlp-main.1092.pdf)
- **Uncertainty** (constructs) — *correlates*
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
- **APIBench** (measurements) — *measured_by*
  - [Tool-Planner: Task Planning with Clusters across Multiple Tools](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f605d59a0dbde101518b552cb616ddf-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  > State-of-the-art MLLMs suffer severe hallucination on geometric figures, which greatly hinders their abilities on solving geometric problems. (Figure 1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **FactScore** (measurements) — *measured_by*
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.622.pdf)
- **Reliability** (constructs) — *causes*
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **Faithfulness** (constructs) — *causes*
  - [Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf)
- **zs-RE** (measurements) — *measured_by*
  - [Stealth edits to large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c8168a8eca2eb23f6b1f5019371043e-Paper-Conference.pdf)
- **RAGTruth** (measurements) — *measured_by*
  - [LLM-Check: Investigating Detection of Hallucinations in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c1e1fdf305195cd620c118aaa9717ad-Paper-Conference.pdf)
- **Truthfulness** (constructs) — *causes*
  - [CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://proceedings.neurips.cc/paper_files/paper/2024/file/5acd3c628aa1819fbf07c39ef73e7285-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLongBench-Doc** (measurements) — *measured_by*
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BFCL** (measurements) — *measured_by*
  > Accuracy performance comparison on BFCL-v3 leaderboard (updated on 09/20/2024). ... Hallucination (Table 2)
  - [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)
- **MMMU** (measurements) — *correlates*
  > We also include self-reported MMMU (Yue et al., 2024) results to demonstrate their significant correlation with hallucination rates: the Pearson correlation between −log HT and MMMU score is 0.902 with a p-value of 3.45×10−4. (Table 2)
  - [TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf)
- **LLMEval** (measurements) — *measured_by*
  > Then, for each example, we can rate it as “correct” or “abstain” or “hallucinate” depending on the LLMEval output. (Section 4.2)
  - [Sufficient Context: A New Lens on Retrieval Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf)
- **Safety** (constructs) — *correlates*
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
- **Predictive uncertainty** (constructs) — *correlates*
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Logit lens** (measurements) — *measured_by*
  - [ActionStudio: A Lightweight Framework for Data and Training of Large Action Models](https://aclanthology.org/2025.emnlp-main.1091.pdf)
- **Model uncertainty** (constructs) — *correlates*
  > we first conduct an uncertainty analysis, revealing a strong positive correlation between hallucination and model uncertainty. (Abstract)
  - [CIKT: A Collaborative and Iterative Knowledge Tracing Framework with Large Language Models](https://aclanthology.org/2025.emnlp-main.976.pdf)
- **BLINK** (measurements) — *measured_by*
  - [MatViX: Multimodal Information Extraction from Visually Rich Articles](https://aclanthology.org/2025.naacl-long.186.pdf)
- **Complex reasoning** (behaviors tasks) — *causes*
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.192.pdf)
- **LongFact** (measurements) — *measured_by*
  > Factuality hallucination benchmark: BioGEN (Min et al., 2023) and LongFact (Wei et al., 2024b); (Section 4.1)
  - [LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios](https://aclanthology.org/2025.acl-long.804.pdf)
- **SAFE** (measurements) — *measured_by*
  > We quantify LLM hallucinations using two public metrics: FActScore (Min et al., 2023) and SAFE (Wei et al., 2024). In contrast, SAFE employs a language model as an investigative agent that iteratively employs Google Search queries to assess whether search results support the fact.
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.622.pdf)
- **FaithEval** (measurements) — *measured_by*
  > As shown in Table 5, the ablation study on FaithEval (Ming et al., 2024) demonstrates that OpAmp not only enhances robustness to noisy contexts but also reduces hallucinations as a valuable secondary benefit. (Section 3.4)
  - [MadaKV: Adaptive Modality-PerceptionKVCache Eviction for Efficient Multimodal Long-Context Inference](https://aclanthology.org/2025.acl-long.653.pdf)
- **Verbalized confidence** (measurements) — *measured_by*
  - [From Scores to Steps: Diagnosing and ImprovingLLMPerformance in Evidence-Based Medical Calculations](https://aclanthology.org/2025.emnlp-main.549.pdf)
- **Activation patching** (measurements) — *measured_by*
  - [ActionStudio: A Lightweight Framework for Data and Training of Large Action Models](https://aclanthology.org/2025.emnlp-main.1091.pdf)

### → Hallucination
- **Faithfulness** (constructs) — *causes*
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
- **Visual perception** (constructs) — *causes*
  > This gap in perception causes hallucinations, resulting in incorrect responses. (Section 4.1)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **Language bias** (constructs) — *causes*
  > LVLMs suffer from hallucinations caused by language bias, which neglects images while over-relying on text. (Abstract)
  - [Do It Yourself (DIY): Modifying Images for Poems in a Zero-Shot Setting Using Weighted Prompt Manipulation](https://aclanthology.org/2025.emnlp-main.995.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbe6dd68b0cf2b1d43b458d2b8ca31b0-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  > Asking the Constructor to complete the whole chain reduces hallucination, and avoids a sub-optimal greedy approach. (Section 3.2)
  - [LoGU: Long-form Generation with Uncertainty Expressions](https://aclanthology.org/2025.acl-long.929.pdf)
- **Overconfidence** (constructs) — *causes*
  > Overconfidence on Unknown Knowledge LLMs often show overconfidence when addressing topics beyond their knowledge, delivering assertive but incorrect responses. ... LLMs perform poorly on unfamiliar topics while maintaining high confidence (Agarwal et al., 2023; Deng et al., 2024). (Section 3.2)
  - [LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios](https://aclanthology.org/2025.acl-long.804.pdf)
- **Information extraction** (behaviors tasks) — *causes*
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *causes*
  - [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *causes*
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Conditional text generation** (behaviors tasks) — *causes*
  > Large Language Models (LLMs), when used for conditional text generation, often produce hallucinations, i.e., information that is unfaithful or not grounded in the input context. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Multimodal alignment** (constructs) — *causes*
  > This eventually leads to an increasingly blurred feature during the final layers of the LLM, which weakens the cross-modal alignment between visual and textual cues, ultimately resulting in suboptimal performance and higher degrees of hallucination (Fig. 1).
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Predictive uncertainty** (constructs) — *causes*
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)
- **Knowledge grounding** (constructs) — *causes*
  - [Fictitious Synthetic Data Can Improve LLM Factuality via Prerequisite Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/98ecdc722006c2959babbdbdeb22eb75-Paper-Conference.pdf)
- **Uncertainty quantification** (constructs) — *causes*
  > Overall, we find strong evidence that accounting for weight uncertainty can improve decoding and reduce hallucinations when finetuning and pretraining from scratch, even without computational overhead. (Introduction)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Image reconstruction** (behaviors tasks) — *causes*
  > This approach encourages LMMs to maintain low-level details, thereby enhancing their fine-grained comprehension abilities and reducing hallucinations. (Section 1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Visual grounding** (constructs) — *causes*
  > Several causes of hallucinations have been identified including biased training data (Liu et al., 2023), the inability of vision encoders to accurately ground images (Jain et al., 2024), misalignment among different modalities (Liu et al., 2024b), and insufficient context attention in LLM decoders (Huang et al., 2024; Liu et al., 2024d). (Section 2.2)
  - [CityEQA: A HierarchicalLLMAgent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **Preference learning** (behaviors tasks) — *causes*
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
- **Knowledge boundary awareness** (constructs) — *causes*
  > We propose MAC-Tuning, which separates the learning process of answer and confidence predictions for enhancing knowledge boundary awareness and reducing hallucination.
  - [SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.35.pdf)
- **Verbal uncertainty** (constructs) — *causes*
  > Paper title: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations
  - [2025.emnlp-main.187.checklist](https://aclanthology.org/attachments/2025.emnlp-main.187.checklist.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
- **Factuality** (constructs)
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
- **Truthfulness** (constructs)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Trustworthiness** (constructs)
  - [Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26d4fbaf7dfa115f1d4b3f104e26bce-Paper-Conference.pdf)
- **Reliability** (constructs)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **Multimodal alignment** (constructs)
  - [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks)
  > "we compared with various decoding strategies on the SEEM-annotated MSCOCO and A-OKVQA datasets provided by POPE" and "addressing object hallucinations"
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
- **Factual accuracy** (constructs)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  > Label Rationalization is more prone to hallucinations, so we prefer direct Answer Generation and use rationalizations only if answer generation fails (Sec. 2.2).
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **Image captioning** (behaviors tasks)
  > To strike a balance between the realism and complexity of the experiments, we primarily focus on the generation of objects in image description scenarios (image caption tasks). (Section 2)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Visual grounding** (constructs)
  > they are far from perfect and still suffer from generating hallucinated texts that are not grounded to the reference image. (Section 1)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Autonomous Agents for Collaborative Task under Information Asymmetry](https://proceedings.neurips.cc/paper_files/paper/2024/file/0534abc9e6db91683d82186ef0d68202-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  > This issue is particularly prevalent in tasks such as image captioning and visual question answering (Liu et al., 2023a; Yin et al., 2023; Zhou et al., 2023b; Zhu et al., 2024a; Gunjal et al., 2024), where maintaining coherence between modalities is critical. (Section 2)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs)
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.508.pdf)
- **Abstractive summarization** (behaviors tasks)
  - [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf)
- **Consistency** (constructs)
  > Although prior medical multimodal foundation models have demonstrated promising capabilities on report generation given the radiology image, they still suffer from serious hallucinations by generating factually inaccurate reports
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **Fairness** (constructs)
  - [NaturalBench: Evaluating Vision-Language Models on Natural Adversarial Samples](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e69ff56d0ebff0752ff29caaddc25dd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Misinformation generation** (behaviors tasks)
  - [Can LLM-Generated Misinformation Be Detected?](https://proceedings.iclr.cc/paper_files/paper/2024/file/94bbcb744bbada8808fda05b9d9290d6-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf)
- **Question answering** (behaviors tasks)
  > This paper focuses on fundamental research of ambiguity-caused hallucination in question answering.
  - [2025.emnlp-main.365.checklist](https://aclanthology.org/attachments/2025.emnlp-main.365.checklist.pdf)
- **Explanation generation** (behaviors tasks)
  - [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf)
- **Language bias** (constructs)
  > These findings provide statistical evidence that language bias is closely related to hallucinations in LVLMs.
  - [Contrastive Prompting Enhances Sentence Embeddings inLLMs through Inference-Time Steering](https://aclanthology.org/2025.acl-long.175.pdf)
- **Self-consistency** (measurements)
  - [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf)
- **Knowledge storage** (constructs)
  - [Knowledge Circuits in Pretrained Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6df31b1be98e04be48af8bedb95b499-Paper-Conference.pdf)
- **Alignment** (constructs)
  - [Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf)
- **Metacognition** (constructs)
  - [Perception of Knowledge Boundary for Large Language Models through Semi-open-ended Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/a1e0d6fa0c30b7d4f75dd9c7ed6189f2-Paper-Conference.pdf)
- **Attribution** (constructs)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  > "To mitigate these issues, integrating external knowledge sources through retrieval-augmented generation (RAG) has become a widely adopted and effective paradigm"
  - [Automated Knowledge Graph Construction using Large Language Models and Sentence Complexity Modelling](https://aclanthology.org/2025.emnlp-main.784.pdf)
- **Knowledge retrieval** (behaviors tasks)
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
- **Role-playing** (behaviors tasks)
  - [WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games](https://proceedings.neurips.cc/paper_files/paper/2024/file/9dd4533e7e4e5ed809344280609c5b05-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (constructs)
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Image description** (behaviors tasks)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Uncertainty** (constructs)
  - [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf)
- **Visual understanding** (constructs)
  > Large Vision-Language Models (LVLMs) have demonstrated impressive capabilities in multi-modal understanding, but they frequently suffer from hallucination - generating content inconsistent with visual inputs. (Abstract)
  - [EAC-MoE: Expert-Selection Aware Compressor for Mixture-of-Experts Large Language Models](https://aclanthology.org/2025.acl-long.634.pdf)
- **Evaluation** (behaviors tasks)
  - [Empowering LLM Agents with Zero-Shot Optimal Decision-Making through Q-learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c25de6a9da675464ebb925e430c58325-Paper-Conference.pdf)
- **Retrieval-augmented generation** (behaviors tasks)
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.365.pdf)
- **Knowledge graph completion** (behaviors tasks)
  - [MKGL: Mastery of a Three-Word Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe03053bd2cf5b5c56de1e463bc53e1a-Paper-Conference.pdf)
- **Semantic uncertainty** (constructs)
  - [Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.187.pdf)
- **Document question answering** (behaviors tasks)
  > However, we also observed that autoregressive large language models like GPT-4o-mini tend to hallucinate responses... in answering questions within the privacy policy context.
  - [Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf)
- **Prediction confidence** (constructs)
  > "knowledge hallucination ... generating nonfactual responses with unwarranted confidence"
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **Video detailed captioning** (behaviors tasks)
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
- **Object recognition** (behaviors tasks)
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Counting** (behaviors tasks)
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Attribute recognition** (behaviors tasks)
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Spatial reasoning** (constructs)
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Action prediction** (behaviors tasks)
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Tool use** (behaviors tasks)
  - [Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf)
- **Logical consistency** (constructs)
  - [Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ds/zhang25ds.pdf)
- **Style transfer** (behaviors tasks)
  - [Reliability of Topic Modeling](https://aclanthology.org/2025.naacl-long.135.pdf)
- **Code summarization** (behaviors tasks)
  - [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1480.pdf)
- **Knowledge graph question answering** (behaviors tasks)
  - [PreP-OCR: A Complete Pipeline for Document Image Restoration and EnhancedOCRAccuracy](https://aclanthology.org/2025.acl-long.750.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  > (Zhai et al., 2023) deem that the hallucination in large models is related to the catastrophic forgetting in continual tuning. (Section 5.4. Analysis of Examples)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Error handling** (constructs)
  > An emerging line of research explores alternative steering techniques for error-related properties like truthfulness, and hallucination (Li et al., 2023; Qiu et al., 2024; Wang et al., 2025; Bhattacharjee et al., 2024). (Section 1).
  - [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf)
- **Closed-book question answering** (behaviors tasks)
  > One significant challenge in CBQA is addressing hallucinations-instances where the model generates incorrect or fabricated answers (Section 2).
  - [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.25.pdf)
- **Verbal uncertainty** (constructs)
  > Hallucinations arise from a miscalibration between VU and SU, where the model fails to express its high uncertainty in its generated output. (Section 4)
  - [Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.187.pdf)
- **Text-to-speech synthesis** (behaviors tasks)
  > LLM-based TTS systems face challenges, with hallucinations being a prominent issue (Sahoo et al., 2024; Song et al., 2024; Neekhara et al., 2024a; Borsos et al., 2023).
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1076.pdf)
- **Misalignment** (constructs)
  > Discussed in Section 6 (Limitations) and Appendix A.5 (Error Analysis), where risks such as retrieval failure, hallucinations, misalignment, and layout errors are described.
  - [2025.emnlp-main.1443.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1443.checklist.pdf)
- **Dialogue summarization** (behaviors tasks)
  > Finally, a notable limitation is the persistence of hallucinations in the generation of item recommendation information and dialogue summaries, where the model fabricates features not present in the source content. (Limitations)
  - [MAviS: A Multimodal Conversational Assistant For Avian Species](https://aclanthology.org/2025.emnlp-main.1456.pdf)
- **Definition generation** (behaviors tasks)
  > “the improved accuracy of the definitions, which helps minimize the hallucinations occasionally observed in the pre-trained model.”
  - [MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1720.pdf)
- **Example generation** (behaviors tasks)
  > When prompting the model to generate new examples, we still find gross hallucinations (Section 4.2).
  - [MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1720.pdf)
