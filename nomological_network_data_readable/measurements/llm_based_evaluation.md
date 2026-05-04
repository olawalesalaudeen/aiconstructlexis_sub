# LLM-based evaluation
**Type:** Measurement  
**Referenced in:** 31 papers  
**Also known as:** GPT-4o evaluation, GPT-based evaluation, LLM-powered evaluation, GPT-4o assisted evaluation, Model-Based Evaluation, GPT-based assessment, GPT evaluation, GPT-4o-based evaluation, Llama3-based metric, Model-based evaluation  

## State of the Field

Across the surveyed literature, LLM-based evaluation is a class of automated methods that leverage the language understanding capabilities of a large language model to serve as the primary performance assessor. The prevailing operationalization involves using a powerful model—most frequently GPT-4 or GPT-4o, but also Claude-3.5 Sonnet and Llama3—as an automated judge to score or compare the outputs of other models. This process is typically guided by structured prompts and predefined criteria, with assessment delivered via Likert scales (e.g., 1-5 or 1-10) or through pairwise comparisons. Several papers frame this approach as a proxy for or a "viable alternative to human annotators" ("Rubrik’s Cube: Testing a New Rubric for Evaluating Explanations on theCUBEdataset"), intended to "simulate more realistic evaluation scenarios" ("Better Embeddings with CoupledAdam"). This instrument is used to measure a wide array of constructs, including linguistic qualities like fluency and simplicity, semantic properties such as faithfulness and relevance, and subjective traits like engagingness and helpfulness. It is also applied to evaluate performance on tasks like visual question answering and image captioning. For example, one study uses GPT-4o to assess dialogues on "coherence, engagingness, closeness, and reflectiveness" ("ClusterAttn:KVCache Compression under Intrinsic Attention Clustering"). The dominant usage is for assessing qualities requiring semantic or subjective judgment, capitalizing on the evaluator model's own understanding capabilities.

## Sources

**[NGQA: A Nutritional Graph Question Answering Benchmark for Personalized Health-aware Nutritional Reasoning](https://aclanthology.org/2025.acl-long.297.pdf) (as "GPT-4o evaluation")**
> An automated evaluation procedure that uses the GPT-4o model to assess the fluency and relevance of generated text on a scale from 1 to 5.

**[LESA](https://aclanthology.org/2025.acl-long.1096.pdf) (as "GPT-based evaluation")**
> Automated scoring method using a strong LLM (e.g., GPT-4) to evaluate model responses on a 0–5 scale across multiple conversational abilities, guided by structured prompts and criteria.

**[Rubrik’s Cube: Testing a New Rubric for Evaluating Explanations on theCUBEdataset](https://aclanthology.org/2025.acl-long.1161.pdf) (as "LLM-powered evaluation")**
> An evaluation methodology where a Large Language Model is used to assess the quality of generated text based on predefined criteria, serving as an alternative to human annotators.

**[Agents Under Siege: Breaking Pragmatic Multi-AgentLLMSystems with Optimized Prompt Attacks](https://aclanthology.org/2025.acl-long.477.pdf)**
> A class of evaluation methods that leverage the language understanding capabilities of large language models as the primary criteria for performance assessment.

**[ClusterAttn:KVCache Compression under Intrinsic Attention Clustering](https://aclanthology.org/2025.acl-long.704.pdf) (as "GPT-4o assisted evaluation")**
> An evaluation protocol that uses the GPT-4o model to assess the quality of generated multi-session dialogues based on criteria like coherence, engagingness, closeness, and reflectiveness.

**[Browsing Like Human: A Multimodal Web Agent with Experiential Fast-and-Slow Thinking](https://aclanthology.org/2025.acl-long.698.pdf) (as "Model-Based Evaluation")**
> Evaluation using a large language model (Claude-3.5 Sonnet) to assess instruction adherence in categories requiring semantic or subjective judgment, such as style, tone, and language switching.

**[Better Embeddings with CoupledAdam](https://aclanthology.org/2025.acl-long.1322.pdf) (as "GPT-based assessment")**
> An evaluation procedure that uses a large generative model, such as GPT-4, as an automated evaluator to assess the quality of another model's output in realistic scenarios.

**[Reviving Cultural Heritage: A Novel Approach for Comprehensive Historical Document Restoration](https://aclanthology.org/2025.acl-long.1403.pdf) (as "GPT evaluation")**
> An evaluation protocol that uses a powerful proprietary model, such as GPT-4, as an automated judge to compare and rate the quality of outputs from other models.

**[On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.327.pdf) (as "Llama3-based metric")**
> Evaluation method using Llama3-8B-Instruct to score simplifications on meaning preservation, fluency, and simplicity via prompt-based judgment.

**[Enhancing Multimodal Entity Linking withJaccard Distance-based Conditional Contrastive Learning and Contextual Visual Augmentation](https://aclanthology.org/2025.naacl-long.342.pdf) (as "Model-based evaluation")**
> An automatic evaluation procedure where an LLM (GPT-4) is used to judge the quality of generated research ideas based on predefined criteria, using both Likert scale ratings and pairwise comparisons.

**[Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf) (as "GPT-4o-based evaluation")**
> A comparative evaluation protocol where the GPT-4o model is used to assess and compare the quality of summaries generated by different methods, serving as a proxy for human judgment.

## Relationships

### → LLM-based evaluation
- **Hallucination** (behaviors tasks) — *measured_by*
  - [Interpretation Meets Safety: A Survey on Interpretation Methods and Tools for ImprovingLLMSafety](https://aclanthology.org/2025.emnlp-main.1092.pdf)
- **Fluency** (constructs) — *measured_by*
  - [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.327.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **Knowledge graph completion** (behaviors tasks) — *measured_by*
  - [UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf)
- **Image captioning** (behaviors tasks) — *measured_by*
  - [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-DeviceLLM](https://aclanthology.org/2025.emnlp-main.534.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8a2070082ad05b4deeff4ffb4312a6f-Paper-Conference.pdf)
- **Naturalness** (constructs) — *measured_by*
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **Coherence** (constructs) — *measured_by*
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **Plausibility** (constructs) — *measured_by*
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [Improving Instruction-Following in Language Models through Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3262a4c965ba9888f120d4f9e13478-Paper-Conference.pdf)
- **Meaning preservation** (constructs) — *measured_by*
  - [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.327.pdf)
- **Simplicity** (constructs) — *measured_by*
  - [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.327.pdf)
- **Novelty** (constructs) — *measured_by*
  - [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-DeviceLLM](https://aclanthology.org/2025.emnlp-main.534.pdf)
- **Engagingness** (constructs) — *measured_by*
  > Engagingness (Eng.): assesses the speaker’s ability to maintain the annotator’s interest for a long-term dialogue (Section 5.1, Table 4).
  - [ClusterAttn:KVCache Compression under Intrinsic Attention Clustering](https://aclanthology.org/2025.acl-long.704.pdf)
- **Reasoning quality** (constructs) — *measured_by*
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)
- **Efficiency** (constructs) — *measured_by*
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)
- **Coverage** (constructs) — *measured_by*
  - [Introducing Spotlight: A Novel Approach for Generating Captivating Key Information from Documents](https://aclanthology.org/2025.emnlp-main.1797.pdf)
- **Conversational ability** (constructs) — *measured_by*
  - [SteeringLLMReasoning Through Bias-Only Adaptation](https://aclanthology.org/2025.emnlp-main.468.pdf)
- **Redundancy** (constructs) — *measured_by*
  - [Introducing Spotlight: A Novel Approach for Generating Captivating Key Information from Documents](https://aclanthology.org/2025.emnlp-main.1797.pdf)
