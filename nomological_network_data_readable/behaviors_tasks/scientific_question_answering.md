# Scientific question answering
**Type:** Behavior  
**Referenced in:** 18 papers  
**Also known as:** Science question answering, Biology question answering  

## State of the Field

Across the surveyed literature, scientific question answering is predominantly framed as the task of answering questions about various scientific domains. The most common definitions describe this behavior as requiring reasoning over provided context or external knowledge, and frequently involves understanding multimodal inputs like diagrams and charts in addition to text. The difficulty of the questions varies, with some work focusing on "subject-specific questions from school curricula" (Matryoshka Query Transformer for Large Vision-Language Models) while other research targets "hard (graduate-level) questions" (Automated Design of Agentic Systems). A smaller line of work narrows the scope to specific disciplines like biology or climate science. This behavior is operationalized and measured using a number of benchmarks, including ScienceQA, SciBench, OpenBookQA, and the ARC suite (ARC, ARC-Challenge, ARC-Easy). Scientific question answering is also studied in relation to constructs such as domain-specific knowledge, numerical ability, long-context understanding, and causal reasoning.

## Sources

**[Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf) (as "Science question answering")**
> The task of answering multiple-choice questions about a wide range of scientific topics, often requiring reasoning over provided context or external knowledge.

**[Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)**
> The task of answering questions related to scientific domains, often requiring understanding of diagrams, charts, or other visual aids in addition to text.

**[STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf) (as "Biology question answering")**
> The observable task of answering questions related to the field of biology.

## Relationships

### Scientific question answering →
- **ARC-Easy** (measurements) — *measured_by*
  - [Debiasing the Fine-Grained Classification Task inLLMs with Bias-AwarePEFT](https://aclanthology.org/2025.acl-long.718.pdf)
- **ScienceQA** (measurements) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [Debiasing the Fine-Grained Classification Task inLLMs with Bias-AwarePEFT](https://aclanthology.org/2025.acl-long.718.pdf)
- **ARC** (measurements) — *measured_by*
  > ARC (AI2 Reasoning Challenge, Clark et al., 2018) was designed to test the reasoning abilities of AI through a series of challenging science questions. (Section 1.1)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [Debiasing the Fine-Grained Classification Task inLLMs with Bias-AwarePEFT](https://aclanthology.org/2025.acl-long.718.pdf)
- **SciBench** (measurements) — *measured_by*
  > SciBench (Wang et al., 2024a) is a benchmark suite of scientific reasoning tasks, where the objective is to answer complex, multi-step scientific questions that require integrating knowledge, reasoning over evidence, and applying scientific principles. (Section 4.4. SciBench)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)

### Associated with
- **Domain knowledge** (constructs)
  - [How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf)
- **Numerical ability** (constructs)
  - [How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf)
- **Long-context understanding** (constructs)
  - [How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf)
- **Causal reasoning** (constructs)
  - [How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf)
