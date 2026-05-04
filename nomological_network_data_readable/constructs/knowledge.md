# Knowledge
**Type:** Construct  
**Referenced in:** 33 papers  
**Also known as:** Knowledge ability, Knowledge capacity, Latent world model, Mathematical world-model, Abstract meta-knowledge, World model  

## State of the Field

Across the surveyed literature, the most prevalent framing of knowledge is as a model's latent ability to recall factual information stored internally, which is not present in the direct input. This is sometimes specified as "knowledge ability" or "knowledge capacity," with the latter also including the utilization of this information to solve professional problems. The construct is operationalized through tasks requiring world knowledge, such as Multiple Choice Question Answering (MCQA), which is noted to assess the ability to recall, understand, and apply information. A distinct but related line of work conceptualizes knowledge as an internal "world model," which is variously defined as a structured representation of an input context, an understanding of "underlying principles, dynamics, and causalities of the real world" (MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos), or a system for predicting the outcomes of actions. More specialized definitions also appear, including a domain-specific "mathematical world-model" and "abstract meta-knowledge" for high-level problem-solving. Thus, while the core definition centers on factual recall, a substantial portion of the literature expands the concept to include the internal modeling of relationships, dynamics, and abstract procedures.

## Sources

**[VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The latent ability to recall facts or information contained in the model that cannot be found directly in the input.

**[LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Knowledge ability")**
> The extent to which a large language model has acquired and can recall factual information about the world.

**[PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Knowledge capacity")**
> The ability of a model to retrieve and utilize acquired knowledge to solve professional problems.

**[Monitoring Latent World States in Language Models with Propositional Probes](https://proceedings.iclr.cc/paper_files/paper/2025/file/3132d0405fabe24b2a7b6cd7ba9de6b5-Paper-Conference.pdf) (as "Latent world model")**
> An internal, structured representation of the entities and relationships described in an input context, which the language model is hypothesized to construct and maintain in its activations.

**[MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf) (as "World modeling")**
> The latent ability to understand and reason about the underlying principles, dynamics, and causalities of the real world.

**[Can Transformers Do Enumerative Geometry?](https://proceedings.iclr.cc/paper_files/paper/2025/file/aee2f03ecb2b2c1ea55a43946b651cfd-Paper-Conference.pdf) (as "Mathematical world-model")**
> An internalized, coherent understanding of mathematical concepts, relationships, and structures that goes beyond surface-level pattern matching.

**[Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf) (as "Abstract meta-knowledge")**
> High-level problem-solving knowledge that abstracts away from task-specific details and can transfer across similar problems.

**[Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf) (as "World model")**
> An internal, learned representation of an environment that allows an agent to predict the outcomes of its actions without actually executing them.

## Relationships

### Knowledge →
- **MMLU** (measurements) — *measured_by*
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [Benchmarking and Improving Generator-Validator Consistency of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfcb583d225b1db8d3ca2331f6785774-Paper-Conference.pdf)
- **ArabicMMLU** (measurements) — *measured_by*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **MM-Vet** (measurements) — *measured_by*
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MME** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMMU** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MathVista** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Natural language inference** (behaviors tasks)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
