# Algorithmic reasoning
**Type:** Construct  
**Referenced in:** 24 papers  
**Also known as:** Algorithmic capability, Algorithmic processing, Algorithmic comprehension  

## State of the Field

Across the surveyed literature, algorithmic reasoning is most commonly defined as the ability to infer and apply multi-step algorithms to solve programming problems from natural-language specifications. A smaller set of studies offers related framings, such as "algorithmic comprehension" or "algorithmic processing," which emphasize the application of generalizable, step-by-step procedures as an alternative to pattern matching or memorization. The construct is operationalized and measured through performance on a range of benchmarks, with several papers explicitly using code generation and competitive programming datasets like CodeContests, HumanEval, and MBPP for evaluation. Other instruments reported to assess this ability include Big-Bench Hard (BBH) and MR-Ben. Algorithmic reasoning is frequently studied in the context of complex code generation, where, as one paper notes, tasks "requiring multi-step algorithmic reasoning… remain challenging." The specific tasks used to probe this ability include graph traversal, pathfinding, and devising search algorithms. It is also studied alongside mathematical and graph reasoning, and one paper reports that chain-of-thought reasoning particularly helps models on problems requiring this type of reasoning.

## Sources

**[DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf)**
> The ability to infer and apply multi-step algorithms needed to solve programming problems from natural-language specifications.

**[Algorithmic Capabilities of Random Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/bccdd196d798a51a4961989984a9ed4a-Paper-Conference.pdf) (as "Algorithmic capability")**
> The latent capacity of a transformer to implement structured computations such as arithmetic, recall, balancing, or sequence generation across different tasks.

**[Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient](https://proceedings.iclr.cc/paper_files/paper/2025/file/fad7c708dda11f3e72cc1629bb130379-Paper-Conference.pdf) (as "Algorithmic processing")**
> The model's ability to apply simple, generalizable rules or procedures to solve tasks, as opposed to relying on memorized instances.

**[Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf) (as "Algorithmic comprehension")**
> The ability to learn and apply robust, generalizable, step-by-step procedures to solve problems, as opposed to relying on pattern matching or memorization.

## Relationships

### Algorithmic reasoning →
- **BBH** (measurements) — *measured_by*
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **CodeContests** (measurements) — *measured_by*
  > Competition-level benchmarks require algorithmic reasoning and thus provide an ideal testbed to evaluate whether CoT techniques can be extended beyond single-turn reasoning. (Section 1)
  - [What Makes Large Language Models Reason in (Multi-Turn) Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fef0802863f47775c3563e18cbba17-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  > Our experiments demonstrate that RaLU significantly outperforms existing baselines in mathematical reasoning (GSM8K, MATH) and algorithmic reasoning (HumanEval+, MBPP+), underscoring its potential to advance LLM reasoning and programming by offering enhanced accuracy and interpretability. (Abstract)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
- **MBPP** (measurements) — *measured_by*
  > Our experiments demonstrate that RaLU significantly outperforms existing baselines in mathematical reasoning (GSM8K, MATH) and algorithmic reasoning (HumanEval+, MBPP+), underscoring its potential to advance LLM reasoning and programming by offering enhanced accuracy and interpretability. (Abstract)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)

### → Algorithmic reasoning
- **MR-Ben** (measurements) — *measured_by*
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)

### Associated with
- **Code generation** (behaviors tasks)
  - [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf)
- **Graph reasoning** (constructs)
  - [Understanding Transformer Reasoning Capabilities via Graph Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f395480c04ac6dfb2c2326a639df88e-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks)
  - [PUZZLES: A Benchmark for Neural Algorithmic Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e5d1eaadeed651ba1021c09149db4b92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Mathematical reasoning** (constructs)
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
