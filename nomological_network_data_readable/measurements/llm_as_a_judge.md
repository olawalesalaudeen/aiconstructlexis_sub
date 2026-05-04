# LLM-as-a-judge
**Type:** Measurement  
**Referenced in:** 440 papers  
**Also known as:** LLM-as-judge, LLM-as-a-Judge, Autonomous evaluator, GPT-Judge, LLM judgment, GPT-4 preference evaluation, GPT-4o Based Evaluation, GPT-4o-based evaluation, GPT-4V-aided evaluation, GPT-Evaluation, LLM-based evaluator, Llama-3 70B judge, Llama-3-70B judge, LLM Judge, LLM judge, GPT-based metric, GPT-4 Rating, Automatic evaluation with GPT-4, Success detector, GPT-Eval, ChatGPT Evaluation, External LLM evaluation, GPT-assisted choice evaluation, Automatic evaluation of explanations, LLM grader, Model of Interestingness, Mixture of judges, Oracle-LLM-as-a-judge, LLM-based evaluation pipeline, GPT-4 judge evaluation, GPT-4 Judge Evaluation, LLM-as-judge evaluation, GPT-4 judge, GPT-4 Judge, LLM-as-Judge, GPT-4 comparison, ChatGPT-based evaluator, LLM evaluator, Ref-GPT4, Arena-Hard Judge, MD-Judge, Vanilla judge, JudgeLM, Automated interpretability with LLMs, RocketEval, GPT-4 scoring, AutoJ Eval, LLM-Eval, Judge model evaluation, Judge function, GPT-4o-mini judge, GPT4o-mini judge, Model-based parsers, Claude 3 Opus Harmful-Yet-Helpful Score, GPT-4o scoring, Automated evaluation, GPT4Score, Claude 3-as-a-Judge, GPT-4 utility judge, GPT-4o Judge, Omni-Judge, LLM-as-Judge (LAJ), GPT Score, GPT-4 eval, GPT-4 assisted evaluation, GPT-4 evaluation, GPT-4 pairwise evaluation, LLM-based auto-evaluation, GPTScore, PandaLM, GPT-4o Score, GPT-4-Preview-1106, LMExaminer, GPT-4o evaluation protocol, Model-based verifier, Procedural LLM-based grading, GPT-4 judgment, Proxy modeling, GPT-4 based evaluation, GPT-4-based evaluation, GPT-4, GPT-4o evaluation, GPT-4o assisted evaluation, LLM-as-judge relevance assessment, MLLM-as-a-Judge, LLMs as Judges, Model-as-Judge, Large-scale pairwise comparison, GPT Judge, GPT-4o judge, Automated interpretability evaluation, Comparative evaluation, Gemini 1.0 Ultra evaluation, Agents-as-an-Evaluator, GPT-4o-based judge, Knowledge Capability, GPT score, Preference-Similarity, GPT-4 based autograder, GPT-4V evaluation, GPT-4-based evaluator, Automated interpretability, Ensemble-as-Judges, GPT-4o automated judge, Oracle Verifier, GPT-3.5, Claude, DeepSeek, LLM judge evaluation, LLM Evaluator, Gemini, LLM-based grading, GPT4-as-a-judge, o3-mini, Claude-3.5-Sonnet Evaluation, Claude Sonnet API evaluation, GPT-based evaluation, Model-as-judge evaluation, HarmBench evaluator, Automated simulation evaluation with language models, GPT-4 complexity estimation, LLM-based Judge, LLM-Judge, Automated interpretability classification, HarmBench judge, Agent-as-a-Judge, Generative-Judge, LLM-as-Prompt-Judge, Oracle judge model, GPT-4 as a judge, GPT-4 evaluating benchmark, GPT-4 preference analysis, GPT-ranking, LLM-as-a-judge evaluation, R-Judge, Google Gemini evaluation pipeline, DeepSeek R1 evaluation, ERNIE Bot 4.0 evaluation, VLM-as-a-Judge, LLM-assisted evaluation, Bias Judge, Granite Judge, NLI Judge, LLM Judge Scores, LM judge evaluation, LLM self-judge, Best of N with LLM Judge, GPT-4o Judgements, GPT-4o-mini Evaluator, LLM-as-judge evaluator, MLLM-as-a-judge, GPT-4o model-based assessment, GPT-4o-based evaluation framework, GPT-eval, LLM-as-Evaluator, LLM-as-a-Meta-Judge, LLM-based Simulated Evaluation, LLM-based alignment evaluation, ESC-Judge, RAG-AS-A-JUDGE, GPT-4o judge evaluation, GPT-4.1 mini re-evaluation, CUA-as-a-Judge, LLM Judger, OpenAI-o3 evaluation, LLM-based story evaluator, Dic-Judge, GPT-as-a-Judge, LLM-based judge, LLM-based Behavior Classification, LLM-based safety moderator, Automated LLM-based evaluation framework, LM-as-a-judge, LLM-based Classical Poetry Metric, GPT-4-as-a-judge, LLM evaluation, GPT-4 multidimensional score, GPT-4 rating, GPT-4V based evaluation, GPT-4 Evaluation, GPT-4 win rate, Judge ability, LLM-as-a-judge ability  

## State of the Field

The LLM-as-a-judge paradigm is a prevalent evaluation protocol where a large language model is used to assess the outputs of another model, frequently serving as a surrogate for human judgment. While the concept is unified, it is operationalized under many specific names (e.g., `GPT-Judge`, `G-Eval`, `Autonomous evaluator`) and employs various powerful models as the judge, with GPT-4 and its variants being the most frequently mentioned. The evaluation format varies across papers, with common approaches including assigning numerical scores on a predefined scale, conducting pairwise comparisons to determine a "win rate," or making binary classifications on correctness or safety. Papers in this set use this method to measure a wide array of constructs, most frequently `Helpfulness`, `Harmlessness`, and `Faithfulness`, as well as to detect undesirable behaviors like `Hallucination` and `Jailbreaking`. It is also commonly applied to evaluate performance on specific tasks such as `Instruction following`, `Question answering`, and `Code generation`. Several studies report a correlation between the outcomes of this protocol and `Human evaluation`, justifying its use as a scalable alternative. However, this view is not universal, as a smaller line of work raises concerns about its reliability, noting that its results "may not align with human judgments" ("LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs").

## Sources

**[OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/85f1225db986e629289f402c46eff1a4-Paper-Conference.pdf) (as "LLM-as-judge")**
> An evaluation protocol where a large language model is used to assess the quality and accuracy of another model's outputs, particularly for open-ended tasks like question answering.

**[IaC-Eval: A Code Generation Benchmark for Cloud Infrastructure-as-Code Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26b29298ae8acd94bd7e839688e329b-Paper-Datasets_and_Benchmarks_Track.pdf)**
> An evaluation protocol in which a language model is used as the judge to assess whether generated solutions are correct.

**[HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf) (as "LLM-as-a-Judge")**
> An evaluation methodology where a large language model is used to judge and score the quality of another model's responses based on a predefined set of criteria.

**[DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf) (as "Autonomous evaluator")**
> A Gemini 1.5 Pro-based evaluation procedure that judges whether a screenshot indicates task completion and assigns success or failure to trajectories.

**[ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5ef9853a6cdea40ae3e301a6d8dc32b5-Paper-Datasets_and_Benchmarks_Track.pdf) (as "GPT-Judge")**
> A GPT-4-based judgment protocol used to compare whether two rationales refer to the same entity with the same properties.

**[Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf) (as "LLM judgment")**
> An evaluation procedure in which an LLM scores a candidate answer against a reference answer on accuracy, coherence, and factuality.

**[VoxDialogue: Can Spoken Dialogue Systems Understand Information Beyond Words?](https://proceedings.iclr.cc/paper_files/paper/2025/file/011df158529ddceb5f2f7a65f2732a5a-Paper-Conference.pdf) (as "GPT-based metric")**
> A qualitative evaluation protocol that uses a large language model (GPT) to assess the quality of generated dialogue responses based on a 5-point scale of contextual relevance and attribute accuracy.

**[SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf) (as "GPT-4 preference evaluation")**
> A pairwise preference evaluation protocol using GPT-4 as a proxy for human judgment to assess the relative faithfulness of two generated texts against a common input.

**[DRESSing Up LLM: Efficient Stylized Question-Answering via Style Subspace Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/09425891e393e64b0535194a81ba15b7-Paper-Conference.pdf) (as "GPT-4 Rating")**
> An evaluation protocol using GPT-4 to rate stylized responses comprehensively on a scale of 0 to 10, serving as a surrogate for human evaluation.

**[InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "G-Eval")**
> An evaluation technique that uses a large language model (specifically GPT-4) to assess the quality of generated text in a way that aligns with human judgment.

**[Agents' Room:  Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf) (as "LLM-based evaluator")**
> An automated evaluation procedure that uses a large language model to perform side-by-side comparisons of system-generated stories based on prompts targeting specific quality dimensions.

**[Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf) (as "GPT-4V-aided evaluation")**
> An evaluation protocol where a powerful vision-language model (GPT-4V) is used to assess the quality, accuracy, and detailedness of responses generated by other models.

**[MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf) (as "LLM-based evaluation")**
> A quality assessment protocol where a large language model, such as GPT-4V, is used to score the factual and diagnostic accuracy of generated medical descriptions.

**[Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf) (as "GPT-Evaluation")**
> An evaluation protocol where GPT-4 is used to score model performance by comparing its generated answers to ground truth answers.

**[Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf) (as "GPT-4o Based Evaluation")**
> A human-like evaluation procedure where the GPT-4o model is used to compare and rate the quality of responses from two different models on safety-related prompts.

**[Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf) (as "Llama-3-70B judge")**
> An evaluation protocol that uses the Llama-3-70B model as a judge to assess the success of jailbreak attacks.

**[Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf) (as "LLM Judge")**
> An evaluation protocol that uses a powerful LLM, such as GPT-4o, to assess and score the quality of another model's generated content.

**[Improving Instruction-Following in Language Models through Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3262a4c965ba9888f120d4f9e13478-Paper-Conference.pdf) (as "GPT-4o-based evaluation")**
> A GPT-4o-based human-like judging procedure in which GPT-4o generates yes/no questions about response quality and then answers them with rationales to score base-query responses.

**[On Speeding Up Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a38cfba4c717e5a37b200294615e546e-Paper-Conference.pdf) (as "LLM judge")**
> A specific application of LLM-based scoring where a powerful LLM acts as an automated judge to evaluate model outputs.

**[Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf) (as "Llama-3 70B judge")**
> A Llama-3 70B-based semantic judge used to evaluate whether responses satisfy the jailbreak criterion.

**[Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1a7774429d5c06cc744ff4260a8e9f-Paper-Conference.pdf) (as "LLM-based evaluation pipeline")**
> An automated evaluation procedure that uses GPT-4o or LLaMA3.1-8b-Instruct to judge classification outputs and post-process regression outputs into task-compatible formats.

**[Mechanistic Permutability: Match Features Across Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/d1422213c9f2bdd5178b77d166fba86a-Paper-Conference.pdf) (as "External LLM evaluation")**
> A large-language-model-based semantic judgment procedure that labels matched feature descriptions as SAME, MAYBE, or DIFFERENT.

**[A-Bench: Are LMMs Masters at Evaluating AI-generated Images?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d355518527578ce26b80da96e9fc2750-Paper-Conference.pdf) (as "GPT-assisted choice evaluation")**
> A technique used to automatically validate the correctness of LMM responses to multiple-choice questions by using a GPT model to handle variations in answer formatting.

**[OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/d40d7cbe7210f8a13ea0149eeae9c6de-Paper-Conference.pdf) (as "Success detector")**
> An LLM- or VLM-based procedure that checks whether an agent has successfully completed a generated task.

**[OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/d40d7cbe7210f8a13ea0149eeae9c6de-Paper-Conference.pdf) (as "Model of Interestingness")**
> An LLM-based evaluation procedure that judges whether a newly generated task is interesting relative to similar archived tasks.

**[NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf) (as "Automatic evaluation of explanations")**
> A reference-based evaluation procedure where a large language model acts as a judge to determine if a model-generated explanation aligns with a set of human-written gold reference explanations.

**[Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf) (as "LLM grader")**
> An LLM-based judging procedure that prompts a language model to determine equivalence between predicted and ground-truth formal statements.

**[Backdooring Vision-Language Models with Out-Of-Distribution Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/da37068018f8f7185720b83ea6f48377-Paper-Conference.pdf) (as "ChatGPT Evaluation")**
> An evaluation protocol that uses ChatGPT to provide judgments on the conceptual consistency of model outputs, serving as an automated proxy for human assessment.

**[Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/dafb7f4ced9ac559e077fc611d6e96e5-Paper-Conference.pdf) (as "GPT-Eval")**
> An evaluation protocol that uses a large language model (GPT-4o mini) as a judge to score model outputs based on semantic criteria such as correctness, helpfulness, and relevance.

**[Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf) (as "Automatic evaluation with GPT-4")**
> An evaluation procedure that uses GPT-4 to rate or compare the outputs of other language models based on criteria like helpfulness and relevance.

**[Is Your Video Language Model a Reliable Judge?](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc4f891373d19087d1ddda33e81e00e4-Paper-Conference.pdf) (as "Mixture of judges")**
> A reliability-gated evaluation procedure that selects a subset of VLM judges based on per-dimension reliability scores before producing a final assessment.

**[Measuring And Improving Persuasiveness Of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf) (as "Oracle-LLM-as-a-judge")**
> An automated evaluation protocol that uses a specially trained LLM (the "Oracle") to rate or compare the persuasive quality of generated content, serving as a proxy for human judgment.

**[FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf) (as "GPT-4 judge")**
> An LLM-as-judge evaluation procedure in which GPT-4 scores model generations using the full dialogue history and the original biased statement.

**[The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf) (as "GPT-4 judge evaluation")**
> An evaluation protocol where GPT-4 is used as a proxy for a human judge to compare and analyze stories generated by different models based on factors like grammar, flow, cohesiveness, and creativity.

**[Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/18fd48d9cbbf9a20e434c9d3db6973c5-Paper-Conference.pdf) (as "LLM-as-Judge")**
> A judge-model evaluation procedure that scores whether generated answers are relevant or appropriate for a query in the unlearning setting.

**[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf) (as "GPT-4 Judge")**
> An evaluation protocol that uses the GPT-4 model to automatically assess and score the harmfulness of an embodied agent's linguistic and action outputs on a scale from 1 to 5.

**[Unbounded: A Generative Infinite Game of Character Life Simulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/da2411768acb844b255bb6770e5a71c7-Paper-Conference.pdf) (as "GPT-4 Judge Evaluation")**
> An evaluation protocol where the GPT-4 model is used as an automated judge to score and compare the responses of two other models on criteria such as state update accuracy, environment relevance, story coherence, and instruction following.

**[FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf) (as "LLM-as-judge evaluation")**
> A procedure where a large language model is used as a judge to evaluate the alignment between informal and formal mathematical statements.

**[Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf) (as "LLM evaluator")**
> An evaluation protocol where a separate large language model is used to assess the quality or correctness of another model's outputs, often guided by a specific prompt and context.

**[TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf) (as "GPT-4 comparison")**
> A human-like pairwise comparison procedure in which GPT-4 compares outputs and determines win-rate.

**[IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf) (as "GPT-4 scoring")**
> A human-readable scoring procedure in which GPT-4 rates open-ended question-answering and caption outputs against reference answers.

**[Sparse Autoencoders Do Not Find Canonical Units of Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/84ca3f2d9d9bfca13f69b48ea63eb4a5-Paper-Conference.pdf) (as "Automated interpretability with LLMs")**
> A procedure that uses GPT-4o-mini to generate natural-language explanations of SAE latents from activating examples and then explain meta-latent groupings.

**[Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf) (as "MD-Judge")**
> An evaluation procedure that uses a large language model-based classifier to assess the safety of instruction-response pairs.

**[From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf) (as "ChatGPT-based evaluator")**
> An automated evaluation procedure that uses a large language model (ChatGPT) to conduct pairwise comparisons of model outputs to determine a winner.

**[Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf) (as "Ref-GPT4")**
> A benchmark in which GPT-4 rates generated responses for open-ended evaluation.

**[RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf) (as "RocketEval")**
> An automated evaluation framework that uses a lightweight LLM to grade responses against an instance-specific, multi-faceted checklist.

**[xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf) (as "JudgeLM")**
> A judge model used for automated evaluation of LLM responses by scoring or selecting outputs.

**[JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf) (as "Arena-Hard Judge")**
> A prompting method for LLM-based judges where the model is instructed to first generate its own reference answer before analyzing and judging the provided response pair.

**[JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf) (as "Vanilla judge")**
> A simple prompting method for LLM-based judges, adapted from AlpacaFarm, that directly asks the LLM to indicate its preferred response without requiring an explanation.

**[EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING](https://proceedings.iclr.cc/paper_files/paper/2025/file/52724c4ea3634f610b0ef0245ce5bd20-Paper-Conference.pdf) (as "Judge function")**
> An automated evaluation procedure using a separate LLM (Llama-3.1-8B-Instruct) to assess a target model's response and assign a binary reward indicating whether the content is harmful (1) or benign (0).

**[Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf) (as "GPT-4o scoring")**
> A GPT-4o-based evaluation procedure that scores sampled preference data on a 1-to-10 scale for quality assessment.

**[Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf) (as "GPT-4o-mini judge")**
> A judge-model evaluation procedure in which GPT-4o-mini is used to score or compare dialogue outputs.

**[Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf) (as "LLM-Eval")**
> An LLM-based evaluation procedure used to judge answer quality for generated responses in the RAG setting.

**[Functional Homotopy: Smoothing Discrete Optimization via Continuous Parameters for LLM Jailbreak Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5ed212957dbe503283c577a94202cb8c-Paper-Conference.pdf) (as "Judge model evaluation")**
> An evaluation procedure where a separate large language model (Llama-2 13B) is used to automatically assess whether a model's response to a prompt constitutes a successful jailbreak.

**[SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf) (as "AutoJ Eval")**
> An in-domain pairwise-comparison test set from AUTO-J containing 58 prompts and 1,392 response pairs labeled as win, tie, or lose.

**[PaCA: Partial Connection Adaptation for Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b4fd4a4607f57fe65b5e276bdb17ed1-Paper-Conference.pdf) (as "GPT4o-mini judge")**
> An evaluation protocol using the GPT4o-mini model to score or judge model outputs on benchmark tasks.

**[MixEval-X: Any-to-any Evaluations from Real-world Data Mixture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6de2e84b8da47bb2eb5e2ac96c63d2b0-Paper-Conference.pdf) (as "Model-based parsers")**
> A grading procedure that uses language models to score responses against problem statements and reference answers.

**[Failures to Find Transferable Image Jailbreaks Between Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e3daaeca6be8579573f69082b2dd58b-Paper-Conference.pdf) (as "Claude 3 Opus Harmful-Yet-Helpful Score")**
> An evaluation procedure where the Claude 3 Opus model is prompted to assess and score the degree to which a VLM's generated output is both harmful and helpful.

**[SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf) (as "GPT4Score")**
> An evaluation procedure where the GPT-4 model is prompted to assign an integer quality rating, from 0 (poor) to 100 (excellent), to a generated response.

**[DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf) (as "GPT Score")**
> An evaluation procedure that uses GPT-4 to quantify the semantic coherence between a generated description and a ground truth description by assigning a similarity score from 0 to 1.

**[Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/efc549c2d22edf2f244b7013387c6251-Paper-Conference.pdf) (as "Automated evaluation")**
> An evaluation protocol that uses foundation models as 'labellers' to produce ratings for the accuracy, thoroughness, and objectivity of responses generated by other target models.

**[ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://proceedings.iclr.cc/paper_files/paper/2025/file/f12b4df26344f3be803c06b555252efe-Paper-Conference.pdf) (as "GPT-4o Judge")**
> A judge-based evaluation procedure using GPT-4o to compare a program-produced figure with the ground truth and rate figure quality.

**[Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf) (as "GPT-4 utility judge")**
> An automated evaluation protocol that uses the GPT-4 model to score the utility of anonymized text based on its readability and similarity in meaning to the original.

**[DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf) (as "LLM-as-Judge (LAJ)")**
> An evaluation protocol where a large language model is used to score the outputs of another model on a numeric scale based on criteria like correctness, clarity, and instruction adherence.

**[Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf) (as "Omni-Judge")**
> An open-source evaluation model developed to assess the consistency between model-generated solutions and reference answers for the Omni-MATH benchmark at a low cost.

**[SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf) (as "Claude 3-as-a-Judge")**
> A judge-based evaluation procedure in which Claude 3 compares model outputs or assigns ratings to assess response quality.

**[Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf) (as "GPT-4 evaluation")**
> An evaluation protocol that uses the GPT-4 model as a proxy for human judgment to assess and compare the quality of responses generated by other models.

**[Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf) (as "GPT-4 eval")**
> An automatic evaluation protocol where GPT-4 is prompted to select which of two generated texts more closely matches the style of a reference text, with results averaged over swapped orders to mitigate bias.

**[PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf) (as "PandaLM")**
> A fine-tuned language model (based on Llama-7b) designed specifically to act as a judge for preference-based evaluation of other LLMs.

**[PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf) (as "GPTScore")**
> An evaluation method that uses a generative pre-trained model (like GPT-3 or Flan-T5) to assess the quality of generated text by calculating the likelihood of the text given instructions and context.

**[ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf) (as "GPT-4o Score")**
> An evaluation procedure that uses the GPT-4o model to assess the high-level visual similarity between a generated chart and a ground-truth chart, producing a score from 0 to 100.

**[MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf) (as "GPT-4 pairwise evaluation")**
> A human-like pairwise judgment procedure in which GPT-4 compares two responses and selects a winner based on task-specific criteria.

**[Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf) (as "GPT-4 assisted evaluation")**
> A human-in-the-loop style evaluation procedure in which GPT-4 judges hallucinations in generated image descriptions sentence by sentence against detailed ground truth.

**[FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf) (as "LLM-based auto-evaluation")**
> A validation procedure where an LLM judge is used to automatically verify the quality of a generated context by checking if a specific answer is both valid and uniquely supported by that context.

**[Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf) (as "GPT-4-Preview-1106")**
> A specific version of the GPT-4 model used as an automated evaluator and baseline on the AlpacaEval-2 and Arena-Hard benchmarks.

**[Benchmarking LLMs' Judgments with No Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9b0e4e205bdf232da9f74bfb9469539-Paper-Conference.pdf) (as "LMExaminer")**
> An evaluation protocol where a large language model (e.g., GPT-4o) is used as an oracle to directly score the quality of another model's generated text.

**[Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf) (as "GPT-4o evaluation protocol")**
> An evaluation procedure where GPT-4o acts as a discriminator to compare pairs of model responses based on user preferences, categorizing outcomes as win, lose, or tie.

**[SysBench: Can LLMs Follow System Message?](https://proceedings.iclr.cc/paper_files/paper/2025/file/b917f916e7eed84ffe8f5e63492b2be8-Paper-Conference.pdf) (as "Model-based verifier")**
> An evaluation protocol that uses an advanced LLM (like GPT-4o) as a judge to automatically assess whether a model's response satisfies the constraints defined in a system message, guided by a manually created checklist.

**[PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf) (as "GPT-4 judgment")**
> An evaluation procedure leveraging GPT-4 to conduct judgments towards certain personalized preferences and report comparative win rates.

**[HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf) (as "Procedural LLM-based grading")**
> An evaluation protocol that uses an LLM (e.g., GPT-4o) as a grader to assess the correctness of intermediate steps in a model's solution procedure, based on a provided answer key and rubric.

**[AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf) (as "Proxy modeling")**
> An approximation method for LOO attribution where a smaller, computationally cheaper 'proxy' model is used to calculate attribution scores for a response generated by a larger 'target' model.

**[Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf) (as "GPT-4 based evaluation")**
> An evaluation protocol where the GPT-4 model is used as a surrogate for human judgment to rate and compare model-generated responses based on criteria like relevance, accuracy, and helpfulness.

**[MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf) (as "GPT-4-based evaluation")**
> An evaluation protocol where a large language model (GPT-4) is used as a judge to determine if a model's generated answer is correct.

**[Adversarial Search Engine Optimization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f12b3c36a781120c4f60e90e855868d-Paper-Conference.pdf) (as "GPT-4")**
> A plugin-augmented LLM used to test whether manipulated plugin descriptions affect plugin choice.

**[A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf) (as "GPT-4o evaluation")**
> An automated evaluation procedure using GPT-4o to assess model safety and quality on test samples.

**[MLLM can see? Dynamic Correction Decoding for Hallucination Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/24079b91da7257cb78805262996152b8-Paper-Conference.pdf) (as "GPT-4o assisted evaluation")**
> An open-ended evaluation protocol where the GPT-4o model is used to assess and score model-generated image descriptions based on criteria such as accuracy, detailedness, and coherence.

**[From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf) (as "LLM-as-judge relevance assessment")**
> An automatic evaluation protocol that uses an LLM as a judge to score the relevance of a fact to a question on a 0-5 scale, based on an existing rubric.

**[Interleaved Scene Graphs for Interleaved Text-and-Image Generation Assessment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e0ceee9751ae8b5c6603c029e4ca42-Paper-Conference.pdf) (as "MLLM-as-a-Judge")**
> A human-aligned evaluation protocol in which a multimodal large language model judges the overall quality of generated responses, sometimes using golden answers and chain-of-thought prompting.

**[Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models](https://aclanthology.org/2025.acl-long.586.pdf) (as "LLMs as Judges")**
> An automated evaluation protocol where large language models assess dialogue quality across multiple dimensions using standardized prompts, serving as objective and scalable judges.

**[HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.680.pdf) (as "Model-as-Judge")**
> Automated evaluation method using a large model to assess the logical consistency and quality of question-answer pairs against visual inputs, used for filtering hallucinated content.

**[From Sub-Ability Diagnosis to Human-Aligned Generation: Bridging the Gap for Text Length Control viaMarkerGen](https://aclanthology.org/2025.acl-long.851.pdf) (as "GPT Judge")**
> An evaluation protocol (Qi et al., 2023) that uses GPT-4 to assess the harmfulness of model responses by assigning a rating on a 1-to-5 scale.

**[Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents](https://aclanthology.org/2025.acl-long.858.pdf) (as "Large-scale pairwise comparison")**
> An automated evaluation method where a powerful LLM (GPT-4) acts as a judge to compare an LLM-generated explanation against a human-written gold standard and select the better one.

**[ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Drafting](https://aclanthology.org/2025.acl-long.1207.pdf) (as "GPT-4o judge")**
> A robust evaluation method using GPT-4o to assess whether model outputs are harmful, leveraging its strong reasoning and content moderation capabilities as a proxy for human judgment.

**[Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf) (as "Gemini 1.0 Ultra evaluation")**
> An evaluation protocol where a prompted Gemini 1.0 Ultra model is used to compare the quality and conciseness of generated summaries against a baseline policy.

**[Aligning LLMs by Predicting Preferences from User Writing Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aroca-ouellette25a/aroca-ouellette25a.pdf) (as "Preference-Similarity")**
> An LLM-as-a-Judge protocol that measures preference quality by prompting an LLM to rate the similarity between an inferred preference description and a true preference description on a 5-point Likert scale.

**[Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf) (as "Comparative evaluation")**
> LLM-based evaluation method where candidate formulations are scored relative to baseline models to produce a consistent reward signal for correctness.

**[Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/betley25a/betley25a.pdf) (as "GPT-4o-based judge")**
> A GPT-4o-based automated evaluation procedure that scores responses for alignment with human values and coherence, and classifies responses as misaligned under specified thresholds.

**[Learning Multi-Level Features with Matryoshka Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bussmann25a/bussmann25a.pdf) (as "Automated interpretability evaluation")**
> Procedure using an LLM judge (e.g., gpt4o-mini) to score feature explanations by predicting when a latent will activate based on input examples.

**[SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25n/chen25n.pdf) (as "Knowledge Capability")**
> Evaluation component in CoIN that uses a large language model (Qwen1.5-32B) to assess the factual correctness of model answers, particularly useful when answers are in non-standard formats.

**[Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf) (as "Agents-as-an-Evaluator")**
> An LLM-based evaluation paradigm where language models generate and rephrase evaluation questions and criteria, potentially introducing data and model bias.

**[De-mark: Watermark Removal in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bq/chen25bq.pdf) (as "GPT score")**
> An evaluation procedure that uses a separate, powerful language model (such as gpt-3.5-turbo-0125) to assess the quality of text generated by another model.

**[SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karvonen25a/karvonen25a.pdf) (as "Automated interpretability")**
> An LLM-based evaluation method that assesses the interpretability of SAE latents by training an LLM judge to predict activation patterns based on proposed feature descriptions.

**[A Simple Model of Inference Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/levi25a/levi25a.pdf) (as "Oracle Verifier")**
> A perfect verification method that determines whether a generated answer is correct, assumed to be available for tasks like mathematical reasoning and coding where correctness can be automatically checked.

**[From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf) (as "Ensemble-as-Judges")**
> Evaluation method that aggregates judgments from multiple LLM judges (e.g., GPT-4-Turbo and Gemini-1.5-Pro) to reduce individual model biases and improve alignment with human preferences.

**[Eliciting Language Model Behaviors with Investigator Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25i/li25i.pdf) (as "GPT-4 based autograder")**
> A specific LLM-as-judge implementation that uses GPT-4 to automatically evaluate the success of attacks in generating harmful behaviors.

**[Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf) (as "GPT-4-based evaluator")**
> An evaluation protocol that uses GPT-4 to perform pairwise comparisons and determine a win-rate between the outputs of different models on a given set of prompts.

**[One Example Shown, Many Concepts Known! Counterexample-Driven Conceptual Reasoning in Mathematical LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ax/li25ax.pdf) (as "GPT-4o automated judge")**
> An evaluation framework using GPT-4o to automatically assess whether model-generated examples align with reference examples in logical structure, problem decomposition, and goal relevance.

**[What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf) (as "GPT-4V evaluation")**
> Human-like evaluation using GPT-4V to rate caption quality and alignment with images on a 1–5 scale based on fluency and correctness.

**[Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf) (as "LLM Evaluator")**
> A validation method that uses a separate language model to score the relevance of schema matches on a numerical scale, guiding a zero-shot optimization process.

**[Reliable and Efficient Amortized Model-based Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25c/truong25c.pdf) (as "GPT4-as-a-judge")**
> An evaluation procedure where a high-performance language model (GPT-4) is used to dichotomously grade the responses of other models.

**[Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf) (as "LLM-based grading")**
> An evaluation protocol where a large language model (GPT-4o in this paper) is used to rate the quality of generated samples on several qualitative dimensions like clarity and factuality.

**[Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25g/wei25g.pdf) (as "GPT-3.5")**
> A large language model from OpenAI used in this study as a Judge LLM to evaluate content harmfulness on a numerical scale.

**[Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25g/wei25g.pdf) (as "Gemini")**
> A large language model from Google used in this study as a Judge LLM to evaluate content harmfulness.

**[Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25g/wei25g.pdf) (as "Claude")**
> A large language model from Anthropic used in this study as a Judge LLM to evaluate content harmfulness.

**[Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25g/wei25g.pdf) (as "DeepSeek")**
> A reasoning-focused large language model used in this study as a Judge LLM to evaluate its robustness to adversarial inputs.

**[Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25g/wei25g.pdf) (as "o3-mini")**
> A reasoning-focused large language model used in this study as a Judge LLM to evaluate its sensitivity to adversarial attacks.

**[CollabLLM: From Passive Responders to Active Collaborators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25i/wu25i.pdf) (as "LLM judge evaluation")**
> Automated assessment using LLMs (e.g., Claude-3.5-Sonnet) to score interactivity and task success on a 0–1 scale based on conversation quality.

**[FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf) (as "GPT-based evaluation")**
> Evaluation method using a strong LLM (e.g., GPT-4) to score model responses on rejection status, completion of harmful request, and illegal/unsafe output.

**[Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf) (as "Claude Sonnet API evaluation")**
> An API-based pairwise evaluation procedure using Claude Sonnet to judge which of two model responses is better, with position swapping to reduce bias.

**[The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25c/miao25c.pdf) (as "Claude-3.5-Sonnet Evaluation")**
> An evaluation protocol where the Claude-3.5-Sonnet model is used as an automated judge to assess the quality of model responses.

**[Evaluating Neuron Explanations: A Unified Framework with Sanity Checks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oikarinen25a/oikarinen25a.pdf) (as "Automated simulation evaluation with language models")**
> An evaluation procedure that measures the correlation between a neuron's actual activations and the activations predicted by a language model that is given the neuron's textual explanation.

**[AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/paulus25a/paulus25a.pdf) (as "HarmBench evaluator")**
> LLM-based evaluation system used to determine if a model's response to a harmful instruction is unsafe, serving as a judge for attack success on the HarmBench dataset.

**[Understanding the Logic of Direct Preference Alignment through Logic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/richardson25a/richardson25a.pdf) (as "Model-as-judge evaluation")**
> Human evaluation protocol adapted from Hong et al. (2024) where a large language model acts as a judge to compare outputs from models trained with different losses.

**[Optimizing Adaptive Attacks against Watermarks for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diaa25a/diaa25a.pdf) (as "LLM-Judge")**
> An automated evaluation metric that uses a large language model to assess the quality of paraphrased text relative to the original, providing a score based on semantic fidelity and fluency.

**[Understanding Complexity in VideoQA via Visual Program Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eyzaguirre25a/eyzaguirre25a.pdf) (as "GPT-4 complexity estimation")**
> Prompt-based evaluation using GPT-4 to estimate question complexity on a Likert scale, serving as a text-based baseline for comparison.

**[Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf) (as "LLM-based Judge")**
> Evaluation protocol using a large language model (Mistral-Large-123B) to score generated responses across multiple quality criteria, aggregating them into a final performance metric.

**[Compute Optimal Inference and Provable Amortisation Gap in Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/o-neill25a/o-neill25a.pdf) (as "Automated interpretability classification")**
> A GPT-4o-based protocol that generates feature explanations from activating examples and then validates them on new examples to judge whether the explanation predicts feature activations.

**[Adversarial Reasoning at Jailbreaking Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sabbaghi25a/sabbaghi25a.pdf) (as "HarmBench judge")**
> A judge model/protocol from HarmBench that determines whether a target response matches the malicious intent and counts as a successful jailbreak.

**[Agent-as-a-Judge: Evaluate Agents with Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuge25a/zhuge25a.pdf) (as "Agent-as-a-Judge")**
> Framework that uses agentic systems to evaluate other agentic systems by analyzing step-by-step task-solving processes, incorporating modules for reading, locating, retrieving, and judging based on hierarchical requirements.

**[Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25s/yang25s.pdf) (as "Generative-Judge")**
> Automated evaluation method using a strong LLM (e.g., GPT-4-turbo) to judge whether model outputs contain harmful content and thus count as successful jailbreaks.

**[R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf) (as "LLM-as-Prompt-Judge")**
> An evaluation protocol where a powerful language model is used to assess the quality of input prompts on a binary or pointwise scale.

**[Preference learning made easy: Everything should be understood through win rate](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bm/zhang25bm.pdf) (as "Oracle judge model")**
> A trained model used to estimate the true preference probability p(ℓ= 1 | x, y0, y1) by relabeling preference annotations, serving as a proxy for human judgment in evaluating win rate.

**[Controlled Text Generation via Language Model Arithmetic](https://proceedings.iclr.cc/paper_files/paper/2024/file/96aad3299d18497e2bea4fc20b949b81-Paper-Conference.pdf) (as "GPT-4 preference analysis")**
> A human-like comparative evaluation procedure in which GPT-4 chooses the best response in terms of toxicity and relevance.

**[Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf) (as "GPT-4 as a judge")**
> An evaluation protocol where the GPT-4 model is prompted to rate and compare the quality of answers generated by other models on a numeric scale.

**[Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing](https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf) (as "GPT-ranking")**
> An evaluation method that uses a large language model, such as GPT-4, to provide relative quality rankings between pairs of generated text outputs.

**[LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf) (as "GPT-4 evaluating benchmark")**
> An evaluation protocol that uses the GPT-4 model to assess and compare the quality of responses from different instruction-following models across a set of 80 questions.

**[TWIST: Text-encoder Weight-editing for Inserting Secret Trojans in Text-to-Image Models](https://aclanthology.org/2025.acl-long.542.pdf) (as "LLM-as-a-judge evaluation")**
> Evaluation method using GPT-4o as a judge to score and compare model-generated friction interventions across seven dimensions including thought-provoking, actionability, and relevance.

**[MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities ofLLMTutors](https://aclanthology.org/2025.emnlp-main.12.pdf) (as "R-Judge")**
> Benchmark for coding and software engineering tasks involving high-risk bash commands or API calls, assessing safety and alignment in programming environments.

**[TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.40.pdf) (as "Google Gemini evaluation pipeline")**
> A model-based evaluation pipeline using Google Gemini to assess synthesized speech on dimensions such as instruction following, naturalness, and expressiveness.

**[PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.38.pdf) (as "DeepSeek R1 evaluation")**
> An evaluation protocol where the DeepSeek R1 model is used to quantitatively assess model outputs on qualitative criteria such as logical consistency and clarity.

**[PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.38.pdf) (as "ERNIE Bot 4.0 evaluation")**
> An evaluation protocol where the ERNIE Bot 4.0 model is used to automatically score the correctness of model predictions against ground truth answers.

**[Parallel Continuous Chain-of-Thought with Jacobi Iteration](https://aclanthology.org/2025.emnlp-main.48.pdf) (as "VLM-as-a-Judge")**
> A prompting-based evaluation procedure in which vision-language models are used offline to judge EQA responses.

**[CondenseLM:LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.66.pdf) (as "LLM-assisted evaluation")**
> An evaluation scheme where an LLM (GPT-4o-mini) is prompted to score model-generated answers on a scale from 0 to 5 across multiple criteria, including depth, comprehensiveness, coherence, and evidence.

**[Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.84.pdf) (as "Bias Judge")**
> An LLM-as-a-judge system that assesses whether a model's response agrees with a biased opinion, considering both direct and implicit bias while excluding explicit rejections of bias.

**[Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.84.pdf) (as "Granite Judge")**
> IBM’s Granite Guardian, an open-source LLM designed to detect risks in prompts and responses, including societal bias, harmful content, and unethical behavior, used as a binary classifier for bias detection.

**[Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.84.pdf) (as "NLI Judge")**
> A natural language inference-based evaluation method that classifies the logical relationship between a biased opinion and the model's output as enforces, agrees, neutral, or negates, used to assess bias in model responses.

**[VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing](https://aclanthology.org/2025.emnlp-main.138.pdf) (as "JudgeBench")**
> A benchmark consisting of challenging questions designed to evaluate LLM performance on various reasoning tasks.

**[NUTMEG: Separating Signal From Noise in Annotator Disagreement](https://aclanthology.org/2025.emnlp-main.145.pdf) (as "LLM Judge Scores")**
> Model preference comparison scores derived from human-aligned rubrics, used to evaluate the behavioral alignment of model outputs based on comparative judgments.

**[Are Generative Models Underconfident? Better Quality Estimation with Boosted Model Probability](https://aclanthology.org/2025.emnlp-main.167.pdf) (as "LM judge evaluation")**
> An automatic evaluation protocol where a state-of-the-art language model is prompted to judge which of two model-generated responses is preferred, with the results aggregated into a win rate.

**[TokenSkip: Controllable Chain-of-Thought Compression inLLMs](https://aclanthology.org/2025.emnlp-main.166.pdf) (as "LLM self-judge")**
> A method where a large language model is prompted to assign a quality score to its own output, requiring an additional inference step.

**[Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.237.pdf) (as "Best of N with LLM Judge")**
> A baseline method that samples multiple candidate answers using CoT and uses an LLM as a judge to select the best one based on correctness.

**[TS-CLIP: Time Series Understanding byCLIP](https://aclanthology.org/2025.emnlp-main.232.pdf) (as "GPT-4o Judgements")**
> An evaluation procedure using the GPT-4o model to score the performance of different methods on five aspects: Fluency, Identification, Comforting, Suggestion, and Overall.

**[JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf) (as "GPT-4o-mini Evaluator")**
> An evaluation procedure that uses the GPT-4o-mini model with a specific prompt to assess the disambiguation capability of other LLMs.

**[ViLBench: A Suite for Vision-Language Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.345.pdf) (as "LLM-as-judge evaluator")**
> An automated evaluation method using an LLM (GPT-4.1) to judge whether model outputs leak confidential information or faithfully include non-confidential content, based on predefined policy targets and discussion summaries.

**[Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.344.pdf) (as "MLLM-as-a-judge")**
> An evaluation paradigm where a Vision Large Language Model is used as an automated judge to score or critique the outputs of other models.

**[ComplexTempQA: A 100m Dataset for Complex Temporal Question Answering](https://aclanthology.org/2025.emnlp-main.464.pdf) (as "GPT-4o model-based assessment")**
> An evaluation protocol using GPT-4o to score model responses on a 1–5 scale by comparing them to reference answers, with scores ≥4 considered correct.

**[Disambiguation in Conversational Question Answering in the Era ofLLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.483.pdf) (as "GPT-4o-based evaluation framework")**
> A GPT-4o-based automatic evaluation procedure that scores generated essays along multiple qualitative dimensions using detailed feedback before scoring.

**[DSG-MCTS: A Dynamic Strategy-GuidedMonteCarlo Tree Search for Diversified Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.533.pdf) (as "GPT-eval")**
> An evaluation protocol that uses a large language model (GPT) to assess the quality of generated text on dimensions like coherence and correctness.

**[A Computational Simulation of Language Production in First Language Acquisition](https://aclanthology.org/2025.emnlp-main.558.pdf) (as "LLM-as-Evaluator")**
> A general evaluation methodology where a large language model is prompted to directly score or assess the quality of a generated text based on given criteria.

**[CoMMIT: Coordinated Multimodal Instruction Tuning](https://aclanthology.org/2025.emnlp-main.583.pdf) (as "LLM-as-a-Meta-Judge")**
> A prompting-based evaluation procedure in which an LLM compares two judgments and selects the more accurate one according to a rubric.

**[Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.682.pdf) (as "LLM-based Simulated Evaluation")**
> An automated evaluation framework where an LLM simulates user behavior to systematically assess a model's performance in handling unspecified queries.

**[Benchmark Profiling: Mechanistic Diagnosis ofLLMBenchmarks](https://aclanthology.org/2025.emnlp-main.790.pdf) (as "LLM-based alignment evaluation")**
> An automatic evaluation procedure where an LLM (Gemini-2.5-Pro) performs a many-to-many matching between generated and reference feedback comments to assess alignment.

**[VisEscape: A Benchmark for Evaluating Exploration-driven Decision-making in Virtual Escape Rooms](https://aclanthology.org/2025.emnlp-main.811.pdf) (as "ESC-Judge")**
> An automated, LLM-driven evaluation framework that compares emotional-support LLMs using synthetic help-seeker roles and a judge model guided by Hill’s Exploration–Insight–Action rubric across nine fine-grained dimensions.

**[Reliable and Cost-Effective Exploratory Data Analysis via Graph-GuidedRAG](https://aclanthology.org/2025.emnlp-main.837.pdf) (as "RAG-AS-A-JUDGE")**
> An evaluation procedure where a large language model, conditioned on retrieved documents, performs binary classification on each step of a reasoning trace to determine its correctness.

**[Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.983.pdf) (as "GPT-4o judge evaluation")**
> Pair-wise comparison using GPT-4o as an automated judge to assess model outputs on coherence, relevance, and quality in open-ended tasks.

**[SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf) (as "GPT-4.1 mini re-evaluation")**
> An automated evaluation procedure where responses marked as incorrect by exact match are re-evaluated by the GPT-4.1 mini model to account for formatting variations or semantic equivalence.

**[Toward Machine Interpreting: Lessons from Human Interpreting Studies](https://aclanthology.org/2025.emnlp-main.1192.pdf) (as "CUA-as-a-Judge")**
> Automated gameplay evaluator implemented using Claude-3.7-Sonnet that verifies milestone completion by interacting with the game environment as an oracle.

**[In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1209.pdf) (as "LLM Judger")**
> An automated evaluation method using large language models (e.g., GPT-4o) to score model responses across multiple role-playing metrics, with temperature set to 0.0 and multiple rounds averaged.

**[Beyond Text: Unveiling Privacy Vulnerabilities in Multi-modal Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1260.pdf) (as "OpenAI-o3 evaluation")**
> An evaluation procedure where a strong reasoning model (OpenAI-o3) is used to identify errors within the intermediate steps of a generated reasoning process.

**[Personality Vector: Modulating Personality of Large Language Models by Model Merging](https://aclanthology.org/2025.emnlp-main.1254.pdf) (as "LLM-based story evaluator")**
> An evaluation protocol where an LLM (Gemini 2.0-Flash) performs pairwise comparisons of generated stories to determine superiority across dimensions like plot, creativity, and language use.

**[PACHAT: Persona-Aware Speech Assistant for Multi-party Dialogue](https://aclanthology.org/2025.emnlp-main.1493.pdf) (as "Dic-Judge")**
> An automated judge used to classify model responses into categories like 'Full Refusal' or 'Full Compliance' for over-refusal analysis.

**[TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf) (as "GPT-as-a-Judge")**
> Automated evaluation protocol using GPT-4.1 as a judge to assess model responses on criteria including relevance, actionability, tool relevance, spelling and grammar, and correctness, based on a structured rubric and chain-of-thought prompting.

**[The Good, the Bad, and the Debatable: A Survey on the Impacts of Data for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1515.pdf) (as "LLM-based judge")**
> A few-shot prompted language-model judge used to label open-ended generations as containing invented information or as refusals/confessions of ignorance.

**[CausalVLBench: Benchmarking Visual Causal Reasoning in Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1562.pdf) (as "LLM-based Behavior Classification")**
> A procedure using gpt-4.1 as a deterministic classifier to map agent state-action trajectories into discrete behavior labels via chain-of-thought prompting.

**[EstimatingLLMConsistency: A User Baseline vs Surrogate Metrics](https://aclanthology.org/2025.emnlp-main.1555.pdf) (as "LLM-based safety moderator")**
> Automated evaluation using LLMs (e.g., GPT-4o, GPT-4o-mini) to classify model responses along safety dimensions such as harmfulness, refusal, and task completion.

**[SEMMA: A Semantic Aware Knowledge Graph Foundation Model](https://aclanthology.org/2025.emnlp-main.1622.pdf) (as "Automated LLM-based evaluation framework")**
> A scalable evaluation pipeline that uses an LLM judge (e.g., GPT-4o) to systematically assess answer correctness, code execution success, visualization readability, and chart accuracy without human annotation.

**[A Text-Based Recommender System that Leverages Explicit Affective State Preferences](https://aclanthology.org/2025.emnlp-main.1669.pdf) (as "LM-as-a-judge")**
> An evaluation protocol in which GPT-4o is prompted to generate a rationale and assign a 1–10 score to model responses relative to human references.

**[Language Models Identify Ambiguities and Exploit Loopholes](https://aclanthology.org/2025.emnlp-main.1678.pdf) (as "LLM-based Classical Poetry Metric")**
> An evaluation procedure using an LLM (GPT-4) with a 1-5 scoring prompt to assess the quality of poetry translations across three dimensions: Beauty of Sound (BS), Beauty of Form (BF), and Beauty of Meaning (BM).

**[The Illusion of Progress: Re-evaluating Hallucination Detection inLLMs](https://aclanthology.org/2025.emnlp-main.1762.pdf) (as "GPT-4-as-a-judge")**
> A judge-model evaluation procedure using GPT-4 to label model responses as harmful or not harmful for jailbreak assessment.

**[A Unified Supervised and Unsupervised Dialogue Topic Segmentation Framework Based on Utterance Pair Modeling](https://aclanthology.org/2025.naacl-long.253.pdf) (as "LLM evaluation")**
> Automated assessment using an LLM as a judge to evaluate insightfulness via pairwise comparisons or correctness via claim validation, calibrated against human judgments.

**[On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf) (as "GPT-4 multidimensional score")**
> A GPT-4-based evaluation procedure that grades story completions along multiple qualitative dimensions.

**[Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf) (as "GPT-4 rating")**
> An automated evaluation protocol where the GPT-4 model is used as a judge to assess the quality and safety of other models' responses based on predefined criteria.

**[Make-it-Real: Unleashing Large Multimodal Model for Painting 3D Objects with Realistic Materials](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf) (as "GPT-4V based evaluation")**
> An evaluation protocol where GPT-4V is prompted to act as an expert to compare the photorealism of 3D objects before and after material refinement, providing a preference and a justification.

**[Language Model Detectors Are Easily Optimized Against](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f9f07df0992ce21698d800eaa891bd8-Paper-Conference.pdf) (as "GPT-4 win rate")**
> A human-or-model preference evaluation in which GPT-4 chooses which of two generations is more fluently and coherently written.

**[Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf) (as "GPT-4 Evaluation")**
> Automated evaluation using GPT-4 to perform blind pairwise comparisons between model outputs, simulating human judgment on quality.

**[Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf) (as "Judge ability")**
> The latent capability of a large language model to evaluate responses, provide accurate preference signals, and render critical judgments.

**[2025.emnlp-main.712.checklist](https://aclanthology.org/attachments/2025.emnlp-main.712.checklist.pdf) (as "LLM-as-a-judge ability")**
> The latent ability of a large language model to accurately and consistently evaluate the quality of other model outputs across diverse tasks.

## Relationships

### LLM-as-a-judge →
- **Task completion** (behaviors tasks) — *measured_by*
  - [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > To assess free-form questions and multiple-round conversations, we utilize the LLM-as-a-Judge methodology
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **Reward-Bench** (measurements) — *measured_by*
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf)

### → LLM-as-a-judge
- **Helpfulness** (constructs) — *measured_by*
  > "We use GPT-4o to assess its safety (prioritized) and quality."
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  > GPT-4 rates the generated texts and instruction-following capability of the privately steered LLM at almost the same quality as the non-private model.
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *correlates*
  > Humans are generally aligned with GPT-4 in terms of evaluation performance in most cases.
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
- **Factuality** (constructs) — *measured_by*
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
- **Relevance** (constructs) — *measured_by*
  > We prompt GPT-4 to rate responses from various decoding strategies on relevance, accuracy, and insightfulness, scoring them from 1 to 10.
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  > The GPT-4V-aided evaluation shown in Table 4 further confirms that our method enhances both the accuracy and detailedness of the generated response, outperforming other hallucination mitigation approaches (Section 4.2).
  - [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Interpretability and explainability** (constructs) — *measured_by*
  > We evaluate feature interpretability using gpt4o-mini as an LLM judge.
  - [Efficient Dictionary Learning with Switch Sparse Autoencoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc4fbc2c77d2150c4e61e0fca6c2e95a-Paper-Conference.pdf)
- **Fluency** (constructs) — *measured_by*
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
- **Truthfulness** (constructs) — *measured_by*
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > To evaluate the quality of the generated dialogues, we compute the winrate (Rafailov et al., 2024b) against the generations from the reference policy, Llama-3-8B-it, using GPT4 (OpenAI, 2023) over a randomly sampled subset of the test set with 500 samples. (Section 4.2)
  - [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
- **Insightfulness** (constructs) — *measured_by*
  > We prompt GPT-4 to rate responses from various decoding strategies on relevance, accuracy, and insightfulness, scoring them from 1 to 10.
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
- **Accuracy** (constructs) — *measured_by*
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
- **Naturalness** (constructs) — *measured_by*
  > "we used GPT-4 (OpenAI et al., 2024) to carefully evaluate each dialogue based on four dimensions: naturalness (NAT), coherence (COH), helpfulness (HELP), and accuracy (ACC)."
  - [PROMPTEVALS: A Dataset of Assertions and Guardrails for Custom Production Large Language Model Pipelines](https://aclanthology.org/2025.naacl-long.214.pdf)
- **Generalization** (constructs) — *measured_by*
  > The GPT-4 judgment results between the generations of different methods and Llama-3-Base are provided in Figure 3... This confirms the superiority of PAD in generalizing to unseen personalized preferences.
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
- **Empathy** (constructs) — *measured_by*
  > We adopt a three-dimensional scoring system for AI therapists, evaluating them on empathy, logical coherence, and guidance. (Section 4.2)
  - [Analyzing (In)Abilities ofSAEs via Formal Languages](https://aclanthology.org/2025.naacl-long.250.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [GuideLLM: ExploringLLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.288.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety... (Section 5)
  - [EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING](https://proceedings.iclr.cc/paper_files/paper/2025/file/52724c4ea3634f610b0ef0245ce5bd20-Paper-Conference.pdf)
- **Creativity** (constructs) — *measured_by*
  > In addition, we develop a LLM-based evaluator (Liusie et al., 2023; Liu et al., 2024; Zheng et al., 2024; Bohnet et al., 2024) to perform side-by-side comparisons of system output. We design prompts targeting the same dimensions of story quality adopted in our human evaluation (Section 6.2).
  - [Agents' Room:  Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf)
- **Multimodal alignment** (constructs) — *measured_by*
  - [Interleaved Scene Graphs for Interleaved Text-and-Image Generation Assessment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e0ceee9751ae8b5c6603c029e4ca42-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *measured_by*
  > Win Rate (Win%), which evaluates effectiveness through pairwise comparisons by a ChatGPT-based evaluator, capturing nuanced performance differences not reflected by rule-based metrics. (Section 3.1)
  - [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  > we adopt a pairwise comparison approach, where an LLM evaluates a question alongside two answers and determines which response is of higher quality. (Section 6.4)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Personalization** (constructs) — *measured_by*
  > “We further explore whether we can employ language models to automate the evaluation... we ask GPT-4 to rate the responses based on their helpfulness and relevance to users’ preferences.”
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
- **Informativeness** (constructs) — *measured_by*
  > We also train several judge models for informativeness following the same procedure as for truthfulness. (Section 3.2.4)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **Clarity** (constructs) — *measured_by*
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **Comprehensiveness** (constructs) — *measured_by*
  > The evaluation framework uses multi-perspective criteria by LLM-as-a-judge, such as comprehensiveness, specificity, and relevance. (Section 1)
  - [MemeArena: Automating Context-Aware Unbiased Evaluation of Harmfulness Understanding for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.891.pdf)
- **Code generation** (behaviors tasks) — *measured_by*
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  > "We employ the HH-RLHF (Bai et al., 2022) and AlpacaEval (Li et al., 2023b) to comprehensively assess the effectiveness of ICDPO, as well as different ways of evaluation (reward model (RM) evaluation for HH-RLHF; GPT-4 evaluation for HH-RLHF and AlpacaEval)"
  - [CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases](https://aclanthology.org/2025.naacl-long.8.pdf)
- **Logical consistency** (constructs) — *measured_by*
  - [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.38.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks) — *measured_by*
  - [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5ef9853a6cdea40ae3e301a6d8dc32b5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
- **Reward overoptimization** (constructs) — *measured_by*
  - [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf)
- **Specificity** (constructs) — *measured_by*
  > The evaluation framework uses multi-perspective criteria by LLM-as-a-judge, such as comprehensiveness, specificity, and relevance. (Section 1)
  - [MemeArena: Automating Context-Aware Unbiased Evaluation of Harmfulness Understanding for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.891.pdf)
- **Dialogue generation** (behaviors tasks) — *measured_by*
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
- **Language proficiency** (constructs) — *measured_by*
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **Video question answering** (behaviors tasks) — *measured_by*
  > The second method involves models freely generating answers, which are then evaluated by GPT-4. Given the question, correct answer, and model’s prediction, GPT-4 returns a True or False judgment.
  - [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf)
- **Consistency** (constructs) — *measured_by*
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks) — *measured_by*
  - [Neuron-Level Differentiation of Memorization and Generalization in Large Language Models](https://aclanthology.org/2025.emnlp-main.813.pdf)
- **EHRNoteQA** (measurements) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Image captioning** (behaviors tasks) — *measured_by*
  > Following Leng et al. (2024), we use GPT-4 to assess the accuracy and detailedness of LVLM’s image captioning using a 10-point Likert scale (Section 4.1).
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **Explanation quality** (constructs) — *measured_by*
  > Explanation quality, which denotes the correctness and policy adherence of the guardrail explanations. Specifically, we consider both GPT-4o as a judge (Zheng et al., 2023) and human evaluators... (Section 5.1)
  - [SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model with Transparent Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/beac6bfb7eac3d651307c16ac747df01-Paper-Conference.pdf)
- **Text generation quality** (constructs) — *measured_by*
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Stereotyping** (constructs) — *measured_by*
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Factual accuracy** (constructs) — *measured_by*
  - [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
- **Code understanding** (constructs) — *measured_by*
  > To tackle this issue, we take the initiative to apply embedding similarity and GPT score for evaluation, both of which assess semantic similarity more effectively. (Section 1)
  - [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf)
- **Output quality** (constructs) — *measured_by*
  > Response Quality : We measure the quality of Ri given Ii. First, we use LLM-as-a-Judge where we prompt an LM to return a discrete score between 1 and 5 that represents the quality of Ri. (Section 5.2)
  - [LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/59f278de1619bdb6b53fd04e8e0976e0-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
- **Image generation** (behaviors tasks) — *measured_by*
  > Additionally, following the GPT-4V metric introduced in Section 4.2, we randomly select a subset of 3,000 our generated images for GPT-4V evaluation.
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
- **Privacy preservation** (constructs) — *measured_by*
  - [LLMThe Genius Paradox: A Linguistic and Math Expert’s Struggle with Simple Word-based Counting Problems](https://aclanthology.org/2025.naacl-long.173.pdf)
- **Argument quality** (constructs) — *measured_by*
  - [MGM: Global Understanding of Audience Overlap Graphs for Predicting the Factuality and the Bias of News Media](https://aclanthology.org/2025.naacl-long.374.pdf)
- **Cultural competence** (constructs) — *measured_by*
  > "To evaluate our model’s performance in these dimensions, we conduct an assessment using GPT-4 on the full test data"
  - [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.388.pdf)
- **Idea generation** (behaviors tasks) — *measured_by*
  - [E-SFT](https://aclanthology.org/2025.acl-long.1390.pdf)
- **Activation steering** (measurements) — *measured_by*
  > For the latter, we use an LLM judge to rate steered outputs on three relevant axes (see §3.3). (Section 3)
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Concept detection** (constructs) — *measured_by*
  > For concept detection, we use the same LLM judge as described in §3.3 to rate the presence of a concept on a scale of 0 to 2.
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Interactivity** (constructs) — *measured_by*
  - [CollabLLM: From Passive Responders to Active Collaborators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25i/wu25i.pdf)
- **Model bias** (constructs) — *measured_by*
  > In Fig. 2, we visualize how ROC and RUC evolve as the strength parameter p in Eq. (4) increases. We observe a significant increase in ROC with growing strength, particularly for models like Llama3.1-70b-Instruct and Yi-34B-Chat. In contrast, RUC remains relatively stable.
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
- **Unlearning** (constructs) — *measured_by*
  - [HS-STaR: Hierarchical Sampling for Self-Taught Reasoners via Difficulty Estimation and Budget Reallocation](https://aclanthology.org/2025.emnlp-main.283.pdf)
- **Reward hacking** (behaviors tasks) — *measured_by*
  > "we use AI feedback to identify hacking samples following Miao et al. (2024). Speciﬁcally, we ﬁrst outline common hacking behaviors ... and then use GPT-4 to evaluate responses based on these criteria"
  - [The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25c/miao25c.pdf)
- **Prompt quality** (constructs) — *measured_by*
  > “We employ Llama 3.1-405B-Instruct to measure the quality of prompts on both a binary (useful/not useful) and pointwise scale (0-5).”
  - [R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf)
- **Expressive power** (constructs) — *measured_by*
  - [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.40.pdf)
- **Verbal uncertainty** (constructs) — *measured_by*
  > We follow recent work in expression decisiveness quantification and employ "LLM-as-a-Judge" to measure VU (Yona et al., 2024; Zheng et al., 2023). (Section 2.2)
  - [Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.187.pdf)
- **Disambiguation** (constructs) — *measured_by*
  - [JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf)
- **Machine translation** (behaviors tasks) — *measured_by*
  - [Language Models Identify Ambiguities and Exploit Loopholes](https://aclanthology.org/2025.emnlp-main.1678.pdf)
- **Pluralistic alignment** (constructs) — *measured_by*
  - [Same Question, Different Words: A Latent Adversarial Framework for Prompt Robustness](https://aclanthology.org/2025.emnlp-main.1596.pdf)
- **Actionability** (constructs) — *measured_by*
  - [TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Personalized response generation** (behaviors tasks) — *measured_by*
  - [Logit Space Constrained Fine-Tuning for Mitigating Hallucinations inLLM-Based Recommender Systems](https://aclanthology.org/2025.emnlp-main.1492.pdf)
- **Direct answering** (behaviors tasks) — *measured_by*
  - [Neuron-Level Differentiation of Memorization and Generalization in Large Language Models](https://aclanthology.org/2025.emnlp-main.813.pdf)
- **Language fluency** (constructs) — *measured_by*
  - [Word Salad Chopper: Reasoning Models Waste A Ton Of Decoding Budget On Useless Repetitions, Self-Knowingly](https://aclanthology.org/2025.emnlp-main.1706.pdf)
- **Definition generation** (behaviors tasks) — *measured_by*
  > we employ a Large Language Model (LLM) as a judge (LLM-as-a-Judge) (Gu et al., 2024) to provide qualitative insights into the quality of generated descriptions (Section 5.4).
  - [Concept-pedia: a Wide-coverage Semantically-annotated Multimodal Dataset](https://aclanthology.org/2025.emnlp-main.1746.pdf)

### Associated with
- **Human evaluation** (measurements)
  > "To ensure the reliability of the G-Eval scores, we conducted a human evaluation... This subset was used to compare the G-Eval scores with human-annotated scores"
  - [OpenDebateEvidence: A Massive-Scale Argument Mining and Summarization Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c630d28df1cff44314d5798f82e02ec-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MT-Bench** (measurements)
  - [RouteLLM: Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
- **BARTScore** (measurements)
  - [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.576.pdf)
- **AlpacaEval 2.0** (measurements)
  > In this benchmark, GPT-4-Preview-1106 serves as both the baseline model and the evaluator for the other models.
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
- **Arena-Hard** (measurements)
  > We report the win rate against GPT-4-0314 using GPT-4-Preview-1106 as the judge model.
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf)
- **Generalization** (constructs)
  > However, these judge models demonstrate poor generalization when evaluating different LLMs and benchmarks (Laskar et al., 2023; Huang et al., 2024). (Section 2)
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
- **FaithEval** (measurements)
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **Pairwise comparison** (behaviors tasks)
  > We explore two typical LLM-as-a-judge methods: Pairwise comparison (Section 2.1)
  - [Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf)
- **Reward model** (measurements)
  > “To develop the reward model, we initially employ GPT-4 to assess various MRPAs across all test samples.”
  - [MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf)
- **Question rephrasing** (behaviors tasks)
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
- **Faithfulness** (constructs)
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **Prompt robustness** (constructs)
  > When we adopt LLM-as-a-Judge evaluations, we observe a substantial reduction in performance variance and a consistently higher correlation in model rankings across prompts. Our findings suggest that modern LLMs are more robust to prompt templates than previously believed...
  - [Hope vs. Hate: Understanding User Interactions withLGBTQ+ News Content in MainstreamUSNews Media through the Lens of Hope Speech](https://aclanthology.org/2025.emnlp-main.1006.pdf)
