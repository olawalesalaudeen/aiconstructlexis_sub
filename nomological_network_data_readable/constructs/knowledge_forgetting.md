# Knowledge forgetting
**Type:** Construct  
**Referenced in:** 149 papers  
**Also known as:** Catastrophic forgetting, Text-only forgetting, Catastrophic Forgetting, Model forgetting, Forgetting, Factual retention, Language attrition, Recency bias, Spurious forgetting, Graceful forgetting, Positional Bias, Primacy bias, Ordering bias, Position bias, Primacy effect, Recency effect, Middle bias, Order bias, Spatial bias  

## State of the Field

Across the surveyed literature, knowledge forgetting is most commonly characterized as the degradation of a model's performance on previously learned tasks or data after it has been updated with new information, a phenomenon frequently termed "catastrophic forgetting." This degradation is often attributed to direct weight updates during adaptation, which can cause models to "lose previously acquired knowledge" ("Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation"). Some work distinguishes this from "spurious forgetting," where performance loss stems from a "misalignment of internal representations" rather than a complete loss of knowledge ("Cost-Optimal Grouped-Query Attention for Long-Context Modeling"). A smaller body of work examines specific manifestations, such as "text-only forgetting" in multimodal models or "language attrition" after fine-tuning on a new language. The concept is also used to describe a distinct set of biases related to information presentation, including "positional bias," where a model's comprehension is influenced by the location of information within its context, often struggling with content "in the middle of inputs" ("SLM-Mod: Small Language Models SurpassLLMs at Content Moderation"). This positional sensitivity is further specified as "primacy bias" (favoring the beginning), "recency bias" (favoring the end), and "order bias" (favoring certain answer positions). The field operationalizes this construct by measuring performance degradation on a wide array of benchmarks, including MMLU, HellaSwag, WinoGrande, SQuAD v1.1, and NaturalQA. Knowledge forgetting is studied in relation to `machine unlearning` and `overfitting`, and some papers report that it can negatively affect model `safety` and `faithfulness`.

## Sources

**[Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf) (as "Catastrophic forgetting")**
> The tendency of direct weight updates to cause a model to lose previously acquired knowledge when adapting to new tasks.

**[Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf) (as "Text-only forgetting")**
> A phenomenon where a Multimodal Large Language Model's performance on text-only tasks degrades significantly after being fine-tuned on multimodal instructions.

**[Bootstrapping Language Models with DPO Implicit Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4de96b9169aa869cc102afe31055e8-Paper-Conference.pdf) (as "Catastrophic Forgetting")**
> The latent risk of the model losing knowledge or capabilities from the initial policy during continual fine-tuning.

**[Sheep’s Skin, Wolf’s Deeds: AreLLMs Ready for Metaphorical Implicit Hate Speech?](https://aclanthology.org/2025.acl-long.815.pdf) (as "Model forgetting")**
> The latent tendency of a model to lose previously modified or learned knowledge after subsequent updates, despite successful initial editing.

**[Towards Style Alignment in Cross-Cultural Translation](https://aclanthology.org/2025.acl-long.1551.pdf) (as "Forgetting")**
> The degradation of a model's performance on previously learned data or tasks after it has been updated with new information.

**[VideoWebArena:  Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf) (as "Factual retention")**
> The ability of an agent to locate and retrieve specific, instruction-relevant pieces of information from within a video to complete a task, even if the information is incidental to the video's main focus.

**[Hierarchical Autoregressive Transformers: Combining Byte- and Word-Level Processing for Robust, Adaptable Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f69eee2fafab3743a3d2ae5981c949f-Paper-Conference.pdf) (as "Knowledge retention")**
> The ability of a model to preserve its performance on previously learned tasks and languages after being further trained on new data.

**[Jigsaw-Puzzles: From Seeing to Understanding to Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1321.pdf) (as "Language attrition")**
> The degradation of a model's ability to generate definitions in languages not included in fine-tuning, despite prior competence in those languages.

**[NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1329.pdf)**
> The degradation of a model's previously acquired knowledge and capabilities after being fine-tuned on a new task or dataset.

**[SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition](https://aclanthology.org/2025.emnlp-main.20.pdf) (as "Recency bias")**
> The tendency of a model, particularly its routing mechanism in a Mixture-of-Experts architecture, to preferentially use its most recently added components or knowledge while neglecting older ones.

**[Cost-Optimal Grouped-Query Attention for Long-Context Modeling](https://aclanthology.org/2025.emnlp-main.273.pdf) (as "Spurious forgetting")**
> A phenomenon where a model's performance on a previously learned task degrades after training on a new task, not due to a complete loss of knowledge but due to a misalignment of internal representations.

**[Merge then Realign: Simple and Effective Modality-Incremental Continual Learning for MultimodalLLMs](https://aclanthology.org/2025.emnlp-main.666.pdf) (as "Graceful forgetting")**
> The ability to enhance learning on a new task by selectively discarding irrelevant or outdated knowledge.

**[Exploring the Role of Large Language Models in Prompt Encoding for Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d68c1d10957c8d21ed9dea209533c5a4-Paper-Conference.pdf) (as "Positional bias")**
> An intrinsic property of decoder-only models where the ability to comprehend and represent information degrades for tokens appearing later in a sequence, due to the causal attention mechanism.

**[From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf) (as "Primacy bias")**
> A form of positional bias where a model is more accurate at retrieving information located at the beginning of the input context.

**[RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf) (as "Positional Bias")**
> A systematic error where evaluation outcomes depend on the order of presentation rather than content quality.

**[ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf) (as "Ordering bias")**
> A tendency for performance to vary depending on the presentation order of premises or statements.

**[Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf) (as "Position bias")**
> A model's latent tendency to give disproportionate weight to information based on its position within the context window, such as favoring content at the beginning or end.

**[Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.448.pdf) (as "Primacy effect")**
> The latent tendency for a model to give greater weight to tokens presented at the beginning of a sequence, influencing later outputs due to early positional salience.

**[Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.448.pdf) (as "Recency effect")**
> The latent tendency for a model to give greater weight to recently presented tokens when generating subsequent outputs, analogous to human short-term memory recall patterns.

**[ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf) (as "Middle bias")**
> The latent tendency of the model to focus disproportionately on a subset of tokens located in the middle of the input sequence, forming a non-uniform attention pattern distinct from sink or recency effects.

**[MemeReaCon: Probing Contextual Meme Understanding in Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.177.pdf) (as "Order bias")**
> The tendency of a model to favor certain answer positions (e.g., A, B, C, D) regardless of content, indicating a vulnerability to the presentation order of options rather than genuine comprehension.

**[Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.501.pdf) (as "Spatial bias")**
> The tendency of models to systematically favor predictions in certain geographic regions—particularly high-density or well-represented urban centers—over others, reflecting uneven learning or data distribution.

**[CoMMIT: Coordinated Multimodal Instruction Tuning](https://aclanthology.org/2025.emnlp-main.583.pdf) (as "Length bias")**
> The tendency of a reward model or judge to systematically prefer longer responses, irrespective of their quality.

## Relationships

### Knowledge forgetting →
- **Robustness** (constructs) — *causes*
  - [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
- **PoSum-Bench** (measurements) — *measured_by*
  - [PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements](https://aclanthology.org/2025.emnlp-main.404.pdf)
- **Reliability** (constructs) — *causes*
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **Privacy** (constructs) — *causes*
  - [Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf)
- **Biography** (measurements) — *measured_by*
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *causes*
  - [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *causes*
  - [Cost-Optimal Grouped-Query Attention for Long-Context Modeling](https://aclanthology.org/2025.emnlp-main.273.pdf)
- **Long-context processing** (constructs) — *causes*
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)

### → Knowledge forgetting
- **Task alignment** (constructs) — *causes*
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *correlates*
  - [SLM-Mod: Small Language Models SurpassLLMs at Content Moderation](https://aclanthology.org/2025.naacl-long.442.pdf)
- **Parameter sensitivity** (constructs) — *causes*
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
- **Overfitting** (constructs) — *causes*
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *causes*
  - [Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bethune25a/bethune25a.pdf)

### Associated with
- **Selection bias** (constructs)
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Pairwise comparison** (behaviors tasks)
  - [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf)
- **Positional bias** (constructs)
  - [On the Emergence of Position Bias in Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ad/wu25ad.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Visual perception** (constructs)
  - [VideoWebArena:  Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf)
- **Audio perception** (constructs)
  - [VideoWebArena:  Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf)
- **Temporal reasoning** (constructs)
  - [VideoWebArena:  Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf)
- **Utility preservation** (constructs)
  - [Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLMCommunication](https://aclanthology.org/2025.naacl-long.204.pdf)
- **Machine unlearning** (constructs)
  - [Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLMCommunication](https://aclanthology.org/2025.naacl-long.204.pdf)
- **Faithfulness** (constructs)
  - [SLM-Mod: Small Language Models SurpassLLMs at Content Moderation](https://aclanthology.org/2025.naacl-long.442.pdf)
- **Knowledge recall** (behaviors tasks)
  - [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.448.pdf)
- **Preference consistency** (constructs)
  - [Investigating Non-Transitivity in LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25w/xu25w.pdf)
- **Overfitting** (constructs)
  - [Understanding Overadaptation in Supervised Fine-Tuning: The Role of Ensemble Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25d/hao25d.pdf)
- **Attention sink** (constructs)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Cognitive bias** (constructs)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Conversational summarization** (behaviors tasks)
  - [2025.emnlp-main.404.checklist](https://aclanthology.org/attachments/2025.emnlp-main.404.checklist.pdf)
- **Task interference** (constructs)
  - [Merge then Realign: Simple and Effective Modality-Incremental Continual Learning for MultimodalLLMs](https://aclanthology.org/2025.emnlp-main.666.pdf)
- **Word sense disambiguation** (behaviors tasks)
  - [MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1720.pdf)
