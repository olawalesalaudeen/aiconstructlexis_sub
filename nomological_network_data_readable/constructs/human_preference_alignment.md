# Human preference alignment
**Type:** Construct  
**Referenced in:** 170 papers  
**Also known as:** Alignment with human preferences, General alignment, User Alignment, Preference alignment, Distributional preference alignment, Human-predictor alignment, Human value alignment, User alignment, Human preferences, Human alignment, Preference following, Preference inference, Alignment with human judgments, Alignment with human population, Human-AI alignment, Ethical values, Value alignment, Value conformity, Moral alignment, Value consistency, Value orientation, Alignment preferences, QA alignment, Personalized preference alignment, Alignment with physician preferences, Personal preference alignment, Value priorities, Implicit values, Alignment with human preference  

## State of the Field

Across the surveyed literature, human preference alignment is most commonly characterized as the degree to which a language model's outputs conform to human values, intentions, and preferences, often encompassing qualities such as helpfulness and harmlessness. While this broad framing is prevalent, a number of papers adopt more specific definitions, focusing on alignment with ethical or moral principles, conformity to the preferences of specific user or demographic groups, or a model's latent ability to infer and follow personalized instructions. The construct is most frequently operationalized and measured through performance on automated benchmarks, with AlpacaEval 2.0, Arena-Hard, and MT-Bench being the most common instruments cited in the provided data. Other measurement approaches include direct human evaluation, LLM-as-a-judge frameworks, and performance on datasets like Anthropic HHH and OASST1. Human preference alignment is reported to influence several desirable behaviors, with some studies stating it causes improved helpfulness, harmlessness, and faithfulness. Conversely, it is also studied in relation to challenges like reward hacking and jailbreaking, and at least one paper reports that alignment processes can increase social bias, highlighting a complex trade-off. The source snippets frequently mention that this alignment is achieved through training techniques like Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO).

## Sources

**[ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf) (as "Alignment with human preferences")**
> The degree to which a model's outputs reflect the qualities preferred by humans, such as being helpful and harmless, learned implicitly through training on preference data rather than explicit instruction.

**[Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf)**
> The degree to which a large language model's behaviors and outputs conform to human values and intentions.

**[SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf) (as "General alignment")**
> The extent to which an LLM's outputs conform to human intentions and broadly desirable assistant behavior across tasks.

**[FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf) (as "User Alignment")**
> The ability to empathize with the user and align responses to their intentions, preferences, and expectations in terms of conciseness, readability, and safety.

**[SaulLM-54B & SaulLM-141B: Scaling Up Domain Adaptation for the Legal Domain](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea3f85a33f9ba072058e3df233cf6cca-Paper-Conference.pdf) (as "Preference alignment")**
> The degree to which model outputs conform to human or model-derived preferences for desirable responses.

**[VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/acbfe708197ff78ad04cc1beb1710979-Paper-Conference.pdf) (as "User alignment")**
> The degree to which a vibe is predictive of or correlates with human preferences for model outputs.

**[No Preference Left Behind: Group Distributional Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/b57b9aafccf6bf6a76d01079e316e14d-Paper-Conference.pdf) (as "Distributional preference alignment")**
> The model's capability to learn from and generate outputs that reflect the statistical distribution of preferences within a specific group.

**[Eliciting Human Preferences with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf) (as "Human preferences")**
> The user's latent desired criteria for how a model should behave or make decisions in a context-dependent task.

**[Eliciting Human Preferences with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf) (as "Human-predictor alignment")**
> The degree to which a model's behavior and predictions correspond to a human user's desired behavior and true preferences.

**[MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf) (as "Human value alignment")**
> The process of adjusting an AI system's behavior to be consistent with specified human values and preferences.

**[Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/28a46044775d97a4efcbcf14e7f13209-Paper-Conference.pdf) (as "Preference following")**
> The latent ability of a model to infer, memorize, and generate responses that adhere to user preferences expressed over a long-context conversation.

**[Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/28a46044775d97a4efcbcf14e7f13209-Paper-Conference.pdf) (as "Preference inference")**
> The latent ability to infer a user's preferences from explicit statements or indirect conversational evidence.

**[Seeing Eye to AI: Human Alignment via Gaze-Based Response Rewards for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4165875c8140617b8c165e18c342ccbb-Paper-Conference.pdf) (as "Human alignment")**
> The degree to which a large language model's outputs and behaviors conform to human expectations, values, and intentions.

**[CU-MAM: Coherence-Driven Unified Macro-Structures for Argument Mining](https://aclanthology.org/2025.acl-long.970.pdf) (as "Alignment with human judgments")**
> The degree to which an LLM judge's safety evaluations match the majority decisions of human annotators on the same content.

**[Uncertainty Quantification for LLM-Based Survey Simulations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25am/huang25am.pdf) (as "Alignment with human population")**
> The degree to which the distribution of an LLM's simulated responses matches the distribution of responses from a real human population.

**[Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://raw.githubusercontent.com/mlresearch/v267/main/assets/badawi25a/badawi25a.pdf) (as "Human-AI alignment")**
> The degree to which an LLM's outputs and behavior remain aligned with human expertise, therapeutic goals, and human-centered care norms.

**[Large Language Models as Automated Aligners for  benchmarking  Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf) (as "Value alignment")**
> The tendency of a model's responses to conform to high-level human quality guidelines such as being helpful, honest, and harmless.

**[DENEVIL: TOWARDS DECIPHERING AND NAVIGATING THE ETHICAL VALUES OF LARGE LANGUAGE MODELS VIA INSTRUCTION LEARNING](https://proceedings.iclr.cc/paper_files/paper/2024/file/efe406d6d2674d176cdcd958ce605d17-Paper-Conference.pdf) (as "Ethical values")**
> The latent moral orientation of an LLM as reflected in whether its outputs conform to or violate value principles across scenarios.

**[DENEVIL: TOWARDS DECIPHERING AND NAVIGATING THE ETHICAL VALUES OF LARGE LANGUAGE MODELS VIA INSTRUCTION LEARNING](https://proceedings.iclr.cc/paper_files/paper/2024/file/efe406d6d2674d176cdcd958ce605d17-Paper-Conference.pdf) (as "Value conformity")**
> The degree to which an LLM's generated behaviors adhere to specified ethical principles or values.

**[Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf) (as "Ethical alignment")**
> The extent to which a model's responses conform to ethical preferences or norms expected in a given setting.

**[Language Model Alignment in Multilingual Trolley Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f32be3e112e151707cb12528bdfa7d5-Paper-Conference.pdf) (as "Moral alignment")**
> The degree to which an LLM's preferences in moral dilemmas correspond to aggregated human preferences.

**[MAGNET: Augmenting Generative Decoders with Representation Learning and Infilling Capabilities](https://aclanthology.org/2025.acl-long.1326.pdf) (as "Value consistency")**
> The extent to which a model maintains adherence to a target value even when prompted with opposing or conflicting guidance.

**[Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.84.pdf) (as "Alignment")**
> The extent to which an LLM's responses adhere to ethical norms and reject harmful or biased content, especially when prompted to engage with or continue from a biased conversational context.

**[QFrCoLA: aQuebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.7.pdf) (as "Value orientation")**
> The latent disposition of an LLM reflecting its preference for certain human values (e.g., individualism, family importance) that shape its responses and decisions across contexts.

**[Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1471.pdf) (as "Alignment preferences")**
> A model's underlying tendencies in expressing views on topics involving human values, political leanings, and moral situations.

**[LeTS: Learning to Think-and-Search via Process-and-Outcome Reward Hybridization](https://aclanthology.org/2025.emnlp-main.258.pdf) (as "QA alignment")**
> The semantic relevance and coherence between a generated question and its corresponding answer in a synthetic data pair.

**[DrDiff: Dynamic Routing Diffusion with Hierarchical Attention for Breaking the Efficiency-Quality Trade-off](https://aclanthology.org/2025.emnlp-main.475.pdf) (as "Personalized preference alignment")**
> The latent ability of a model to tailor its outputs to conform to the specific, individual preferences of a particular user.

**[Women, Infamous, and Exotic Beings: A Comparative Study of Honorific Usages inWikipedia andLLMs forBengali andHindi](https://aclanthology.org/2025.emnlp-main.967.pdf) (as "Alignment with physician preferences")**
> The degree to which a model's outputs match the subjective preferences of physicians regarding clinical note quality, beyond mere factual correctness.

**[2025.emnlp-main.1723.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1723.checklist.pdf) (as "Personal preference alignment")**
> The latent ability of an LLM to generate outputs that reflect individual user preferences, inferred from comparative response evaluations.

**[2025.emnlp-main.806.checklist](https://aclanthology.org/attachments/2025.emnlp-main.806.checklist.pdf) (as "Value priorities")**
> The underlying set of ethical or moral principles that an LLM uses to make judgments in complex situations.

**[AdvancingArabic Diacritization: Improved Datasets, Benchmarking, and State-of-the-Art Models](https://aclanthology.org/2025.emnlp-main.847.pdf) (as "Implicit values")**
> Fundamental principles that guide decision-making in a given context, even when not explicitly stated in the task, reflecting culturally situated preferences such as environmentalism, diversity, or community.

**[Energy-Based Preference Model Offers Better Offline Alignment than the Bradley-Terry Preference Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25i/hong25i.pdf) (as "Alignment with human preference")**
> The degree to which a language model's outputs conform to human judgments of quality, desirability, or correctness, as inferred from preference data.

## Relationships

### Human preference alignment →
- **MT-Bench** (measurements) — *measured_by*
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  > “Extensive experiments on widely used real-world benchmarks, including MT-Bench, AlpacaEval 2, and 10 key benchmarks of the Open LLM Leaderboard”
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Arena-Hard** (measurements) — *measured_by*
  > "We evaluate our method by AlpacaEval 2 (Li et al., 2023b) and Arena-Hard (Li et al., 2024)."
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > For HH-RLHF, we randomly select 200 samples from the test set to evaluate ICDPO, ICDPO+ ˆS, and all baselines except Zero-shot... Their decoded responses are compared with the chosen ones in HH-RLHF to compute the win/tie/lose rates. (Section 4.2.2)
  - [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf)
- **AlpacaEval 2** (measurements) — *measured_by*
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **LMSYS Chatbot Arena** (measurements) — *measured_by*
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
- **Instruction following** (constructs) — *causes*
  - [Reward-Augmented Data Enhances Direct Preference Alignment of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25az/zhang25az.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > "We employ the HH-RLHF (Bai et al., 2022) and AlpacaEval (Li et al., 2023b) to comprehensively assess the effectiveness of ICDPO, as well as different ways of evaluation (reward model (RM) evaluation for HH-RLHF; GPT-4 evaluation for HH-RLHF and AlpacaEval)"
  - [CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases](https://aclanthology.org/2025.naacl-long.8.pdf)
- **Anthropic HHH** (measurements) — *measured_by*
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
- **Reward model** (measurements) — *measured_by*
  - [NICE Data Selection for Instruction Tuning in LLMs with Non-differentiable Evaluation Metric](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bm/wang25bm.pdf)
- **Anthropic HH (RLHF)** (measurements) — *measured_by*
  - [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf)
- **Truthfulness** (constructs) — *causes*
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Ethical reasoning** (constructs) — *causes*
  > RLHF applied to a general-purpose preference dataset leads to a substantial average improvement of 31% on the machine ethics benchmark. (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Social bias** (constructs) — *causes*
  > the effects on other trustworthiness aspects are negative: stereotypical bias increases by 150%... (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements) — *measured_by*
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Professionalism** (constructs) — *causes*
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
- **Readability** (constructs) — *causes*
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
- **OASST1** (measurements) — *measured_by*
  > OASST1 is a human-generated, human-annotated, assistant-style conversation, created through global crowdsourcing and widely used for human alignment tasks (K¨opf et al., 2023; Dettmers et al., 2023; Wu et al., 2024b).
  - [Seeing Eye to AI: Human Alignment via Gaze-Based Response Rewards for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4165875c8140617b8c165e18c342ccbb-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences inLLMReasoning](https://aclanthology.org/2025.emnlp-main.1046.pdf)
- **Arena-Hard-Auto** (measurements) — *measured_by*
  > Thus we adopt MT-Bench (Zheng et al., 2023), AlpacaEval (Li et al., 2023b), and Arena-Hard-Auto (Li et al., 2024b) to evaluate human preference to models’ generations. (Section 3.2)
  - [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.52.pdf)
- **WildVision** (measurements) — *measured_by*
  - [Can Large Language Models Detect Errors in Long Chain-of-Thought Reasoning?](https://aclanthology.org/2025.acl-long.906.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [PIPA: Preference Alignment as Prior-Informed Statistical Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cl/li25cl.pdf)
- **MATH** (measurements) — *measured_by*
  > “Both algorithms demonstrate a 3 ∼10% performance enhancement on the GSM8K and MATH benchmarks across all configurations”
  - [PIPA: Preference Alignment as Prior-Informed Statistical Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cl/li25cl.pdf)
- **World Values Survey** (measurements) — *measured_by*
  - [QFrCoLA: aQuebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.7.pdf)
- **Value Kaleidoscope** (measurements) — *measured_by*
  - [Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1471.pdf)

### → Human preference alignment
- **LMSYS Chatbot Arena** (measurements) — *measured_by*
  - [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf)
- **Reward modeling** (constructs) — *causes*
  > By leveraging the evolved reward model’s nuanced signals, the LLM’s policy updates align better with subtle distinctions in response quality. (Section 3, STEP 4)
  - [SELF-EVOLVED REWARD LEARNING FOR LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/26f5a4e26c13d1e0a47f46790c999361-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *correlates*
  - [Exploiting Contextual Knowledge inLLMs through𝒱-usable Information based Layer Enhancement](https://aclanthology.org/2025.acl-long.1532.pdf)

### Associated with
- **Harmlessness** (constructs)
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
- **Helpfulness** (constructs)
  > "our method uses weak model supervision for alignment to enhance helpfulness while maintaining the strong model’s original ability."
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
- **Readability** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Conciseness** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Alignment** (constructs)
  - [AdvancingArabic Diacritization: Improved Datasets, Benchmarking, and State-of-the-Art Models](https://aclanthology.org/2025.emnlp-main.847.pdf)
- **Refusal to answer** (behaviors tasks)
  - [Large Language Models as Automated Aligners for  benchmarking  Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf)
- **Trustworthiness** (constructs)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Theory of mind** (constructs)
  - [Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation](https://proceedings.neurips.cc/paper_files/paper/2024/file/984dd3db213db2d1454a163b65b84d08-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Verbosity** (constructs)
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **Mode-seeking behavior** (constructs)
  > “SimPER also theoretically promotes mode-seeking behavior by optimizing the Total Variation distance (TVD) between the model distribution πθ and the distribution of chosen response.”
  - [SimPER: A Minimalist Approach to Preference  Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  > “To perform well on our benchmark, LLMs should demonstrate four key capabilities: (1) Preference Inference—the capacity to accurately infer user preferences through dialogue, whether explicitly stated or implicitly revealed; (2) Long-Context Retrieval—the ability to track and recall user preferences across long conversation”
  - [Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/28a46044775d97a4efcbcf14e7f13209-Paper-Conference.pdf)
- **Truthfulness** (constructs)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Consistency** (constructs)
  - [Direct Density Ratio Optimization: A Statistically Consistent Approach to Aligning Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/higuchi25a/higuchi25a.pdf)
- **Interlocutor awareness** (constructs)
  - [Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1471.pdf)
