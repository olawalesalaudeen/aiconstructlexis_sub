# Helpfulness
**Type:** Construct  
**Referenced in:** 186 papers  
**Also known as:** Perceived helpfulness  

## State of the Field

Helpfulness is a widely studied construct in large language model research, most commonly defined as the quality of an AI assistant's response in being useful, relevant, and satisfying to a user's query. While this framing is prevalent, some work offers more specific definitions, such as simply completing the basic task in an instruction, or a user-centric view of "perceived helpfulness" based on subjective experience. Across the surveyed literature, helpfulness is consistently treated as a central objective of human preference and safety alignment, frequently studied alongside and sometimes in tension with Harmlessness. It is also commonly associated with constructs like honesty and truthfulness. The construct is most frequently operationalized through evaluation by both automated and human judges, with the use of LLM-as-a-judge, particularly GPT-4, being a widespread practice. To elicit and score helpfulness, researchers commonly employ preference datasets, with the helpfulness-focused subsets of Anthropic HHH and PKU-SafeRLHF being popular choices. Additionally, benchmarks such as MT-Bench, AlpacaEval 2.0, and Arena-Hard are frequently used to assess this construct. A smaller line of work highlights its subjective nature, especially for personal advice, where one study notes it is associated with empathy, actionability, and creativity.

## Sources

**[Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)**
> The quality of an AI assistant's responses in being useful, relevant, and satisfying to a user's query or instruction.

**[Benchmarking Complex Instruction-Following with Multiple Constraints Composition](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8c24b08b96a08ec7a7a975feea7777e-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Supportiveness")**
> The degree to which a response remains faithful to the input instruction or source text.

**[Learning from Few Samples: A Novel Approach for High-Quality Malcode Generation](https://aclanthology.org/2025.emnlp-main.71.pdf) (as "Perceived helpfulness")**
> The extent to which a user feels an LLM effectively supports their specific needs and goals during a collaborative interaction.

## Relationships

### Helpfulness →
- **LLM-as-a-judge** (measurements) — *measured_by*
  > "We use GPT-4o to assess its safety (prioritized) and quality."
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
- **Anthropic HHH** (measurements) — *measured_by*
  > For HH-RLHF, we assess our model on helpfulness and harmlessness using GPT-4-1106-preview as an initial evaluator (Zheng et al., 2024), with human annotators providing a final verification for precise results, following (Chen et al., 2023b) and (Dai et al., 2023).
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > Human judges were tasked in the first stage with selecting the more Helpful, Honest, and Harmless response between 100 pairs without access to the LLM’s rationale. (Section 5.3)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **UltraFeedback** (measurements) — *measured_by*
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **PKU-SafeRLHF** (measurements) — *measured_by*
  > "Experimental results on the HH-RLHF and PKU-SafeRLHF datasets, evaluated using both automatic metrics and human judgments"
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
- **Arena-Hard** (measurements) — *measured_by*
  > we use three metrics to measure aligned models’ ability to be helpful in responding to user prompts: GPT-4-Turbo MT Bench (Zheng et al., 2023), AlpacaEval 2.0 Length Controlled (Dubois et al., 2024) and Arena Hard (Li et al., 2024).
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  > Helpfulness is measured using AlpacaEval 2.0 (Alpaca) (Dubois et al., 2024a; Li et al., 2023; Dubois et al., 2024b).
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
- **Anthropic HH (RLHF)** (measurements) — *measured_by*
  - [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf)
- **Beavertails** (measurements) — *measured_by*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Just-Eval** (measurements) — *measured_by*
  > In addition, we evaluate the helpfulness of the output on Just-Eval (Lin et al., 2023) from the aspects of helpfulness, clarity, factuality, depth, and engagement. (Section 5.1)
  - [From Sub-Ability Diagnosis to Human-Aligned Generation: Bridging the Gap for Text Length Control viaMarkerGen](https://aclanthology.org/2025.acl-long.851.pdf)
- **AlpacaEval 2.0 Length Controlled** (measurements) — *measured_by*
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **PKU-SafeRLHF-10K** (measurements) — *measured_by*
  > the PKU-SafeRLHF-10K dataset (Ji et al., 2023; Dai et al., 2024), which contains human-labeled preference data on the helpfulness and harmlessness of prompt-response pairs (Section 6.4)
  - [A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf)
- **ArmoRM** (measurements) — *measured_by*
  > For the evaluation of 'harmless', 'helpful', and 'humor' dimensions... Additionally, we employ the ArmoRM (Wang et al., 2024b), a multi-dimension reward model... For these reward models, we report their scores assessing LLM responses from various perspectives.
  - [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)
- **Safe-RLHF** (measurements) — *measured_by*
  - [PromptRefine: Enhancing Few-Shot Performance on Low-ResourceIndic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.18.pdf)
- **MMLU** (measurements) — *measured_by*
  > We also assess the helpfulness of the targeted LLMs... To do this, we select 500 examples from three sources: ...MMLU (knowledge tests)... (Section 4.1)
  - [A-TASC:AsianTED-Based Automatic Subtitling Corpus](https://aclanthology.org/2025.acl-long.158.pdf)
- **GPT-4 Head-to-head Comparison** (measurements) — *measured_by*
  - [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf)
- **AlpacaFarm** (measurements) — *measured_by*
  - [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  > we evaluate the impact of safety heads ablation on helpfulness. We use lm-eval (Gao et al., 2024) to assess model performance after ablating safety heads of Llama-2-7b-chat on zero-shot tasks... (Section 5.3)
  - [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf)
- **HelpSteer** (measurements) — *measured_by*
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
- **AUTO-J** (measurements) — *measured_by*
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-DeviceLLM](https://aclanthology.org/2025.emnlp-main.534.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
- **Verbosity** (constructs) — *correlates*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **HelpSteer2** (measurements) — *measured_by*
  - [LORAXBENCH: A Multitask, Multilingual Benchmark Suite for 20Indonesian Languages](https://aclanthology.org/2025.emnlp-main.882.pdf)
- **Pairwise comparison** (behaviors tasks) — *measured_by*
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MME** (measurements) — *measured_by*
  > “For multimodal helpfulness benchmarks, we use MMBench (Liu et al., 2023d), MME (Fu et al., 2024), and SEEDBench (Li et al., 2023a).”
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  > “We tested the models on the following benchmarks: • TRIVIAQA (Joshi et al., 2017): Assesses the model’s question-answering capability.”
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > “• HELLASWAG (Zellers et al., 2019): Measures how well the model can generate the most natural continuation from four candidate sentences following a given sentence fragment.”
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
- **IFEval** (measurements) — *measured_by*
  > Our experiments focus on Helpfulness (Alpaca Eval 2.0 (Dubois et al., 2024) and IFEval (Zhou et al., 2023)), Harmlessness (Toxigen (Hartvigsen et al., 2022)), and Coding (MBPP (Austin et al., 2021), HumanEval (Chen et al., 2021)). (Section 4)
  - [DialUp! Modeling the Language Continuum by Adapting Models to Dialects and Dialects to Models](https://aclanthology.org/2025.acl-long.990.pdf)
- **LLaVA-Bench-in-the-Wild** (measurements) — *measured_by*
  > LLaVA-Bench-in-the-Wild (Liu et al., 2024), which examines the helpfulness of VLMs in aspects like instruction following and complex reasoning (Section 5.2)
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
- **GPQA** (measurements) — *measured_by*
  > Safety and helpfulness results for different fine-tuning strategies across three LLMs. ... higher helpfulness values reflect better benchmark performance. (Table 2 Caption)
  - [TokenSelect: Efficient Long-Context Inference and Length Extrapolation forLLMs via Dynamic Token-LevelKVCache Selection](https://aclanthology.org/2025.emnlp-main.1080.pdf)
- **MORBENCH** (measurements) — *measured_by*
  > We have explored the safety decision boundaries of various LLMs and construct the MORBENCH evaluation set to facilitate robust assessment of model safety and helpfulness across multiple languages. (Abstract)
  - [‘Rich Dad, Poor Lad’: How do Large Language Models Contextualize Socioeconomic Factors in College Admission ?](https://aclanthology.org/2025.emnlp-main.1065.pdf)
- **PLLuM-Align** (measurements) — *measured_by*
  > For scalar multi-attribute rating, annotators evaluated each response on a 5-point Likert scale across seven criteria: i) truthfulness, (ii) linguistic correctness, (iii) safety, (iv) fairness, (v) conciseness, (vi) coherence & reasoning, as well as vii) helpfulness & instruction-following.
  - [REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### → Helpfulness
- **Adaptability** (constructs) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **Alignment** (constructs) — *causes*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Anthropic HH (RLHF)** (measurements) — *measured_by*
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks) — *causes*
  - [Towards Transferable Personality Representation Learning based on Triplet Comparisons and Its Applications](https://aclanthology.org/2025.emnlp-main.510.pdf)
- **Safety alignment** (constructs) — *causes*
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
- **Coherence** (constructs) — *correlates*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Faithfulness** (constructs) — *correlates*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Complexity** (constructs) — *correlates*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmlessness** (constructs) — *correlates*
  - [PromptRefine: Enhancing Few-Shot Performance on Low-ResourceIndic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.18.pdf)

### Associated with
- **Harmlessness** (constructs)
  - [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  > "our method uses weak model supervision for alignment to enhance helpfulness while maintaining the strong model’s original ability."
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Safety alignment** (constructs)
  > “Ideally, by training on decentralized data that is aligned with human preferences and safety principles, federated instruction tuning (FedIT) can result in an LLM that could behave helpfully and safely.”
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Alignment** (constructs)
  - [BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling](https://proceedings.neurips.cc/paper_files/paper/2024/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks)
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
- **Helpful response generation** (behaviors tasks)
  - [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness inLLMAgents](https://aclanthology.org/2025.naacl-long.596.pdf)
- **Factuality** (constructs)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Accuracy** (constructs)
  - [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf)
- **Humor understanding** (constructs)
  > In practice, human preferences are multi-dimensional and we often need to align LLMs to balance multiple, sometimes conflicting, preference dimensions such as helpfulness, harmlessness, and humor (Section 2. Related Work)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
- **Empathy** (constructs)
  > Wang and Torres (2022) collected helpful and unhelpful advice from Reddit and analyzed that the main factor is ‘empathy’, consistent with our findings in Figure 4. (Section 2)
  - [TRANSIENTTABLES: EvaluatingLLMs’ Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.333.pdf)
- **Actionability** (constructs)
  > Figure 4: Analysis results of the primary value of evaluation metric: ... the PL model prioritizes Empathy, Actionability, and Creativity. Being trained on the threads of AdvisorQA, the PL model reflects the Reddit forum’s source, valuing advice that resonates empathetically with the given situation, is actionable, and creative, as preferred by the majority. (Section 4.1)
  - [TRANSIENTTABLES: EvaluatingLLMs’ Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.333.pdf)
- **Creativity** (constructs)
  > Figure 4: Analysis results of the primary value of evaluation metric: ... the PL model prioritizes Empathy, Actionability, and Creativity. Being trained on the threads of AdvisorQA, the PL model reflects the Reddit forum’s source, valuing advice that resonates empathetically with the given situation, is actionable, and creative, as preferred by the majority. (Section 4.1)
  - [TRANSIENTTABLES: EvaluatingLLMs’ Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.333.pdf)
- **ETHICS** (measurements)
  - [TRANSIENTTABLES: EvaluatingLLMs’ Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.333.pdf)
