# Prompt engineering
**Type:** Behavior  
**Referenced in:** 84 papers  
**Also known as:** Question formulation, Follow-up question generation, Prompt generation, Question generation, Task description generation, Prompt inversion, Asking clarifying questions, Prompt paraphrasing, Expression rewriting, Prompt rewriting, Query modification, Prompt distillation, Prompt evolution, Hybrid prompt generation, Discrete prompt optimization, Black-box prompt tuning, Soft prompt tuning, Contrastive prompt generation, Clarification question asking, Clarifying question generation, Question asking, Open-ended questioning, Chain-of-thought prompting, Query synthesis, Open-ended question asking, Pseudo-query generation  

## State of the Field

Across the surveyed literature, prompt engineering is predominantly characterized as the observable behavior of either generating new textual inputs or modifying existing ones to guide language models toward desired outcomes. The most common form is the generation of new content, which encompasses a wide range of actions from producing search queries for retrieval and formulating questions to resolve ambiguity, to creating novel mathematical problems or task instructions. For instance, several papers define this as asking clarifying questions to "elicit more information" ("Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions"), while others focus on generating new data for model training. A second, widely discussed aspect involves the modification and optimization of existing prompts. This includes rewriting queries to be more "search-engine-friendly" ("MMSearch: Unveiling the Potential of Large Models as Multi-modal Search Engines"), rephrasing prompts to bypass safety measures, or systematically refining them to improve task performance. The literature describes several distinct optimization methods, such as "soft prompt tuning," which optimizes trainable embedding vectors, and "black-box prompt tuning," which adjusts prompts based only on model outputs. The effectiveness of these behaviors is operationalized and evaluated using benchmarks including MS-COCO, MovieLens, and SQuAD v1.1. Prompt engineering is frequently studied alongside disambiguation and mathematical reasoning, and some work reports that specific techniques can influence model generalization, interpretability, and flexibility.

## Sources

**[InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "Question formulation")**
> The observable act of generating relevant and specific questions to explore a dataset in pursuit of a high-level goal.

**[Pareto Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf) (as "Prompt generation")**
> Producing textual prompts that are fed to a task-specific language model to elicit desired outputs.

**[BIRD: A Trustworthy Bayesian Inference Framework for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/19452e14fe6e0a8ac00410f1eebcbded-Paper-Conference.pdf) (as "Follow-up question generation")**
> The observable act of generating questions to acquire additional information needed to improve confidence in a decision.

**[OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf) (as "Question generation")**
> The observable task of creating new mathematical problems, often based on seed examples from an existing dataset.

**[Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b00f67a2e03916b26f56b66b38445f7-Paper-Conference.pdf) (as "Instruction generation")**
> The task of producing a natural language instruction that accurately describes a given trajectory through an environment.

**[Grounding by Trying: LLMs with Reinforcement Learning-Enhanced Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/4169f1425b80c3a6e7daa84a1d09b077-Paper-Conference.pdf) (as "Search query generation")**
> The observable action of a model producing a textual query to be sent to a retriever or search engine.

**[Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf) (as "Prompt inversion")**
> Generating a textual prompt that, when provided to a text-to-image model, reproduces a given target image.

**[OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/d40d7cbe7210f8a13ea0149eeae9c6de-Paper-Conference.pdf) (as "Task description generation")**
> The observable action of producing a novel task description in natural language, intended to be both learnable for an agent and distinct from previously seen tasks.

**[Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf) (as "Asking clarifying questions")**
> The act of generating a question in response to a user's query to resolve ambiguity and elicit more information.

**[MMSearch: Unveiling the Potential of Large Models as Multi-modal Search Engines](https://proceedings.iclr.cc/paper_files/paper/2025/file/04e6525463afaa460b5a2e6868b18f18-Paper-Conference.pdf) (as "Query reformulation")**
> Rewriting a user query into a clearer or search-engine-friendly form, sometimes incorporating information extracted from an image.

**[Re-Aligning Language to Visual Objects with an Agentic Workflow](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf) (as "Expression rewriting")**
> The task of modifying an existing language expression to correct inaccuracies and better align it with a target visual object.

**[One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf) (as "Prompt rewriting")**
> Rephrasing an input prompt while preserving its meaning, often to make malicious intent less detectable.

**[Rare-to-Frequent: Unlocking Compositional Generation Power of Diffusion Models on Rare Concepts with LLM Guidance](https://proceedings.iclr.cc/paper_files/paper/2025/file/262ba7d20578417435414ce00e69fb12-Paper-Conference.pdf) (as "Prompt paraphrasing")**
> The observable behavior of rewriting a text prompt to make it easier for a model to interpret, while preserving the original meaning.

**[Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf) (as "Question rephrasing")**
> The action of restating a given problem or question, often to clarify conditions or focus on key information.

**[DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf) (as "Query rewriting")**
> The observable action of reformulating an input query to improve its clarity or comprehensibility before attempting to solve it.

**[Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf) (as "Query modification")**
> The observable action of adjusting input tokens in a query, such as removing noisy or correcting erroneous tokens.

**[Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf) (as "Prompt distillation")**
> Shortening a long, descriptive text prompt into a more concise version while preserving its core semantic meaning for image generation.

**[GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf) (as "Prompt optimization")**
> Refining a prompt to improve a language model's performance on a target task.

**[C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf) (as "Query generation")**
> The task of creating effective search queries to send to a retriever to obtain relevant information for a given question.

**[FedOne: Query-Efficient Federated Learning for Black-box Discrete Prompt Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ab/wang25ab.pdf) (as "Discrete prompt optimization")**
> The process of adjusting sequences of discrete tokens (prompts) through interaction with a black-box LLM to improve task performance without access to model gradients.

**[FedOne: Query-Efficient Federated Learning for Black-box Discrete Prompt Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ab/wang25ab.pdf) (as "Black-box prompt tuning")**
> Adjusting input prompts to a large language model based solely on its outputs, without access to internal model states or gradients, typically via API queries.

**[Efficient and Privacy-Preserving Soft Prompt Transfer for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ds/wang25ds.pdf) (as "Soft prompt tuning")**
> The process of optimizing trainable embedding vectors prepended to the input of a frozen language model to adapt it to a downstream task.

**[DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf) (as "Hybrid prompt generation")**
> The process of combining structural knowledge from a document-level knowledge graph and semantic context from retrieved sentences into a unified prompt for LLM input.

**[Reward-Guided Prompt Evolving in Reinforcement Learning for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25a/ye25a.pdf) (as "Prompt evolution")**
> Modifying existing prompts through rewriting or transformation to increase their complexity or learning value for the model.

**[CPCF: A Cross-Prompt Contrastive Framework for Referring Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25h/zhu25h.pdf) (as "Contrastive prompt generation")**
> Producing alternative visual prompts from misleading regions that are used to contrast against the original input prompt during decoding.

**[Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ffd05ca3cf3985f4572af015b4cfc1e-Paper-Conference.pdf) (as "Clarification question asking")**
> Producing a clarifying question instead of directly answering when the user request is ambiguous or underspecified.

**[Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf) (as "Clarifying question generation")**
> Producing questions intended to elicit missing task specifications that distinguish among multiple compatible solutions.

**[MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf) (as "Question asking")**
> Generating follow-up inquiries to gather additional patient information when initial context is insufficient.

**[Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf) (as "Open-ended questioning")**
> The behavior of asking questions that encourage detailed, narrative responses rather than simple yes/no answers.

**[Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf) (as "Chain-of-thought prompting")**
> Generating prompts that encourage step-by-step reasoning before answering a problem.

**[STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Query synthesis")**
> Generating natural-sounding user queries from relational and textual requirements for benchmark construction.

**[ChameleonLLMs: User Personas Influence Chatbot Personality Shifts](https://aclanthology.org/2025.emnlp-main.876.pdf) (as "Open-ended question asking")**
> Posing free-form questions that elicit descriptive answers, rather than binary yes/no responses, to gather richer information about a hidden object.

**[Extracting and Combining Abilities For Building Multi-lingual Ability-enhanced Large Language Models](https://aclanthology.org/2025.emnlp-main.888.pdf) (as "Pseudo-query generation")**
> The process by which an LLM generates synthetic queries from unlabeled passages to form augmented training pairs for retrieval models.

## Relationships

### Prompt engineering →
- **Generalization** (constructs) — *causes*
  > VGD enhances the interpretability, generalization, and flexibility of prompt generation without the need for additional training. (Section 1)
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  - [Code-Switching Red-Teaming:LLMEvaluation for Safety and Multilingual Understanding](https://aclanthology.org/2025.acl-long.658.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  > Additionally, we add the perplexity regularization term Lperpl to promote the interpretability of the optimized prompt
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [Reward-Guided Prompt Evolving in Reinforcement Learning for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25a/ye25a.pdf)
- **Flexibility** (constructs) — *causes*
  > VGD enhances the interpretability, generalization, and flexibility of prompt generation without the need for additional training. (Section 1)
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **Style transfer** (behaviors tasks) — *causes*
  > VGD can also be easily adapted to style transfer. (Section 4.2)
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **MS-COCO** (measurements) — *measured_by*
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **MovieLens** (measurements) — *measured_by*
  > Experimental results on the QM task, using LLaRA as the LLM4Rec model on the MovieLens and LastFM datasets. (Table 3)
  - [Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf)
- **LastFM** (measurements) — *measured_by*
  - [Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf)
- **Expressive power** (constructs) — *causes*
  - [RNNs are not Transformers (Yet):  The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  - [Reading Between the Prompts: How Stereotypes ShapeLLM’s Implicit Personalization](https://aclanthology.org/2025.emnlp-main.1030.pdf)

### → Prompt engineering
- **Mathematical reasoning** (constructs) — *measured_by*
  - [SimulS2S-LLM: Unlocking Simultaneous Inference of SpeechLLMs for Speech-to-Speech Translation](https://aclanthology.org/2025.acl-long.818.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  - [Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf)
- **Question answering** (behaviors tasks)
  - [Characterizing the Role of Similarity in the Property Inferences of Language Models](https://aclanthology.org/2025.naacl-long.575.pdf)
- **FeTaQA** (measurements)
  > To further increase data diversity, we also adapt FetaQA (Nan et al., 2022), WikiTableQuestion (Pasupat & Liang, 2015), and ToTTo (Parikh et al., 2020) into formats suitable for training column embeddings, resulting in three adapted tasks: ③Question Generation... ④Table Titling... and ⑤Row Summarization (Section 4.2).
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks)
  - [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf)
- **Ambiguity handling** (constructs)
  - [Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  > Using the generated instruction IL, we prompt πS to produce two responses: a chosen response yS ∼πS(y ∣xS) based on the short context xS, and a rejected response yL∼πS(y ∣xL) derived from the long context xL.
  - [Reward-Guided Prompt Evolving in Reinforcement Learning for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25a/ye25a.pdf)
- **Disambiguation** (constructs)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-OnlyLLMs](https://aclanthology.org/2025.emnlp-main.482.pdf)
