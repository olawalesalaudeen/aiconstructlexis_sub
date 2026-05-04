# Code generation
**Type:** Behavior  
**Referenced in:** 544 papers  
**Also known as:** Code auto-completion, Docstring completion, Next-line prediction, Code problem solving, Interactive coding, Function completion, Patch generation, Chart-to-code generation, Binary code decompilation, Action execution program generation, Evaluation program generation, Visual program generation, Whole-function generation, Text-to-ES query generation, Repository-level code completion, Feature function generation, Stub file generation, Test case generation, Text-to-SQL generation, Backend application generation, Incremental SQL generation, Multi-agent system generation, Program generation, Standalone function implementation, Python code generation, SQL query generation, SQL generation, Text-to-SQL conversion, NL2SQL, Database query generation, Verilog code generation, Program synthesis, Code synthesis, Symbolic regression, Mathematical function learning, Sequential edit generation, Policy-to-code translation, EDA code generation, LaTeX code generation, Cone code generation, Code comprehension and generation, Data visualization code generation, Mockup-to-code generation, Game code generation, Heuristic function generation, Text-to-Python generation, ORM code generation, Text-to-SQL parsing, Text-to-SQL, Code translation, Code infilling, Chart code generation, Reference image to slide generation, Slide code generation, Prolog program generation, Text-to-visualization generation, Visualization code generation, SQL trigger generation, SQL UPDATE generation, SQL query execution  

## State of the Field

Code generation is prevalently defined across the surveyed literature as the task of producing functional source code from a natural language description. The field operationalizes this behavior in numerous ways, including completing partially written code snippets (code completion, code infilling), translating natural language into database queries (Text-to-SQL), generating unit tests, and producing code patches to resolve software issues. A smaller body of work frames it as generating code from visual inputs like charts or mockups, translating between programming languages, or synthesizing entire programs for tasks like symbolic regression and backend application development. Across the provided papers, this behavior is most commonly measured using the HumanEval and MBPP benchmarks, which evaluate a model's ability to generate correct Python functions from docstrings and problem descriptions. Other frequently used instruments include APPS and LiveCodeBench for more complex, competition-level problems, and Spider for the specific sub-task of SQL generation. The behavior is also evaluated in contexts of long-form code completion with LongBench, repository-level patch generation with SWE-bench, and multi-turn conversational coding with MT-Bench. Code generation is often studied alongside programming ability and algorithmic reasoning, and some work suggests that capabilities like chain-of-thought reasoning and schema linking can influence its performance.

## Sources

**[Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition](https://proceedings.iclr.cc/paper_files/paper/2025/file/916ee60e315531d6b3954af8a8dc3437-Paper-Conference.pdf) (as "Docstring completion")**
> A code-related task that involves generating a documentation string (docstring) for a given function or code block.

**[Let the Code LLM Edit Itself When You Edit the Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/9530635032b95cea9585bd800d308300-Paper-Conference.pdf) (as "Next-line prediction")**
> Given code context, the model predicts the next line or next token to complete the snippet.

**[The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/9aa4e5caaf6d62767787500ee487c7fb-Paper-Conference.pdf) (as "Code problem solving")**
> The task of generating functionally correct code that solves a given programming problem, typically described in natural language.

**[PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf) (as "Code auto-completion")**
> The task of predicting and generating the next segment of code based on the current context.

**[Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf)**
> The task of producing functional source code in a programming language based on a natural language description or other specifications.

**[CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf) (as "Code completion")**
> The task of generating or selecting code to complete a partially written snippet based on requirements.

**[Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf) (as "Interactive coding")**
> The task of solving filesystem manipulation problems by issuing a sequence of Bash commands in an interactive terminal.

**[TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/26ded5c8ee8ec1bc4caced4e1c9b1584-Paper-Conference.pdf) (as "Unit test generation")**
> Generating an entire unit test suite for a file under test from the provided prompt context.

**[To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf) (as "Function completion")**
> A specific code generation task where the model must complete the body of a function given its signature and docstring.

**[SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf) (as "Patch generation")**
> The observable action of producing a set of code changes (a patch) intended to resolve a software issue.

**[ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf) (as "Chart-to-code generation")**
> Generating executable code from a chart image and textual instruction so that the code reproduces or modifies the chart.

**[Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef283d62b4bce30854a8d4827f331229-Paper-Conference.pdf) (as "Binary code decompilation")**
> Recovering higher-level source code from assembly code given an instruction prompt.

**[Advancing Collaborative Debates with Role Differentiation through Multi-Agent Reinforcement Learning](https://aclanthology.org/2025.acl-long.1106.pdf) (as "Visual program generation")**
> The task of generating code for a visual programming language, typically in a text-based format like XML, JSON, or a metaprogram, based on a user's natural language instruction.

**[SOTOPIA-Ω: Dynamic Strategy Injection Learning and Social Instruction Following Evaluation for Social Agents](https://aclanthology.org/2025.acl-long.1204.pdf) (as "Whole-function generation")**
> Generating complete function bodies from natural language descriptions and repository context, as opposed to single-line or partial code completions.

**[Shaping the Safety Boundaries: Understanding and Defending Against Jailbreaks in Large Language Models](https://aclanthology.org/2025.acl-long.1234.pdf) (as "Action execution program generation")**
> Producing a Python program that satisfies a user's natural language request by composing primitives from an assistant library, including proper use of control flow and function calls.

**[Shaping the Safety Boundaries: Understanding and Defending Against Jailbreaks in Large Language Models](https://aclanthology.org/2025.acl-long.1234.pdf) (as "Evaluation program generation")**
> Generating a program that executes an action execution program and verifies its correctness through assertions that check goal completion and absence of side effects.

**[Safer or Luckier?LLMs as Safety Evaluators Are Not Robust to Artifacts](https://aclanthology.org/2025.acl-long.971.pdf) (as "Text-to-ES query generation")**
> The specific task of converting a natural language question into an executable Elasticsearch (ES) query, which may include both a DSL query body and post-processing code.

**[LV-XAttn: Distributed Cross-Attention for Long Visual Inputs in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25c/chang25c.pdf) (as "Repository-level code completion")**
> The task of generating code completions based on the context of an entire software repository.

**[ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25at/chen25at.pdf) (as "Feature function generation")**
> The observable action of generating structured, executable code, specifically Python functions, that represents task-relevant features based on multimodal inputs.

**[TypyBench: Evaluating LLM Type Inference for Untyped Python Repositories](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25l/dong25l.pdf) (as "Stub file generation")**
> Producing a .pyi file containing only type annotations for functions and variables in a corresponding untyped Python file, preserving the original function signatures without implementation.

**[MONA: Myopic Optimization with Non-myopic Approval Can Mitigate Multi-step Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/farquhar25a/farquhar25a.pdf) (as "Test case generation")**
> The observable behavior of an LLM writing input/output test cases to formalize a programming problem before solving it.

**[Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf) (as "Text-to-SQL generation")**
> The task of converting a natural language question into a structured SQL query that can be executed against a database.

**[GRAIL: Graph Edit Distance and Node Alignment using LLM-Generated Code](https://raw.githubusercontent.com/mlresearch/v267/main/assets/verma25a/verma25a.pdf) (as "Program generation")**
> The process by which the LLM produces executable code that computes or approximates Graph Edit Distance based on input graph pairs.

**[BaxBench: Can LLMs Generate Correct and Secure Backends?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vero25a/vero25a.pdf) (as "Backend application generation")**
> Producing a complete, self-contained backend application with multiple files and functions that implements specified API endpoints and handles requests correctly.

**[MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf) (as "Multi-agent system generation")**
> The task of generating an executable code representation of a multi-agent system based on a natural language user query.

**[Structure-Guided Large Language Models for Text-to-SQL Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25k/zhang25k.pdf) (as "Incremental SQL generation")**
> The process of generating a complex SQL query step-by-step, often by decomposing the problem into smaller sub-tasks or syntax components.

**[Synthesizing Software Engineering Data in a Test-Driven Manner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cn/zhang25cn.pdf) (as "Standalone function implementation")**
> The task of writing a single, self-contained function based on a given specification, without dependencies on a larger codebase.

**[Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf) (as "Python code generation")**
> The task of generating Python code, particularly for data science applications, to solve a problem specified in natural language and via test cases.

**[EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/a291dad965af9bc2e39ffeb2ca1c6dc0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "SQL query generation")**
> The task of creating a structured query language (SQL) query based on information extracted from natural language text to retrieve data from a database.

**[CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf) (as "SQL generation")**
> The observable behavior of an LLM producing a structured query language (SQL) program in response to a natural language query and a table schema.

**[StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Text-to-SQL conversion")**
> The task of generating correct SQL code from a user's natural language query about a database.

**[Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf) (as "NL2SQL")**
> The task of translating a natural language question into a corresponding SQL query, given a specific database schema and content.

**[Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf) (as "Database query generation")**
> The task of generating correct database queries (e.g., SQL) to retrieve or manipulate data based on a natural language request.

**[CraftRTL: High-quality Synthetic Data Generation for Verilog Code Models with Correct-by-Construction Non-Textual Representations and Targeted Code Repair](https://proceedings.iclr.cc/paper_files/paper/2025/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf) (as "Verilog code generation")**
> The task of producing functionally correct Verilog code from a natural language or non-textual problem description.

**[Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf) (as "Program synthesis")**
> Generating executable programs that implement environment dynamics or solve coding problems from specifications and examples.

**[LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf) (as "Code synthesis")**
> Generating scripts that implement source/sink extraction or path-condition solving using external libraries and solvers.

**[Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf) (as "Symbolic regression")**
> The task of searching for a compact, programmatic mathematical expression that best explains a given dataset of input-output examples.

**[Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf) (as "Mathematical function learning")**
> The observable behavior of a model predicting the output of a mathematical function for a given input, after being provided with several input-output examples of that function in context.

**[Training Language Models on Synthetic Edit Sequences Improves Code Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43f900f571de6c96a70d5724a0fb565-Paper-Conference.pdf) (as "Sequential edit generation")**
> The observable process of generating a program as a sequence of incremental insertion edits, rather than producing the entire program in a single pass.

**[Structuring Radiology Reports: ChallengingLLMs with Lightweight Models](https://aclanthology.org/2025.emnlp-main.393.pdf) (as "Policy-to-code translation")**
> The specific task of converting natural language policy documents into executable functions in a programming language.

**[Sparse Neurons Carry Strong Signals of Question Ambiguity inLLMs](https://aclanthology.org/2025.emnlp-main.814.pdf) (as "LaTeX code generation")**
> The task of generating compilable LaTeX source code from a textual description or prompt.

**[DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset forLLM-based Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.836.pdf) (as "EDA code generation")**
> The task of automatically producing executable Python code to perform Exploratory Data Analysis (EDA) on a given dataset.

**[GuessingGame: Measuring the Informativeness of Open-Ended Questions in Large Language Models](https://aclanthology.org/2025.emnlp-main.877.pdf) (as "Cone code generation")**
> Generating HDL code for combinational logic cones that determine the next state of a register, based on functional descriptions and I/O constraints.

**[Memorization≠Understanding: Do Large Language Models Have the Ability of Scenario Cognition?](https://aclanthology.org/2025.emnlp-main.1048.pdf) (as "Code comprehension and generation")**
> The observable task of understanding and producing computer code based on a natural language prompt.

**[Supervised Attention Mechanism for Low-quality Multimodal Data](https://aclanthology.org/2025.emnlp-main.1085.pdf) (as "Coding")**
> The task of generating executable source code in a programming language based on a natural language description.

**[HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings inLatinAmerica](https://aclanthology.org/2025.emnlp-main.1276.pdf) (as "Mockup-to-code generation")**
> The task of generating structured HTML and CSS code from a visual representation of a webpage, such as a hand-drawn sketch or a digital mockup.

**[DPED: Multi-Layer Noise Distillation for Privacy-Preserving Text Embeddings](https://aclanthology.org/2025.emnlp-main.1283.pdf) (as "Data visualization code generation")**
> The observable task of producing executable code that creates a data plot or visualization based on a natural language prompt.

**[Too Helpful, Too Harmless, Too Honest or Just Right?](https://aclanthology.org/2025.emnlp-main.1511.pdf) (as "Game code generation")**
> Producing executable game code from a natural-language description of game mechanics.

**[Too Helpful, Too Harmless, Too Honest or Just Right?](https://aclanthology.org/2025.emnlp-main.1511.pdf) (as "Heuristic function generation")**
> Converting natural language strategies into executable Python functions that score candidate actions based on game state.

**[Aligning Text/Speech Representations from Multimodal Models withMEGBrain Activity During Listening](https://aclanthology.org/2025.emnlp-main.1749.pdf) (as "Text-to-Python generation")**
> Generating Python code from natural language instructions to perform data processing, computation, or reasoning tasks not easily expressible in SQL.

**[Towards Robust Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1795.pdf) (as "Data transformation")**
> Generating executable code to transform tabular data based on natural language instructions or input-output examples.

**[A ComprehensiveLiteraryChinese Reading Comprehension Dataset with an Evidence Curation Based Solution](https://aclanthology.org/2025.emnlp-main.178.pdf) (as "ORM code generation")**
> The task of generating Object Relational Mapping (ORM) code from a natural language question, which serves as a dialect-agnostic intermediate representation.

**[Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.34.pdf) (as "Text-to-SQL parsing")**
> The task of converting a natural language question into a formal SQL query that can be executed against a relational database.

**[Subtle Risks, Critical Failures: A Framework for Diagnosing Physical Safety ofLLMs for Embodied Decision Making](https://aclanthology.org/2025.emnlp-main.1306.pdf) (as "Text-to-SQL")**
> Generating SQL queries from natural language prompts.

**[Addressing Tokenization Inconsistency in Steganography and Watermarking Based on Large Language Models](https://aclanthology.org/2025.emnlp-main.362.pdf) (as "Code translation")**
> The observable task of converting a source code snippet from one programming language into a functionally equivalent snippet in another programming language.

**[SUE: Sparsity-based Uncertainty Estimation via Sparse Dictionary Learning](https://aclanthology.org/2025.emnlp-main.1672.pdf) (as "Code infilling")**
> The task of generating a missing segment of code given the preceding (prefix) and subsequent (suffix) contexts.

**[Semantic Inversion, Identical Replies: Revisiting Negation Blindness in Large Language Models](https://aclanthology.org/2025.emnlp-main.1089.pdf) (as "Chart code generation")**
> Producing executable code (e.g., Python with matplotlib) that renders a data table into a visual chart according to specified conditions.

**[Accelerate Parallelizable Reasoning via Parallel Decoding within One Sequence](https://aclanthology.org/2025.emnlp-main.458.pdf) (as "Reference image to slide generation")**
> The task of automatically generating executable code to create an editable slide that is visually and structurally consistent with a given reference image.

**[Accelerate Parallelizable Reasoning via Parallel Decoding within One Sequence](https://aclanthology.org/2025.emnlp-main.458.pdf) (as "Slide code generation")**
> Producing Python code using the python-pptx library that, when executed, generates a slide matching a reference image in layout and visual appearance.

**[Improving Multilingual Retrieval-Augmented Language Models through Dialectic Reasoning Argumentations](https://aclanthology.org/2025.emnlp-main.462.pdf) (as "Prolog program generation")**
> The production of an executable Prolog program that encodes logical constraints from a math problem and yields a symbolic answer upon execution.

**[SEMMA: A Semantic Aware Knowledge Graph Foundation Model](https://aclanthology.org/2025.emnlp-main.1622.pdf) (as "Text-to-visualization generation")**
> Producing visualization code and a chart from a natural-language query and data table.

**[SEMMA: A Semantic Aware Knowledge Graph Foundation Model](https://aclanthology.org/2025.emnlp-main.1622.pdf) (as "Visualization code generation")**
> Producing executable Python code using libraries like Matplotlib or Seaborn to generate a chart from a data table and natural language query.

**[A Knowledge-driven Adaptive Collaboration ofLLMs for Enhancing Medical Decision-making](https://aclanthology.org/2025.emnlp-main.1700.pdf) (as "SQL trigger generation")**
> The task of automatically creating SQL TRIGGER scripts that maintain data consistency for derived or aggregate metrics in response to data modification events.

**[A Knowledge-driven Adaptive Collaboration ofLLMs for Enhancing Medical Decision-making](https://aclanthology.org/2025.emnlp-main.1700.pdf) (as "SQL UPDATE generation")**
> Producing SQL UPDATE statements from natural language instructions and schema information.

**[Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.511.pdf) (as "SQL query execution")**
> The observable behavior of processing and correctly executing SQL queries on database tables.

## Relationships

### Code generation →
- **HumanEval** (measurements) — *measured_by*
  > Code-Completion (CC): Given an initial set of lines of a code, the model is prompted to complete the code snippet. ... We perform zero-shot evaluations on HumanEval benchmark dataset (Chen et al., 2021) and report the Pass@1 (P@1) metric. (Section 4.3)
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
- **MBPP** (measurements) — *measured_by*
  > Text-to-Code (T2C): Given a textual context, the model is prompted to generate the corresponding code snippet. ... We perform 3-shot inference on the MBPP dataset (Austin et al., 2021) and report P@1. (Section 4.3)
  - [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf)
- **APPS** (measurements) — *measured_by*
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
- **LiveCodeBench** (measurements) — *measured_by*
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
- **Spider** (measurements) — *measured_by*
  > We use six datasets spanning different domains: GLUE for natural language understanding (Wang et al., 2019), DART for RDF-to-text generation (Nan et al., 2021), SAMSum (Gliwa et al., 2019) for summarization, Spider for text-to-SQL generation (Yu et al., 2018), and two vision datasets—CIFAR-10 (Krizhevsky et al., 2009) and CelebA (Liu et al., 2015), with the vision datasets processed by cropping, resizing, and flattening pixel values into space-separated numerical sentences.
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BIRD** (measurements) — *measured_by*
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BigCodeBench** (measurements) — *measured_by*
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **DS-1000** (measurements) — *measured_by*
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
- **MultiPL-E** (measurements) — *measured_by*
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
- **EvalPlus** (measurements) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
- **SWE-bench** (measurements) — *measured_by*
  > A notable example is SWE-bench (Jimenez et al., 2024), which assesses the ability of agents to generate patches to resolve real-world GitHub issues. (Section 1)
  - [RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph](https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf)
- **CodeContests** (measurements) — *measured_by*
  - [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.189.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **bigcode-evaluation-harness** (measurements) — *measured_by*
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **TACO** (measurements) — *measured_by*
  - [Learning How Hard to Think: Input-Adaptive Allocation of LM Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf)
- **LeetCode Contest** (measurements) — *measured_by*
  - [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf)
- **Codeforces** (measurements) — *measured_by*
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Faithfulness** (constructs) — *causes*
  - [Structure-Guided Large Language Models for Text-to-SQL Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25k/zhang25k.pdf)
- **CoSQL** (measurements) — *measured_by*
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LeetCode** (measurements) — *measured_by*
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  - [Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pourcel25a/pourcel25a.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  - [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf)
- **AgentBench** (measurements) — *measured_by*
  - [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf)
- **CodeSearchNet** (measurements) — *measured_by*
  - [Selective Aggregation for Low-Rank Adaptation in Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53a37f820d5be5930415d964f4a0187-Paper-Conference.pdf)
- **GUI automation** (behaviors tasks) — *causes*
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **ChartMimic** (measurements) — *measured_by*
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
- **ClassEval** (measurements) — *measured_by*
  - [Multi-task Adversarial Attacks against Black-box Model with Few-shot Queries](https://aclanthology.org/2025.acl-long.685.pdf)
- **Instruction understanding** (constructs) — *causes*
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
- **HumanEvalPack** (measurements) — *measured_by*
  - [Internal Chain-of-Thought: Empirical Evidence for Layer‐wise Subtask Scheduling inLLMs](https://aclanthology.org/2025.emnlp-main.1148.pdf)
- **Image editing** (behaviors tasks) — *causes*
  - [ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
- **WebMMU** (measurements) — *measured_by*
  - [2025.emnlp-main.1276.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1276.checklist.pdf)

### → Code generation
- **Schema linking** (behaviors tasks) — *causes*
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf)
- **Codeforces** (measurements) — *measured_by*
  - [To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *causes*
  - [Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf)
- **Task decomposition** (behaviors tasks) — *causes*
  - [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [Mixture of Attentions For Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f31bf160569618084ba9bdc2a8de29d0-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Are Large Language Models Ready for Multi-Turn Tabular Data Analysis?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aj/li25aj.pdf)
- **Table understanding** (behaviors tasks) — *measured_by*
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)
- **GUI understanding** (constructs) — *causes*
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **Expressive power** (constructs) — *causes*
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **Synthetic data generation** (behaviors tasks) — *causes*
  - [Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e0bfe8bbaa0e70809f0a8ccd9c2ff3e-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *causes*
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
- **Semantic parsing** (behaviors tasks) — *causes*
  - [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Self-reflection** (behaviors tasks) — *causes*
  - [ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25at/chen25at.pdf)
- **Plan generation** (behaviors tasks) — *causes*
  - [Code-Generated Graph Representations Using Multiple LLM Agents for Material Properties Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25an/huang25an.pdf)

### Associated with
- **Reasoning** (constructs)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Programming** (behaviors tasks)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
- **Tool use** (behaviors tasks)
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Critique** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  - [Test-Time Training on Nearest Neighbors for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f02f1185b97518ab5bd7ebde466992d3-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
- **Algorithmic reasoning** (constructs)
  - [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf)
- **Structural reasoning** (constructs)
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
- **Data transformation** (behaviors tasks)
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
- **Generalization** (constructs)
  > ...the generalization abilities of the pre-trained model (i.e., code comprehension, instruction-following, code generation, etc.). (Section 4)
  - [Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dt/li25dt.pdf)
- **Semantic parsing** (behaviors tasks)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.289.pdf)
- **Self-correction** (behaviors tasks)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coding** (behaviors tasks)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Inductive reasoning** (constructs)
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **State tracking** (constructs)
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs)
  - [RAG-SR: Retrieval-Augmented Generation for Neural Symbolic Regression](https://proceedings.iclr.cc/paper_files/paper/2025/file/19a8e70828c01059631f913442ae31e6-Paper-Conference.pdf)
- **Joint prediction** (behaviors tasks)
  - [Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [UI-Hawk: Unleashing the Screen Stream Understanding for MobileGUIAgents](https://aclanthology.org/2025.emnlp-main.921.pdf)
- **Schema linking** (behaviors tasks)
  - [OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **Faithfulness** (constructs)
  - [Removal of Hallucination on Hallucination: Debate-AugmentedRAG](https://aclanthology.org/2025.acl-long.771.pdf)
- **Natural language understanding** (constructs)
  - [Iterative Multilingual Spectral Attribute Erasure](https://aclanthology.org/2025.emnlp-main.1489.pdf)
- **Chart generation** (behaviors tasks)
  - [Sharpness-Aware Minimization for Topic Models with High-Quality Document Representations](https://aclanthology.org/2025.naacl-long.232.pdf)
- **Long-context processing** (constructs)
  - [Beyond Logits: Aligning Feature Dynamics for Effective Knowledge Distillation](https://aclanthology.org/2025.acl-long.1126.pdf)
