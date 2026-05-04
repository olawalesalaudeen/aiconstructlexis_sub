# Human evaluation
**Type:** Measurement  
**Referenced in:** 729 papers  
**Also known as:** Human Evaluation, Human grading, Human spot-checking, Human annotation, Human Annotation, Human performance evaluation, Human analysis, Side-by-side comparisons, Human verification protocol, A/B testing, Expert evaluation, Human preference study, Human verification, Clinician Annotation, Expert relevance annotation, Human expert annotation, Human agreement study, User preference study, Human crowdworker rating, Human study, User feedback interface, Professional Nutritionist Study, User study, Expert explanation evaluation, Manual evaluation, Crowdsourcing study, Human annotations, A/B test, Human expert forecasts, Human-as-a-Judge, Clinician validation study, Human user study, Human survey, Expert user study, Crowdsourced highly activating inputs evaluation, GPT-4–judged pairwise comparisons, Case study, Expert annotation evaluation, Expert verification evaluation, Human experiment, Clinical reader study, Reader study, AV-Human, Human validation study, Inter-annotator agreement study, Human judgment, Human expert review, Expert review, Expert study, Human CAI study, Expert validation study, Human pairwise comparison, Open-ended interview, Human-LLM agreement study, Human-interactive evaluation, Preference-Based Evaluation, Manual validation, Domain scholar evaluation, Collaborative LLM annotation, Human-in-the-loop evaluation, LLM-based zero-shot annotation, Manual error annotation, Human rating study, Inter-annotator agreement, Native speaker preference study, Physician reader study, Heuristic evaluation, Crowdsourced annotation study, Ecological validity study, 5-point Likert scale, Human-in-the-loop insight annotation, Human-in-the-loop tuple annotation, Pairwise evaluation, Human factuality assessment, Human annotation verification, Automated evaluation, Human inspection, Demonstration Effect study, Prolific study, Simulated user study, Human adjudication, Pilot expert validation, Human expert verification, Human-baseline study, Human-eval, Side-by-side evaluation, Human inter-annotator agreement, Expert annotation, Human annotation evaluation, Human expert evaluation, Expert human evaluation, Clinician evaluation, Domain-expert evaluation, Human pairwise evaluation, Human preference evaluation, Human performance study, Human preference-based evaluation, Human evaluation study  

## State of the Field

Across the surveyed literature, human evaluation represents a broad category of assessment protocols frequently positioned as the "gold standard" for judging model outputs, particularly for open-ended tasks. It is commonly used to validate and measure the correlation of automated metrics, with several papers noting that evaluations from an `LLM-as-a-judge` can align closely with human assessments. The most prevalent operationalizations involve human annotators performing pairwise comparisons—such as A/B testing or side-by-side evaluations—to select a preferred response, or rating outputs on multi-point scales according to predefined rubrics. Other common procedures include labeling outputs for specific attributes like safety, spot-checking automated grades, and establishing performance baselines by having humans complete the benchmark tasks themselves. Researchers use these methods to assess a wide range of qualities, most frequently targeting core alignment dimensions such as helpfulness, harmlessness, and faithfulness. It is also widely applied to measure linguistic quality (including fluency and coherence), instruction following, and the presence of object hallucination. The evaluators themselves vary across studies, ranging from crowdworkers and general users to domain specialists like clinicians, legal professionals, and mathematicians who assess outputs in their respective fields. This variety in both procedure and personnel underscores that human evaluation is treated not as a single method but as a flexible framework adapted to specific research questions.

## Sources

**[AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf)**
> Large-scale annotation study with over 10,000 human judgments from verified English speakers, assessing preference between model-generated and original text continuations across Wikipedia and fictional story contexts.

**[Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf) (as "Human Evaluation")**
> A manual evaluation method where human annotators label translated model outputs as safe, unsafe, or invalid to assess safety in multilingual contexts.

**[SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bbf38332580c1bed99fa99bc9ee53229-Paper-Conference.pdf) (as "Human grading")**
> An evaluation procedure where human raters assess the quality of model-generated text, often based on a provided rubric.

**[SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bbf38332580c1bed99fa99bc9ee53229-Paper-Conference.pdf) (as "Human spot-checking")**
> A procedure where human evaluators review a subset of auto-graded responses to verify the accuracy and reliability of the grading model's assessments.

**[MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf) (as "Human annotation")**
> The process of having human experts or annotators score model responses according to a predefined rubric, used in this paper to create a dataset for training a scoring model.

**[Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf) (as "Human Annotation")**
> A human evaluation protocol where judges assess agent outputs or validate automated evaluations for consistency.

**[VideoWebArena:  Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf) (as "Human performance evaluation")**
> A protocol where human participants attempt tasks from the benchmark to establish a baseline for success rates and efficiency, with evaluation conducted by a third party.

**[An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf) (as "A/B testing")**
> A human evaluation method where raters compare two model outputs (A and B) and choose the better one.

**[Reliable and Diverse Evaluation of LLM Medical Knowledge Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/91a5bb5e5939cb075f5f2464d7b8bbf0-Paper-Conference.pdf) (as "Human analysis")**
> A doctor-rated evaluation procedure used to judge generated samples on lexical diversity, structural diversity, and reliability.

**[First-Person Fairness in Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/92af0c8c2664429de2bb44c2692d84ae-Paper-Conference.pdf) (as "Human annotation study")**
> A validation procedure where a diverse group of human crowd-workers are recruited to rate chatbot response pairs for harmful stereotypes, with their average judgments used to corroborate LMRA-generated labels.

**[BOND: Aligning LLMs with Best-of-N Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/947f37882a394140f7add476bb99d1d3-Paper-Conference.pdf) (as "Side-by-side comparisons")**
> Human evaluation procedure in which outputs are compared directly to assess higher quality.

**[A Benchmark for Semantic Sensitive Information in LLMs Outputs](https://proceedings.iclr.cc/paper_files/paper/2025/file/994a53df880f1ec64fd5cbf1bba4a8af-Paper-Conference.pdf) (as "Human verification protocol")**
> A two-part process involving human annotators to ensure the effectiveness and reliability of automated GPT-4o labeling, consisting of independent a priori labeling and a posteriori review.

**[VoxDialogue: Can Spoken Dialogue Systems Understand Information Beyond Words?](https://proceedings.iclr.cc/paper_files/paper/2025/file/011df158529ddceb5f2f7a65f2732a5a-Paper-Conference.pdf) (as "Human verification")**
> A human-annotator quality-check procedure used to assess the naturalness and logical consistency of synthesized spoken dialogue samples.

**[SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf) (as "Human preference study")**
> Human evaluation protocol where annotators rate which of two model descriptions is more faithful to a table.

**[MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf) (as "Expert evaluation")**
> A human evaluation protocol in which medical professionals assess the accuracy of generated descriptions against ground-truth annotations.

**[Recognize Any Surgical Object: Unleashing the Power of Weakly-Supervised Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/53d3f45797970d323bd8a0d379c525aa-Paper-Conference.pdf) (as "Clinician Annotation")**
> A human evaluation method where medical experts provide ground-truth labels or annotations for surgical images, used as a benchmark for model performance.

**[DarkBench: Benchmarking Dark Patterns in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f6421fbc2351067ef9c75e4bcd12af5-Paper-Conference.pdf) (as "Human expert annotation")**
> An evaluation procedure where human experts in a specific domain review and validate model outputs or automated annotations.

**[From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf) (as "Expert relevance annotation")**
> A human evaluation protocol where domain experts (senior medical students) annotate the relevance of microtheory facts for a specific task (USMLE tests) using a 5-point rubric.

**[Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps](https://proceedings.iclr.cc/paper_files/paper/2025/file/6794f555524c9069e26970a408d353cc-Paper-Conference.pdf) (as "User preference study")**
> A human evaluation protocol where participants are shown a question and responses from multiple models and asked to choose the most creative and humorous one.

**[DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf) (as "Human agreement study")**
> A human evaluation protocol where annotators rank pairwise state-action samples to assess agreement with the model's utility elicitation.

**[GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf) (as "Human study")**
> A human evaluation protocol where annotators compare and select the preferred response from different models acting as a GUI assistant.

**[Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ba4d47a83e498c2b1a0868cba20f6de-Paper-Conference.pdf) (as "Human crowdworker rating")**
> A human evaluation protocol where crowdworkers rate the interpretability of model components such as features or neurons.

**[NutriBench: A Dataset for Evaluating Large Language Models in Nutrition Estimation from Meal Descriptions](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef3a57e4f26b640e6f90d78cbb011feb-Paper-Conference.pdf) (as "Professional Nutritionist Study")**
> A human evaluation procedure where professional nutritionists provide carbohydrate estimates for a subset of meal descriptions to compare against LLM performance.

**[REvolve: Reward Evolution with Large Language Models using Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc8ee7c7ab5b5f6b1615045dfb617ed6-Paper-Conference.pdf) (as "User feedback interface")**
> A system for collecting human feedback on policy rollouts, which includes both pairwise preference judgments and qualitative natural language comments on specific aspects of the behavior.

**[Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf) (as "User study")**
> A human evaluation protocol in which 30 people with programming experience rated sampled data points on task quality and trajectory quality from 1 to 10.

**[Decision Information Meets Large Language Models: The Future of Explainable Operations Research](https://proceedings.iclr.cc/paper_files/paper/2025/file/a48e5877c7bf86a513950ab23b360498-Paper-Conference.pdf) (as "Expert explanation evaluation")**
> A human blind review protocol where OR experts anonymously score the explanations generated by different methods.

**[Towards Better Evaluation for Generated Patent Claims](https://aclanthology.org/2025.acl-long.191.pdf) (as "Manual evaluation")**
> Human or expert analysis of model outputs to assess qualitative aspects of reasoning, such as whether a second chain corrects the first, based on sampled instances from multiple datasets.

**[Do Language Models Have Semantics? On the Five Standard Positions](https://aclanthology.org/2025.acl-long.1259.pdf) (as "Crowdsourcing study")**
> A human evaluation protocol where participants highlight phrases in LLM-generated text they perceive as human-like, rate the text's humanness on a five-point scale, and rewrite the text to be less human-like.

**[A Hitchhiker’s Guide to Scaling Law Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/choshen25a/choshen25a.pdf) (as "A/B test")**
> An experimental procedure where two models are trained under similar conditions, with a single attribute manipulated, to measure the effect of that attribute on performance.

**[Automated Hypothesis Validation with Agentic Sequential Falsifications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25n/huang25n.pdf) (as "Human annotations")**
> Qualitative assessment by human experts rating the strength of implication in LLM-generated falsification tests using a standardized rubric, used to evaluate relevance and logical coherence.

**[Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf) (as "Clinician validation study")**
> A human evaluation protocol where licensed clinicians assess the difficulty of benchmark tasks by answering questions and providing subjective difficulty ratings on a 1-10 scale.

**[Agent-as-a-Judge: Evaluate Agents with Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuge25a/zhuge25a.pdf) (as "Human-as-a-Judge")**
> A human expert evaluation protocol in which expert evaluators review agent outputs and decide whether each requirement was satisfied, including consensus adjudication.

**[Position: LLM Social Simulations Are a Promising Research Method](https://raw.githubusercontent.com/mlresearch/v267/main/assets/anthis25a/anthis25a.pdf) (as "Human expert forecasts")**
> An evaluation protocol where human experts predict research outcomes, used as a performance baseline to compare against LLM simulation accuracy.

**[Proactive Agents for Multi-Turn Text-to-Image Generation Under Uncertainty](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hahn25a/hahn25a.pdf) (as "Human user study")**
> A human evaluation in which participants judge the helpfulness of proactive clarification, belief graphs, and generated images for text-to-image workflows.

**[Proactive Agents for Multi-Turn Text-to-Image Generation Under Uncertainty](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hahn25a/hahn25a.pdf) (as "Human survey")**
> A questionnaire study of regular text-to-image users assessing frustrations and the perceived helpfulness of clarification, entity graphs, and relationship graphs.

**[Automated Hypothesis Validation with Agentic Sequential Falsifications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25n/huang25n.pdf) (as "Expert user study")**
> A human evaluation protocol where domain experts, such as computational biologists, perform a task like hypothesis validation, and their performance and process are compared against an automated system.

**[Evaluating Neuron Explanations: A Unified Framework with Sanity Checks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oikarinen25a/oikarinen25a.pdf) (as "Crowdsourced highly activating inputs evaluation")**
> An evaluation procedure where human raters are shown inputs that highly activate a neuron and are asked to judge whether a given textual explanation or concept applies to those inputs.

**[Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.26.pdf) (as "GPT-4–judged pairwise comparisons")**
> Human-like evaluation where GPT-4 compares model outputs in a pairwise fashion across test sets to determine relative quality.

**[Mixture of Length and Pruning Experts for Knowledge Graphs Reasoning](https://aclanthology.org/2025.emnlp-main.24.pdf) (as "Case study")**
> A qualitative evaluation method involving an in-depth analysis of a specific example to illustrate a system's behavior and interpretability.

**[2025.emnlp-main.42.checklist](https://aclanthology.org/attachments/2025.emnlp-main.42.checklist.pdf) (as "Expert annotation evaluation")**
> Human evaluation by domain experts to rate model responses on moral stage and harmfulness using defined criteria and rating scales.

**[POSITIONBIASMITIGATESPOSITIONBIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.79.pdf) (as "Expert verification evaluation")**
> Human evaluation in which professional translators assess translation quality on accuracy, fluency, and completeness using a 5-point Likert scale.

**[Continuously SteeringLLMs Sensitivity to Contextual Knowledge with Proxy Models](https://aclanthology.org/2025.emnlp-main.234.pdf) (as "Human experiment")**
> A study conducted with human participants to establish a baseline for Wisdom of Crowds effects in guesstimation tasks and to compare human performance with that of LLMs.

**[TRUST-VL: An Explainable News Assistant for General Multimodal Misinformation Detection](https://aclanthology.org/2025.emnlp-main.285.pdf) (as "Clinical reader study")**
> A human evaluation involving clinicians who score model outputs on correctness, completeness, and logical flow using USMLE-style questions from MedQA.

**[2025.emnlp-main.285.checklist](https://aclanthology.org/attachments/2025.emnlp-main.285.checklist.pdf) (as "Reader study")**
> A human evaluation procedure in which readers assess model outputs; the checklist notes that reader study setups are described in Section 5.2.1.

**[SPEAttention: Making Attention Equivariant to Semantic-Preserving Permutation for Code Processing](https://aclanthology.org/2025.emnlp-main.333.pdf) (as "AV-Human")**
> The human-annotated subset of AVUT containing 698 videos and 1,734 question-answer pairs created by trained annotators.

**[Multilingual Prompting for ImprovingLLMGeneration Diversity](https://aclanthology.org/2025.emnlp-main.325.pdf) (as "Human validation study")**
> A user study with 204 participants recruited via Prolific, comparing human and agent engagement behaviors on curated social media snapshots containing factual and false news articles.

**[LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-Shot Stance Detection](https://aclanthology.org/2025.emnlp-main.300.pdf) (as "Inter-annotator agreement study")**
> A study measuring consistency among human annotators in evaluating cluster coherence, using Fleiss’ kappa to assess reliability of binary vs. graded judgments.

**[ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf) (as "Human judgment")**
> Manual evaluation by human annotators who rate model responses on a 1–10 scale based on accuracy and quality relative to reference answers, used as a gold standard for validating automated metrics.

**[Noise, Adaptation, and Strategy: AssessingLLMFidelity in Decision-Making](https://aclanthology.org/2025.emnlp-main.392.pdf) (as "Human expert review")**
> An evaluation protocol where five board-certified radiologists assessed 223 generated reports for errors and adherence to a predefined template compared to their original free-form counterparts.

**[Variance Sensitivity Induces Attention Entropy Collapse and Instability in Transformers](https://aclanthology.org/2025.emnlp-main.422.pdf) (as "Expert review")**
> A human evaluation protocol where domain experts, such as radiologists or physicians, assess the quality, clinical alignment, and reliability of model-generated responses.

**[Accelerate Parallelizable Reasoning via Parallel Decoding within One Sequence](https://aclanthology.org/2025.emnlp-main.458.pdf) (as "Human subject study")**
> A human evaluation protocol in which doctoral students rated slide complexity on three dimensions using a 0–100 scoring range.

**[IndoSafety: Culturally Grounded Safety forLLMs inIndonesian Languages](https://aclanthology.org/2025.emnlp-main.466.pdf) (as "Expert study")**
> A human evaluation involving ten domain experts who assessed the correctness, realism, and practicality of tasks in the EnterpriseBench sandbox environment using a realism scale and task execution validation.

**[IndoSafety: Culturally Grounded Safety forLLMs inIndonesian Languages](https://aclanthology.org/2025.emnlp-main.466.pdf) (as "Human CAI study")**
> A human evaluation in which human participants acted as LLM agents to complete EnterpriseBench tasks, used to measure upper-bound performance and compare against model agents.

**[CROP: Contextual Region-Oriented Visual Token Pruning](https://aclanthology.org/2025.emnlp-main.493.pdf) (as "Expert validation study")**
> A human evaluation protocol where four trained project moderators independently annotated a random sample of 100 passages to validate the reliability of citizen science annotations.

**[CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-DeviceLLM](https://aclanthology.org/2025.emnlp-main.534.pdf) (as "Human pairwise comparison")**
> An evaluation protocol where human experts assess hypothesis quality by selecting the better option from a pair of hypotheses or indicating no discernible difference.

**[Back Attention: Understanding and Enhancing Multi-Hop Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.568.pdf) (as "Open-ended interview")**
> A 30-minute qualitative interview protocol used to elicit participants’ detailed feedback about GlossLM and its fit in documentation workflows.

**[Collaborative Beam Search: EnhancingLLMReasoning via Collective Consensus](https://aclanthology.org/2025.emnlp-main.575.pdf) (as "Human-LLM agreement study")**
> A validation study comparing LLM-generated judgments on counterfactual quality with human annotator labels to assess reliability, using 500 random samples.

**[Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.682.pdf) (as "Human-interactive evaluation")**
> A user study where human participants interact with models by providing unspecified tool-use queries to assess real-world performance and user satisfaction.

**[2025.emnlp-main.672.checklist](https://aclanthology.org/attachments/2025.emnlp-main.672.checklist.pdf) (as "Preference-Based Evaluation")**
> A human evaluation procedure in which annotators, including NLP practitioners and general users, assess model outputs using an evaluation interface.

**[Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline](https://aclanthology.org/2025.emnlp-main.763.pdf) (as "Manual validation")**
> A human evaluation procedure where two or more annotators independently review and label generated sentences as valid or invalid to filter out content that could skew evaluation.

**[Automated Knowledge Graph Construction using Large Language Models and Sentence Complexity Modelling](https://aclanthology.org/2025.emnlp-main.784.pdf) (as "Domain scholar evaluation")**
> Expert evaluation by an Islamic scholarship domain expert using a 5-point scale to assess the accuracy and correctness of model responses, with qualitative feedback on answer quality.

**[Retrieval-augmentedGUIAgents with Generative Guidelines](https://aclanthology.org/2025.emnlp-main.903.pdf) (as "Collaborative LLM annotation")**
> A structured prompting procedure using an LLM to generate error labels and rewritten text, followed by human verification and revision.

**[LORAXBENCH: A Multitask, Multilingual Benchmark Suite for 20Indonesian Languages](https://aclanthology.org/2025.emnlp-main.882.pdf) (as "Human-in-the-loop evaluation")**
> An evaluation protocol where human annotators qualitatively inspect model outputs to assess specific qualities, such as manipulative or unsafe patterns.

**[UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging](https://aclanthology.org/2025.emnlp-main.922.pdf) (as "LLM-based zero-shot annotation")**
> Automated evaluation method using large language models (e.g., GPT-4.1, Gemini-2.0) in zero-shot or few-shot settings with prompting techniques to replicate human episode labeling.

**[RRInf: Efficient Influence Function Estimation via Ridge Regression for Large Language Models and Text-to-Image Diffusion Models](https://aclanthology.org/2025.emnlp-main.934.pdf) (as "Manual error annotation")**
> A procedure where human annotators manually identify and count errors in model-generated text according to a predefined set of categories, such as incorrect assembly operations or order.

**[RRInf: Efficient Influence Function Estimation via Ridge Regression for Large Language Models and Text-to-Image Diffusion Models](https://aclanthology.org/2025.emnlp-main.934.pdf) (as "Human rating study")**
> A user study in which experienced sewing participants rate generated instructions step by step and at the instruction level on Likert scales.

**[TreeRare: Syntax Tree-Guided Retrieval and Reasoning for Knowledge-Intensive Question Answering](https://aclanthology.org/2025.emnlp-main.948.pdf) (as "Inter-annotator agreement")**
> Statistical measure (Cohen’s kappa, Fleiss’ kappa) used to assess consistency among human annotators or between human and model predictions in toxicity labeling.

**[ACING: Actor-Critic for Instruction Learning in Black-BoxLLMs](https://aclanthology.org/2025.emnlp-main.966.pdf) (as "Native speaker preference study")**
> A human study where native experts are asked to indicate their preferred honorific forms for specific entities in a formal, Wikipedia-style writing context.

**[Women, Infamous, and Exotic Beings: A Comparative Study of Honorific Usages inWikipedia andLLMs forBengali andHindi](https://aclanthology.org/2025.emnlp-main.967.pdf) (as "Physician reader study")**
> Human evaluation involving nine physicians who assessed the quality of clinical notes selected by different PRM checkpoints through blinded, randomized review.

**[Hope vs. Hate: Understanding User Interactions withLGBTQ+ News Content in MainstreamUSNews Media through the Lens of Hope Speech](https://aclanthology.org/2025.emnlp-main.1006.pdf) (as "Heuristic evaluation")**
> A class of evaluation methods that rely on simple, rigid rules, such as regular-expression-based answer extraction or log-likelihood scoring, to determine the correctness of a model's output.

**[Exploring Artificial Image Generation for Stance Detection](https://aclanthology.org/2025.emnlp-main.1005.pdf) (as "Crowdsourced annotation study")**
> A human annotation protocol using the Prolific platform where raters, evenly distributed across Republican, Democrat, and Independent political leanings, label YouTube comments.

**[Beyond the Score: Uncertainty-CalibratedLLMs for Automated Essay Assessment](https://aclanthology.org/2025.emnlp-main.993.pdf) (as "Ecological validity study")**
> An evaluation procedure that assesses the practical utility of a label correction method by training smaller models on the corrected datasets and measuring their downstream performance.

**[AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models](https://aclanthology.org/2025.emnlp-main.1036.pdf) (as "5-point Likert scale")**
> A rating scale used to allow finer-grained judgments within difficulty levels, where a score from 1 to 5 indicates the position of a text within a broader difficulty category.

**[Drivel-ology: ChallengingLLMs with Interpreting Nonsense with Depth](https://aclanthology.org/2025.emnlp-main.1178.pdf) (as "Human-in-the-loop insight annotation")**
> A human-in-the-loop annotation procedure in which candidate opinion-centric insights are reviewed, selected, and refined by human annotators to produce gold abstractive summaries.

**[Drivel-ology: ChallengingLLMs with Interpreting Nonsense with Depth](https://aclanthology.org/2025.emnlp-main.1178.pdf) (as "Human-in-the-loop tuple annotation")**
> A human-in-the-loop annotation procedure in which LLM-generated candidate tuples are reviewed, refined, and validated by human annotators to produce gold structured opinion labels.

**[KCS: Diversify Multi-hop Question Generation with Knowledge Composition Sampling](https://aclanthology.org/2025.emnlp-main.1182.pdf) (as "Pairwise evaluation")**
> A comparative evaluation procedure in which an LVLM judge selects which of two images better aligns with a given textual prompt, with order reversed to control position bias.

**[Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1204.pdf) (as "Human factuality assessment")**
> Manual evaluation by human annotators to judge the factual accuracy of summaries, used as a gold standard for correlation analysis.

**[Evaluating the Evaluators: Are readability metrics good measures of readability?](https://aclanthology.org/2025.emnlp-main.1226.pdf) (as "Human annotation verification")**
> A procedure where human annotators manually classify data samples to validate findings from automated analysis, such as the presence of modality bias.

**[Rewarding the Unlikely: LiftingGRPOBeyond Distribution Sharpening](https://aclanthology.org/2025.emnlp-main.1299.pdf) (as "Automated evaluation")**
> An evaluation procedure comparing generated keyword sequences and verbal cues using automated measures of phonetic similarity, omission, modification, context completeness, and perplexity.

**[FairGen: Controlling Sensitive Attributes for Fair Generations in Diffusion Models via Adaptive Latent Guidance](https://aclanthology.org/2025.emnlp-main.1288.pdf) (as "Human inspection")**
> A human evaluation protocol used to validate the quality of dataset samples generated by different filtering methods.

**[Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1302.pdf) (as "Demonstration Effect study")**
> A one-shot prompting comparison that tests how answerable versus unanswerable exemplars affect refusal behavior on uncomputable cases.

**[Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1264.pdf) (as "Prolific study")**
> An IRB-approved Prolific annotation study in which workers watched videos, read questions and answer options, and wrote reasoning traces.

**[DPED: Multi-Layer Noise Distillation for Privacy-Preserving Text Embeddings](https://aclanthology.org/2025.emnlp-main.1283.pdf) (as "Simulated user study")**
> An experimental method where two machine agents, a 'director' and a 'coder', engage in a dialogue to simulate human-AI interaction for resolving ambiguity in code generation tasks.

**[OWL: Probing Cross-Lingual Recall of Memorized Texts via World Literature](https://aclanthology.org/2025.emnlp-main.1315.pdf) (as "Human adjudication")**
> A verification protocol where two human annotators with backgrounds in Computational Linguistics review, correct, or add relation labels and condition cues that were automatically generated for noun-noun compounds.

**[Sentence Smith: Controllable Edits for Evaluating Text Embeddings](https://aclanthology.org/2025.emnlp-main.1344.pdf) (as "Pilot expert validation")**
> A human evaluation protocol where board-certified physicians review a sample of model-generated examples to assess their medical quality.

**[2025.emnlp-main.1335.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1335.checklist.pdf) (as "Human expert verification")**
> A procedure where human experts check the correctness of data processed by a large language model, in this case, the conversion of PDF data.

**[2025.emnlp-main.1359.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1359.checklist.pdf) (as "Human-baseline study")**
> A human evaluation procedure in which volunteering student participants completed the same instructions as the models to provide a baseline for comparison.

**[Logit Space Constrained Fine-Tuning for Mitigating Hallucinations inLLM-Based Recommender Systems](https://aclanthology.org/2025.emnlp-main.1492.pdf) (as "Human-eval")**
> A human evaluation protocol in which multiple raters score model outputs on response quality, with scores averaged to ensure fairness.

**[NL2Lean: Translating Natural Language into Lean 4 through Multi-Aspect Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1587.pdf) (as "Side-by-side evaluation")**
> A comparative judging procedure in which summaries with and without guardrails are presented together and the evaluator selects a winner or draw.

**[MPCG: Multi-Round Persona-Conditioned Generation for Modeling the Evolution of Misinformation withLLMs](https://aclanthology.org/2025.emnlp-main.1728.pdf) (as "Human inter-annotator agreement")**
> A human annotation protocol in which two annotators independently label explanations with the proposed taxonomy and agreement is assessed.

**[CompA: Addressing the Gap in Compositional Reasoning in Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/43c18853329c7504996b255252b6cb1f-Paper-Conference.pdf) (as "Expert annotation")**
> A human evaluation procedure in which subject-matter experts annotate audio events and validate or correct captions for benchmark and training data.

**[Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2cefdb2c4c3274b78cd450bac35228df-Paper-Conference.pdf) (as "Human annotation evaluation")**
> A procedure where human annotators assess the relevance of a generated passage given a query and instruction, used here to validate an automatic filtering process.

**[AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.582.pdf) (as "Human expert evaluation")**
> A process where human experts with extensive SQL experience independently evaluate the semantic correctness of generated queries, with discrepancies resolved through consensus.

**[Enhancing Lexicon-Based Text Embeddings with Large Language Models](https://aclanthology.org/2025.acl-long.931.pdf) (as "Expert human evaluation")**
> A human evaluation protocol where a legal expert assesses model-generated responses on a 5-point Likert scale across criteria including correctness, faithfulness, fluency, and coherence.

**[Direct Prompt Optimization with Continuous Representations](https://aclanthology.org/2025.acl-long.134.pdf) (as "Clinician evaluation")**
> A human evaluation protocol where domain experts (in this case, two orthopaedic surgeons) perform pairwise comparisons of summaries based on overall quality and annotate errors like confabulations or missing information.

**[Bypass Back-propagation: Optimization-based Structural Pruning for Large Language Models via Policy Gradient](https://aclanthology.org/2025.acl-long.1422.pdf) (as "Domain-expert evaluation")**
> A human evaluation protocol where researchers with deep expertise in a specific field assess the quality of model outputs, such as comparative summaries, based on criteria like factuality, breadth, and contextualization.

**[MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf) (as "Human pairwise evaluation")**
> A human judgment procedure in which annotators compare two responses and choose the preferred one using task-specific criteria.

**[Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf) (as "Human preference evaluation")**
> A human evaluation protocol where evaluators are presented with outputs from two models side-by-side and asked to choose which is significantly better or if there is no significant difference.

**[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Human performance study")**
> An evaluation protocol where human participants (computer science students) perform the benchmark tasks to establish a baseline for performance, time, and accuracy.

**[HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Human preference-based evaluation")**
> A human evaluation protocol where annotators are shown outputs from two different models for the same input and are asked to choose the better one or declare a tie.

**[Are Models Biased on Text without Gender-related Language?](https://proceedings.iclr.cc/paper_files/paper/2024/file/37771cc0be272368102a37f202bb88d8-Paper-Conference.pdf) (as "Human evaluation study")**
> A small-scale human annotation procedure in which participants judged whether generated benchmark examples were neutral.

## Relationships

### Human evaluation →
- **LLM-as-a-judge** (measurements) — *correlates*
  > Humans are generally aligned with GPT-4 in terms of evaluation performance in most cases.
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Cost-efficient Collaboration between On-device and Cloud Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/narayan25a/narayan25a.pdf)
- **TaskBench** (measurements) — *correlates*
  - [TaskBench: Benchmarking Large Language Models for Task Automation](https://proceedings.neurips.cc/paper_files/paper/2024/file/085185ea97db31ae6dcac7497616fd3e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Bongard Problems** (measurements) — *measured_by*
  - [Bongard in Wonderland: Visual Puzzles that Still Make AI Go Mad?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wust25a/wust25a.pdf)

### → Human evaluation
- **Faithfulness** (constructs) — *measured_by*
  - [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > Human judges were tasked in the first stage with selecting the more Helpful, Honest, and Harmless response between 100 pairs without access to the LLM’s rationale. (Section 5.3)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  > “We perform a comprehensive human evaluation to assess the quality of the generated samples.”
  - [Guiding Instruction-based Image Editing via Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f0e91b1314fa5eabf1d7ef6d1561ecec-Paper-Conference.pdf)
- **Coherence** (constructs) — *measured_by*
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Fluency** (constructs) — *measured_by*
  - [IQA-EVAL: Automatic Evaluation of Human-Model Interactive Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a23b26eaaefd187973658f5001f4fe-Paper-Conference.pdf)
- **Naturalness** (constructs) — *measured_by*
  > We perform human evaluation at the conversation and utterance levels to examine the quality of the dialogues. The metrics are summarized in Table 2. For conversation-level evaluations, judges are asked to score each conversation on a 5-point Likert scale. ... Overall naturalness Overall subjective impression of the conversation and whether it sounds natural. (Table 2)
  - [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Factuality** (constructs) — *measured_by*
  - [Human Feedback is not Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2024/file/f719b8ca81221f380836e573d479c223-Paper-Conference.pdf)
- **Conciseness** (constructs) — *measured_by*
  - [VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > To corroborate these G-Eval findings, we conduct human evaluations involving 5 in-house annotators who assessed 50 randomly selected ChatGPT’s generations across the datasets. (Section 4.2)
  - [Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps](https://proceedings.iclr.cc/paper_files/paper/2025/file/6794f555524c9069e26970a408d353cc-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  > “we conduct comprehensive expert evaluations of the translation quality.”
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Relevance** (constructs) — *measured_by*
  > To further validate the effectiveness of our metrics, we performed a small-scale human evaluation, referencing existing studies (Fabbri et al., 2021). Specifically, six highly educated annotators evaluated the relevance of news summaries generated by five SLMs based on the original news articles (scored on a 1-5 scale, with higher scores indicating greater relevance).
  - [A Unified Supervised and Unsupervised Dialogue Topic Segmentation Framework Based on Utterance Pair Modeling](https://aclanthology.org/2025.naacl-long.253.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  > For HH-RLHF, we randomly select 200 samples from the test set to evaluate ICDPO, ICDPO+ ˆS, and all baselines except Zero-shot... Their decoded responses are compared with the chosen ones in HH-RLHF to compute the win/tie/lose rates. (Section 4.2.2)
  - [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *measured_by*
  > For Pythia SAEs, we asked human crowdworkers to rate the interpretability of random features, random neurons, features from our feature circuits, and neurons from our neuron circuits.
  - [Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ba4d47a83e498c2b1a0868cba20f6de-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  > Due to incomplete text annotations on the MMHal, GPT-4 couldn't reliably detect hallucinations. To make the results more reliable, we invited experts to manually annotate the data
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Consistency** (constructs) — *measured_by*
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
- **Comprehensiveness** (constructs) — *measured_by*
  > We find the sub-question coverage as an answer quality metric can approximate human perception of answer quality well (section 4).
  - [VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf)
- **Creativity** (constructs) — *measured_by*
  > "We evaluate system output by soliciting pairwise preferences ... along four dimensions"
  - [MetaDesigner: Advancing Artistic Typography through AI-Driven, User-Centric, and Multilingual WordArt Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/a10c3d85879c29331ba4d73ede56c7d3-Paper-Conference.pdf)
- **Informativeness** (constructs) — *measured_by*
  > Three independent annotators are asked to review the source video and evaluate corresponding model outputs (and the human upper bound) on a 1–5 Likert scale for Faithfulness, Relevance, Informativeness, Conciseness, and Coherence (higher scores indicate better quality). (Section 7)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **Response quality** (constructs) — *measured_by*
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
- **Planning** (constructs) — *measured_by*
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  - [TaskBench: Benchmarking Large Language Models for Task Automation](https://proceedings.neurips.cc/paper_files/paper/2024/file/085185ea97db31ae6dcac7497616fd3e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Decision-making** (constructs) — *measured_by*
  - [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks) — *measured_by*
  - [When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Factual accuracy** (constructs) — *measured_by*
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (constructs) — *measured_by*
  > While humans can recognize frames from movies they’ve seen (avg. accuracy 0.19), their accuracy drops sharply (0.02) on unseen titles, highlighting that generalization alone cannot explain the VLMs performance on the same task. (Figure 8).
  - [DIS-CO: Discovering Copyrighted Content in VLMs Training Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duarte25a/duarte25a.pdf)
- **Readability** (constructs) — *measured_by*
  > users rate Readability (Ribeiro et al., 2023) to ensure the extra perspectives do not harm comprehension. (Section 6.3)
  - [tRAG: Term-level Retrieval-Augmented Generation for Domain-Adaptive Retrieval](https://aclanthology.org/2025.naacl-long.335.pdf)
- **Meaning preservation** (constructs) — *measured_by*
  - [VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf)
- **Text generation quality** (constructs) — *measured_by*
  > “we find a similar-sized effect in the opposite direction, suggesting model quality according to humans may have slightly degraded.”
  - [Branch-GAN: Improving Text Generation with (not so) Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/02a92b52670752daf17b53f04f1ab405-Paper-Conference.pdf)
- **Engagement** (constructs) — *measured_by*
  - [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Leftover Lunch: Advantage-based Offline Reinforcement Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3b18d368150474ac6fc9bb665d3eb3da-Paper-Conference.pdf)
- **Coherence** (constructs) — *correlates*
  - [BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *measured_by*
  - [VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25h/zeng25h.pdf)
- **Cultural competence** (constructs) — *measured_by*
  - [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.388.pdf)
- **Usefulness** (constructs) — *measured_by*
  - [TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Plausibility** (constructs) — *measured_by*
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1372.pdf)
- **Data contamination** (constructs) — *measured_by*
  > We undertake a human evaluation, led by two domain experts, to characterize contamination by identifying both exact matches and near-exact matches of individual instances. (Section 4)
  - [Time Travel in LLMs: Tracing Data Contamination in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc39a59c49b731c51398ad6b12f301d3-Paper-Conference.pdf)
- **MuSR** (measurements) — *measured_by*
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
- **Trustworthiness** (constructs) — *measured_by*
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **Sycophancy** (constructs) — *measured_by*
  - [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  - [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Information extraction** (behaviors tasks) — *measured_by*
  > To further verify, a human rater compared 20 Mind2Web trajectories with intent predictions from Gemini Flash 8B, choosing between CoT and Decomposed-FT responses (details in Appendix D). (Section 6.1)
  - [[CLS]](https://aclanthology.org/2025.emnlp-main.1313.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Automated Hypothesis Validation with Agentic Sequential Falsifications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25n/huang25n.pdf)
- **Truthfulness** (constructs) — *measured_by*
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **Novelty** (constructs) — *measured_by*
  > we also assess the intrinsic quality of the generated content. Specifically, we focus on two key dimensions: novelty and feasibility...human evaluation includes results on 40 of them. (Section 10, Table 4)
  - [ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf)
- **Semantic textual similarity** (behaviors tasks) — *measured_by*
  - [SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf)
- **OSWORLD** (measurements) — *measured_by*
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge graph completion** (behaviors tasks) — *measured_by*
  - [UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf)
- **Multimodal alignment** (constructs) — *measured_by*
  - [YouDream: Generating Anatomically Controllable Consistent Text-to-3D Animals](https://proceedings.neurips.cc/paper_files/paper/2024/file/6fe5d7a2de090168917425fe89a6c1b8-Paper-Conference.pdf)
- **Pathfinding** (behaviors tasks) — *measured_by*
  - [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)
- **Image generation** (behaviors tasks) — *measured_by*
  - [Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdcc6d47c1627350014a3076112ab824-Paper-Conference.pdf)
- **Image captioning** (behaviors tasks) — *measured_by*
  - [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf)
- **Video editing** (behaviors tasks) — *measured_by*
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Emotional alignment** (constructs) — *measured_by*
  - [Apathetic or Empathetic? Evaluating LLMs' Emotional Alignments with Humans](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0049c3f9c53fb06f674ae66c2cf2376-Paper-Conference.pdf)
- **Linguistic quality** (constructs) — *measured_by*
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text-to-3D generation** (behaviors tasks) — *measured_by*
  - [YouDream: Generating Anatomically Controllable Consistent Text-to-3D Animals](https://proceedings.neurips.cc/paper_files/paper/2024/file/6fe5d7a2de090168917425fe89a6c1b8-Paper-Conference.pdf)
- **Accuracy** (constructs) — *measured_by*
  - [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.290.pdf)
- **3D question answering** (behaviors tasks) — *measured_by*
  - [MMScan: A Multi-Modal 3D Scene Dataset with Hierarchical Grounded Language Annotations](https://proceedings.neurips.cc/paper_files/paper/2024/file/5aed0d900297bd5593afc14ff452d4a8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Empathy** (constructs) — *measured_by*
  > Expert Evaluation: Five psychologists evaluated responses generated for 100 videos using a 1-to-5 Likert scale (1 = poor, 5 = exceptional). We utilized the same 3 aforementioned criteria. (Section 5)
  - [Controlled Generation for Private Synthetic Text](https://aclanthology.org/2025.emnlp-main.1664.pdf)
- **EHRNoteQA** (measurements) — *correlates*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Realism** (constructs) — *measured_by*
  - [CLAIM: Mitigating Multilingual Object Hallucination in Large Vision-Language Models with Cross-Lingual Attention Intervention](https://aclanthology.org/2025.acl-long.641.pdf)
- **Controllability** (constructs) — *measured_by*
  > We conducted a user preference study with 200 participants to evaluate helpfulness. (Hypothetical example in instructions — NOT in paper)
  - [BRIDGE: Bootstrapping Text to Control Time-Series Generation via Multi-Agent Iterative Optimization and Diffusion Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ah/li25ah.pdf)
- **Explanation quality** (constructs) — *measured_by*
  > we conduct a blind review process where OR experts anonymously score the explanations generated by different methods.
  - [SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model with Transparent Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/beac6bfb7eac3d651307c16ac747df01-Paper-Conference.pdf)
- **Code understanding** (constructs) — *measured_by*
  > To further validate our model’s performance, we have conducted human evaluations, which show that DeepRTL-220m, GPT-4, and o1-preview achieve accuracies of 78%, 72%, and 67%, respectively. (Section 5.2)
  - [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf)
- **Action generation** (behaviors tasks) — *measured_by*
  > To further evaluate our model qualitatively, we conduct a user study on TTR vs. the latest SOTA method ReGenNet, and the results are shown in Figure 7 (Section 4.7).
  - [Think Then React: Towards Unconstrained Action-to-Reaction Motion Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea0b28cbbd0cbc45ec4ac38e92da9cb2-Paper-Conference.pdf)
- **Personalization** (constructs) — *measured_by*
  > “We then ask the participant to rate the extent to which the LLM response is personalized to the given context, Ci.”
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
- **Multilingual ability** (constructs) — *measured_by*
  - [MetaDesigner: Advancing Artistic Typography through AI-Driven, User-Centric, and Multilingual WordArt Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/a10c3d85879c29331ba4d73ede56c7d3-Paper-Conference.pdf)
- **Translation quality** (constructs) — *measured_by*
  > We conduct a manual evaluation to determine whether bilingual human annotators rate translations generated using our winning rewrite method (simplification with TOWER-INSTRUCT) as superior to the original translations. (§5.3)
  - [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.602.pdf)
- **Simplicity** (constructs) — *measured_by*
  > Using a 1-5 Likert scale, the judges are asked to rate the model output based on five criteria: comprehensiveness, layness, meaning preservation, conciseness, and fluency. (Section 5.3.3).
  - [VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf)
- **Insightfulness** (constructs) — *measured_by*
  - [ALiiCE: Evaluating Positional Fine-grained Citation Generation](https://aclanthology.org/2025.naacl-long.24.pdf)
- **Completeness** (constructs) — *measured_by*
  > Each sample was scored on a 0–10 scale for: completeness (whether it covered all clinically relevant considerations), correctness (factual accuracy of reasoning and answers), and logical flow (coherence and structure of the reasoning path). (Section 5.2.1)
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **Code debugging** (behaviors tasks) — *measured_by*
  - [Assessing the State of the Art in Scene Segmentation](https://aclanthology.org/2025.naacl-long.501.pdf)
- **Specificity** (constructs) — *measured_by*
  > Specificity: this aspect measures whether the responses are directly related to the specific issues raised in the question, providing clear and targeted answers rather than generalized responses.
  - [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.290.pdf)
- **Reliability** (constructs) — *measured_by*
  - [Commonsense Reasoning inArab Culture](https://aclanthology.org/2025.acl-long.381.pdf)
- **Reasoning error** (behaviors tasks) — *measured_by*
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.582.pdf)
- **Flawed reasoning** (behaviors tasks) — *measured_by*
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.582.pdf)
- **Coverage** (constructs) — *measured_by*
  > After each conversation, participants rate the model’s responses on a 5-point scale ... across five criteria ...: (4) Coverage: Response comprehensively addresses all components of questions asked, including sub-questions. (Section 3.2.3)
  - [TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Safety awareness** (constructs) — *measured_by*
  > The safeguard rate measures how often UFO requests user confirmation when the request involves sensitive actions. All metrics are assessed through human evaluation. (Section 4.1)
  - [WebQuality: A Large-scale Multi-modal Web Page Quality Assessment Dataset with Multiple Scoring Dimensions](https://aclanthology.org/2025.naacl-long.26.pdf)
- **Actionability** (constructs) — *measured_by*
  > After each conversation, participants rate the model’s responses on a 5-point scale ... across five criteria ...: (3) Actionability: Response provides clear steps or instructions. (Section 3.2.3)
  - [TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Authenticity** (constructs) — *measured_by*
  > The human evaluation encompasses multiple dimensions, namely Readability (Read.), Information Conveyance (Info.), Authenticity (Auth.), and Interestingness (Intr.) (Section 4.1).
  - [tRAG: Term-level Retrieval-Augmented Generation for Domain-Adaptive Retrieval](https://aclanthology.org/2025.naacl-long.335.pdf)
- **Cultural knowledge** (constructs) — *measured_by*
  > For the evaluator M (·) used to compute MES, we utilize GPT-4o (OpenAI et al., 2024) as a simulated evaluator and recruit real human evaluators from Prolific.
  - [Grammar Control in Dialogue Response Generation for Language Learning Chatbots](https://aclanthology.org/2025.naacl-long.496.pdf)
- **Social and emotional intelligence** (constructs) — *measured_by*
  - [PAT: Parameter-Free Audio-Text Aligner to Boost Zero-Shot Audio Classification](https://aclanthology.org/2025.naacl-long.617.pdf)
- **Cultural adaptation** (constructs) — *measured_by*
  - [Inter-sentence Context Modeling and Structure-aware Representation Enhancement for Conversational Sentiment Quadruple Extraction](https://aclanthology.org/2025.emnlp-main.868.pdf)
- **Privacy preservation** (constructs) — *measured_by*
  > We further evaluate the LMs capability in generating private summaries by conducting a human evaluation. (Section 4.5)
  - [FinetuningLLMs for Human Behavior Prediction in Social Science Experiments](https://aclanthology.org/2025.emnlp-main.1531.pdf)
- **Role-playing** (behaviors tasks) — *measured_by*
  - [CoSER: Coordinating LLM-Based Persona Simulation of Established Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dk/wang25dk.pdf)
- **Persuasiveness** (constructs) — *measured_by*
  > For a more comprehensive analysis, we conduct a human evaluation... They follow the same five evaluation dimensions used in the automatic evaluation... (Section 4.2)
  - [Disambiguation in Conversational Question Answering in the Era ofLLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.483.pdf)
- **Emotional resonance** (constructs) — *measured_by*
  - [Inter-sentence Context Modeling and Structure-aware Representation Enhancement for Conversational Sentiment Quadruple Extraction](https://aclanthology.org/2025.emnlp-main.868.pdf)
- **Feasibility** (constructs) — *measured_by*
  - [ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf)
- **Repetitive generation** (behaviors tasks) — *measured_by*
  - [The Impact of Token Granularity on the Predictive Power of Language Model Surprisal](https://aclanthology.org/2025.acl-long.210.pdf)
- **Personalized response generation** (behaviors tasks) — *measured_by*
  > PAChat achieves the best results across all metrics, demonstrating significant improvements in personalized response generation and particularly winning favor with both GPT and human judges. (Section 5.3.1)
  - [Logit Space Constrained Fine-Tuning for Mitigating Hallucinations inLLM-Based Recommender Systems](https://aclanthology.org/2025.emnlp-main.1492.pdf)
- **Meaningfulness** (constructs) — *measured_by*
  > We follow the evaluation protocol from (Veluri et al., 2024) and conduct a human study involving 25 annotators with native-level English proficiency... we use a 5-point Likert scale to evaluate the Naturalness (N-MOS) of turn-taking and the Meaningfulness (M-MOS) of the generated dialogue content.
  - [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf)
- **Interactivity** (constructs) — *measured_by*
  - [CollabLLM: From Passive Responders to Active Collaborators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25i/wu25i.pdf)
- **Compositional reasoning** (constructs) — *measured_by*
  > "Traces were rated to assess references to low-level cues (fine-grained), information cross-referenced across steps (compositional), relevant evidence (comprehensive), correctness of modality tags, and validity of reasoning"
  - [Definition Generation for Word Meaning Modeling: Monolingual, Multilingual, and Cross-Lingual Perspectives](https://aclanthology.org/2025.emnlp-main.1322.pdf)
- **Ambiguity handling** (constructs) — *measured_by*
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **Clinical interpretability** (constructs) — *measured_by*
  > “the clinical interpretability and reliability of the generated responses have not yet been directly assessed through expert review.”
  - [Variance Sensitivity Induces Attention Entropy Collapse and Instability in Transformers](https://aclanthology.org/2025.emnlp-main.422.pdf)
- **Modality bias** (constructs) — *measured_by*
  > "As shown in Figure 9, most predictions are judged as mostly visual with some text"
  - [Evaluating the Evaluators: Are readability metrics good measures of readability?](https://aclanthology.org/2025.emnlp-main.1226.pdf)
- **Textual bias** (constructs) — *measured_by*
  > “Human annotation also verifies that around 80% samples in both datasets are textually biased, which supports our findings.”
  - [Evaluating the Evaluators: Are readability metrics good measures of readability?](https://aclanthology.org/2025.emnlp-main.1226.pdf)
- **Multi-hop reasoning** (constructs) — *measured_by*
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1372.pdf)
- **Meeting summarization** (behaviors tasks) — *measured_by*
  > In meeting summarization, other evaluations have focused on how well summaries capture decision-making content from the meeting (Murray et al., 2009) (Section 5.1).
  - [Frequency & Compositionality in Emergent Communication](https://aclanthology.org/2025.emnlp-main.1388.pdf)

### Associated with
- **LLM-as-a-judge** (measurements)
  > "To ensure the reliability of the G-Eval scores, we conducted a human evaluation... This subset was used to compare the G-Eval scores with human-annotated scores"
  - [OpenDebateEvidence: A Massive-Scale Argument Mining and Summarization Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c630d28df1cff44314d5798f82e02ec-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GAVIE** (measurements)
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  > The user study consists of two parts. In the first part, we ask participants to specify four email-writing tasks (e.g., Write an email to your advisor asking for feedback). (Section 4.2)
  - [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf)
- **FaithEval** (measurements)
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **G-Eval** (measurements)
  - [SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49c1879ae366644ce2c17fb39ddea982-Paper-Conference.pdf)
- **Reward model** (measurements)
  > “we engage four human evaluators to compare responses from two MRPAs on each metric for every question in the validation set.”
  - [MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf)
