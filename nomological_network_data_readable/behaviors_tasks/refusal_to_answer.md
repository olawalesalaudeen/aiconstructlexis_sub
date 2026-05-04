# Refusal to answer
**Type:** Behavior  
**Referenced in:** 111 papers  
**Also known as:** Refusal, Abstention, Abstaining from answering, Over-refusal, Task avoidance, Evasive response generation, Selective answering, Overrefusal, Harmful query rejection, Unsafe prompt rejection, Answer abstention, Staying silent, Over-rejection, Toxic prompt rejection, Avoidance, Dispreferred response rejection, Harmful content rejection, Punting, Ill-defined problem rejection  

## State of the Field

Across the surveyed literature, "Refusal to answer" is a multifaceted behavior predominantly framed as a model's abstention from responding to malicious or harmful instructions, often as a direct result of safety alignment. This is the most common usage, with models typically outputting explicit statements like "I cannot fulfill your request" to reject unsafe prompts. A second, distinct line of work treats this behavior as a mechanism for handling uncertainty, where models "abstain" or emit special tokens like "[IDK]" when confidence is low or knowledge is lacking, a behavior studied in relation to faithfulness. These desired forms of refusal are contrasted with the widely discussed failure mode of "over-refusal," defined as the incorrect rejection of benign or harmless queries, which is frequently cited as an undesirable side effect of safety fine-tuning. Less common framings include "evasive response generation" for politically sensitive topics and "punting" due to over-cautiousness. The field operationalizes and measures this behavior using numerous benchmarks, including XSTEST, OR-Bench, and PHTest, to assess both appropriate rejections and over-refusals. The behavior is consistently studied alongside the constructs of safety, harmlessness, and helpfulness, highlighting a recurring trade-off between model safety and utility.

## Sources

**[Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf) (as "Refusal")**
> The model's observable behavior of abstaining from responding to a malicious instruction, typically by stating it cannot assist with harmful requests.

**[MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf) (as "Abstention")**
> The observable behavior of refraining from providing a final answer when confidence is low, opting instead to ask a question.

**[I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf) (as "Abstaining from answering")**
> Withholding an answer by emitting an uncertainty signal or equivalent refusal-like output instead of a substantive response.

**[Exploiting LLM Quantization](https://proceedings.neurips.cc/paper_files/paper/2024/file/496720b3c860111b95ac8634349dcc88-Paper-Conference.pdf) (as "Over-refusal")**
> The behavior of refusing to answer harmless user queries, often providing a plausible but unnecessary reason for the refusal.

**[A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf) (as "Evasive response generation")**
> The model's behavior of avoiding a direct answer to a prompt, often as a safety mechanism, which can sometimes be an undesirable side effect of alignment.

**[Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf) (as "Task avoidance")**
> The behavior of a model failing to provide a definitive answer to a task as instructed in the prompt.

**[QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf) (as "Selective answering")**
> The observable behavior of returning an answer only when confidence exceeds a threshold, otherwise abstaining from responding.

**[On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf) (as "Harmful query rejection")**
> The observable behavior of a model refusing to answer a harmful or malicious query, often by outputting a canned refusal phrase.

**[Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf) (as "Overrefusal")**
> The model's incorrect refusal to answer a benign or borderline request, often as an unintended side effect of safety fine-tuning.

**[SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf) (as "Unsafe prompt rejection")**
> The model declining or refusing to answer requests that are dangerous, unethical, or violate safety policies.

**[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://proceedings.iclr.cc/paper_files/paper/2025/file/75c37811e830bf029584b1c6fac17726-Paper-Conference.pdf) (as "Staying silent")**
> The observable behavior of an agent correctly refraining from offering assistance when it determines the user does not need help.

**[Fictitious Synthetic Data Can Improve LLM Factuality via Prerequisite Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/98ecdc722006c2959babbdbdeb22eb75-Paper-Conference.pdf) (as "Answer abstention")**
> The model's action of declining to answer a question, often by stating "I don't know", when it lacks the necessary knowledge.

**[X-ALMA: Plug & Play Modules and Adaptive Rejection for Quality Translation at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec0c9ca85b4ea49c7ebfb503cf55f2ae-Paper-Conference.pdf) (as "Over-rejection")**
> An observable failure mode in preference learning for translation where the model's output style shifts significantly away from the preferred data distribution.

**[OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf) (as "Toxic prompt rejection")**
> The observable behavior where a model correctly refuses to respond to a harmful or dangerous user request.

**[HPS: Hard Preference Sampling for Human Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25c/zou25c.pdf) (as "Harmful content rejection")**
> The observable behavior of a model refusing to generate outputs that are inappropriate, offensive, or malicious.

**[HPS: Hard Preference Sampling for Human Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25c/zou25c.pdf) (as "Dispreferred response rejection")**
> Avoiding or downweighting responses that are ranked below the preferred answer, including those that are only mildly or highly dispreferred.

**[Position: Political Neutrality in AI Is Impossible — But Here Is How to Approximate It](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fisher25a/fisher25a.pdf) (as "Avoidance")**
> The observable behavior of providing a related but non-responsive answer to a politically sensitive query, without directly addressing the input.

**[Multilingual Pretraining for Pixel Language Models](https://aclanthology.org/2025.emnlp-main.1505.pdf) (as "Punting")**
> The model's tendency to avoid answering a question altogether, often as a result of over-cautiousness induced by uncertainty prompts.

**[Breaking Bad Tokens: Detoxification ofLLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.642.pdf) (as "Ill-defined problem rejection")**
> The observable behavior of a model refusing to generate a solution when presented with a mathematical problem that has missing or contradictory conditions.

**[Perception of Knowledge Boundary for Large Language Models through Semi-open-ended Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/a1e0d6fa0c30b7d4f75dd9c7ed6189f2-Paper-Conference.pdf)**
> The action of explicitly declining to provide an answer to a question, often by stating an inability to do so or citing knowledge limitations.

## Relationships

### Refusal to answer →
- **XSTEST** (measurements) — *measured_by*
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **OR-Bench** (measurements) — *measured_by*
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
- **OR-Bench-Hard-1K** (measurements) — *measured_by*
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
- **PHTest** (measurements) — *measured_by*
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
- **TDIUC** (measurements) — *measured_by*
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *causes*
  - [Towards Transferable Personality Representation Learning based on Triplet Comparisons and Its Applications](https://aclanthology.org/2025.emnlp-main.510.pdf)
- **WildChat** (measurements) — *measured_by*
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
- **Databricks Dolly-15k** (measurements) — *measured_by*
  - [LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect](https://proceedings.neurips.cc/paper_files/paper/2024/file/064f6bcd7d3c72fb187bfca35ba2bfd4-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Neuron-Level Differentiation of Memorization and Generalization in Large Language Models](https://aclanthology.org/2025.emnlp-main.813.pdf)
- **LLMEval** (measurements) — *measured_by*
  - [Sufficient Context: A New Lens on Retrieval Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf)
- **SORRY-Bench** (measurements) — *measured_by*
  - [Programming Refusal with Conditional Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf)
- **LongMemEval** (measurements) — *measured_by*
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **OKTest** (measurements) — *measured_by*
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
- **Fairness** (constructs) — *causes*
  - [Position: Political Neutrality in AI Is Impossible — But Here Is How to Approximate It](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fisher25a/fisher25a.pdf)
- **AIAH** (measurements) — *measured_by*
  - [Towards Transferable Personality Representation Learning based on Triplet Comparisons and Its Applications](https://aclanthology.org/2025.emnlp-main.510.pdf)
- **MORBENCH** (measurements) — *measured_by*
  - [‘Rich Dad, Poor Lad’: How do Large Language Models Contextualize Socioeconomic Factors in College Admission ?](https://aclanthology.org/2025.emnlp-main.1065.pdf)

### → Refusal to answer
- **Safety alignment** (constructs) — *causes*
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Safety** (constructs) — *causes*
  - [Safety Layers in Aligned Large Language Models: The Key to LLM Security](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3bfbd65743e60c685a3845bd61ce15f-Paper-Conference.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Safety** (constructs)
  - [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf)
- **Helpfulness** (constructs)
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
- **Harmlessness** (constructs)
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
- **Safety alignment** (constructs)
  - [Injecting Universal Jailbreak Backdoors into LLMs in Minutes](https://proceedings.iclr.cc/paper_files/paper/2025/file/1160e7f31d0a74abbbe1bbf7924b949c-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  - [Large Language Models as Automated Aligners for  benchmarking  Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf)
- **Preference bias** (constructs)
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [DrawEduMath: Evaluating Vision Language Models with Expert-Annotated Students’ Hand-Drawn Math Images](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Specificity** (constructs)
  - [DrawEduMath: Evaluating Vision Language Models with Expert-Annotated Students’ Hand-Drawn Math Images](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Factuality** (constructs)
  - [Deriving Strategic Market Insights with Large Language Models: A Benchmark for Forward Counterfactual Generation](https://aclanthology.org/2025.emnlp-main.576.pdf)
- **Hallucination detection** (behaviors tasks)
  > The hallucination detection task aims to test the model’s ability to decline answering questions that are not mentioned in the given context. (Section 3.2)
  - [LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dv/li25dv.pdf)
- **Usefulness** (constructs)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)
- **Truthfulness** (constructs)
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.512.pdf)
