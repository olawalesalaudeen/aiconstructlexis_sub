# Harmful content detection
**Type:** Behavior  
**Referenced in:** 21 papers  
**Also known as:** Harmful meme detection, Offensive language detection, Toxicity detection, Threat detection, Abusive language detection, Bias and discrimination detection, Implicit hate classification, Instruction classification, Unsafe content detection, Harmful prompt classification, Prompt Classification, Toxicity classification, Harmful prompt detection, Safety filtering, Suicide risk detection  

## State of the Field

Across the provided literature, harmful content detection is predominantly framed as an observable classification task, most often a binary decision of whether an input is harmful, unsafe, or toxic versus benign. The scope of what is considered harmful is broad, encompassing categories such as hate speech, toxicity, offensive or abusive language, threats, and various forms of bias and discrimination. This behavior is applied to different types of inputs, including text statements, user prompts, instruction-response pairs, and in some cases, multimodal content like memes. The task is frequently operationalized as a "safety filter" or "guardrail model" intended to "detect and block malicious jailbreak attempts" or reject unsafe content before it is processed by a generative model. To measure performance, researchers employ a variety of benchmarks and evaluation procedures, including XSTEST, ToxicChat, Beavertails, SimpleSafetyTests, and the OpenAI moderation API. While most work treats this as a direct classification, some papers introduce more specific framings, such as distinguishing between classifying instructions alone versus instruction-response pairs, or focusing on the challenge of identifying "highly implicit content" that cannot be detected by simple pattern matching. A few studies also report that model capabilities like contextual understanding and cultural knowledge influence performance on this task.

## Sources

**[Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf) (as "Hate speech detection")**
> Identifying hateful or toxic content in text statements.

**[Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Harmful meme detection")**
> The observable task of performing binary classification on a multimodal meme (image and text) to determine if it is harmful or benign.

**[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf) (as "Offensive language detection")**
> Classifying a text as offensive or not offensive based on its content.

**[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf) (as "Toxicity detection")**
> Classifying text as toxic or non-toxic.

**[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf) (as "Threat detection")**
> Classifying text as containing threats or not.

**[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf) (as "Bias detection")**
> Classifying text as expressing bias, stereotype, homophobia, misogyny, or related prejudicial content.

**[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf) (as "Abusive language detection")**
> Classifying text as abusive or non-abusive.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Bias and discrimination detection")**
> Assessing a model's potential for unfair treatment related to subjective preferences, social stereotypes, race, gender, or religion in judicial decision-making.

**[HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)**
> The observable task of classifying a given input, such as an instruction or an instruction-response pair, as harmful or not.

**[HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf) (as "Instruction classification")**
> A specific classification task where the model determines the harmfulness of a user instruction alone, with the response being an empty sequence.

**[Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf) (as "Implicit hate classification")**
> Assigning a tweet or text to the implied hateful statement or target context it most likely expresses.

**[$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf) (as "Unsafe content detection")**
> The observable task of assigning a probability of being unsafe to a given text prompt, based on its adherence to safety policies.

**[Beyond Mere Token Analysis: A Hypergraph Metric Space Framework for Defending Against Socially Engineered LLM Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/18699b47bb4abf5f92b0b73266b3ffc8-Paper-Conference.pdf) (as "Harmful prompt classification")**
> The task of identifying and categorizing input prompts as either harmful/malicious or benign/safe.

**[Beyond Mere Token Analysis: A Hypergraph Metric Space Framework for Defending Against Socially Engineered LLM Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/18699b47bb4abf5f92b0b73266b3ffc8-Paper-Conference.pdf) (as "Prompt Classification")**
> The system assigning a label (harmful or benign) to an input prompt based on its geometric representation.

**[BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf) (as "Toxicity classification")**
> The task of classifying a given text prompt or response as either toxic/unsafe or non-toxic/safe.

**[Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf) (as "Safety filtering")**
> Detecting and rejecting harmful or unsafe user prompts before they are processed by a generative model, implemented using encoder-based LLMs as classifiers.

**[Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf) (as "Harmful prompt detection")**
> The task of identifying user prompts that are designed to elicit harmful or unsafe responses from a language model.

**[Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://raw.githubusercontent.com/mlresearch/v267/main/assets/badawi25a/badawi25a.pdf) (as "Suicide risk detection")**
> The task of identifying language or patterns in user input that indicate a risk of suicide.

## Relationships

### Harmful content detection →
- **OpenAI moderation API** (measurements) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **XSTEST** (measurements) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **ToxicChat** (measurements) — *measured_by*
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Beavertails** (measurements) — *measured_by*
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **SimpleSafetyTests** (measurements) — *measured_by*
  > To assess calibration in the context of binary prompt classification, we evaluate performance using a range of public benchmarks, including OpenAI Moderation (Markov et al., 2023), ToxicChat Test (Lin et al., 2023), Aegis Safety Test (Ghosh et al., 2024), SimpleSafetyTests (Vidgen et al., 2023), XSTest (R¨ottger et al., 2023), Harmbench Prompt (Mazeika et al., 2024) and WildGuardMix Test Prompt (Han et al., 2024).
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
- **GCG attack** (measurements) — *measured_by*
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)

### → Harmful content detection
- **Contextual understanding** (constructs) — *causes*
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Cultural knowledge** (constructs) — *causes*
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)
