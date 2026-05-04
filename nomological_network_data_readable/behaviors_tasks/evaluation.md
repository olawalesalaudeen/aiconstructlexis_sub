# Evaluation
**Type:** Behavior  
**Referenced in:** 269 papers  
**Also known as:** Answer verification, Bug detection, Accounting bug detection, Error awareness, Stepwise error detection, Invalid node identification, Fault localization, Misleading region localization, Self-verification, Self-checking, Draft verification, Probability estimation, Confidence Expression, Expressing uncertainty, Confidence score generation, Step correctness prediction, Confidence correction, Verbalized confidence, Nuanced uncertainty expression, Linguistic uncertainty expression, Natural language uncertainty expression, Self-knowledge estimation, Uncertainty estimation, Noise correction, Spelling correction, Error correction, Typo correction, Correcting errors, Mistake correction, Student mistake correction, Fact refinement, Iterative hypothesis refinement, Patch refinement, Bug fixing, Answer refinement, Natural language refinement, Self-refinement, Text correction, Assessment refinement, Chain-of-thought correction, Thought refinement, Hallucination correction, Multi-round self-correction, Invalid SMILES correction, Code fixing, Response refinement, Iterative self-correction, Iterative chart refinement, Over-correction, Grammar correction, Chinese spelling correction, Overcorrection, Undercorrection, Activity evaluation, Peer evaluation, Policy evaluation, Trajectory evaluation, Answerable judging, Outcome judging, Process judging, Anomaly discrimination, Interestingness evaluation, Self-examination, Providing feedback, Response judgment, Patch scoring, Response verification, Self-critique, Hypothesis evaluation, Summarization evaluation, Peer review generation, Quality rating, Solution verification, Self-assessment, Checklist grading, Single answer grading, Multi-turn chat judging, Multimodal judging, Research idea evaluation, LLM judging, Scoring, Pairwise preference judgment, Preference judgment, Arena-style comparison, Binary response comparison, Preference feedback generation, Pair-wise preference, Pairwise preference selection, Knowledge comparison, Plausibility prediction, Response pair judgment, LM-as-a-judge, Authenticity judgment, Abnormal detail selection, Response comparison, Response critique, Open-ended generation evaluation, Pairwise response evaluation, Success evaluation, Thought evaluation, Unit test evaluation, Answer existence judgment, Double-checking, Action evaluation, Program evaluation, Veracity analysis, Factuality checking, Fact extraction and verification, Veracity judgment, Fact verification, Table fact verification, Statement verification, Verdict prediction, Factual consistency evaluation, Veracity labeling, Hypothesis validation, Correction verification, Ownership verification, Plan verification, Verification, Forward verification, Proof verification, Answer correctness assessment, Reasoning chain validation, Sentence-level verification, Factual verification, Hypothesis verification, Label verification, Cross-modal verification, Connection verification, Sequence answer verification, Evaluation capability  

## State of the Field

Across the surveyed literature, 'Evaluation' is predominantly framed as a diverse set of observable behaviors rather than a single, unified task, although a few papers define it as a latent ability. These behaviors can be broadly categorized into several activities: identifying errors, assessing output quality, expressing internal confidence, and rectifying mistakes. The most common forms of evaluation involve assessing outputs, which includes judging the correctness of a solution, as in 'Outcome judging', and making comparative judgments, frequently through pairwise preference selection ('Pairwise preference judgment', 'LM-as-a-judge'). Another prevalent category is fact and claim verification, where a model's output is checked against a knowledge source ('Fact checking', 'Claim verification'). A distinct line of work focuses on a model's capacity for introspection, operationalized as its ability to express confidence or uncertainty, either through numerical scores ('Confidence estimation') or natural language phrases ('Expressing uncertainty'). The literature also extensively covers the subsequent act of rectifying identified issues, with numerous definitions for behaviors like 'Self-correction', 'Iterative refinement', and 'Bug fixing'. To measure these behaviors, researchers employ a wide array of benchmarks; fact verification is commonly measured using datasets like FEVER and TabFact, while judging capabilities are often assessed with MT-Bench, and correction in problem-solving is operationalized through benchmarks such as GSM8k and HumanEval. Evaluation is frequently studied alongside 'Self-reflection', which some papers suggest is a driver for evaluation capabilities, and is also closely related to the concepts of 'Faithfulness' and 'Self-correction'.

## Sources

**[Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf) (as "Answer verification")**
> The observable behavior of generating and executing a specific procedure, typically code-based, to check the validity of a previously derived answer.

**[LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf) (as "Bug detection")**
> The observable task of identifying specific categories of vulnerabilities or errors in source code, such as divide-by-zero, cross-site scripting, or OS command injection.

**[Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf) (as "Error detection")**
> The observable process of an agent identifying mistakes or failures in its own or another agent's reasoning or actions.

**[Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1d8400fec75f683c4d823f5836a81bb-Paper-Conference.pdf) (as "Accounting bug detection")**
> Identifying smart-contract statements or code regions that violate domain-specific financial-model constraints.

**[Targeted Syntactic Evaluation for Grammatical Error Correction](https://aclanthology.org/2025.acl-long.1027.pdf) (as "Error awareness")**
> The observable task of identifying the presence of general errors in a given video, typically evaluated with binary (Yes/No) questions.

**[Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bb/wang25bb.pdf) (as "Stepwise error detection")**
> The observable task of examining a specified step within a given solution to a problem and determining whether that step is correct or incorrect.

**[SafeKey: Amplifying Aha-Moment Insights for Safety Reasoning](https://aclanthology.org/2025.emnlp-main.1292.pdf) (as "Invalid node identification")**
> The task of identifying the specific papers within an invalid reasoning chain where the logical progression or coherence breaks down.

**[RuCCoD: Towards AutomatedICDCoding inRussian](https://aclanthology.org/2025.emnlp-main.130.pdf) (as "Fault localization")**
> Identifying the source of a bug or failure within code or a repository.

**[DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.695.pdf) (as "Misleading region localization")**
> The observable task of identifying and outputting the coordinates of specific regions within a chart that are considered deceptive or misleading.

**[Mitigating Hallucinations inLM-BasedTTSModels via Distribution Alignment UsingGFlowNets](https://aclanthology.org/2025.emnlp-main.977.pdf) (as "Error localization")**
> The observable task of pinpointing the specific contiguous span of text within a molecular description that contains a chemical error.

**[AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf) (as "Self-verification")**
> The observable process where a model assesses the correctness or reliability of its own generated output, typically by checking for consistency with a given context.

**[Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf) (as "Self-checking")**
> The action of a model reviewing its own generated rationale to identify and correct potential errors.

**[Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf) (as "Draft verification")**
> Checking whether proposed draft tokens match the base language model's greedy next-token predictions.

**[Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf) (as "Confidence estimation")**
> The model generates a numerical score representing its certainty that its judgment aligns with human preferences.

**[BIRD: A Trustworthy Bayesian Inference Framework for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/19452e14fe6e0a8ac00410f1eebcbded-Paper-Conference.pdf) (as "Probability estimation")**
> The observable act of assigning a numerical probability or confidence score to a potential outcome given a context.

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf) (as "Confidence Expression")**
> Providing probability estimates or confidence levels for predictions, often by verifying if a predicted answer is correct via token probability.

**[Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf) (as "Expressing uncertainty")**
> The observable behavior of a model explicitly stating its lack of confidence or knowledge in its response, such as by outputting phrases like 'I am unsure'.

**[Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf) (as "Confidence score generation")**
> The action of producing numerical confidence values for each potential class in a classification task, expressed within a natural language response.

**[AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.171.pdf) (as "Step correctness prediction")**
> The observable task of assigning a confidence score to each reasoning step indicating whether it is correct or incorrect, based on internal model states.

**[AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.171.pdf) (as "Self-evaluation")**
> The observable behavior of an LLM producing internal confidence signals about its own reasoning steps without external feedback.

**[2025.emnlp-main.530.checklist](https://aclanthology.org/attachments/2025.emnlp-main.530.checklist.pdf) (as "Confidence expression")**
> The model's output of a probability or likelihood score associated with its generated response or prediction.

**[WISE: Weak-Supervision-Guided Step-by-Step Explanations for MultimodalLLMs in Image Classification](https://aclanthology.org/2025.emnlp-main.742.pdf) (as "Confidence correction")**
> The observable pattern in which a model's confidence increases beyond accuracy (overconfidence) and then decreases to better align with accuracy in later layers, indicating active recalibration of confidence.

**[VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.73.pdf) (as "Verbalized confidence")**
> The observable expression of a model's certainty in its answer, typically in the form of a percentage or probability statement.

**[Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.187.pdf) (as "Nuanced uncertainty expression")**
> The generation of text that qualifies an answer with expressions of doubt or uncertainty, such as "I am not sure but..." or "maybe".

**[Multilingual Pretraining for Pixel Language Models](https://aclanthology.org/2025.emnlp-main.1505.pdf) (as "Linguistic uncertainty expression")**
> The observable use of words, phrases, and hedging language to convey a degree of confidence or doubt in a generated response.

**[2025.emnlp-main.1505.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1505.checklist.pdf) (as "Natural language uncertainty expression")**
> The model generates explicit statements about its confidence or uncertainty using natural language (e.g., 'I'm not sure' or 'I'm highly confident').

**[Your Language Model Can Secretly Write Like Humans: Contrastive Paraphrase Attacks onLLM-Generated Text Detectors](https://aclanthology.org/2025.emnlp-main.434.pdf) (as "Self-knowledge estimation")**
> The observable task of assigning a score to a model's own generated answer that reflects the model's confidence in its factual correctness, framed as a binary classification problem.

**[Your Language Model Can Secretly Write Like Humans: Contrastive Paraphrase Attacks onLLM-Generated Text Detectors](https://aclanthology.org/2025.emnlp-main.434.pdf) (as "Uncertainty estimation")**
> The model's generation of confidence or uncertainty signals (e.g., perplexity, token entropy) in response to input questions, used to infer implicit awareness of evergreen-ness.

**[MentalGLMSeries: Explainable Large Language Models for Mental Health Analysis onChinese Social Media](https://aclanthology.org/2025.emnlp-main.687.pdf) (as "Confidence scoring")**
> Assigning a numerical confidence level to a diagnostic decision based on factual consistency and evidence from a reasoning subgraph.

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

**[RuCCoD: Towards AutomatedICDCoding inRussian](https://aclanthology.org/2025.emnlp-main.130.pdf) (as "Self-correction")**
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

**[PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf) (as "Peer evaluation")**
> The observable action of one LLM assessing the quality of a response generated by another LLM, often by making a comparative judgment.

**[Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf) (as "Trajectory evaluation")**
> Judging whether an action sequence and its observations satisfy an instruction or task intent.

**[Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf) (as "Activity evaluation")**
> The observable process of an agent assessing the potential impact of each candidate activity on its internal desire states.

**[Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf) (as "Answerable judging")**
> The observable behavior of determining whether a given mathematical problem contains sufficient information to be solved.

**[Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf) (as "Outcome judging")**
> The observable behavior of determining whether the final answer in a provided solution to a math problem is correct.

**[Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf) (as "Process judging")**
> The observable behavior of identifying the specific step in a provided incorrect solution where the first error occurs.

**[Zero-shot Model-based Reinforcement Learning using Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf) (as "Policy evaluation")**
> Estimating the value or performance of a policy using a combination of online interaction and model-based rollout.

**[SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf) (as "Response judgment")**
> The observable action of a model producing an assessment of a given response, typically including a label and an explanation of whether the response followed an instruction.

**[Self-Improvement in Language Models: The Sharpening Mechanism](https://proceedings.iclr.cc/paper_files/paper/2025/file/bee8c2bc757f6bbc3efd7cf1b979f0c9-Paper-Conference.pdf) (as "Response verification")**
> The observable action of a model evaluating the quality of a given response, typically by assigning it a score or probability.

**[Empowering LLM Agents with Zero-Shot Optimal Decision-Making through Q-learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c25de6a9da675464ebb925e430c58325-Paper-Conference.pdf) (as "Self-examination")**
> An observable process where a model uses its own capabilities to check, validate, and correct its generated outputs, such as actions or state predictions.

**[OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/d40d7cbe7210f8a13ea0149eeae9c6de-Paper-Conference.pdf) (as "Interestingness evaluation")**
> The observable action of assessing a newly generated task to determine if it is sufficiently novel, surprising, or worthwhile compared to a collection of existing tasks.

**[Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf) (as "Patch scoring")**
> The behavior of assigning a numerical score to a candidate code patch based on an evaluation of its correctness and quality.

**[MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d91ffbe9c126765755ff52d36b715683-Paper-Conference.pdf) (as "Anomaly discrimination")**
> Judging whether an industrial image contains a defect or anomaly.

**[ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf) (as "Providing feedback")**
> Generating critique or guidance on another agent's answer during a collaborative exchange.

**[Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf) (as "Summarization evaluation")**
> The task of judging the quality of generated summaries against human preferences.

**[CycleResearcher: Improving Automated Research via Automated Review](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a48036026dc7946ef6033ae14719cc5-Paper-Conference.pdf) (as "Peer review generation")**
> The observable task of generating textual feedback on a research paper, including strengths, weaknesses, and numerical scores for different criteria, simulating a human peer review.

**[Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/12f483f624b378f9f3058d8ecd3c7ff5-Paper-Conference.pdf) (as "Hypothesis evaluation")**
> The process of scoring or assessing generated hypotheses based on their ability to accurately predict the future actions of other agents.

**[DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf) (as "Quality rating")**
> Assigning a discrete quality level to a document based on criteria such as coherence, creativity, or professionalism.

**[Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf) (as "Self-critique")**
> The observable behavior where a model is instructed to critique its own output as a step towards improving it.

**[Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf) (as "Solution verification")**
> The observable task of a model assessing a given problem-solution pair and predicting its correctness, typically as a 'Yes' or 'No' token.

**[JudgeLM: Fine-tuned Large Language Models are Scalable Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f8f73134e253845a8f82983219a8452-Paper-Conference.pdf) (as "Single answer grading")**
> The observable task of evaluating a single model-generated answer and assigning it a score.

**[JudgeLM: Fine-tuned Large Language Models are Scalable Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f8f73134e253845a8f82983219a8452-Paper-Conference.pdf) (as "Multimodal judging")**
> Assessing answers or outputs from multimodal models that combine text with other modalities.

**[JudgeLM: Fine-tuned Large Language Models are Scalable Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f8f73134e253845a8f82983219a8452-Paper-Conference.pdf) (as "Multi-turn chat judging")**
> Evaluating conversational responses across multiple dialogue turns.

**[RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf) (as "Checklist grading")**
> The task of evaluating a model's response against a series of specific, independent criteria or questions, typically with a binary or scaled judgment for each item.

**[Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf) (as "Self-assessment")**
> Evaluating whether the generated definition, formulation, and code are correct based on the execution result.

**[GraphEval: A Lightweight Graph-Based LLM Framework for Idea Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5ce40ee957e4f76ef53c09d0bae20f4-Paper-Conference.pdf) (as "Research idea evaluation")**
> Assigning a quality judgment or review decision to a research idea based on its title and abstract.

**[Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf) (as "LLM judging")**
> Using an LLM as a judge to compare model responses and produce win-tie-loss style judgments.

**[Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf) (as "Scoring")**
> The observable task where an LLM judge provides a numerical score for a single given response based on specified criteria.

**[Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf) (as "Preference judgment")**
> The observable task of comparing two candidate answers to a prompt and selecting the preferred one.

**[Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf) (as "Pairwise preference judgment")**
> Selecting one of two model outputs as better according to explicit or implicit criteria.

**[How to Evaluate Reward Models for RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e01083b381b4865919b4915ef32e3d2-Paper-Conference.pdf) (as "Pairwise preference selection")**
> Choosing one of two responses as preferred in a head-to-head comparison.

**[BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf) (as "Pair-wise preference")**
> Choosing a winner between two candidate responses or models.

**[Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf) (as "Preference feedback generation")**
> The observable task of providing a comparative judgment between two responses to a given prompt, indicating which one is preferred.

**[Interpreting Language Reward Models via Contrastive Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/3538a22cd3ceb8f009cc62b9e535c29f-Paper-Conference.pdf) (as "Binary response comparison")**
> Choosing one of two candidate responses to the same prompt as the preferred response.

**[Limits to scalable evaluation at the frontier: LLM as judge won’t beat twice the data](https://proceedings.iclr.cc/paper_files/paper/2025/file/4264ee4376776907c0b87ed70b959585-Paper-Conference.pdf) (as "Arena-style comparison")**
> Comparing two model responses to the same prompt and selecting which response is better.

**[Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf) (as "Knowledge comparison")**
> Answering questions that compare two stored attributes and decide which one is greater or better according to a ranking.

**[NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf) (as "Plausibility prediction")**
> The observable task of determining which of two hypothesis images is more plausible given a premise image, or assigning a plausibility score to a single hypothesis.

**[JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf) (as "Response pair judgment")**
> Selecting which of two candidate responses is better or more correct, optionally with a tie option.

**[Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf) (as "LM-as-a-judge")**
> The task of using a language model to evaluate and select the better of two candidate responses for a given prompt or question.

**[LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afd6374c7f2839cba22f537f15f4f760-Paper-Conference.pdf) (as "Authenticity judgment")**
> The task of making a binary determination of whether a given piece of data is synthetic or real.

**[LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afd6374c7f2839cba22f537f15f4f760-Paper-Conference.pdf) (as "Abnormal detail selection")**
> The task of identifying specific inconsistent or anomalous elements within a piece of synthetic content from a list of choices.

**[An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf) (as "Unit test evaluation")**
> Evaluating candidate responses against generated unit tests and using the test outcomes to rank or filter responses.

**[An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf) (as "Response critique")**
> Producing strengths and weaknesses for candidate responses so they can be improved or selected.

**[Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf) (as "Pairwise response evaluation")**
> The task of taking an instruction and a pair of model-generated responses as input and producing a judgment indicating which response is better.

**[Accelerating Large Language Model Reasoning via Speculative Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25di/wang25di.pdf) (as "Thought evaluation")**
> The process of assessing the quality of generated reasoning steps using a thought evaluator such as a process reward model, determining which thoughts to accept or reject.

**[SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf) (as "Open-ended generation evaluation")**
> The task of assessing the quality of unconstrained, free-form text generated by a language model, often using another LLM as a judge.

**[Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf) (as "Response comparison")**
> The behavior of directly comparing two or more candidate responses to determine which is correct, particularly when verification scores are close.

**[Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf) (as "Answer existence judgment")**
> Determining whether the correct answer to a medical question is present within a given set of candidate options, testing the model's ability to assess answer plausibility in open decision spaces.

**[Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ah/zhou25ah.pdf) (as "Success evaluation")**
> Assessing whether a task has been completed successfully based on final outcomes, typically using binary judgments from VLMs or humans.

**[FunBO: Discovering Acquisition Functions for Bayesian Optimization with FunSearch](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aglietti25a/aglietti25a.pdf) (as "Program evaluation")**
> Running a full Bayesian optimization loop to assess the performance of a candidate acquisition function on a set of objective functions.

**[Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf) (as "Double-checking")**
> The observable behavior of generating a subsequent solution to verify or re-evaluate a previously generated solution, often using the same reasoning strategy.

**[Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf) (as "Action evaluation")**
> The observable process of assigning numerical values (Q-values) to candidate actions based on token logits for 'GOOD'/'BAD' outcomes, incorporating future trajectory rollouts and reflections.

**[Self-Critique and Refinement for Faithful Natural Language Explanations](https://aclanthology.org/2025.emnlp-main.428.pdf) (as "Veracity prediction")**
> The task of classifying a claim as true, false, or another relevant category based on retrieved evidence.

**[AnchorAttention: Difference-Aware Sparse Attention with Stripe Granularity](https://aclanthology.org/2025.emnlp-main.431.pdf) (as "Veracity analysis")**
> The process of synthesizing evidence to make a judgment on whether a claim should be believed, including handling cases of missing or contradictory evidence.

**[Stop Looking for “Important Tokens” in Multimodal Language Models: Duplication Matters More](https://aclanthology.org/2025.emnlp-main.506.pdf) (as "Fact extraction and verification")**
> The task of identifying factual claims in text and verifying their correctness against a knowledge source.

**[PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.508.pdf) (as "Factuality checking")**
> Judging whether a generated fact is entailed by retrieved evidence.

**[PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf) (as "Fact checking")**
> The task of verifying the truthfulness of a given claim against a corpus of evidence.

**[RCScore: Quantifying Response Consistency in Large Language Models](https://aclanthology.org/2025.emnlp-main.291.pdf) (as "Veracity judgment")**
> The task of making a final determination on whether a piece of news is true or false, based on provided analysis, evidence, and decision rules.

**[DMDTEval: An Evaluation and Analysis ofLLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.310.pdf) (as "Claim verification")**
> Determining whether a scientific claim is supported or refuted by evidence in a given abstract or paper, often accompanied by extracted supporting or refuting statements.

**[NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.365.pdf) (as "Fact verification")**
> The task of determining whether a given claim is supported or refuted by evidence from a provided knowledge source.

**[R2I-Bench: Benchmarking Reasoning-Driven Text-to-Image Generation](https://aclanthology.org/2025.emnlp-main.637.pdf) (as "Table fact verification")**
> The task of determining whether a given statement is true or false based on the content of an associated table.

**[One Planner To Guide Them All ! Learning Adaptive Conversational Planners for Goal-oriented Dialogues](https://aclanthology.org/2025.emnlp-main.1124.pdf) (as "Statement verification")**
> The observable behavior of a model assessing whether a given statement is factually correct, often through step-by-step reasoning.

**[Language Models Can be Efficiently Steered via Minimal Embedding Layer Transformations](https://aclanthology.org/2025.emnlp-main.1171.pdf) (as "Verdict prediction")**
> Classifying the truthfulness of a claim based on retrieved evidence, typically as Supported, Refuted, or NotEnoughInfo.

**[iVISPAR— An Interactive Visual-Spatial Reasoning Benchmark forVLMs](https://aclanthology.org/2025.emnlp-main.1360.pdf) (as "Factual consistency evaluation")**
> Assessing whether a generated text (e.g., summary, dialogue response) is factually consistent with respect to a grounding text or source document.

**[Extending Automatic Machine Translation Evaluation to Book-Length Documents](https://aclanthology.org/2025.emnlp-main.1646.pdf) (as "Veracity labeling")**
> Assigning a truthfulness label to a claim-evidence pair after reviewing both elements, either through human annotation or LLM-assisted labeling.

**[EasyRec: Simple yet Effective Language Models for Recommendation](https://aclanthology.org/2025.emnlp-main.895.pdf) (as "Hypothesis validation")**
> Assessing the validity of scientific hypotheses through code generation, replication, or outcome prediction.

**[Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1475.pdf) (as "Ownership verification")**
> Querying a model via API with predefined watermark inputs and analyzing outputs to detect the presence of embedded identifiers for tracing purposes.

**[The Good, the Bad and the Constructive: Automatically Measuring Peer Review’s Utility for Authors](https://aclanthology.org/2025.emnlp-main.1477.pdf) (as "Correction verification")**
> Judging whether a proposed correction is better than the original sentence or whether both versions are incorrect.

**[Token-level Proximal Policy Optimization for Query Generation](https://aclanthology.org/2025.emnlp-main.1590.pdf) (as "Verification")**
> Identifying errors or checking whether a solution is correct.

**[Discursive Circuits: How Do Language Models Understand Discourse Relations?](https://aclanthology.org/2025.emnlp-main.1658.pdf) (as "Plan verification")**
> Comparing two versions of a plan and selecting the one judged to be superior in terms of correctness, completeness, or safety.

**[SAKI-RAG: Mitigating Context Fragmentation in Long-DocumentRAGvia Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.64.pdf) (as "Forward verification")**
> Using chain-of-thought reasoning to assess and correct the semantic consistency between a synthesized natural language question and its corresponding formal query.

**[Diagnosing Memorization in Chain-of-Thought Reasoning, One Token at a Time](https://aclanthology.org/2025.emnlp-main.158.pdf) (as "Proof verification")**
> Checking whether a generated formal proof is accepted by the Lean4 compiler or verifier.

**[2025.emnlp-main.710.checklist](https://aclanthology.org/attachments/2025.emnlp-main.710.checklist.pdf) (as "Answer correctness assessment")**
> Observably determining whether a generated answer is factually accurate and logically sound based on evidence from heterogeneous documents.

**[SafeKey: Amplifying Aha-Moment Insights for Safety Reasoning](https://aclanthology.org/2025.emnlp-main.1292.pdf) (as "Reasoning chain validation")**
> Determining whether a sequence of chronologically ordered scientific papers forms a logically coherent and valid path of reasoning, and identifying breakpoints where inconsistencies occur.

**[Exploring Large Language Models for Detecting Mental Disorders](https://aclanthology.org/2025.emnlp-main.1753.pdf) (as "Sentence-level verification")**
> The observable process of checking the factual correctness of individual sentences as they are generated during text production.

**[SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection](https://aclanthology.org/2025.emnlp-main.826.pdf) (as "Factual verification")**
> The observable task of assessing a given factual statement and producing a binary output of "True" or "False" based on the instructional context.

**[SOLAR: Towards Characterizing Subjectivity of Individuals through Modeling Value Conflicts and Trade-offs](https://aclanthology.org/2025.emnlp-main.1054.pdf) (as "Hypothesis verification")**
> Determining whether a hypothesis is true, false, or unknown from a set of facts and rules.

**[Beyond the Score: Uncertainty-CalibratedLLMs for Automated Essay Assessment](https://aclanthology.org/2025.emnlp-main.993.pdf) (as "Label verification")**
> The observable behavior of an LLM checking whether a provided label for a query is consistent with its internal knowledge by attempting to reproduce it in a task-specific context.

**[Hanfu-Bench: A Multimodal Benchmark on Cross-Temporal Cultural Understanding and Transcreation](https://aclanthology.org/2025.emnlp-main.1252.pdf) (as "Cross-modal verification")**
> Validating emotion predictions by checking consistency between textual reasoning and visual evidence across iterative refinement steps.

**[Rule Discovery for Natural Language Inference Data Generation Using Out-of-Distribution Detection](https://aclanthology.org/2025.emnlp-main.1320.pdf) (as "Connection verification")**
> The task of determining the spatial relationship (e.g., above-below, left-right, or non-adjacent) between two randomly selected patches from an original image.

**[ReflAct: World-Grounded Decision Making inLLMAgents via Goal-State Reflection](https://aclanthology.org/2025.emnlp-main.1698.pdf) (as "Sequence answer verification")**
> Evaluating responses that consist of ordered sequences of elements, requiring element-by-element matching against a reference sequence.

**[DrDiff: Dynamic Routing Diffusion with Hierarchical Attention for Breaking the Efficiency-Quality Trade-off](https://aclanthology.org/2025.emnlp-main.475.pdf) (as "Preferred response prediction")**
> Selecting the most likely user-preferred response from a set of candidates for a given context, based on a learned reward model.

**[Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf) (as "Evaluation capability")**
> The model's latent ability to accurately assess the quality or correctness of a generated trajectory or its intermediate steps.

**[AI-Assisted Human Evaluation of Machine Translation](https://aclanthology.org/2025.naacl-long.256.pdf)**
> The latent ability of MLLMs to make judgments based on criteria and standards, such as assessing image quality or discerning content authenticity.

## Relationships

### Evaluation →
- **FEVER** (measurements) — *measured_by*
  - [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **SelfCheckGPT** (measurements) — *measured_by*
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **TabFact** (measurements) — *measured_by*
  - [Mitigating Lost-in-Retrieval Problems in Retrieval Augmented Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.1090.pdf)
- **FEVEROUS** (measurements) — *measured_by*
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *causes*
  - [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Critique** (behaviors tasks) — *causes*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **FB15k-237** (measurements) — *measured_by*
  - [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Automated Hypothesis Validation with Agentic Sequential Falsifications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25n/huang25n.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
- **Vicuna-Bench** (measurements) — *measured_by*
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
- **RTE** (measurements) — *measured_by*
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
- **Reward-Bench** (measurements) — *measured_by*
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Creak** (measurements) — *measured_by*
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
- **SWE-bench** (measurements) — *measured_by*
  - [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf)
- **ALFWorld** (measurements) — *measured_by*
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
- **HoVer** (measurements) — *measured_by*
  - [Grounding by Trying: LLMs with Reinforcement Learning-Enhanced Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/4169f1425b80c3a6e7daa84a1d09b077-Paper-Conference.pdf)
- **SWE-bench Lite** (measurements) — *measured_by*
  - [AlignDistil: Token-Level Language Model Alignment as Adaptive Policy Distillation](https://aclanthology.org/2025.acl-long.973.pdf)
- **DiscoveryBench** (measurements) — *measured_by*
  - [Automated Hypothesis Validation with Agentic Sequential Falsifications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25n/huang25n.pdf)
- **PairRM** (measurements) — *measured_by*
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
- **Conformal Prediction** (measurements) — *measured_by*
  - [Can Transformers Do Enumerative Geometry?](https://proceedings.iclr.cc/paper_files/paper/2025/file/aee2f03ecb2b2c1ea55a43946b651cfd-Paper-Conference.pdf)
- **VAL** (measurements) — *measured_by*
  - [On the self-verification limitations of large language models on reasoning and planning tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3c5e56274140e0420baa3916c529210-Paper-Conference.pdf)
- **CSCD-NS** (measurements) — *measured_by*
  - [The Good, the Bad and the Constructive: Automatically Measuring Peer Review’s Utility for Authors](https://aclanthology.org/2025.emnlp-main.1477.pdf)
- **LEMON** (measurements) — *measured_by*
  - [The Good, the Bad and the Constructive: Automatically Measuring Peer Review’s Utility for Authors](https://aclanthology.org/2025.emnlp-main.1477.pdf)
- **CLIMATEVIZ** (measurements) — *measured_by*
  - [2025.emnlp-main.1196.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1196.checklist.pdf)
- **FM2** (measurements) — *measured_by*
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.365.pdf)

### → Evaluation
- **Explanation generation** (behaviors tasks) — *causes*
  - [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
- **Overconfidence** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-reflection** (behaviors tasks)
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **Robustness** (constructs)
  - [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.189.pdf)
- **Inductive reasoning** (constructs)
  - [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf)
- **Hypothesis generation** (behaviors tasks)
  - [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Cooperative or Competitive? Understanding the Interaction between Attention Heads From A Game Theory Perspective](https://aclanthology.org/2025.acl-long.689.pdf)
- **Grounded reasoning** (constructs)
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  - [Empowering LLM Agents with Zero-Shot Optimal Decision-Making through Q-learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c25de6a9da675464ebb925e430c58325-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements)
  - [RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf)
- **Theory of mind** (constructs)
  - [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/12f483f624b378f9f3058d8ecd3c7ff5-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs)
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Self-evaluation** (behaviors tasks)
  - [Do LLMs estimate uncertainty well in instruction-following?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf)
- **Knowledge manipulation** (constructs)
  - [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf)
- **Task generalization** (constructs)
  - [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf)
- **Table question answering** (behaviors tasks)
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **Game of 24** (measurements)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [UI-Hawk: Unleashing the Screen Stream Understanding for MobileGUIAgents](https://aclanthology.org/2025.emnlp-main.921.pdf)
- **Binary decision making** (behaviors tasks)
  - [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.503.pdf)
- **Grammatical error correction** (behaviors tasks)
  - [Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning](https://aclanthology.org/2025.naacl-long.251.pdf)
- **Unit test generation** (behaviors tasks)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Information extraction** (behaviors tasks)
  - [LimRank: Less is More for Reasoning-Intensive Information Reranking](https://aclanthology.org/2025.emnlp-main.1042.pdf)
