# SuperGLUE
**Type:** Measurement  
**Referenced in:** 44 papers  

## State of the Field

Across the provided literature, SuperGLUE is consistently characterized as a benchmark suite for evaluating language models, frequently described as a more challenging successor to the GLUE benchmark. Its primary and most common application is to measure the construct of "natural language understanding," with papers also using it to assess more specific abilities like reasoning, comprehension, and inference. The benchmark is composed of a collection of diverse tasks, and is described by one paper as a "widely acceptable benchmark for evaluating general-purpose language understanding." While the exact number of tasks cited varies between six, seven, and eight across different sources, specific sub-tasks mentioned include BoolQ, MultiRC, WiC, WSC, and CB. Researchers employ SuperGLUE in various evaluation settings, including standard fine-tuning, few-shot adaptation, and in-context learning. While most papers use it to evaluate general model quality on classification and reasoning tasks, at least one study uses it to measure "parameter efficiency."

## Sources

**[A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf)**
> A more challenging benchmark suite than GLUE, consisting of complex language understanding tasks that test reasoning and comprehension abilities.

## Relationships

### → SuperGLUE
- **Natural language understanding** (constructs) — *measured_by*
  > "We benchmark FIRE as well as other positional encoding approaches on a wide range of real-world language modeling (C4, arXiv, and Github), long text benchmark (SCROLLS), zero-shot long-context question answering (NarrativeQA), and natural language understanding benchmarks (GLUE/SuperGLUE)."
  - [A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **Classification** (behaviors tasks) — *measured_by*
  - [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c570b0f9938c7a58a612e5b00af9cc0-Paper-Conference.pdf)
- **Parameter efficiency** (constructs) — *measured_by*
  > We extended our evaluation to the more challenging SuperGLUE benchmark... SSMLoRA achieves comparable or superior performance across most tasks while utilizing only half the parameters of traditional approaches. (Section 4.6)
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)

### Associated with
- **BoolQ** (measurements)
  > For question answering tasks, we utilize BoolQ (from SuperGLUE) (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
