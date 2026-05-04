# Explanation generation
**Type:** Behavior  
**Referenced in:** 102 papers  
**Also known as:** Text explanation, Fallacy explanation, Verbal feedback generation, Hint generation, Plausibility explanation, Analogical explanation, Rule violation explanation, Justification generation, Wordplay generation, Justification production, Rationale generation, Reasoning generation, Classification rationale generation, Alert explanation, Anomaly explanation, Anomaly justification, Free-form explanation, Natural language explanation generation  

## State of the Field

Across the provided literature, explanation generation is predominantly characterized as the observable behavior of a model producing natural language text to justify, rationalize, or clarify an output, with terms like "justification generation" and "rationale generation" used frequently. The applications are diverse, ranging from justifying answers in question-answering and explaining product recommendations to providing feedback on programming errors and clarifying logical fallacies. A smaller set of studies operationalizes it as elaborating on content, such as expanding a surgical keystep into a full description or explaining what a piece of code does. This behavior is typically elicited by prompting a model to provide an explanation, sometimes structured "to request that LLMs first generate an explanation and then the final answer" (Superlatives in Context...). The quality of the generated text is then measured using `Human evaluation` or `LLM-as-a-judge`. In the context of the research network, explanation generation is frequently positioned as a mechanism for achieving `Interpretability and explainability`. It is also studied in relation to the quality of the generated text, co-occurring with investigations into `Faithfulness`, `Hallucination`, and `Self-consistency`.

## Sources

**[Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)**
> The observable task of generating natural language text that explains why a particular product is a good or bad match for a user.

**[Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf) (as "Text explanation")**
> Expanding a short surgical keystep into a more descriptive explanation of events, anatomy, and instruments.

**[When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Fallacy explanation")**
> The task of generating a natural language explanation that clarifies the fallacy, logical error, or humorous aspect within a given cunning text.

**[Data-Driven Discovery of Dynamical Systems in Pharmacology using Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aea8bdc42d8ba3a67a69b3f18be93f69-Paper-Conference.pdf) (as "Verbal feedback generation")**
> The behavior of generating natural language text that reflects on a model's performance and provides specific suggestions for improvement.

**[Hints-In-Browser: Benchmarking Language Models for Programming Feedback Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/34cc2ded6daba59357134c0b9fb06bfe-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Hint generation")**
> Producing a natural language hint as feedback to aid a learner in resolving programming errors without directly revealing the solution.

**[Policy Improvement using Language Feedback Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4d4f7cf206bb00f9a38a5b6ae92cf79a-Paper-Conference.pdf) (as "Feedback generation")**
> The generation of explanatory text that not only classifies a behavior but also provides reasons for the classification.

**[NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf) (as "Plausibility explanation")**
> The observable task of generating a free-form text that justifies why a chosen hypothesis image is plausible or more plausible than an alternative.

**[A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf) (as "Analogical explanation")**
> The task of explaining complex subjects by generating responses that use analogies.

**[Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf) (as "Code explanation")**
> The observable behavior of generating a natural language explanation for what a piece of code does.

**[SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49c1879ae366644ce2c17fb39ddea982-Paper-Conference.pdf) (as "Rule violation explanation")**
> The task of generating a textual explanation for why a specific action in a video constitutes a rule violation.

**[A Reasoning-Based Approach to Cryptic Crossword Clue Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/andrews25a/andrews25a.pdf) (as "Wordplay generation")**
> The task of creating natural language explanations (wordplay) that justify how a candidate answer can be derived from a cryptic clue.

**[DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf) (as "Justification generation")**
> Producing a concise, readable summary that explains the reasoning and critical evidence behind a verdict.

**[Self-Critique and Refinement for Faithful Natural Language Explanations](https://aclanthology.org/2025.emnlp-main.428.pdf) (as "Justification production")**
> The task of generating explanations or justifications for a veracity prediction, often by summarizing or structuring evidence.

**[Transferable Direct Prompt Injection via Activation-GuidedMCMCSampling](https://aclanthology.org/2025.emnlp-main.103.pdf) (as "Critique generation")**
> The action of producing a natural language explanation or analysis to justify an evaluation judgement.

**[Mind the Value-Action Gap: DoLLMs Act in Alignment with Their Values?](https://aclanthology.org/2025.emnlp-main.155.pdf) (as "Rationale generation")**
> Producing free-form explanations or scoring rationales alongside an assessment decision.

**[MOSAIC: Modeling SocialAIfor Content Dissemination and Regulation in Multi-Agent Simulations](https://aclanthology.org/2025.emnlp-main.326.pdf) (as "Reasoning generation")**
> The model's observable behavior of producing natural language justifications for its answers to predicate questions, intended to reflect its internal logical analysis.

**[Memorization or Reasoning? Exploring the Idiom Understanding ofLLMs](https://aclanthology.org/2025.emnlp-main.1100.pdf) (as "Classification rationale generation")**
> Producing detailed, linguistically grounded descriptions of sentiment labels by analyzing representative examples, covering lexical patterns, semantic-pragmatic features, and domain associations.

**[SPaRC: A Spatial Pathfinding Reasoning Challenge](https://aclanthology.org/2025.emnlp-main.527.pdf) (as "Alert explanation")**
> Explaining detected security alerts in response to an instruction.

**[Beyond Online Sampling: Bridging Offline-to-Online Alignment via Dynamic Data Transformation forLLMs](https://aclanthology.org/2025.emnlp-main.1379.pdf) (as "Anomaly explanation")**
> Providing a rationale for why a described situation is considered anomalous, based on underlying commonsense knowledge.

**[Beyond Online Sampling: Bridging Offline-to-Online Alignment via Dynamic Data Transformation forLLMs](https://aclanthology.org/2025.emnlp-main.1379.pdf) (as "Anomaly justification")**
> Generating a plausible sequence of events or circumstances that could have led to the observed anomalous situation.

**[MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1720.pdf) (as "Free-form explanation")**
> The task of generating an unconstrained, natural language explanation of a target word's meaning in a given context.

**[ERAS: Evaluating the Robustness ofChineseNLPModels to Morphological Garden Path Errors](https://aclanthology.org/2025.naacl-long.160.pdf) (as "Natural language explanation generation")**
> Producing a fluent, natural language summary of SQL execution results to enhance user understanding.

## Relationships

### Explanation generation →
- **Human evaluation** (measurements) — *measured_by*
  - [When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [SocialGPT: Prompting LLMs for Social Relation Reasoning via Greedy Segment Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/047682108c3b053c61ad2da5a6057b4e-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5ef9853a6cdea40ae3e301a6d8dc32b5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Evaluation** (behaviors tasks) — *causes*
  - [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf)
- **Knowledge manipulation** (constructs) — *causes*
  > "KG-SFT focuses on generating high-quality explanations to improve the quality of the Q&A pair, which reveals a promising direction for supplementing existing data augmentation methods."
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)

### → Explanation generation
- **Instruction following** (constructs) — *causes*
  - [InstructRAG: Instructing Retrieval-Augmented Generation via Self-Synthesized Rationales](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdce0de17dc3cf97019a35baa65aebd0-Paper-Conference.pdf)
- **Self-consistency** (measurements) — *causes*
  - [CanLLMs Reason Abstractly Over Math Word Problems WithoutCoT? Disentangling Abstract Formulation From Arithmetic Computation](https://aclanthology.org/2025.emnlp-main.724.pdf)

### Associated with
- **Label prediction** (behaviors tasks)
  > It involved training the smaller language model simultaneously on both label prediction and rationale generation tasks, effectively leveraging their mutual benefits. (Section 1)
  - [Unlocking General Long Chain-of-Thought Reasoning Capabilities of Large Language Models via Representation Engineering](https://aclanthology.org/2025.acl-long.340.pdf)
- **Reasoning** (constructs)
  - [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](https://aclanthology.org/2025.acl-long.1155.pdf)
- **Tool use** (behaviors tasks)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs)
  > Human readability and explainability are essential to effective fact-checking. ... This final, post-prediction stage addresses that need by generating a concise summary that distills the key findings and critical evidence, including hyperlinks. (Section 3)
  - [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf)
- **Hallucination** (behaviors tasks)
  - [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf)
- **Knowledge retrieval** (behaviors tasks)
  - [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity](https://aclanthology.org/2025.emnlp-main.427.pdf)
- **Code debugging** (behaviors tasks)
  - [Hints-In-Browser: Benchmarking Language Models for Programming Feedback Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/34cc2ded6daba59357134c0b9fb06bfe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-consistency** (measurements)
  - [Do Vision & Language Decoders use Images and Text equally? How Self-consistent are their Explanations?](https://proceedings.iclr.cc/paper_files/paper/2025/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **Rationale compression** (behaviors tasks)
  > All rationales are generated and compressed via automated API-based models, and the datasets used are publicly available. (Section D1)
  - [2025.emnlp-main.618.checklist](https://aclanthology.org/attachments/2025.emnlp-main.618.checklist.pdf)
