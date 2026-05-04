# Domain knowledge
**Type:** Construct  
**Referenced in:** 41 papers  
**Also known as:** Professional knowledge, Task knowledge, Domain expertise, Scientific prior knowledge, Scientific knowledge, Science-related abilities, Industrial knowledge, Math knowledge, Specialized knowledge, Technical expertise, Topical knowledge, Chemistry knowledge, Medical knowledge, Clinical domain knowledge  

## State of the Field

Across the surveyed literature, domain knowledge is most commonly defined as a model's repository of specialized information and its ability to apply that information to interpret observations and perform actions within a specific field. While the prevailing usage centers on applying knowledge, a smaller set of definitions frame it as a latent, encoded "theory" a model possesses about a topic. The concept is invoked across a wide array of fields, including scientific areas like medicine and climate science, technical domains such as coding, and professional settings like operations research. Researchers operationalize and measure this construct by evaluating model performance on a variety of specialized benchmarks. For instance, MMLU is frequently used to assess broad academic and professional knowledge, while benchmarks like SciQ, MedQA, and PubMedQA are used to evaluate knowledge in scientific and clinical domains. Furthermore, technical expertise is measured using WildBench, and math knowledge is studied in relation to benchmarks like MathQA and GSM8k. One study highlights a complexity in its acquisition, noting that while training on domain-specific texts can "imbue the general model with domain knowledge," it may also cause a "drastic drop in prompting performance." Ultimately, domain knowledge is treated as a latent capability that allows models to understand specialized terminology and context, with its presence typically inferred from performance on domain-specific tasks.

## Sources

**[Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf)**
> Knowledge of environment-specific concepts and entities needed to interpret observations and choose appropriate actions.

**[Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf) (as "Professional knowledge")**
> The model's encoded repository of information across a wide spectrum of specialized subjects, ranging from elementary to advanced professional levels.

**[Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf) (as "Domain-specific knowledge")**
> The ability to access and apply factual knowledge in specialized domains such as health and science, which require background understanding and quantitative reasoning.

**[Prompt Optimization with EASE? Efficient Ordering-aware Automated Selection of Exemplars](https://proceedings.neurips.cc/paper_files/paper/2024/file/dd8e7dae18cecd7c9137840161e1bf62-Paper-Conference.pdf) (as "Task knowledge")**
> The amount of prior task-specific knowledge the model already has before receiving in-context exemplars.

**[LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf) (as "Scientific knowledge")**
> The model's capacity to understand and apply knowledge from scientific domains to answer questions.

**[CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf) (as "Domain expertise")**
> The possession of deep, specialized knowledge in a particular scientific field, enabling comprehension and application of complex concepts.

**[Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf) (as "Science-related abilities")**
> The capability to understand and answer questions related to scientific knowledge across various domains.

**[LLM-SR: Scientific Equation Discovery via Programming with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/28df8e730c054c5331855fd4d5403ba9-Paper-Conference.pdf) (as "Scientific prior knowledge")**
> The extent to which an LLM can draw on domain-specific scientific knowledge when proposing plausible equations or hypotheses.

**[MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf) (as "Specialized knowledge")**
> The latent ability to answer questions requiring domain-specific factual or conceptual knowledge across multiple subjects.

**[EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf) (as "Math knowledge")**
> The extent of an LLM's competence on math-related content, as reflected by performance patterns across math benchmarks.

**[MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d91ffbe9c126765755ff52d36b715683-Paper-Conference.pdf) (as "Industrial knowledge")**
> The model's internalized knowledge specific to industrial products, manufacturing processes, and defect types, which is necessary for accurate quality inspection.

**[WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf) (as "Technical expertise")**
> The ability to produce correct outputs in technical domains such as coding, debugging, and software design.

**[From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf) (as "Topical knowledge")**
> The latent, overall understanding or "theory" a language model possesses about a specific subject area, which can be distilled into a set of core factual statements.

**[OSDA Agent: Leveraging Large Language Models for De Novo Design of Organic Structure Directing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38fbf326eb71f4749d04102323f7f79-Paper-Conference.pdf) (as "Chemistry knowledge")**
> The extent of the model's embedded knowledge about chemical principles, structures, and synthesis rules.

**[MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Medical knowledge")**
> The extent of a model's embedded knowledge about medical concepts, including diseases, symptoms, treatments, and medications.

**[EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Clinical domain knowledge")**
> The extent of an LLM's acquired knowledge about medical concepts, procedures, and reasoning, typically inferred from performance on tasks like answering questions from medical licensing exams.

## Relationships

### Domain knowledge →
- **MMLU** (measurements) — *measured_by*
  > We measure this knowledge reservoir using the Massive Multitask Language Understanding dataset (MMLU) (Hendrycks et al., 2021). (Section 4.1)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
- **PubMedQA** (measurements) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Creativity** (constructs) — *causes*
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MedQA** (measurements) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MedMCQA** (measurements) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WildBench** (measurements) — *measured_by*
  > “The tasks in WILDBENCH typically demand higher-order reasoning, such as writing and/or debugging code with specific constraints, creative writing with multiple constraints on the style and content, or designing a software system with complex requirements. These tasks often require critical thinking, creativity, and technical expertise”
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  > SciQ (Welbl et al., 2017) for science-related abilities. (Section 3.1)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **DiscoveryBench** (measurements) — *measured_by*
  - [DiscoveryBench: Towards Data-Driven Discovery with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d70af566e69f1dfb687791ecf955e28-Paper-Conference.pdf)
- **Disambiguation** (constructs) — *causes*
  - [JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf)

### Associated with
- **GSM8k** (measurements)
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)
- **MathQA** (measurements)
  > For instance, there is a total MSE improvement of 0.271 when GSM8k is incorporated to predicting MathQA... As all three benchmarks are math-related, we can deduce that the level of math knowledge of our selected models are indeed learned and reflected in our model embeddings.
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)
- **Scientific question answering** (behaviors tasks)
  - [How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf)
