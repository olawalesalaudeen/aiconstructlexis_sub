# Self-correction
**Type:** Behavior  
**Referenced in:** 255 papers  
**Also known as:** Self-correction and refinement, Noise correction, Spelling correction, Error correction, Typo correction, Correcting errors, Mistake correction, Student mistake correction, Fact refinement, Iterative hypothesis refinement, Patch refinement, Bug fixing, Answer refinement, Natural language refinement, Self-refinement, Text correction, Assessment refinement, Chain-of-thought correction, Thought refinement, Hallucination correction, Multi-round self-correction, Invalid SMILES correction, Code fixing, Response refinement, Iterative self-correction, Self-checking, Iterative chart refinement, Over-correction, Grammar correction, Chinese spelling correction, Overcorrection, Undercorrection, Generative error correction, Intrinsic self-correction, Response correction, Iterative sequence editing, Self-enhancement, Reflection generation, Iterative sequence optimization, Artifact refinement, Iterative response refinement, Iterative editing, Critique and refinement, Iterative revision, Iterative self-improvement, Hypothesis refinement, Output editing, Cross-refinement, Rationale refinement, Description revision, Failure correction, Answer correction, Token correction, Conditional weak-to-strong correction, Discrimination, Evaluation capability, Fine-grained evaluation capability, Reflection, Self-critique, Self-debugging, Self-repair, Self-refinement capability, Self-correction ability, Self-correction capability, Refinement capability, Progressive refinement, Self-repair capability, Error recovery, Self-critique ability, Self-revision capability, Self-repair ability, Debugging capability, Debugging ability, Bug localization, Debuggability, Self-debugging capability, Self-verification, Self-evolution, Self-improvement, Continuous improvement, Self-improvement capability, Policy improvement, Iterative reflection capability, Learning from mistakes, Self-Reflection, Reflection capability, Introspection, Current reflection, Metacognitive monitoring, Meta-reflection, Mistake detection, Refinement, Solution refinement, Action evaluation, Reasoning quality evaluation, Self-assessment, Critiquing ability, Judging ability  

## State of the Field

Across the surveyed literature, self-correction is broadly characterized as the observable behavior of a model identifying and rectifying errors in its own generated artifacts. This process is applied to a wide array of outputs, including code, mathematical proofs, SQL queries, reasoning chains, and natural language text, and is most commonly described as an iterative or multi-round refinement. The correction is frequently triggered by feedback from various sources, such as execution results, environmental error messages, user input, or other AI agents acting as critics. A smaller line of work distinguishes this from "intrinsic self-correction," where a model revises its output without any external feedback or hints. This behavior is operationalized and measured using instruments like the HyPoradise and EvalPlus benchmarks, as well as through Human evaluation. Self-correction is often studied alongside latent capabilities thought to enable it, such as "self-reflection" (analyzing past failures), "self-critique" (evaluating one's own output), and the broader capacity for "self-improvement." The behavior is frequently investigated for its reported influence on downstream capabilities like problem-solving, mathematical reasoning, and generalization. Finally, a few papers also define specific failure modes of this process, including "over-correction," where correct parts of an input are erroneously altered, and "undercorrection," where errors are left unfixed.

## Sources

**[ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf) (as "Noise correction")**
> The task of evaluating a given SQL query against a question and database, determining if it is correct, and providing a revised query if it is not.

**[Efficient Perplexity Bound and Ratio Matching in Discrete Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/23e6f78bdec844a9f7b6c957de2aae91-Paper-Conference.pdf) (as "Spelling correction")**
> The task of identifying and correcting spelling errors in a given text at the character level.

**[ImProver: Agent-Based Automated Proof Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/4864005cfdea7ebd07086ed1b9846825-Paper-Conference.pdf) (as "Error correction")**
> The process of identifying and fixing errors in a generated proof, often through an iterative refinement process that uses feedback from a verifier.

**[LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf) (as "Typo correction")**
> The task of identifying and fixing misspellings in a text while preserving all other stylistic and formatting elements.

**[A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf) (as "Correcting errors")**
> The observable task of identifying and rectifying mistakes in a given artifact, such as code or text.

**[Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding](https://aclanthology.org/2025.emnlp-main.11.pdf) (as "Student mistake correction")**
> The observable task of generating a correct reasoning chain and final answer for a problem, even when conditioned on a dialogue history containing an incorrect solution from the student.

**[Gradient-Attention Guided Dual-Masking Synergetic Framework for Robust Text-based Person Retrieval](https://aclanthology.org/2025.emnlp-main.15.pdf) (as "Mistake correction")**
> The task of providing feedback or guidance to help a student fix an identified error in their work.

**[EasyRec: Simple yet Effective Language Models for Recommendation](https://aclanthology.org/2025.emnlp-main.895.pdf) (as "Iterative hypothesis refinement")**
> The observable process of progressively improving a scientific hypothesis through repeated cycles of evaluation and modification.

**[Answer Convergence as a Signal for Early Stopping in Reasoning](https://aclanthology.org/2025.emnlp-main.905.pdf) (as "Fact refinement")**
> The process of revising incomplete or missing facts by incorporating omitted conditions, comparanda, or relational context to make them self-contained and verifiable.

**[UI-Hawk: Unleashing the Screen Stream Understanding for MobileGUIAgents](https://aclanthology.org/2025.emnlp-main.921.pdf) (as "Patch refinement")**
> Evaluating a generated patch for correctness, performance, or maintainability and producing an improved version or detailed analysis report.

**[Chat-Driven Text Generation and Interaction for Person Retrieval](https://aclanthology.org/2025.emnlp-main.267.pdf) (as "Response revision")**
> The observable act of reviewing an initial response and generating an updated one.

**[Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.286.pdf) (as "Bug fixing")**
> Revising failing code snippets to remove defects identified by test failures or execution traces.

**[2025.emnlp-main.72.checklist](https://aclanthology.org/attachments/2025.emnlp-main.72.checklist.pdf) (as "Answer refinement")**
> The observable task of editing or improving an existing answer to enhance its quality, accuracy, or clarity.

**[MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.80.pdf) (as "Iterative refinement")**
> A multi-step process where a model progressively improves an output, such as code or a natural language plan, based on feedback or further analysis.

**[MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.80.pdf) (as "Natural language refinement")**
> The observable act of modifying a natural language description of code logic to correct errors, based on execution feedback and analysis.

**[RuCCoD: Towards AutomatedICDCoding inRussian](https://aclanthology.org/2025.emnlp-main.130.pdf)**
> Iteratively improving generated code or reasoning by analyzing execution feedback and revising outputs accordingly.

**[Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes](https://aclanthology.org/2025.emnlp-main.133.pdf) (as "Self-refinement")**
> The observable behavior of a model updating its own response in a subsequent turn based on user feedback, even if the improvement is limited.

**[Mind the Value-Action Gap: DoLLMs Act in Alignment with Their Values?](https://aclanthology.org/2025.emnlp-main.155.pdf) (as "Assessment refinement")**
> The observable act of revising an initial assessment and its rationale in response to critical feedback.

**[AdaRewriter: Unleashing the Power of Prompting-based Conversational Query Reformulation via Test-Time Adaptation](https://aclanthology.org/2025.emnlp-main.194.pdf) (as "Text correction")**
> Detecting and correcting errors in text, including typos and other modifications needed to match a reference answer.

**[Confidence-guided Refinement Reasoning for Zero-shot Question Answering](https://aclanthology.org/2025.emnlp-main.355.pdf) (as "Chain-of-thought correction")**
> The process of analyzing an initial reasoning trace (chain-of-thought) and refining it to improve accuracy or format compliance.

**[ToDi: Token-wise Distillation via Fine-Grained Divergence Control](https://aclanthology.org/2025.emnlp-main.410.pdf) (as "Thought refinement")**
> Regenerating or revising a prior reasoning step based on execution feedback to correct logical errors and improve the reasoning trajectory.

**[The Impact of Negated Text on Hallucination with Large Language Models](https://aclanthology.org/2025.emnlp-main.685.pdf) (as "Multi-round self-correction")**
> The observable process where a model iteratively refines a sequence of answers for a given question, with each new answer being a correction of the previous one.

**[SciNLP: A Domain-Specific Benchmark for Full-Text Scientific Entity and Relation Extraction inNLP](https://aclanthology.org/2025.emnlp-main.733.pdf) (as "Hallucination correction")**
> Reducing or eliminating factually incorrect statements in model outputs by applying knowledge edits.

**[Financial Risk Relation Identification through Dual-view Adaptation](https://aclanthology.org/2025.emnlp-main.1337.pdf) (as "Code fixing")**
> Editing existing code to correct errors such as indentation or syntax issues.

**[ConvSearch-R1: Enhancing Query Reformulation for Conversational Search with Reasoning via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1350.pdf) (as "Invalid SMILES correction")**
> Modifying a syntactically or semantically invalid SMILES string to produce a valid one, either through iterative refinement or structural transformation.

**[TS-CLIP: Time Series Understanding byCLIP](https://aclanthology.org/2025.emnlp-main.232.pdf) (as "Response refinement")**
> Improving a selected response by evaluating its consistency with the conversation, alignment with the chosen strategy, and effectiveness in alleviating emotional stress.

**[32.3%](https://aclanthology.org/2025.emnlp-main.809.pdf) (as "Iterative self-correction")**
> Revising generated constraint model code over multiple rounds using feedback from a symbolic solver and retrieved correction exemplars.

**[Multi-Document Event Extraction Using Large and Small Language Models](https://aclanthology.org/2025.emnlp-main.973.pdf) (as "Self-checking")**
> An iterative process where the model refines its solution over multiple rounds to improve correctness and verify results.

**[Semantic Inversion, Identical Replies: Revisiting Negation Blindness in Large Language Models](https://aclanthology.org/2025.emnlp-main.1089.pdf) (as "Iterative chart refinement")**
> The observable process of modifying chart code and visual output across multiple steps based on feedback from evaluation agents.

**[Glider: Global and Local Instruction-Driven Expert Router](https://aclanthology.org/2025.emnlp-main.320.pdf) (as "Over-correction")**
> An observable failure mode where the model introduces errors by altering correct parts of the input hypothesis, particularly under strict correctness constraints in ASR.

**[Principled Personas: Defining and Measuring the Intended Effects of Persona Prompting on Task Performance](https://aclanthology.org/2025.emnlp-main.1365.pdf) (as "Grammar correction")**
> Identifying and generating the correct form of a given input that contains grammatical errors.

**[The Good, the Bad and the Constructive: Automatically Measuring Peer Review’s Utility for Authors](https://aclanthology.org/2025.emnlp-main.1477.pdf) (as "Chinese spelling correction")**
> The task of detecting and correcting erroneous characters within Chinese sentences.

**[Improving Large Language Model Safety with Contrastive Representation Learning](https://aclanthology.org/2025.emnlp-main.1431.pdf) (as "Overcorrection")**
> The observable behavior of making excessive, unnecessary changes to input text during correction, including altering correct parts or adding redundant content.

**[Improving Large Language Model Safety with Contrastive Representation Learning](https://aclanthology.org/2025.emnlp-main.1431.pdf) (as "Undercorrection")**
> Failing to make all needed edits, leaving some grammatical errors uncorrected.

**[It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf) (as "Generative error correction")**
> The process by which an LLM corrects ASR output by mapping an N-best list of hypotheses to a final predicted transcription in an auto-regressive manner.

**[Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf) (as "Artifact refinement")**
> The observable action of an agent modifying and improving a piece of work (an artifact) based on instructions or feedback from another agent.

**[Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf) (as "Iterative response refinement")**
> Producing a revised answer over multiple attempts that improves on earlier outputs.

**[Bayesian Optimization of Antibodies Informed by a Generative Model of Evolving Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cdd4ce9330025967dd1ed0bed3010f5-Paper-Conference.pdf) (as "Iterative sequence optimization")**
> The observable process of engaging in a multi-step loop of proposing a sequence, receiving a measurement of its quality, and using that feedback to inform the next proposal.

**[Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf) (as "Reflection generation")**
> The process where the model analyzes a failed trajectory and produces a natural language summary explaining the reason for failure to guide future attempts.

**[Training Language Models to Self-Correct via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf) (as "Intrinsic self-correction")**
> Revising an initial answer without external feedback or oracle hints, based only on the problem and the model's own prior attempt.

**[Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf) (as "Response correction")**
> The observable action of rectifying the model's output response, including updating outdated answers or incorrect classifications.

**[DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf) (as "Self-enhancement")**
> The observable behavior of a model re-generating a data item to produce an improved version, using its own prior self-reflection as guidance.

**[Data Distillation for extrapolative protein design through exact preference optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ea92ef18aae17627d133534209e640-Paper-Conference.pdf) (as "Iterative sequence editing")**
> The observable process where a model proposes modifications to a given protein sequence to generate a new sequence with a predicted higher fitness value.

**[FlexCAD: Unified and Versatile Controllable CAD Generation with Fine-tuned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/090b23d52bc2722eef2fbf79c5ebf9ec-Paper-Conference.pdf) (as "Iterative editing")**
> The process of progressively modifying a CAD model through a sequence of edits, where each step refines the design to better match user specifications.

**[Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf) (as "Iterative revision")**
> The observable behavior of generating a sequence of answers, where each new answer is conditioned on the model's previous attempts.

**[Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf) (as "Critique and refinement")**
> The observable behavior of a critic agent evaluating responses from other agents and then generating an updated, improved response based on that evaluation.

**[MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](https://proceedings.iclr.cc/paper_files/paper/2025/file/51fd9a7d1706023cb9f8210cc6ac357c-Paper-Conference.pdf) (as "Hypothesis refinement")**
> Improving generated hypotheses based on feedback regarding validness, novelty, clarity, and significance.

**[Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf) (as "Iterative self-improvement")**
> The observable, multi-round process where a model repeatedly generates data, verifies it, and fine-tunes on the filtered results, leading to changes in its performance and output distribution over time.

**[It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf) (as "Rationale refinement")**
> The observable act of modifying a previously generated rationale to improve its quality, which can be done by the same model (self-refinement) or a different model (cross-refinement).

**[It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf) (as "Cross-refinement")**
> Improving a rationale using a different model variant than the one that generated it.

**[Uncovering Gaps in How Humans and LLMs Interpret Subjective Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362fbc0d182c6b4b8dadb90177239e4-Paper-Conference.pdf) (as "Output editing")**
> The observable task where an LLM revises its own previously generated text to better align with a specified subjective quality or constitutional principle.

**[PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebf8764ecf0688cdd9fe1e5a9c525d0d-Paper-Conference.pdf) (as "Description revision")**
> The observable task of editing a given textual description to improve its accuracy or quality with respect to an associated image.

**[Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf) (as "Failure correction")**
> Revising an action choice after a failed execution by proposing a more suitable next action.

**[Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf) (as "Answer correction")**
> Editing or rewriting an initial model answer into a revised answer that better satisfies the desired criteria.

**[SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf) (as "Token correction")**
> Replacing or rewriting selected generated tokens using the full model during decoding.

**[MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf) (as "Conditional weak-to-strong correction")**
> The observable process of taking a 'weak' (less preferred) model output as input and generating a 'strong' (more preferred) output that is better aligned with specified objectives.

**[Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf) (as "Self-debugging")**
> The model's capacity to identify and correct errors in its own generated code based on feedback from code execution.

**[Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf) (as "Self-reflection")**
> The ability of an agent to analyze its past actions and failures to generate insights for future improvement.

**[Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf) (as "Self-evaluation")**
> The observable process where a language model assesses its own generated text against a given criterion, such as harmlessness, to produce a score.

**[Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) (as "Fine-grained evaluation capability")**
> The ability to judge text quality using detailed, user-defined criteria rather than only coarse or generic preferences.

**[Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) (as "Evaluation capability")**
> The latent ability of a language model to assess the quality of generated text according to customized, fine-grained criteria provided via score rubrics and reference materials.

**[DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf) (as "Reflection")**
> The ability of the model to evaluate past decision sequences, identify errors, and generate corrected reasoning to improve future performance.

**[Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf) (as "Discrimination")**
> The latent ability of a model to identify and analyze potential mistakes, errors, or harmful elements within a given response.

**[Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf) (as "Self-critique")**
> The capability of a model to evaluate, identify flaws in, and analyze its own generated outputs without external feedback.

**[LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf) (as "Self-repair")**
> A latent mechanism by which a model compensates for changes or losses in individual functional components to maintain stable task performance.

**[SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf) (as "Self-refinement capability")**
> The ability to iteratively improve generated code by identifying and fixing its own errors based on internal analysis or feedback.

**[SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf) (as "Self-correction ability")**
> The latent capacity of a model to independently identify and rectify errors within its own generated reasoning process.

**[Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/80790082a3b0e4fa9061730ee876f5ba-Paper-Conference.pdf) (as "Self-correction capability")**
> The latent ability of a model to identify and rectify its own errors in reasoning or generation without external corrective feedback.

**[SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf) (as "Refinement capability")**
> The latent ability of a model to correct or improve a response that fails to follow an instruction, ideally with minimal irrelevant revisions.

**[Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf) (as "Progressive refinement")**
> The ability of a model to iteratively improve the accuracy, depth, and quality of its responses starting from an initial thought or approximate solution.

**[LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf) (as "Self-repair capability")**
> The latent ability to use error feedback to revise an initially flawed program into a correct solution.

**[ACCORD: Closing the Commonsense Measurability Gap](https://aclanthology.org/2025.naacl-long.194.pdf) (as "Error recovery")**
> The ability of an LLM agent to adjust its strategy and correct its course of action based on feedback from the environment, such as error messages.

**[OASIS: Order-Augmented Strategy for Improved Code Search](https://aclanthology.org/2025.acl-long.905.pdf) (as "Self-critique ability")**
> The latent capacity of a model to accurately evaluate and identify errors in its own reasoning process, as opposed to evaluating others' reasoning.

**[AnRe: Analogical Replay for Temporal Knowledge Graph Forecasting](https://aclanthology.org/2025.acl-long.232.pdf) (as "Self-revision capability")**
> The latent ability of a model to effectively correct its own incorrect reasoning or answers during iterative refinement, without external feedback.

**[Maximizing the Effectiveness of LargerBERTModels for Compression](https://aclanthology.org/2025.acl-long.1068.pdf) (as "Self-repair ability")**
> The capacity of LLMs to detect and correct their own errors in formal specification generation when provided with feedback or targeted prompts, indicating metacognitive reasoning and adaptability.

**[SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf) (as "Debugging capability")**
> The latent ability to identify, analyze, and correct errors in source code.

**[Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/83ba7056bce2c3c3c27e17397cf3e1f0-Paper-Conference.pdf) (as "Debugging ability")**
> The latent capability of a large language model to identify, analyze, and correct errors in source code or computational workflows.

**[kGym: A Platform and Dataset to Benchmark Large Language Models on Linux Kernel Crash Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/8e9ed2a28af7d9085180e3817b2c9a57-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Bug localization")**
> The ability to infer which code files or functions are responsible for a reported crash from limited diagnostic information.

**[Concept Bottleneck Language Models For Protein Design](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cf2d1a2fef23281af0f50d1a04dfd7c-Paper-Conference.pdf) (as "Debuggability")**
> The capacity to easily identify, diagnose, and correct unwanted behaviors or errors in the model by inspecting its internal concept-based representations.

**[Automated Proof Generation for Rust Code via Self-Evolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2e20d7402c9985eae4ba924c65370a8-Paper-Conference.pdf) (as "Self-debugging capability")**
> The latent ability of a model to repair incorrect proofs or outputs based on feedback from a verification system.

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf) (as "Self-verification")**
> The inherent ability of a model to assess the correctness of its own generated solutions or reasoning steps, particularly by generating and executing code to validate an answer.

**[AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf) (as "Self-evolution")**
> The ability of a model to autonomously improve its capabilities and reinforce its knowledge utilization through iterative self-generated training, without external process supervision.

**[CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf) (as "Self-improvement")**
> The latent capacity of a model to effectively analyze and correct flaws in its own or others' responses, facilitated by critique ability.

**[StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Continuous improvement")**
> The ability of an LLM agent to enhance its performance on a task over time by learning from a continuous sequence of inputs and feedback.

**[Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf) (as "Self-improvement capability")**
> The latent ability of a large language model to improve its performance by generating outputs, verifying them, and then updating itself based on the verified data.

**[Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c4a7643ab90cd62320df95c873a1c6f-Paper-Conference.pdf) (as "Policy improvement")**
> The latent process of refining a strategy or policy in-context to maximize cumulative rewards based on new information discovered through interaction.

**[Kill two birds with one stone: generalized and robustAI-generated text detection via dynamic perturbations](https://aclanthology.org/2025.naacl-long.447.pdf) (as "Learning from mistakes")**
> The model's capacity to improve its reasoning by analyzing and correcting flawed rationales, treating errors as opportunities for self-improvement.

**[DCE-LLM: Dead Code Elimination with Large Language Models](https://aclanthology.org/2025.naacl-long.502.pdf) (as "Iterative reflection capability")**
> The latent ability of a model to effectively refine its responses over multiple cycles of self-evaluation and revision, avoiding degradation due to redundancy, drift, or stubbornness.

**[DCE-LLM: Dead Code Elimination with Large Language Models](https://aclanthology.org/2025.naacl-long.502.pdf) (as "Self-Reflection")**
> A reflection-based evaluation procedure in which the model iteratively revises its own answer using feedback.

**[Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf) (as "Reflection capability")**
> The degree of an agent's proficiency in generating useful verbal feedback from prior experiences to improve subsequent task performance.

**[Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Introspection")**
> The ability to access information about internal representations or predict one's own behavior in hypothetical scenarios, using mechanisms that do not depend solely on learning from the training distribution.

**[HalluLens:LLMHallucination Benchmark](https://aclanthology.org/2025.acl-long.1177.pdf) (as "Current reflection")**
> The ability of a persona update process to adapt to recent user behaviors by incorporating dynamic changes and correcting errors in the existing persona.

**[MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gaven25a/gaven25a.pdf) (as "Metacognitive monitoring")**
> The latent ability of an LLM agent to model its own competence and learning progress across goals by leveraging semantic relationships, enabling self-directed curriculum learning.

**[Reflection-Bench: Evaluating Epistemic Agency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cu/li25cu.pdf) (as "Meta-reflection")**
> The higher-order capacity to recognize and anticipate global patterns across multiple cycles of prediction, action, and feedback, enabling regulation beyond local adaptation.

**[SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1313.pdf) (as "Mistake detection")**
> The latent ability to identify incorrect or flawed reasoning steps within a chain of thought, even when the final answer may appear plausible.

**[SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf) (as "Refinement")**
> The ability of a model to iteratively improve its output based on feedback or further instructions.

**[Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf) (as "Solution refinement")**
> The latent ability of an LLM to dynamically improve its answers to complex scientific or technical questions through iterative self-evaluation and critique.

**[Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf) (as "Action evaluation")**
> The internal capacity of an LLM to assess the quality or likely success of candidate actions based on simulated outcomes and reasoning, serving as a critic in decision-making.

**[Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mukherjee25a/mukherjee25a.pdf) (as "Error detection")**
> The model's underlying capability to recognize inaccuracies in reasoning steps, including both inherent errors and those arising from flawed dependencies.

**[VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25h/zeng25h.pdf) (as "Reasoning quality evaluation")**
> The ability to judge whether intermediate reasoning steps are correct, logical, and supported by prior steps.

**[Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cw/liu25cw.pdf) (as "Self-assessment")**
> The ability of an agent to accurately evaluate its own knowledge, skills, strengths, and weaknesses.

**[Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf) (as "Critiquing ability")**
> The capacity to generate feedback that both accurately assesses a solution and helps improve it in subsequent revisions.

**[Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf) (as "Judging ability")**
> The latent capacity of an LLM to accurately assess the quality of model-generated responses, particularly in guiding test-time computation through reranking, beam search, or refinement.

## Relationships

### Self-correction →
- **Generalization** (constructs) — *causes*
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **HyPoradise** (measurements) — *measured_by*
  - [It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  - [AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf)
- **EvalPlus** (measurements) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  - [LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbe6dd68b0cf2b1d43b458d2b8ca31b0-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Financial Risk Relation Identification through Dual-view Adaptation](https://aclanthology.org/2025.emnlp-main.1337.pdf)
- **Problem-solving** (behaviors tasks) — *causes*
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Decision-making** (constructs) — *causes*
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
- **Output diversity** (constructs) — *causes*
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *causes*
  - [Adaptive Self-improvement LLM Agentic System for ML Library Development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25at/zhang25at.pdf)

### → Self-correction
- **Self-reflection** (behaviors tasks) — *causes*
  - [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *causes*
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Code execution** (behaviors tasks) — *causes*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *causes*
  - [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **Memory management** (constructs) — *causes*
  - [Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](https://proceedings.neurips.cc/paper_files/paper/2024/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Planning** (constructs) — *causes*
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Instruction following** (constructs) — *causes*
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Iterative refinement** (behaviors tasks) — *causes*
  - [Articulate-Anything:  Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf)
- **Specialization** (constructs) — *causes*
  - [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf)
- **Critique generation** (behaviors tasks) — *causes*
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **In-context reinforcement learning** (constructs) — *causes*
  - [In-Context Reinforcement Learning From Suboptimal Historical Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25d/dong25d.pdf)
- **Meta-learning** (constructs) — *causes*
  - [Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cw/liu25cw.pdf)

### Associated with
- **Self-reflection** (behaviors tasks)
  - [Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
- **Critique** (behaviors tasks)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  - [SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1313.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Think Smarter not Harder: Adaptive Reasoning with Inference Aware Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25s/yu25s.pdf)
- **Code generation** (behaviors tasks)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **STAR** (measurements)
  - [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf)
- **Hypothesis generation** (behaviors tasks)
  - [MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](https://proceedings.iclr.cc/paper_files/paper/2025/file/51fd9a7d1706023cb9f8210cc6ac357c-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [Pay More Attention to Images: Numerous Images-Oriented Multimodal Summarization](https://aclanthology.org/2025.naacl-long.475.pdf)
- **Generalization** (constructs)
  - [UniRAG: Unified Query Understanding Method for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.694.pdf)
- **System 2 thinking** (constructs)
  - [MaXIFE: Multilingual and Cross-lingual Instruction Following Evaluation](https://aclanthology.org/2025.acl-long.699.pdf)
