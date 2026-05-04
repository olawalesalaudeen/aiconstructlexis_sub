# Iterative refinement
**Type:** Behavior  
**Referenced in:** 44 papers  
**Also known as:** Self-debugging, Correction suggestion generation, Stepwise revision, Self-refinement, Self-revision, Response refinement, Bug fixing, Proofreading, Error refinement, Iterative self-calibration, Answer revision, Argument revision, Code revision, Program refinement, Thought correction, Refinement during generation, Solution optimization, Multi-step rectification, Action refinement, Candidate refinement, Solution revision, Iterative critique-revision  

## State of the Field

Iterative refinement is a widely studied behavior, consistently defined as a multi-step process where a model improves an initial output based on some form of feedback. The mechanism for improvement varies across papers: it can be driven by internal processes like self-evaluation and uncertainty monitoring, as in "iterative self-calibration," or by external feedback. This external feedback includes execution results for code ("self-debugging"), explicit user instructions ("response refinement"), input from other models ("iterative critique-revision"), or feedback from a formal verifier ("program refinement"). The behavior is operationalized across numerous domains, most frequently in code-related tasks like "bug fixing" and "solution revision," but also in modifying reasoning steps ("stepwise revision"), arguments ("argument revision"), and general text ("proofreading"). Some research identifies this behavior through explicit linguistic markers, noting that models may use phrases like "Wait" or "Alternatively" to signal a "self-revision" of their reasoning. The effectiveness of this behavior is measured using benchmarks such as GPQA and MMLU. It is studied in relation to code generation and self-correction, and some work posits that it is driven by constructs like uncertainty awareness.

## Sources

**[Enhancing Spoken Discourse Modeling in Language Models Using Gestural Cues](https://aclanthology.org/2025.acl-long.887.pdf) (as "Self-debugging")**
> The observable process where a model identifies errors in its own generated code based on execution feedback and attempts to correct them.

**[Neural Incompatibility](https://aclanthology.org/2025.acl-long.1048.pdf) (as "Stepwise revision")**
> The observable behavior of modifying specific reasoning steps identified as incorrect while preserving earlier correct steps in an iterative manner.

**[PsyDial: A Large-scale Long-term Conversational Dataset for Mental Health Support](https://aclanthology.org/2025.acl-long.1050.pdf) (as "Correction suggestion generation")**
> The observable behavior of a model, after identifying an inconsistency, generating a specific suggestion for how to improve or correct the output.

**[AnRe: Analogical Replay for Temporal Knowledge Graph Forecasting](https://aclanthology.org/2025.acl-long.232.pdf) (as "Self-revision")**
> The observable act of a model extending its reasoning process to re-evaluate and modify its previous statements, often indicated by explicit markers like "Wait" or "Alternatively".

**[GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models](https://aclanthology.org/2025.acl-long.256.pdf) (as "Self-refinement")**
> Iteratively improving an initial response through self-evaluation and regeneration, either within a single model or via multi-agent debate.

**[ELABORATION: A Comprehensive Benchmark on Human-LLMCompetitive Programming](https://aclanthology.org/2025.acl-long.5.pdf) (as "Self-correction")**
> The model's ability to revise or improve its own outputs upon instruction or internal reasoning, potentially reducing harmful or biased content.

**[Reviving Cultural Heritage: A Novel Approach for Comprehensive Historical Document Restoration](https://aclanthology.org/2025.acl-long.1403.pdf) (as "Response refinement")**
> Generating an initial response and then improving it in a subsequent turn through explicit refinement instructions, creating a contrast between raw and polished outputs.

**[RPO: Retrieval Preference Optimization for Robust Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.262.pdf)**
> Generating multiple attempts at solving a problem, where later outputs are influenced by feedback on earlier ones, either through context or parameter updates.

**[Déjà Vu? Decoding Repeated Reading from Eye Movements](https://aclanthology.org/2025.acl-long.957.pdf) (as "Proofreading")**
> Reviewing and correcting grammar, spelling, and punctuation errors in a text without providing explanations or analysis.

**[AlignDistil: Token-Level Language Model Alignment as Adaptive Policy Distillation](https://aclanthology.org/2025.acl-long.973.pdf) (as "Bug fixing")**
> The task of identifying, diagnosing, and correcting errors or bugs within a software codebase.

**[Optimal Transport-Based Token Weighting scheme for Enhanced Preference Optimization](https://aclanthology.org/2025.acl-long.1036.pdf) (as "Error refinement")**
> The task of correcting an erroneous scene graph to align with a given textual description and context.

**[Value Residual Learning](https://aclanthology.org/2025.acl-long.1376.pdf) (as "Iterative self-calibration")**
> An observable process where a model repeatedly refines its generated answer over multiple rounds, using its previous outputs and associated uncertainty scores as input for the next iteration.

**[Bypass Back-propagation: Optimization-based Structural Pruning for Large Language Models via Policy Gradient](https://aclanthology.org/2025.acl-long.1422.pdf) (as "Argument revision")**
> The observable process by which a model updates its claims in response to counterarguments, incorporating new reasoning or evidence to refine its position.

**[PARME: Parallel Corpora for Low-ResourcedMiddleEastern Languages](https://aclanthology.org/2025.acl-long.1452.pdf) (as "Code revision")**
> Modifying existing code based on feedback from critique agents to correct visual or structural mismatches with a reference chart.

**[Stochastic Chameleons: Irrelevant Context Hallucinations Reveal Class-Based (Mis)Generalization inLLMs](https://aclanthology.org/2025.acl-long.1459.pdf) (as "Answer revision")**
> The observable change in an agent's response from one turn to the next, reflecting updates based on peer input.

**[AlphaVerus: Bootstrapping Formally Verified Code Generation through Self-Improving Translation and Treefinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25a/aggarwal25a.pdf) (as "Program refinement")**
> Iteratively modifying an incorrect or partially verified program using feedback from a verifier to produce a fully verified version.

**[Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf) (as "Candidate refinement")**
> The process of filtering and prioritizing a list of potential attribute matches to create a smaller, more relevant set for final evaluation.

**[Reflection-Window Decoding: Text Generation with Selective Refinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25a/tang25a.pdf) (as "Refinement during generation")**
> The observable act of revising or correcting a segment of previously generated text before continuing with new content, triggered by a pausing criterion.

**[Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wan25g/wan25g.pdf) (as "Action refinement")**
> The process by which an LLM generates improved actions for suboptimal decisions identified in RL trajectories, validated through environment simulation.

**[Accelerating Large Language Model Reasoning via Speculative Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25di/wang25di.pdf) (as "Thought correction")**
> The refinement of rejected reasoning thoughts using a large model via token-level speculative decoding to ensure output quality matches that of the large model.

**[Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf) (as "Solution revision")**
> Modifying an existing code solution based on feedback to improve correctness or efficiency.

**[Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf) (as "Solution optimization")**
> The iterative refinement of answers to complex scientific or technical questions through self-evaluation and critique, aiming to improve accuracy over multiple steps.

**[Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf) (as "Multi-step rectification")**
> Correcting an incorrect answer to a medical question by first identifying its inaccuracy and then providing the correct response from remaining options, simulating sequential clinical reasoning.

**[Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf) (as "Iterative critique-revision")**
> An observable multi-step process where a critic model provides feedback on a solution, which a generator model then uses to produce a revised solution.

## Relationships

### Iterative refinement →
- **Response quality** (constructs) — *causes*
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Articulate-Anything:  Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **MMLU** (measurements) — *measured_by*
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)

### → Iterative refinement
- **Self-reflection** (behaviors tasks) — *causes*
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **Uncertainty awareness** (constructs) — *causes*
  > we reconstruct the input by including the content and uncertainty scores of documents alongside the primary answers... enabling the answer to be calibrated iteratively based on the given documents and the previously generated answers.
  - [Value Residual Learning](https://aclanthology.org/2025.acl-long.1376.pdf)
- **Complex reasoning** (behaviors tasks) — *causes*
  - [Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wan25g/wan25g.pdf)

### Associated with
- **Schema linking** (behaviors tasks)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
