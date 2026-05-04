# Autoformalization
**Type:** Behavior  
**Referenced in:** 16 papers  
**Also known as:** Formalization, Informalization, Statement formalization, Natural language to formal language translation, Formal problem modeling, Proof informalization, Statement informalization, Statement autoformalization, Autoformalization capability  

## State of the Field

Across the provided literature, autoformalization is predominantly characterized as the observable behavior of translating mathematical content from natural language into a formal, machine-verifiable language. The source material is typically a mathematical problem or statement, sometimes including LaTeX, while the target formal languages mentioned include proof assistant languages like Isabelle/HOL and Lean4, as well as symbolic representations such as SMT-LIB and first-order logic. This behavior is operationalized and evaluated using benchmarks including miniF2F, MATH, and ProofNet. Autoformalization is studied in relation to concepts like theorem proving and consistency, and one paper suggests that information retrieval can be used to improve its performance. While the prevailing usage treats it as a task, a less common framing defines it as a latent "autoformalization capability" of a model. Several papers also define and study the inverse process, "informalization," which translates formal statements back into natural language. The scope of the task varies, with some definitions focusing on entire problems and others on specific components like "statement autoformalization" or the reverse task of "proof informalization." One paper summarizes the task as a "transformation function from natural language and LaTeX symbols S to a formal language F" ("CiteBART: Learning to Generate Citations for Local Citation Recommendation").

## Sources

**[Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf) (as "Formalization")**
> The task of translating a natural language math problem into a formal symbolic representation (e.g., SMT-LIB).

**[Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)**
> The observable task of translating a mathematical statement from a natural language description into a formal language representation, such as Isabelle/HOL.

**[Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf) (as "Informalization")**
> Translating a formal SMT-LIB math problem back into a natural-language word problem or pure math prompt.

**[SQUAB: EvaluatingLLMrobustness to Ambiguous and Unanswerable Questions in Semantic Parsing](https://aclanthology.org/2025.emnlp-main.907.pdf) (as "Statement formalization")**
> The observable task of generating a formal language representation of a mathematical statement given its natural language counterpart.

**[Diagnosing Memorization in Chain-of-Thought Reasoning, One Token at a Time](https://aclanthology.org/2025.emnlp-main.158.pdf) (as "Natural language to formal language translation")**
> Converting natural language math problems and their solutions into formal Lean4 theorem statements that preserve semantic meaning and mathematical constraints.

**[Breaking Bad Tokens: Detoxification ofLLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.642.pdf) (as "Formal problem modeling")**
> The observable behavior of translating a natural language math problem into a formal representation (e.g., SMT-Lib) with variables and constraints.

**[Herald: A Natural Language Annotated Lean 4 Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c2bb821410066459be64d03a4dc5719-Paper-Conference.pdf) (as "Statement informalization")**
> The specific task of translating a mathematical statement from its formal language representation into natural language.

**[Herald: A Natural Language Annotated Lean 4 Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c2bb821410066459be64d03a4dc5719-Paper-Conference.pdf) (as "Proof informalization")**
> The specific task of translating a mathematical proof from its formal language representation into a natural language explanation.

**[Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf) (as "Statement autoformalization")**
> Translating an informal mathematical statement into a formal statement in a proof assistant language.

**[Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf) (as "Autoformalization capability")**
> The latent ability of an LLM to translate natural-language mathematical statements into correct formal statements.

## Relationships

### Autoformalization →
- **miniF2F** (measurements) — *measured_by*
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **MATH** (measurements) — *measured_by*
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **ProofNet** (measurements) — *measured_by*
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)
- **Theorem proving** (behaviors tasks) — *causes*
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)

### → Autoformalization
- **Information retrieval** (behaviors tasks) — *causes*
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)

### Associated with
- **Semantic consistency** (constructs)
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **Semantic alignment** (constructs)
  - [FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf)
- **Symbolic reasoning** (constructs)
  - [Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ds/zhang25ds.pdf)
- **Theorem proving** (behaviors tasks)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
