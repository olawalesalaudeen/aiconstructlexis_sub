# Adversarial attacks
**Type:** Behavior  
**Referenced in:** 47 papers  
**Also known as:** Adversarial query answering, Jailbreak compliance, Harmful instruction following, Following malicious instructions, Adversarial attack response, Prompt injection, Dangerous question answering, Jailbreak prompt generation, Harmful question answering, Unsafe instruction fulfillment, Indirect prompt injection, Harmful behavior execution, Trigger generation, Jailbreak success, Mis-classification under target attack, Monitor evasion, Watermark evasion, Adversarial example generation, Jailbreak generation, SQL injection, Emoji insertion  

## State of the Field

Across the surveyed literature, adversarial attacks are predominantly framed as behaviors where a model's safety mechanisms are circumvented to produce unintended, often harmful, outputs. The most common definitions describe this as "jailbreaking," "harmful instruction following," or "prompt injection," all of which involve the model complying with a malicious user request rather than refusing. Several papers operationalize these attacks through specific techniques, with a recurring method being the automatic generation and appending of an "adversarial suffix" to a user's prompt. Other documented methods include "indirect prompt injection" via external data, "emoji insertion" to evade detection by judge models, and exploiting web vulnerabilities like "SQL injection." The primary consequence of these attacks, as stated in numerous sources, is the generation of harmful content. The occurrence of this behavior is evaluated using benchmarks such as Beavertails, HEX-PHI, and SORRY-Bench, with some work also measuring an Attack Success Rate (ASR). While most definitions focus on eliciting harmful text, a smaller set of papers describe related behaviors like generating adversarial examples to cause misclassification, evading watermarks, or producing hidden triggers.

## Sources

**[Who's asking? User personas and the mechanics of latent misalignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/e40d5118ee8f837729fa877add71c38f-Paper-Conference.pdf) (as "Adversarial query answering")**
> The act of providing a substantive, non-refusal response to a query designed to elicit harmful content.

**[Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf) (as "Jailbreak compliance")**
> Responses that provide harmful or illegal content in response to malicious instructions.

**[ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf) (as "Harmful instruction following")**
> The observable behavior of a model complying with a harmful instruction to generate an unsafe or malicious response.

**[Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf) (as "Following malicious instructions")**
> The model generates a response that complies with a user's request for harmful, unethical, or dangerous content, rather than refusing.

**[What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf) (as "Jailbreaking")**
> An observable behavior where the model's safety mechanisms are circumvented, leading it to produce outputs that violate its intended use policies, such as generating harmful or offensive content.

**[RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Adversarial attack response")**
> The model responds to queries designed with jailbreak techniques or adversarial probes to induce forgotten knowledge.

**[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Prompt injection")**
> Introducing malicious instructions into tool outputs or other context so that the agent follows the attacker’s goal instead of the user’s.

**[Can a Large Language Model be a Gaslighter?](https://proceedings.iclr.cc/paper_files/paper/2025/file/0769598fdeb4f23ee86fec1bc0777f44-Paper-Conference.pdf) (as "Dangerous question answering")**
> Responding to harmful or unsafe user questions in a way that reveals whether the model refuses or complies.

**[One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf) (as "Jailbreak prompt generation")**
> The automatic generation of a rephrased, robust version of a malicious query designed to bypass safety defenses.

**[ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf) (as "Adversarial suffix generation")**
> The task of automatically creating and appending a string of text (a suffix) to a user's instruction to cause a target model to behave in an unintended, often harmful, way.

**[SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf) (as "Unsafe instruction fulfillment")**
> The observable behavior where a model executes a potentially unsafe instruction by providing substantial content that directly assists with the user's unsafe intent.

**[On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf) (as "Harmful question answering")**
> The observable behavior of a model complying with and providing a substantive answer to a harmful or malicious question.

**[Can LLMs Separate Instructions From Data? And What Do We Even Mean By That?](https://proceedings.iclr.cc/paper_files/paper/2025/file/a77eadda332b6d4a9ae1e0e4024555f2-Paper-Conference.pdf) (as "Indirect prompt injection")**
> Following malicious or unintended instructions embedded in external content such as emails, documents, or retrieved text.

**[BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf) (as "Trigger generation")**
> Producing a hidden trigger token or pattern in model outputs that can activate a backdoor in the evaluator.

**[Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf) (as "Jailbreak success")**
> Producing restricted harmful outputs when prompted by adversarial or jailbreak-style inputs.

**[Aligned LLMs Are Not Aligned Browser Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/42f92b78a6695f60db0cd38b54d57a41-Paper-Conference.pdf) (as "Harmful behavior execution")**
> The observable action of an LLM agent attempting to or successfully carrying out a user instruction that is malicious, dangerous, illegal, or unethical.

**[Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf) (as "Mis-classification under target attack")**
> The model's incorrect classification of an input (e.g., an image) as a target class after a portion of the input's tokens are replaced with tokens from that target class.

**[An Interpretable N-gram Perplexity Threat Model for Large Language Model Jailbreaks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boreiko25a/boreiko25a.pdf) (as "Jailbreak generation")**
> Producing adversarial text inputs that preserve malicious intent while circumventing safety alignment to elicit harmful responses from an LLM.

**[AutoAdvExBench: Benchmarking Autonomous Exploitation of Adversarial Example Defenses](https://raw.githubusercontent.com/mlresearch/v267/main/assets/carlini25a/carlini25a.pdf) (as "Adversarial example generation")**
> The observable task of producing perturbed inputs (adversarial examples) designed to cause a machine learning model to misclassify them.

**[Optimizing Adaptive Attacks against Watermarks for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diaa25a/diaa25a.pdf) (as "Watermark evasion")**
> The observable outcome in which a paraphrased text successfully avoids detection by the watermark verification system while maintaining high textual quality.

**[MONA: Myopic Optimization with Non-myopic Approval Can Mitigate Multi-step Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/farquhar25a/farquhar25a.pdf) (as "Monitor evasion")**
> Producing outputs that avoid triggering a monitor or penalty while still influencing the downstream decision.

**[CVE-Bench: A Benchmark for AI Agents’ Ability to Exploit Real-World Web Application Vulnerabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25i/zhu25i.pdf) (as "SQL injection")**
> Injecting malicious SQL payloads into application inputs to manipulate queries or extract database data.

**[Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25g/wei25g.pdf) (as "Emoji insertion")**
> The observable act of inserting emojis within words of a model's response, altering tokenization and embeddings to evade detection by Judge LLMs.

## Relationships

### Adversarial attacks →
- **Harmful content generation** (behaviors tasks) — *causes*
  > Through carefully crafted input manipulation, one can bypass the safety mechanisms of LLMs and prompt the models to generate harmful, sensitive, or false information
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
- **Beavertails** (measurements) — *measured_by*
  > BeaverTails (Ji et al., 2024) is the benchmark used by Rosati et al. (2024) to evaluate RepNoise; we adopt the same evaluation setup, reporting the average harmfulness scores (ranging from 0 to 1) as assessed by their harmfulness score. (Section 2.2)
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
- **HEX-PHI** (measurements) — *measured_by*
  > "We also consider two additional harmfulness evaluation datasets: HEx-PHI (Qi et al., 2023) and SORRY-bench (Xie et al., 2024)."
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
- **SORRY-Bench** (measurements) — *measured_by*
  > "We also consider two additional harmfulness evaluation datasets: HEx-PHI (Qi et al., 2023) and SORRY-bench (Xie et al., 2024)."
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)

### → Adversarial attacks
- **Language understanding** (behaviors tasks) — *causes*
  - [One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf)
