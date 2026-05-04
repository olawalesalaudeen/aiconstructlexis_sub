# Instruction following
**Type:** Construct  
**Referenced in:** 764 papers  
**Also known as:** Guideline following, Instruction adherence, Instruction-following, Instruction-following ability, Instruction-following capability, Prompt adherence, Task adherence, Constraint following, Prompt-following, Prompt following, Rule following, Rule-following, Instruction comprehension, Principle adherence, Instruction compliance, System message following, Instruction fidelity, Rule comprehension, Instruction-following precision, Format-instruction following, Topic following, Intention following, Constraint adherence, Task-aware ability, Constraints following, Instruction-following capabilities, Rule adherence, Constraint management, Format adherence, Keyword exclusion, Constrained generation, Placeholder generation, Keyword inclusion, Prompt execution, Rule application, Requirement fulfillment, Following natural language instructions, Compliance, Speech instruction following, Compliant response generation, Feasible sequence generation, Task decomposition compliance, Paraphrase execution, Requirement satisfaction, Poor instruction-following, Policy violation, Instruction execution, Instruction acceptance, Instruction violation, Format-consistent output generation, Text formatting, Template adherence, Instruction non-compliance, Phrase repetition, Length-constrained generation  

## State of the Field

Across the provided literature, "Instruction following" is predominantly characterized in two ways: as a model's ability to adhere to explicit, verifiable constraints like formatting rules or word limits, and more broadly as a latent capacity to understand and faithfully execute complex, open-ended user instructions. This conceptual breadth is reflected in the varied terminology used, including "instruction adherence," "constraint following," "rule following," and "prompt adherence," with some definitions tailored to specific modalities like image generation or conversational agents. The more constrained version of this construct is most commonly operationalized and measured using the IFEval benchmark, which assesses performance on tasks with "programmatically checkable criteria." The broader, latent ability to follow user intent in conversational or multi-turn settings is frequently measured using benchmarks like MT-Bench, AlpacaEval 2.0, and Arena-Hard. These evaluations often employ an "LLM-as-a-judge" methodology, where a powerful model is used to score the quality and adherence of a model's response, a practice supplemented by direct human evaluation in some studies. Research in this set of papers studies instruction following alongside capabilities such as chain-of-thought reasoning, with some work suggesting that strong instruction-following enables more complex reasoning. A recurring theme in the source snippets is that this ability is enhanced through methods like instruction tuning, supervised fine-tuning (SFT), and reinforcement learning from human feedback (RLHF). The construct is investigated across a wide array of tasks, from general chatbot interactions and coding to multimodal web navigation and scientific applications.

## Sources

**[#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf) (as "Instruction-following")**
> The ability of a model to adhere to explicit constraints and rules provided in its prompt, such as formatting requirements or word limits.

**[Evaluating Language Model Agency Through Negotiations](https://proceedings.iclr.cc/paper_files/paper/2024/file/03876dc6875571c18b3b09a624c77e96-Paper-Conference.pdf) (as "Instruction adherence")**
> Following explicit constraints such as word limits and formatting rules (e.g., valid JSON) in both private notes and public messages during the negotiation process.

**[A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)**
> The latent ability of an LLM to understand and adhere to complex prompting procedures, such as generating a skeleton and expanding points under specific constraints.

**[An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf) (as "Task adherence")**
> The extent to which a model stays aligned with the desired objective or requested behavior during generation.

**[NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf) (as "Instruction-following ability")**
> The latent capacity of a model to understand and faithfully respond to open-ended user instructions in a coherent and helpful manner.

**[LLM Blueprint: Enabling Text-to-Image Generation with Complex and Detailed Prompts](https://proceedings.iclr.cc/paper_files/paper/2024/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf) (as "Prompt adherence")**
> The degree to which a generated image faithfully represents all objects, attributes, and relationships described in a complex, lengthy text prompt.

**[Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf) (as "Instruction-following capability")**
> The model's ability to understand and execute user instructions in multimodal contexts, particularly in non-English languages, after instruction tuning.

**[GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf) (as "Guideline following")**
> The latent ability of a model to interpret and adhere to detailed annotation instructions, enabling accurate performance on unseen information extraction tasks.

**[DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf) (as "Instruction understanding")**
> The ability to correctly interpret natural language commands and map them to corresponding goals or actions.

**[Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf) (as "Constraint following")**
> The ability of a model to generate outputs that adhere to a set of strict, formally specified logical rules or constraints.

**[Multimodal Large Language Models Make Text-to-Image Generative Models Align Better](https://proceedings.neurips.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf) (as "Prompt-following")**
> The degree to which a generated image faithfully represents the objects, attributes, and relationships described in the input text prompt.

**[Exploring the Role of Large Language Models in Prompt Encoding for Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d68c1d10957c8d21ed9dea209533c5a4-Paper-Conference.pdf) (as "Prompt following")**
> The model's ability to adhere to the specific constraints, objects, and attributes detailed in the input prompt during generation.

**[{$\tau$}-bench: A Benchmark for \underline{T}ool-\underline{A}gent-\underline{U}ser Interaction in Real-World Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf) (as "Rule following")**
> The ability of an agent to accurately adhere to complex, domain-specific policies and guidelines provided in a document.

**[Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e2dd37e10bb18ed9d6d488f63094631-Paper-Conference.pdf) (as "Rule-following")**
> The latent ability of a model to reliably adhere to and operate according to a set of prompt-specified instructions or rules.

**[OSDA Agent: Leveraging Large Language Models for De Novo Design of Organic Structure Directing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38fbf326eb71f4749d04102323f7f79-Paper-Conference.pdf) (as "Instruction comprehension")**
> The ability to understand and interpret user-provided commands, constraints, and goals within a prompt.

**[SysBench: Can LLMs Follow System Message?](https://proceedings.iclr.cc/paper_files/paper/2025/file/b917f916e7eed84ffe8f5e63492b2be8-Paper-Conference.pdf) (as "System message following")**
> The ability of a large language model to understand and adhere to a set of pre-defined instructions, or constraints, provided in a system message throughout a conversation.

**[On-the-fly Preference Alignment via Principle-Guided Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcd1d7a599f33c06f06615429793c69b-Paper-Conference.pdf) (as "Principle adherence")**
> The extent to which a model's behavior conforms to an explicitly provided rule, guideline, or principle during generation.

**[Controlled LLM Decoding via Discrete Auto-regressive Biasing](https://proceedings.iclr.cc/paper_files/paper/2025/file/bce52456a36be2be1abd95427139de37-Paper-Conference.pdf) (as "Constraint satisfaction")**
> The degree to which a generated text sequence adheres to user-defined external constraints.

**[Beyond Content Relevance: Evaluating Instruction Following in Retrieval Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d37a4093931f359eb5fac5a25199db57-Paper-Conference.pdf) (as "Instruction compliance")**
> The degree to which a model’s retrieval outputs satisfy specified instruction conditions rather than only matching query content.

**[MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/571082ea18d30060177dfcaf662ff0e5-Paper-Conference.pdf) (as "Instruction fidelity")**
> The extent to which a model's response matches the exact specifications of an instruction without deviation.

**[Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf) (as "Rule comprehension")**
> The ability to internalize and correctly apply a set of provided rules to a given situation.

**[RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf) (as "Instruction-following precision")**
> The degree to which a response satisfies the specific constraints and intent expressed in an instruction.

**[MIRAGE-Bench: Automatic Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems](https://aclanthology.org/2025.naacl-long.15.pdf) (as "Format-instruction following")**
> The latent capability of an LLM to adhere to specified output formatting constraints, such as enclosing answers in bold or generating structured lists, independent of task performance.

**[Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf) (as "Topic following")**
> The latent ability to adhere to dialogue rules about allowed topics, conversation flow, and style in task-oriented conversations.

**[Can Graph Neural Networks Learn Language with Extremely Weak Text Supervision?](https://aclanthology.org/2025.acl-long.546.pdf) (as "Intention following")**
> The ability of LLM-controlled characters to understand and generate reactions that appropriately fulfill a player's expressed or implied intentions.

**[Literature Meets Data: A Synergistic Approach to Hypothesis Generation](https://aclanthology.org/2025.acl-long.13.pdf) (as "Constraint adherence")**
> The degree to which a model's generated output complies with a given set of predefined rules or requirements.

**[Finding Needles in Images: Can Multi-modalLLMs Locate Fine Details?](https://aclanthology.org/2025.acl-long.1153.pdf) (as "Task-aware ability")**
> The model's capacity to be sensitive to and correctly interpret key, task-defining information within an instruction, as opposed to relying on superficial patterns.

**[NewsInterview: a Dataset and a Playground to EvaluateLLMs’ Grounding Gap via Informational Interviews](https://aclanthology.org/2025.acl-long.1581.pdf) (as "Constraints following")**
> The ability of a model to both comprehend and strictly adhere to diverse and complex constraints specified within natural language instructions.

**[Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.26.pdf) (as "Instruction-following capabilities")**
> The ability of a large language model to understand and accurately execute tasks specified in natural language instructions.

**[CTCC: A Robust and Stealthy Fingerprinting Framework for Large Language Models via Cross-Turn Contextual Correlation Backdoor](https://aclanthology.org/2025.emnlp-main.357.pdf) (as "Rule adherence")**
> The latent tendency of an LLM to generate outputs that conform to predefined syntactic or semantic rules, such as subsequence or lookup-based abbreviation patterns, even when not explicitly prompted.

**[Biased Tales: Cultural and Topic Bias in Generating Children’s Stories](https://aclanthology.org/2025.emnlp-main.4.pdf) (as "Structural reasoning")**
> The latent ability of the model to generate outputs that adhere to complex hierarchical and temporal constraints inherent in microservice call graphs, such as valid DAG formation and correct start/finish time ordering.

**[LGA:LLM-GNNAggregation for Temporal Evolution Attribute Graph Prediction](https://aclanthology.org/2025.emnlp-main.1059.pdf) (as "Constraint management")**
> The model's underlying capacity to simultaneously satisfy multiple, diverse constraints across content, format, situation, and style within a single or multi-instruction context.

**[Model Unlearning via Sparse Autoencoder Subspace Guided Projections](https://aclanthology.org/2025.emnlp-main.1349.pdf) (as "Format adherence")**
> The model's capability to consistently produce outputs that conform to a predefined structural template, such as including specific tags or sections.

**[Do LLMs ``know'' internally when they follow instructions?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca6980a3dba7fb3e4e66925656dba68b-Paper-Conference.pdf) (as "Keyword inclusion")**
> The observable task of generating a response that contains a specific set of predefined keywords as instructed.

**[Do LLMs ``know'' internally when they follow instructions?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca6980a3dba7fb3e4e66925656dba68b-Paper-Conference.pdf) (as "Keyword exclusion")**
> The observable task of generating a response that does not contain a specific set of forbidden keywords as instructed.

**[Do LLMs ``know'' internally when they follow instructions?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca6980a3dba7fb3e4e66925656dba68b-Paper-Conference.pdf) (as "Placeholder generation")**
> The observable task of generating a response that includes placeholders as instructed.

**[Controllable Generation via Locally Constrained Resampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/d98ce7a82af78cd02968e79ea3fe89e8-Paper-Conference.pdf) (as "Constrained generation")**
> The observable behavior of producing outputs that satisfy a set of predefined formal or logical rules.

**[Ask, and it shall be given: On the Turing completeness of prompting](https://proceedings.iclr.cc/paper_files/paper/2025/file/123d3e814e257e0781e5d328232ead9b-Paper-Conference.pdf) (as "Prompt execution")**
> The model processing and acting upon a specific input prompt to perform a designated task.

**[Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf) (as "Requirement fulfillment")**
> Producing code that satisfies itemized software requirements and passes corresponding verification tests.

**[SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49c1879ae366644ce2c17fb39ddea982-Paper-Conference.pdf) (as "Rule application")**
> Applying sport-specific rules to a concrete scenario or video to determine the correct judgment.

**[Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf) (as "Following natural language instructions")**
> The observable act of generating a response that adheres to the constraints and commands specified in a natural language prompt.

**[Programming Refusal with Conditional Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf) (as "Compliance")**
> The model's observable action of following a user's instruction and providing a direct, substantive answer to the prompt.

**[DNASpeech: A Contextualized and Situated Text-to-Speech Dataset with Dialogues, Narratives and Actions](https://aclanthology.org/2025.acl-long.912.pdf) (as "Speech instruction following")**
> Receiving spoken instructions and generating appropriate spoken responses that fulfill the user's request.

**[Generalists vs. Specialists: Evaluating LLMs on Highly-Constrained Biophysical Sequence Optimization Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bg/chen25bg.pdf) (as "Feasible sequence generation")**
> Generating sequences that satisfy predefined structural or functional constraints required for validity in the optimization task.

**[Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf) (as "Compliant response generation")**
> The observable act of a model providing a direct and helpful answer to a user's query, as opposed to refusing it.

**[Resolving Lexical Bias in Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rizwan25a/rizwan25a.pdf) (as "Paraphrase execution")**
> Generating the correct edited output when presented with a paraphrased version of the original edit prompt.

**[SafeArena: Evaluating the Safety of Autonomous Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tur25a/tur25a.pdf) (as "Task decomposition compliance")**
> The observable behavior of an agent executing a harmful task when the malicious intent is broken down into a sequence of seemingly benign substeps provided over multiple interaction turns.

**[Agent-as-a-Judge: Evaluate Agents with Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuge25a/zhuge25a.pdf) (as "Requirement satisfaction")**
> Demonstrating that a generated solution fulfills specified functional and structural conditions defined in a task, including dependency-aware milestones.

**[BabyLM’s First Constructions: Causal interventions provide a signal of learning](https://aclanthology.org/2025.emnlp-main.114.pdf) (as "Policy violation")**
> The observable act of an agent performing an action that contradicts a stated domain-specific rule or constraint, such as canceling a non-refundable ticket.

**[Large Language Models Do Multi-Label Classification Differently](https://aclanthology.org/2025.emnlp-main.127.pdf) (as "Poor instruction-following")**
> Failing to adhere to task instructions, such as generating output in the wrong language or format.

**[Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.511.pdf) (as "Instruction execution")**
> Following detailed directives by carrying out the requested steps or constraints.

**[Refining Attention for Explainable and Noise-Robust Fact-Checking with Transformers](https://aclanthology.org/2025.emnlp-main.1296.pdf) (as "Instruction acceptance")**
> The model's behavior of complying with and attempting to fulfill the instructions in a given prompt, as opposed to refusing.

**[Less is More: The Effectiveness of Compact Typological Language Representations](https://aclanthology.org/2025.emnlp-main.1311.pdf) (as "Instruction violation")**
> The observable behavior where a model generates a response that contradicts or ignores the original instruction, such as revealing forbidden information in a narrative context.

**[Culture Cartography: Mapping the Landscape of Cultural Knowledge](https://aclanthology.org/2025.emnlp-main.92.pdf) (as "Format-consistent output generation")**
> Producing answers in the same format (e.g., numeral vs. written English) as the in-context example, even when the example is arithmetically incorrect.

**[AdaRewriter: Unleashing the Power of Prompting-based Conversational Query Reformulation via Test-Time Adaptation](https://aclanthology.org/2025.emnlp-main.194.pdf) (as "Text formatting")**
> The task of arranging text into a specific layout or structure as requested.

**[Noise, Adaptation, and Strategy: AssessingLLMFidelity in Decision-Making](https://aclanthology.org/2025.emnlp-main.392.pdf) (as "Template adherence")**
> Correctly applying section headers, organ system labels, and formatting rules (e.g., numbered impressions) as defined in a clinical reporting template.

**[CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning inSLMs](https://aclanthology.org/2025.emnlp-main.705.pdf) (as "Instruction non-compliance")**
> The observable failure of a model to adhere to the specified format or constraints of a given task or prompt.

**[Ensembling Prompting Strategies for Zero-Shot Hierarchical Text Classification with Large Language Models](https://aclanthology.org/2025.emnlp-main.919.pdf) (as "Phrase repetition")**
> The observable task of a model accurately reproducing a specific phrase provided in the input prompt when instructed to do so.

**[2025.emnlp-main.1233.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1233.checklist.pdf) (as "Length-constrained generation")**
> Producing text outputs that adhere to specific length requirements specified in the instruction, such as word count, sentence count, or token limits.

## Relationships

### Instruction following →
- **MT-Bench** (measurements) — *measured_by*
  > We evaluate finetuned models on MT-Bench (Zheng et al., 2023), by generating model responses to a pre-defined set of 80 multi-turn questions and subsequently evaluating these using GPT-4 (OpenAI, 2023). (Section 4.3)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
- **IFEval** (measurements) — *measured_by*
  > We call on the research community to develop more targeted benchmarks for specific HHH factors of interest, such as the recent IFEval (Zhou et al., 2023b) for instruction following (Section 7).
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  > We also evaluate instruction-tuned model, Vicuna-v1.5 (Zheng et al., 2023), with AlpacaEval 2.0 (Dubois et al., 2024), which is an automatic evaluation tool for instruction-following tasks.
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Arena-Hard** (measurements) — *measured_by*
  > "To evaluate whether PPO-M and PPO-C compromise the instruction-following abilities of LLMs gained through PPO, we assess their performance on two benchmarks: MT-Bench (Zheng et al., 2024) and Arena-Hard (Li et al., 2024)."
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > GPT-4 rates the generated texts and instruction-following capability of the privately steered LLM at almost the same quality as the non-private model.
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **AlpacaEval 2** (measurements) — *measured_by*
  > “AlpacaEval 2 (Li et al., 2023), Arena-Hard (Li et al., 2024b) and WildBench v2 (Lin et al., 2024) are general instruction-following benchmarks.”
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > “We perform a comprehensive human evaluation to assess the quality of the generated samples.”
  - [Guiding Instruction-based Image Editing via Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f0e91b1314fa5eabf1d7ef6d1561ecec-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > We also evaluate on the massive multitask language understanding (MMLU) (Hendrycks et al., 2020) benchmark. The results are summarized in Table 4. We found that compared to the base model, our model has improved zero-shot performance... on MMLU. (Section 3.4)
  - [MUFFIN: Curating Multi-Faceted Instructions for Improving Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d1a0188e18c1d74a0f8d6eb5ecede4f-Paper-Conference.pdf)
- **UltraFeedback** (measurements) — *measured_by*
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [Towards Optimal Multi-draft Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0907335ecf28faf15be54485dbcbe70e-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  > For models trained on general instruction datasets, we follow InstructEval (Chia et al., 2023) and report accuracy (%) on MMLU (Hendrycks et al., 2020), BBH (Suzgun et al., 2022), CRASS (Frohberg and Binder, 2021), DROP (Dua et al., 2019). (Section 4.2)
  - [MUFFIN: Curating Multi-Faceted Instructions for Improving Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d1a0188e18c1d74a0f8d6eb5ecede4f-Paper-Conference.pdf)
- **LLMBar** (measurements) — *measured_by*
  > LLMBar (Zeng et al., 2023): meta-evaluation benchmark aimed at assessing LLM evaluators’ ability to distinguish instruction-following outputs.
  - [Evaluating Large Language Models at Evaluating Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/afc8b034823271816d14f7c1aefe1dff-Paper-Conference.pdf)
- **FollowBench** (measurements) — *measured_by*
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **Vicuna-Bench** (measurements) — *measured_by*
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements) — *measured_by*
  - [Learning Diverse Attacks on Large Language Models for Robust Red-Teaming and Safety Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e128701ceca0ba03658a305faf39deb-Paper-Conference.pdf)
- **TyDiQA** (measurements) — *measured_by*
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **InfoBench** (measurements) — *measured_by*
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.511.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
- **BigCodeBench** (measurements) — *measured_by*
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **FOLLOWIR** (measurements) — *measured_by*
  - [Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2cefdb2c4c3274b78cd450bac35228df-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [Decoupling Angles and Strength in Low-rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3379ce104189b72d5f7baaa03ae81329-Paper-Conference.pdf)
- **LiveBench** (measurements) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **UltraChat** (measurements) — *measured_by*
  > We are interested in the task of instruction-following, for which we use UltraChat (Ding et al., 2023), a large-scale dataset of instructional conversations. (Section 6.1)
  - [Model Equality Testing: Which Model is this API Serving?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d73234a13815fc1f9779dd17d89be9b4-Paper-Conference.pdf)
- **ArmoRM** (measurements) — *measured_by*
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)
- **WildBench** (measurements) — *measured_by*
  - [Instruct-SkillMix: A Powerful Pipeline for LLM Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)
- **VicunaEval** (measurements) — *measured_by*
  - [A Grounded Typology of Word Classes](https://aclanthology.org/2025.naacl-long.522.pdf)
- **Arena-Hard-Auto** (measurements) — *measured_by*
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **CFBench** (measurements) — *measured_by*
  > we propose CFBench, a large-scale Chinese Comprehensive Constraints Following Benchmark for LLMs, featuring 1,000 curated samples that cover more than 200 real-life scenarios and over 50 NLP tasks. (Abstract)
  - [NewsInterview: a Dataset and a Playground to EvaluateLLMs’ Grounding Gap via Informational Interviews](https://aclanthology.org/2025.acl-long.1581.pdf)
- **Multi-IF** (measurements) — *measured_by*
  - [PunMemeCN: A Benchmark to Explore Vision-Language Models’ Understanding ofChinese Pun Memes](https://aclanthology.org/2025.emnlp-main.945.pdf)
- **ShareGPT** (measurements) — *measured_by*
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.227.pdf)
- **Zero-shot generalization** (constructs) — *causes*
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **AgentBench** (measurements) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Super-NaturalInstructions** (measurements) — *measured_by*
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
- **Self-Instruct** (measurements) — *measured_by*
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
- **GAVIE** (measurements) — *measured_by*
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
- **CNN/DailyMail** (measurements) — *measured_by*
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **OpenOrca** (measurements) — *measured_by*
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)
- **GRIT** (measurements) — *measured_by*
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **DROP** (measurements) — *measured_by*
  - [LeTS: Learning to Think-and-Search via Process-and-Outcome Reward Hybridization](https://aclanthology.org/2025.emnlp-main.258.pdf)
- **ALFWorld** (measurements) — *measured_by*
  - [Policy Improvement using Language Feedback Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4d4f7cf206bb00f9a38a5b6ae92cf79a-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  > By leveraging the strong instruction-following abilities of large language models, INSTRUCTRAG generates detailed rationales that articulate how the ground-truth answers can be derived from the retrieved documents. (Section 5)
  - [CART: A Generative Cross-Modal Retrieval Framework With Coarse-To-Fine Semantic Modeling](https://aclanthology.org/2025.acl-long.736.pdf)
- **MMBench** (measurements) — *measured_by*
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks) — *causes*
  - [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ARC** (measurements) — *measured_by*
  - [Decoupling Angles and Strength in Low-rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3379ce104189b72d5f7baaa03ae81329-Paper-Conference.pdf)
- **FLAN** (measurements) — *measured_by*
  - [MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf)
- **Zero-shot learning** (constructs) — *causes*
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **HelpSteer** (measurements) — *measured_by*
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *causes*
  - [JMMMU: AJapanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.44.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks) — *causes*
  - [InstructRAG: Instructing Retrieval-Augmented Generation via Self-Synthesized Rationales](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdce0de17dc3cf97019a35baa65aebd0-Paper-Conference.pdf)
- **MATH** (measurements) — *measured_by*
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
- **ASDIV** (measurements) — *measured_by*
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
- **SVAMP** (measurements) — *measured_by*
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
- **TRACE** (measurements) — *measured_by*
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Super-Natural Instructions** (measurements) — *measured_by*
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
- **MT-Bench-101** (measurements) — *measured_by*
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
- **LongGenBench** (measurements) — *measured_by*
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Visual grounding** (constructs) — *causes*
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
- **Paraphrasing** (behaviors tasks) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Creative writing** (behaviors tasks) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **EvolInstruct** (measurements) — *measured_by*
  > After training, we evaluate DISTILLM-2 for general purpose instruction-following task on AlpacaEval (Li et al., 2023), Evol-Instruct (Xu et al., 2024a), and UltraFeedback (Cui et al., 2024).
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
- **AlpacaEval 2.0 Length Controlled** (measurements) — *measured_by*
  > We evaluate all variants on Length-controlled (LC) AlpacaEval 2.0 (Li et al., 2023) and MixEval (Ni et al., 2024). LC AlpacaEval 2.0 is a well-recognized benchmark for chat model evaluation.
  - [Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf)
- **BabyAI** (measurements) — *measured_by*
  - [The Synergy of LLMs & RL Unlocks Offline Learning of Generalizable Language-Conditioned Policies with Low-fidelity Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pouplin25a/pouplin25a.pdf)
- **T-Eval** (measurements) — *measured_by*
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **MixEval** (measurements) — *measured_by*
  > We evaluate all variants on Length-controlled (LC) AlpacaEval 2.0 (Li et al., 2023) and MixEval (Ni et al., 2024). MixEval is a ground-truth-based benchmark that collects data from numerous QA datasets under real-world data distribution.
  - [Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf)
- **C-Eval** (measurements) — *measured_by*
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.511.pdf)
- **VoiceBench** (measurements) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **PLLuM-Align** (measurements) — *measured_by*
  > For scalar multi-attribute rating, annotators evaluated each response on a 5-point Likert scale across seven criteria: i) truthfulness, (ii) linguistic correctness, (iii) safety, (iv) fairness, (v) conciseness, (vi) coherence & reasoning, as well as vii) helpfulness & instruction-following.
  - [REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### → Instruction following
- **In-context learning** (constructs) — *causes*
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Alignment** (constructs) — *causes*
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *causes*
  - [Reward-Augmented Data Enhances Direct Preference Alignment of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25az/zhang25az.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Cost-efficient Collaboration between On-device and Cloud Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/narayan25a/narayan25a.pdf)
- **AudioBench** (measurements) — *measured_by*
  - [SVD-LLMV2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.218.pdf)

### Associated with
- **Helpfulness** (constructs)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Alignment** (constructs)
  - [A Critical Evaluation of AI Feedback for Aligning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/33870b3e099880cd8e705cd07173ac27-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks)
  - [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **Factuality** (constructs)
  - [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Safety alignment** (constructs)
  - [Certifying Counterfactual Bias in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c6decac1477fbcc2cbf12d314ce0133-Paper-Conference.pdf)
- **Task generalization** (constructs)
  - [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf)
- **Machine translation** (behaviors tasks)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Grounding** (constructs)
  - [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Language understanding** (behaviors tasks)
  - [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf)
- **Safety** (constructs)
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
- **Verbalized confidence** (measurements)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
- **Commonsense knowledge** (constructs)
  - [Discourse-Driven Evaluation: Unveiling Factual Inconsistency in Long Document Summarization](https://aclanthology.org/2025.naacl-long.104.pdf)
- **Text summarization** (behaviors tasks)
  > Weaker instruction-following at 128k length. For summarization tasks, the summaries generated by Llama-3.1-70B-Instruct at 128k tokens become longer and often contain details not present in the reference. (Section 7.1)
  - [Can We Further Elicit Reasoning inLLMs? Critic-Guided Planning with Retrieval-Augmentation for Solving Challenging Tasks](https://aclanthology.org/2025.acl-long.1245.pdf)
- **Multi-task capability** (constructs)
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Robotic manipulation** (behaviors tasks)
  - [PERIA: Perceive, Reason, Imagine, Act via Holistic Language and Vision Planning for Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6af963e891e7efa229c24a1607fa7f-Paper-Conference.pdf)
- **UltraFeedback** (measurements)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **Role-playing** (behaviors tasks)
  - [ImproveLLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.713.pdf)
- **Video question answering** (behaviors tasks)
  > In some failure cases observed in the model, we found that prompting the model to generate a comprehensive caption for the video input can lead to outputs that include the correct answer. This phenomenon may be attributed to a disruption in the model's instruction-following capabilities during the training.
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
- **Knowledge transferability** (constructs)
  - [Improving Handshape Representations for Sign Language Processing: A Graph Neural Network Approach](https://aclanthology.org/2025.emnlp-main.1484.pdf)
- **Soundness** (constructs)
  - [Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e2dd37e10bb18ed9d6d488f63094631-Paper-Conference.pdf)
- **Coding** (behaviors tasks)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
- **Verbosity** (constructs)
  - [L3Ms — Lagrange Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/92d3d2a9801211ca3693ccb2faa1316f-Paper-Conference.pdf)
- **Constraint satisfaction** (constructs)
  - [SysBench: Can LLMs Follow System Message?](https://proceedings.iclr.cc/paper_files/paper/2025/file/b917f916e7eed84ffe8f5e63492b2be8-Paper-Conference.pdf)
- **Speech understanding** (constructs)
  - [SVD-LLMV2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.218.pdf)
- **Content moderation** (behaviors tasks)
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf)
- **Relevance** (constructs)
  > Specifically, we define three fundamental dimensions of instruction-following: relevance, factuality, and adherence. (Section 1)
  - [FiNE: Filtering and Improving Noisy Data Elaborately with Large Language Models](https://aclanthology.org/2025.naacl-long.438.pdf)
- **Output diversity** (constructs)
  - [ImproveLLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.713.pdf)
- **Coherence** (constructs)
  - [ReSURE: Regularizing Supervision Unreliability for Multi-turn Dialogue Fine-tuning](https://aclanthology.org/2025.emnlp-main.960.pdf)
- **Beam search** (measurements)
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.573.pdf)
