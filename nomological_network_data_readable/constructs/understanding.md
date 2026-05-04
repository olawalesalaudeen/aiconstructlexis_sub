# Understanding
**Type:** Construct  
**Referenced in:** 46 papers  
**Also known as:** Comprehension, Comprehension ability, General comprehension capability, Context awareness, Multi-chart comprehension, Multi-image comprehension, Screen reading comprehension, Task comprehension, Understanding capability, Patient comprehension, Expert-like text comprehension  

## State of the Field

Across the surveyed literature, Understanding is most commonly defined as a latent ability of a model to correctly interpret, identify, and reason about content, instructions, or tasks. This general framing is specified in various contexts, including the comprehension of few-shot prompts, the implicit and explicit requirements of an instruction, and domain-specific content like cybersecurity or medical texts. A notable line of work explicitly contrasts this construct with generative fluency, arguing that a model's ability to generate expert-like outputs is not necessarily contingent on its ability to understand them. As one paper states, a model's "generative capabilities... can therefore exceed... their ability to understand those same types of outputs” (The Generative AI Paradox: “What It Can Create, It May Not Understand”). To operationalize this construct, researchers measure performance on a wide array of benchmarks, including MMLU, GSM8k, BBH, and DROP. For multimodal contexts, specific instruments are used, such as SEED-Bench-2, which "evaluates the ability to comprehend multimodal inputs containing multiple images." Understanding is frequently studied alongside reasoning and information extraction, and some work suggests it influences more complex behaviors like autonomous task solving.

## Sources

**[An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf) (as "Comprehension ability")**
> The latent capacity of a large language model to understand and correctly interpret complex instructions or tasks, such as those provided in a few-shot prompt.

**[The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf)**
> The latent ability to correctly identify, interpret, or reason about content, as evidenced by performance on discriminative or interrogative tasks, independent of generative fluency.

**[FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf) (as "Comprehension")**
> The ability to understand the implicit and explicit purpose and requirements of an instruction.

**[Empowering LLM Agents with Zero-Shot Optimal Decision-Making through Q-learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c25de6a9da675464ebb925e430c58325-Paper-Conference.pdf) (as "General comprehension capability")**
> The foundational ability of a large language model, derived from training on extensive text data, to understand and process information.

**[Smurfs: Multi-Agent System using Context-EfficientDFSDTfor Tool Planning](https://aclanthology.org/2025.naacl-long.170.pdf) (as "Multi-image comprehension")**
> The ability to process, integrate, and reason about information presented across multiple images within a single input context.

**[AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf) (as "Reading comprehension")**
> The general task of reading a passage of text and answering questions about its content.

**[Regularized Best-of-N Sampling with MinimumBayes Risk Objective for Language Model Alignment](https://aclanthology.org/2025.naacl-long.473.pdf) (as "Task comprehension")**
> The ability to correctly understand the requirements and goals of a given task based on the provided prompt and context.

**[MASTER: A Multi-Agent System withLLMSpecializedMCTS](https://aclanthology.org/2025.naacl-long.477.pdf) (as "Screen reading comprehension")**
> The capacity to read and understand textual and symbolic information presented on a screen to answer specific questions.

**[Exploring Safety-Utility Trade-Offs in Personalized Language Models](https://aclanthology.org/2025.naacl-long.566.pdf) (as "Multi-chart comprehension")**
> The underlying capacity to understand, integrate, and reason over information presented across multiple semantically related charts.

**[Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.624.pdf) (as "Context awareness")**
> The model's ability to adapt its reasoning and response strategy based on the sufficiency or ambiguity of contextual information provided in a question-answering task.

**[AdaRewriter: Unleashing the Power of Prompting-based Conversational Query Reformulation via Test-Time Adaptation](https://aclanthology.org/2025.emnlp-main.194.pdf) (as "Understanding capability")**
> The model's latent ability to comprehend and correctly interpret the meaning and intent of input text.

**[Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.546.pdf) (as "Patient comprehension")**
> The degree to which a patient understands and retains critical discharge information as a result of the model's educational efforts.

**[[CLS]](https://aclanthology.org/2025.emnlp-main.1313.pdf) (as "Expert-like text comprehension")**
> The latent ability of a model to understand medical case reports in a manner similar to expert clinicians, including identifying diagnostically salient information and organizing it hierarchically.

## Relationships

### Understanding →
- **MMLU** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Autonomous task solving** (behaviors tasks) — *causes*
  - [Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://proceedings.iclr.cc/paper_files/paper/2025/file/75c37811e830bf029584b1c6fac17726-Paper-Conference.pdf)
- **SEED-Bench-2** (measurements) — *measured_by*
  > Multi-image Tasks: Seed-Bench-2 (Li et al., 2024) evaluates the ability to comprehend multimodal inputs containing multiple images.
  - [Smurfs: Multi-Agent System using Context-EfficientDFSDTfor Tool Planning](https://aclanthology.org/2025.naacl-long.170.pdf)
- **Needle-in-a-haystack test** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **GPQA** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **BBH** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **MATH** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **DROP** (measurements) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Mantis-Eval** (measurements) — *measured_by*
  - [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
- **QBench** (measurements) — *measured_by*
  - [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
- **BLINK** (measurements) — *measured_by*
  - [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)

### Associated with
- **Generative capability** (constructs)
  - [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf)
- **Natural language understanding** (constructs)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Information extraction** (behaviors tasks)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **In-context learning** (constructs)
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks)
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **Sign language recognition** (behaviors tasks)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
- **Sign language translation** (behaviors tasks)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
