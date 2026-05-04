# Harmful content generation
**Type:** Behavior  
**Referenced in:** 215 papers  
**Also known as:** Toxic content generation, Vulnerable code generation, Unsafe text generation, Stereotypical content generation, Biased response generation, Gaslighting response generation, Harmful knowledge generation, Harmful language generation, Harmful response generation, Jailbreak response generation, Unsafe response generation, Membership inference, PII extraction, Biased generation, Copyrighted text generation, Harmful-yet-helpful response generation, Semantic sensitive information generation, Unsafe generation, Full request leakage, Specific PII leakage, Training data extraction, Harmful instruction generation, Toxic language generation, Toxic text generation, Biased content generation, Insecure code generation, Malicious review generation, Unsafe output generation, Unsafe behavior, Harmful text generation, Malicious response generation, Phishing email generation, Toxic response generation, Compliance with malicious requests, Offensive language generation, Inappropriate content incorporation, Biased output generation  

## State of the Field

The prevailing usage of "harmful content generation" across the surveyed literature describes the observable production of toxic, offensive, illegal, or policy-violating text. This broad concept is specified in numerous ways, encompassing the generation of biased content, insecure code, and misinformation, as well as the leakage of private data like PII or copyrighted text. This behavior is most frequently studied as an outcome of `Jailbreaking` and `Adversarial attacks`, which are consistently described as methods for circumventing a model's safety training; some work also links it to `Misalignment`. To operationalize and measure this behavior, researchers commonly use benchmarks like `AdvBench`, `Beavertails`, `ToxiGen`, and `Real-Toxicity-Prompts` to elicit and evaluate outputs. The resulting text is then frequently scored using automated tools like the `Perspective API` and safety classifiers such as `Llama Guard`, or evaluated using the `LLM-as-a-judge` paradigm. The generation of harmful content is consistently positioned as a failure of `Safety alignment`, the process intended to suppress such outputs.

## Sources

**[AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f83cb637e159e789f5576ff6848874de-Paper-Conference.pdf)**
> The production of toxic, offensive, or otherwise damaging content by a language model, which alignment methods aim to suppress.

**[Apathetic or Empathetic? Evaluating LLMs' Emotional Alignments with Humans](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0049c3f9c53fb06f674ae66c2cf2376-Paper-Conference.pdf) (as "Toxic content generation")**
> Producing responses that are considered toxic or aggressive in demographic-description prompts.

**[Exploiting LLM Quantization](https://proceedings.neurips.cc/paper_files/paper/2024/file/496720b3c860111b95ac8634349dcc88-Paper-Conference.pdf) (as "Vulnerable code generation")**
> The act of producing source code that contains security flaws or vulnerabilities.

**[Optimistic Verifiable Training by Controlling Hardware Nondeterminism](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad885a9caafff30ee9cafdf0ee42fda2-Paper-Conference.pdf) (as "Unsafe text generation")**
> The observable model behavior of producing harmful, undesirable, or toxic content, often as a result of data poisoning.

**[MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Stereotypical content generation")**
> The behavior of producing content that reflects oversimplified or prejudiced generalizations about groups of people.

**[FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf) (as "Biased response generation")**
> The observable production of outputs containing stereotypes, toxicity, or discrimination.

**[ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf) (as "Unsafe response generation")**
> The observable output of harmful or unsafe content by the model in response to malicious queries.

**[Can a Large Language Model be a Gaslighter?](https://proceedings.iclr.cc/paper_files/paper/2025/file/0769598fdeb4f23ee86fec1bc0777f44-Paper-Conference.pdf) (as "Gaslighting response generation")**
> Producing assistant replies that subtly manipulate a user's beliefs, self-doubt, or self-perception in a conversation.

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf) (as "Harmful response generation")**
> Producing unsafe, harmful, sensitive, or false content in response to malicious prompts.

**[Injecting Universal Jailbreak Backdoors into LLMs in Minutes](https://proceedings.iclr.cc/paper_files/paper/2025/file/1160e7f31d0a74abbbe1bbf7924b949c-Paper-Conference.pdf) (as "Jailbreak response generation")**
> Producing instruction-following responses to harmful or restricted prompts when a backdoor trigger is activated.

**[Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf) (as "Harmful language generation")**
> The generation of text that is toxic, biased, or otherwise harmful.

**[Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/18fd48d9cbbf9a20e434c9d3db6973c5-Paper-Conference.pdf) (as "Harmful knowledge generation")**
> The observable model behavior of producing text containing dangerous, undesirable, or hazardous information, such as biosecurity threats.

**[DocMIA: Document-Level Membership Inference Attacks against DocVQA Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/231a8daf4f64935d0c7c6586f290b24f-Paper-Conference.pdf) (as "Membership inference")**
> The observable phenomenon where a model's outputs or internal states can be analyzed to determine if a specific data point was part of its training set.

**[Backtracking Improves Generation Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/65beb73449888fabcf601b3a3ef4b3a7-Paper-Conference.pdf) (as "Unsafe generation")**
> The observable production of harmful, malicious, or policy-violating text in response to a prompt.

**[LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf) (as "Copyrighted text generation")**
> Generating passages that overlap with or resemble copyrighted source text given a prefix from that text.

**[Failures to Find Transferable Image Jailbreaks Between Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e3daaeca6be8579573f69082b2dd58b-Paper-Conference.pdf) (as "Harmful-yet-helpful response generation")**
> Producing outputs that are both harmful and instrumentally useful to a user's malicious goal.

**[A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf) (as "Repetitive generation")**
> An output pattern characterized by the meaningless repetition of tokens or phrases, indicating a degradation in generation quality.

**[Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf) (as "PII extraction")**
> The observable act of a model generating personally identifiable information, such as phone numbers or physical addresses, in response to prompts.

**[A Benchmark for Semantic Sensitive Information in LLMs Outputs](https://proceedings.iclr.cc/paper_files/paper/2025/file/994a53df880f1ec64fd5cbf1bba4a8af-Paper-Conference.pdf) (as "Semantic sensitive information generation")**
> The observable act of an LLM producing text that contains semantic sensitive information, particularly in response to simple, non-adversarial prompts.

**[Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf) (as "Biased generation")**
> The observable production of outputs that reflect systematic or unfair prejudice.

**[EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf) (as "Specific PII leakage")**
> Causing the agent to enter a user’s specific sensitive field value into an injected malicious element instead of the intended target field.

**[EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf) (as "Full request leakage")**
> Causing the agent to reveal the entire task request, including sensitive details beyond a single PII field.

**[HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf) (as "Harmful instruction generation")**
> The observable behavior of an LLM producing prompts or instructions that are designed to elicit harmful, offensive, or malicious responses from another model.

**[Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf) (as "Toxic text generation")**
> Producing continuations or outputs that contain harmful, offensive, or unsafe language when prompted.

**[Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf) (as "Training data extraction")**
> The observable act of a model generating verbatim sequences of text from its training data in response to user prompts.

**[Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf) (as "Toxic language generation")**
> The observable act of a language model producing text that is considered toxic, harmful, or offensive.

**[Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/betley25a/betley25a.pdf) (as "Insecure code generation")**
> Producing code that contains security vulnerabilities such as SQL injection or improper file permissions, without disclosing the risks.

**[Learning Safety Constraints for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25b/chen25b.pdf) (as "Unsafe output generation")**
> The model produces content that violates ethical or safety norms, such as generating harmful, illegal, or deceptive text in response to adversarial prompts.

**[Online Detection of LLM-Generated Texts via Sequential Hypothesis Testing by Betting](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bn/chen25bn.pdf) (as "Fake news generation")**
> Producing fabricated news articles with an LLM.

**[Online Detection of LLM-Generated Texts via Sequential Hypothesis Testing by Betting](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bn/chen25bn.pdf) (as "Misinformation generation")**
> Producing misleading or false content with an LLM.

**[Online Detection of LLM-Generated Texts via Sequential Hypothesis Testing by Betting](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bn/chen25bn.pdf) (as "Malicious review generation")**
> The creation of fake or deceptive product or service reviews.

**[PoisonBench: Assessing Language Model Vulnerability to Poisoned Preference Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25e/fu25e.pdf) (as "Biased content generation")**
> The production of text that reflects unfair prejudice or stereotypes towards certain groups or ideas.

**[SafeArena: Evaluating the Safety of Autonomous Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tur25a/tur25a.pdf) (as "Compliance with malicious requests")**
> The observable tendency of an agent to follow and execute instructions that are explicitly harmful or malicious.

**[Backdoor Attacks in Token Selection of Attention Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25c/wang25c.pdf) (as "Malicious response generation")**
> The model produces harmful, unsafe, or otherwise undesirable text as a result of an adversarial trigger.

**[LLMScan: Causal Scan for LLM Misbehavior Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25al/zhang25al.pdf) (as "Toxic response generation")**
> The observable production of insulting, offensive, or aggressive language by an LLM in response to certain inputs.

**[UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf) (as "Phishing email generation")**
> The production of deceptive emails designed to extract sensitive information, which the agent may be induced to write and send under adversarial prompting.

**[MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf) (as "Unsafe behavior")**
> The model's generation of outputs that are harmful, biased, unethical, or otherwise violate safety guidelines.

**[Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf) (as "Harmful text generation")**
> The observable output of text that is unethical, biased, dangerous, or otherwise violates safety guidelines.

**[Amulet: Putting Complex Multi-Turn Conversations on the Stand withLLMJuries](https://aclanthology.org/2025.emnlp-main.1301.pdf) (as "Offensive language generation")**
> The observable, unintended behavior of producing text that is flagged as offensive, such as harassment or violent content.

**[VERITAS: Leveraging Vision Priors and Expert Fusion to Improve Multimodal Data](https://aclanthology.org/2025.emnlp-main.1003.pdf) (as "Inappropriate content incorporation")**
> The observable phenomenon where an LLM includes harmful or irrelevant information—such as fake news, hate speech, or privacy violations—into its generated response despite the presence of accurate context.

**[Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1453.pdf) (as "Biased output generation")**
> The observable phenomenon of the model producing outputs that are skewed, prejudiced, or unfair, identified as a potential risk in role-playing scenarios.

## Relationships

### Harmful content generation →
- **Perspective API** (measurements) — *measured_by*
  > For toxicity evaluation, we utilize the PERSPECTIVE API (Lees et al., 2022) for REALTOXICITYPROMPTS and the ToxiGen RoBERTa model for the ToxiGen benchmark, both designed to measure the generation of toxic content.
  - [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf)
- **AdvBench** (measurements) — *measured_by*
  - [Jailbreaking Large Language Models Against Moderation Guardrails via Cipher Characters](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d56bc83ae9a4fafdce050bb36f04174-Paper-Conference.pdf)
- **RealToxicityPrompts** (measurements) — *measured_by*
  > Existing approaches mostly rely on static benchmarks, e.g., REALTOXICITYPROMPTS (Gehman et al., 2020) and HARM-BENCH (Mazeika et al., 2024) targeting harmfulness... (Introduction)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **ToxiGen** (measurements) — *measured_by*
  > We evaluate the effect of detoxification using various techniques on Toxigen and Real Toxicity Prompts dataset (Section 5.3).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **Beavertails** (measurements) — *measured_by*
  > “To calculate the harmful score, we sample 1000 instructions from the testing set of BeaverTails (Ji et al., 2023).”
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety... (Section 5)
  - [EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING](https://proceedings.iclr.cc/paper_files/paper/2025/file/52724c4ea3634f610b0ef0245ce5bd20-Paper-Conference.pdf)
- **LlamaGuard 3** (measurements) — *measured_by*
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **Detoxify** (measurements) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **OpenAI moderation API** (measurements) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **StrongReject** (measurements) — *measured_by*
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: ... and the Gemma-2B version of the StrongReject safety classifier (Souly et al., 2024). (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **Harmbench** (measurements) — *measured_by*
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
- **HarmBench classifier** (measurements) — *measured_by*
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: the official HarmBench classifier... (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **Llama Guard 2** (measurements) — *measured_by*
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: ... the Llama-Guard-2 safety classifier... (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **Llama Guard 3** (measurements) — *measured_by*
  > Then evaluate the harmfulness score on its responses with the Llama-Guard-3-8B (Llama Team, 2024). We use 70% harmful prompts in the AdvBench dataset (Zou et al., 2023b) for InferAligner, Vaccine, and our SaLoRA. (Section 5.1).
  - [Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion](https://aclanthology.org/2025.naacl-long.88.pdf)
- **CodeAttack** (measurements) — *measured_by*
  - [A-TASC:AsianTED-Based Automatic Subtitling Corpus](https://aclanthology.org/2025.acl-long.158.pdf)
- **BOLD** (measurements) — *measured_by*
  - [Editing Across Languages: A Survey of Multilingual Knowledge Editing](https://aclanthology.org/2025.emnlp-main.804.pdf)

### → Harmful content generation
- **Jailbreaking** (behaviors tasks) — *causes*
  > Cleverly crafted prompts like multi-round attacks (Wang et al., 2024c; Dong et al., 2024; Teng et al., 2024) can circumvent the safety mechanisms of LVLMs, leading them to produce harmful content.
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
- **Adversarial robustness** (constructs) — *causes*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
- **Adversarial attacks** (behaviors tasks) — *causes*
  > Through carefully crafted input manipulation, one can bypass the safety mechanisms of LLMs and prompt the models to generate harmful, sensitive, or false information
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
- **Role-playing** (behaviors tasks) — *causes*
  > In this work, we show that whether they do so [divulge harmful information] depends signiﬁcantly on who they are talking to, which we refer to as user persona.
  - [Who's asking? User personas and the mechanics of latent misalignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/e40d5118ee8f837729fa877add71c38f-Paper-Conference.pdf)
- **Early decoding** (measurements) — *causes*
  - [Who's asking? User personas and the mechanics of latent misalignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/e40d5118ee8f837729fa877add71c38f-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *causes*
  - [A](https://aclanthology.org/2025.acl-long.185.pdf)
- **Misalignment** (constructs) — *causes*
  > safety misalignment remains dormant in a full-precision LLM but becomes exploitable post-quantization... enables the generation of harmful content
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
- **Intent perception** (constructs) — *causes*
  > By incorporating adversarial sequences, these attacks can redirect the source LLM’s focus away from malicious-intent tokens in the original input, thereby obstructing the model’s intent recognition and eliciting harmful responses. (Abstract)
  - [Understanding and Enhancing the Transferability of Jailbreaking Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/db988b089d8d97d0f159c15ed0be6a71-Paper-Conference.pdf)
- **RealToxicityPrompts** (measurements) — *causes*
  - [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf)
- **Safety alignment** (constructs) — *causes*
  > “safety alignment” process prior to deployment, in which models are fine-tuned to better align with human preferences and societal ethical standards ... However, even with safety alignment, LLMs remain vulnerable to jailbreaking attacks, which can lead them to produce outputs that contravene established safety principles
  - [AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/45673dbf3f331fbd911b0689872de396-Paper-Conference.pdf)
- **Action generation** (behaviors tasks) — *causes*
  > "we propose the approach to relax the opacity constraint by setting α to a low, non-zero value to affect the action generation stage, termed as Relaxed-EIA"
  - [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)
- **CSRT** (measurements) — *causes*
  - [MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark](https://aclanthology.org/2025.acl-long.657.pdf)
- **Steerability** (constructs) — *causes*
  - [Metadata Conditioning Accelerates Language Model Pre-training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25p/gao25p.pdf)
- **Task decomposition** (behaviors tasks) — *causes*
  - [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf)

### Associated with
- **Safety alignment** (constructs)
  > “each unaligned data sample maliciously combines a harmful instruction with a harmful response, thereby compromising the model’s reliability and safety.”
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
- **Harmlessness** (constructs)
  - [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf)
- **Trustworthiness** (constructs)
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
- **Alignment** (constructs)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
