# Multi-task capability
**Type:** Construct  
**Referenced in:** 10 papers  
**Also known as:** Cross-task generalization, Compositional multi-tasking  

## State of the Field

Across the surveyed literature, "Multi-task capability" is framed in several distinct ways, with no single dominant definition. One perspective treats it as the ability of a merged model to retain the functionalities of its specialist components, allowing it to "perform multiple tasks" effectively ("UNComp: Can Matrix Entropy Uncover Sparsity? — A Compressor Design from an Uncertainty-Aware Perspective"). Another view, labeled "cross-task generalization," focuses on a model's ability to handle unseen or diverse task types, such as generating instruction data for both open-book and closed-book QA. A third, more specific framing is "compositional multi-tasking," defined as the latent ability for "simultaneous execution of multiple tasks" within a single inference pass ("Video-RTS: Rethinking Reinforcement Learning and Test-Time Scaling for Efficient and Enhanced Video Reasoning"). To assess this construct, papers operationalize it using performance on benchmarks like `Super-NaturalInstructions` and tasks such as `Link prediction`. The concept is studied in relation to `Zero-shot learning`, `Commonsense knowledge`, and question-answering behaviors. Furthermore, some research suggests that constructs like `Planning` and `Self-reflection` may be causes of multi-task capability.

## Sources

**[UNComp: Can Matrix Entropy Uncover Sparsity? — A Compressor Design from an Uncertainty-Aware Perspective](https://aclanthology.org/2025.emnlp-main.210.pdf)**
> The latent ability of a merged model to retain and perform multiple tasks effectively after combining specialist models.

**[OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf) (as "Cross-task generalization")**
> The ability of the data synthesis model to generate high-quality instruction data for unseen or diverse task types by leveraging flexible task definitions such as open-book and closed-book QA.

**[Video-RTS: Rethinking Reinforcement Learning and Test-Time Scaling for Efficient and Enhanced Video Reasoning](https://aclanthology.org/2025.emnlp-main.1429.pdf) (as "Compositional multi-tasking")**
> The latent ability of a model to simultaneously execute multiple distinct tasks (e.g., summarization and translation) in a single inference pass, integrating their requirements into a coherent output.

## Relationships

### Multi-task capability →
- **Link prediction** (behaviors tasks) — *measured_by*
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
- **Super-NaturalInstructions** (measurements) — *measured_by*
  - [Neuron-Level Sequential Editing for Large Language Models](https://aclanthology.org/2025.acl-long.816.pdf)

### → Multi-task capability
- **Planning** (constructs) — *causes*
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks) — *causes*
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)

### Associated with
- **Zero-shot learning** (constructs)
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Closed-book question answering** (behaviors tasks)
  > AQuilt achieves better task generalization by incorporating Chinese data and defining more flexible task types. Specifically, AQuilt assigns the task type as closed/open-book QA and uses task requirements as question prefixes. (Section 4.3)
  - [OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf)
- **Document question answering** (behaviors tasks)
  - [OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf)
