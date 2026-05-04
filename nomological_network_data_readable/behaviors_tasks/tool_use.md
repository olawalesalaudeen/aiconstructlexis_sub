# Tool use
**Type:** Behavior  
**Referenced in:** 161 papers  
**Also known as:** Tool calling, Tool usage, Tool invocation, Dependency invocation, Tool-integrated reasoning, Function calling, API call generation, Tool execution, API selection, Paragraph understanding, Multi-step tool calling, API chaining, Multi-API calling, Single-API calling, Dependent function calling, Parallel function calling, Tool usage updating, Code generation and execution, API interaction, Remote server interaction, API invocation generation, API call selection, API calling, Task-oriented semantic parsing, Tool utilization capability, Tool-use proficiency, Tool utilization, Tool-use capability, Tool Use, Tool-use ability, Tool-usage reasoning, Tool learning, Tool comprehension, Tool-using capability, Flexible tool selection, Tool manipulation, Tool-calling capability, Tool-calling decision-making, Function-calling capability, Tool-using ability, Planning with functions, API call generation capability, Function Calling, Function-calling ability, Nested tool calling, Meta-learning, Constructional knowledge, Learning capacity, Learnable potential, Contextualised tool use  

## State of the Field

Across the surveyed literature, 'Tool use' is characterized in two primary ways: as an observable behavior involving the invocation of external systems, and as a latent capability of a model to effectively leverage those systems. The most prevalent framing treats it as the observable action of an agent calling external tools, frequently referred to as 'tool calling' or 'function calling'. This behavior involves generating formatted requests, such as API calls or code snippets, to interact with systems like calculators, search engines, or code interpreters to solve sub-problems or access information beyond the model's parametric knowledge. A substantial body of work also defines it as a latent 'tool-use capability' or 'function-calling ability', focusing on the underlying capacity to select the appropriate tool, formulate correct invocations, and process the outputs. To operationalize and measure this behavior, researchers employ a wide array of benchmarks, with some of the most frequently cited being ToolBench, which provides a large-scale set of real-world APIs, and BFCL (the Berkeley Function Calling Leaderboard), which evaluates performance across various function-calling scenarios. Other instruments mentioned include API-Bank, GAIA, and BigCodeBench, which assess different facets of tool interaction. The study of tool use is commonly situated alongside research into planning and chain-of-thought reasoning, as models must often decompose tasks and perform multi-step decision-making to sequence tool invocations. The literature distinguishes between different levels of complexity, from 'single-API calling' to more intricate behaviors like 'API chaining', 'dependent function calling', and 'parallel function calling'. While the dominant focus is on API and code execution, a few definitions frame tool use more broadly, including interactions with RL pipelines or as a form of 'task-oriented semantic parsing'.

## Sources

**[RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)**
> The behavior of invoking and utilizing an external capability or system, such as an RL training pipeline, to solve a sub-problem.

**[Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0f7ee1901fef1da4dae2b88dfd43195-Paper-Conference.pdf) (as "Tool calling")**
> The observable action of executing a chosen tool with specific parameters, typically by generating a formatted API request.

**[Unlocking the Capabilities of Thought: A Reasoning Boundary Framework to Quantify and Optimize Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/62ab1c2cb4b03e717005479efb211841-Paper-Conference.pdf) (as "Tool usage")**
> Using external tools during reasoning to perform computations or other operations.

**[UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf) (as "Tool invocation")**
> The action of calling external, specialized functions, such as a distance calculator or geohash encoder, to obtain information needed for a reasoning process.

**[EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Dependency invocation")**
> The observable behavior of a model generating code that calls or uses other functions, classes, or modules defined within the provided context.

**[Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf) (as "Tool-integrated reasoning")**
> The behavior of solving problems by generating and executing code or using other external tools as part of the reasoning process.

**[Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf) (as "Function calling")**
> The task of identifying when to use external tools or APIs based on a user's request and generating the correct function calls with appropriate arguments.

**[Gorilla: Large Language Model Connected with Massive APIs](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4c61f578ff07830f5c37378dd3ecb0d-Paper-Conference.pdf) (as "API call generation")**
> The task of producing a syntactically and semantically correct API call based on a natural language instruction.

**[ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf) (as "API selection")**
> Choosing the appropriate API from a candidate tool list for a user request.

**[Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf) (as "Paragraph understanding")**
> The observable task of reading a paragraph and answering a question based on its content.

**[An Intelligent Agentic System for Complex Image Restoration Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/921ac785fa9edc73cacaf2664f43d234-Paper-Conference.pdf) (as "Tool execution")**
> Sequentially applying specific IR models or tools to the image according to the planned operations.

**[ToolDial: Multi-turn Dialogue Generation Method for Tool-Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afb27164624b641e8fbba961b2301acf-Paper-Conference.pdf) (as "API chaining")**
> The observable behavior of calling multiple APIs in sequence where one API's output serves as another's input.

**[AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c493d23af93118975cdbc32cbe7323f5-Paper-Conference.pdf) (as "Multi-step tool calling")**
> Executing several tool calls in sequence, often with dependencies between calls, to satisfy a request.

**[Understanding the Generalization of In-Context Learning in Transformers: An Empirical Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd19ca8039547b339a6a37bd4df24405-Paper-Conference.pdf) (as "Single-API calling")**
> A specific tool-calling task that requires only a single API invocation to fulfill the user's instruction.

**[Understanding the Generalization of In-Context Learning in Transformers: An Empirical Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd19ca8039547b339a6a37bd4df24405-Paper-Conference.pdf) (as "Multi-API calling")**
> A complex tool-calling task that requires the combined use of multiple API invocations to achieve a desired functionality.

**[ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf) (as "Dependent function calling")**
> A specific type of function calling where the model makes a sequence of API calls, where the output of one call is used as the input for a subsequent call.

**[ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf) (as "Parallel function calling")**
> A specific type of function calling where the model makes multiple, independent API calls simultaneously to fulfill a user request.

**[Learning Evolving Tools for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d8d1d325f822e07d16866780cc23deb2-Paper-Conference.pdf) (as "Tool usage updating")**
> The observable process of a model summarizing the usage of a new or changed tool and incorporating that new definition into its available tool set, often within the prompt context.

**[Unifying Uniform and Binary-coding Quantization for Accurate Compression of Large Language Models](https://aclanthology.org/2025.acl-long.1383.pdf) (as "Code generation and execution")**
> The behavior of writing and running code to perform computations or other programmatic tasks as part of a larger problem-solving process.

**[EnIGMA: Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramovich25a/abramovich25a.pdf) (as "Remote server interaction")**
> The observable action of an agent using a tool to initiate, maintain, and terminate connections with an external server to send and receive data.

**[MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dihan25a/dihan25a.pdf) (as "API interaction")**
> Generating valid API queries, processing structured responses, and using the retrieved data to support reasoning and answer formulation.

**[CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25t/wang25t.pdf) (as "API invocation generation")**
> The observable behavior of generating a specific line or block of code that calls a function, method, or class initializer from an external library.

**[DSG-MCTS: A Dynamic Strategy-GuidedMonteCarlo Tree Search for Diversified Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.533.pdf) (as "API call selection")**
> Selecting and generating the appropriate API invocation based on a multi-modal user query, such as one involving an image reference.

**[TIDES: Technical Information Discovery and Extraction System](https://aclanthology.org/2025.emnlp-main.1104.pdf) (as "API calling")**
> The model generates function calls with arguments to invoke external tools in response to a user request.

**[ReviewRL: Towards Automated Scientific Review withRL](https://aclanthology.org/2025.emnlp-main.858.pdf) (as "Task-oriented semantic parsing")**
> Converting natural-language user requests into structured machine-readable representations such as API calls.

**[GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf) (as "Tool-use proficiency")**
> The general capability of an AI system to effectively select and utilize external tools, such as web browsers or code interpreters, to accomplish tasks.

**[AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf) (as "Tool utilization capability")**
> The model's latent ability to effectively select and use external tools to solve complex problems.

**[Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf) (as "Tool utilization")**
> The latent ability to select and invoke external tools appropriately during task execution.

**[GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Tool-use capability")**
> The ability of a large language model to effectively select, invoke, and coordinate external tools to solve complex tasks.

**[MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf) (as "Tool-use ability")**
> The latent capacity of an LLM to choose, call, and use external tools appropriately to satisfy user requests across dialogue settings.

**[Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf) (as "Tool Use")**
> The latent ability to interact with external tools and APIs, including functions such as web browsing, code execution, and file uploads.

**[Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf) (as "Tool-usage reasoning")**
> The latent ability to choose and sequence external tools effectively when solving multi-modal tasks.

**[Tool-Planner: Task Planning with Clusters across Multiple Tools](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f605d59a0dbde101518b552cb616ddf-Paper-Conference.pdf) (as "Tool learning")**
> The capability of an LLM to understand and utilize external tools or APIs to solve problems that it cannot complete independently.

**[From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf) (as "Tool comprehension")**
> The degree to which an LLM understands what a tool does, when to invoke it, and how to use it correctly from documentation and feedback.

**[From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf) (as "Tool-using capability")**
> The latent ability of an LLM to effectively leverage external tools to solve complex real-world tasks.

**[ReasVQA: AdvancingVideoQAwith Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.83.pdf) (as "Tool manipulation")**
> The skill of interacting with and controlling external tools or APIs, typically by generating code or commands.

**[PAPILLON: Privacy Preservation fromInternet-based and Local Language Model Ensembles](https://aclanthology.org/2025.naacl-long.174.pdf) (as "Tool-calling decision-making")**
> The latent ability of a model to determine whether to call a tool, ask for more information, admit inability to answer, or generate a direct response based on the availability and relevance of tools and input completeness.

**[PROMPTEVALS: A Dataset of Assertions and Guardrails for Custom Production Large Language Model Pipelines](https://aclanthology.org/2025.naacl-long.214.pdf) (as "Tool-calling capability")**
> The model's latent ability to understand user requests, select appropriate external tools, formulate correct API calls, and process their outputs.

**[Are We Done withMMLU?](https://aclanthology.org/2025.naacl-long.263.pdf) (as "Flexible tool selection")**
> The ability to dynamically and accurately choose the most appropriate tool from a large and complex toolkit based on the specific requirements of a given task or scenario.

**[LLMBraces: Straightening OutLLMPredictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.394.pdf) (as "Function-calling capability")**
> The underlying ability of a large language model to generate appropriate function calls based on natural language input and a provided list of available functions.

**[MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bc/zhang25bc.pdf) (as "Tool-using ability")**
> The underlying capability of agents within a system to interact with external tools (e.g., code interpreter, search engine) to extend their functional scope and access real-world data.

**[API Pack: A Massive Multi-Programming Language Dataset for API Call Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ca1cca58101545e937302be7050098-Paper-Conference.pdf) (as "API call generation capability")**
> The model's latent ability to produce syntactically and semantically correct code snippets for invoking APIs based on natural language instructions.

**[Facilitating Multi-turn Function Calling for LLMs via Compositional Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/69c49f75ca31620f1f0d38093d9f3d9b-Paper-Conference.pdf) (as "Planning with functions")**
> The cognitive capability to decompose complex tasks into manageable steps and determine the appropriate sequence of function calls required to solve them.

**[ACCORD: Closing the Commonsense Measurability Gap](https://aclanthology.org/2025.naacl-long.194.pdf) (as "Function Calling")**
> An agentic evaluation setup in which the model interacts with the environment through Python wrapper functions that call CRM APIs.

**[Are We Done withMMLU?](https://aclanthology.org/2025.naacl-long.263.pdf) (as "Nested tool calling")**
> The ability to recursively invoke additional tools during task execution when initial tools or information are insufficient, enabling resolution of complex dependencies such as unit mismatches or missing parameters.

**[Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.578.pdf) (as "Function-calling ability")**
> The latent capacity of a model to correctly interpret user queries and generate valid function calls with appropriate arguments, given a set of available tools.

**[Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.727.pdf) (as "Meta-learning")**
> The latent capacity of a model to rapidly adapt to new tasks by leveraging previously acquired abstract strategies, enabling fast and effective learning from limited data.

**[SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.113.pdf) (as "Constructional knowledge")**
> The ability of a model to learn and represent constructions, defined as conventionalized form-meaning pairings in a language.

**[What Makes a Good Reasoning Chain? Uncovering Structural Patterns in Long Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.330.pdf) (as "Learning capacity")**
> The model's ability to absorb task-specific information during fine-tuning and translate it into improved downstream performance.

**[Learning Like Humans: AdvancingLLMReasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation](https://aclanthology.org/2025.emnlp-main.337.pdf) (as "Learnable potential")**
> A measure of how much additional knowledge a model can acquire in a given domain, estimated by the gap between current performance and a mastery ceiling defined by a reference model.

**[What You See is What You Ask: Evaluating Audio Descriptions](https://aclanthology.org/2025.emnlp-main.1200.pdf) (as "Contextualised tool use")**
> The specific ability to use tools effectively by integrating information from the conversational history and user profile.

## Relationships

### Tool use →
- **ToolBench** (measurements) — *measured_by*
  > Projects like the Berkeley Function Calling Leaderboard (BFCL), ToolBench and MetaTool test tool use/function calling in multiple programming languages and propose various methods for evaluating the accuracy of function calls. (Section 2)
  - [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://proceedings.iclr.cc/paper_files/paper/2024/file/28e50ee5b72e90b50e7196fde8ea260e-Paper-Conference.pdf)
- **BFCL** (measurements) — *measured_by*
  > The evaluation datasets employed are sourced from open-source collections as reported in the Llama3 paper, which include MMLU(Hendrycks et al., 2021a), IFEval(Zhou et al., 2023), HumanEval(Chen et al., 2021), MBPP(Austin et al., 2021), GSM8K(Cobbe et al., 2021), MATH(Hendrycks et al., 2021b), ARC Challenge (Clark et al., 2018), GPQA (Rein et al., 2023), BFCL(Yan et al., 2024), API-Bank(Li et al., 2023), and MGSM(Shi et al., 2022).
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
- **API-Bank** (measurements) — *measured_by*
  > The evaluation datasets employed are sourced from open-source collections as reported in the Llama3 paper, which include MMLU(Hendrycks et al., 2021a), IFEval(Zhou et al., 2023), HumanEval(Chen et al., 2021), MBPP(Austin et al., 2021), GSM8K(Cobbe et al., 2021), MATH(Hendrycks et al., 2021b), ARC Challenge (Clark et al., 2018), GPQA (Rein et al., 2023), BFCL(Yan et al., 2024), API-Bank(Li et al., 2023), and MGSM(Shi et al., 2022).
  - [Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf)
- **GAIA** (measurements) — *measured_by*
  > We evaluate MaAS on six public benchmarks covering three domains: ... and (3) tool use, GAIA (Mialon et al., 2023) (Section 4.1).
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **BigCodeBench** (measurements) — *measured_by*
  > We introduce BigCodeBench, a new high-quality programming benchmark constructed via the collaboration between human experts and LLMs, assessing the capability of tool use and complex instruction following. (Section 6)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > Win Rate (Win%), which evaluates effectiveness through pairwise comparisons by a ChatGPT-based evaluator, capturing nuanced performance differences not reflected by rule-based metrics. (Section 3.1)
  - [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  - [Are We Done withMMLU?](https://aclanthology.org/2025.naacl-long.263.pdf)
- **Complex reasoning** (behaviors tasks) — *causes*
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **GTA** (measurements) — *measured_by*
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MetaTool** (measurements) — *measured_by*
  > Projects like the Berkeley Function Calling Leaderboard (BFCL), ToolBench and MetaTool test tool use/function calling in multiple programming languages and propose various methods for evaluating the accuracy of function calls. (Section 2)
  - [ShortcutsBench: A Large-Scale Real-world Benchmark for API-based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c16a99558b0b4f6b10966ca9bdb98ade-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)
- **Protein understanding** (behaviors tasks) — *causes*
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)
- **Planning** (constructs) — *causes*
  - [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf)
- **ToolQA** (measurements) — *measured_by*
  > ToolQA (Zhuang et al., 2024) evaluates agents’ abilities to use external tools. (§4.2.1)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **StableToolBench** (measurements) — *measured_by*
  - [Benchmarking Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/adbe936993aa7cf41e45054d8b72f183-Paper-Conference.pdf)
- **Seal-Tools** (measurements) — *measured_by*
  - [Robust Function-Calling for On-Device Language Model via Function Masking](https://proceedings.iclr.cc/paper_files/paper/2025/file/d45e0bfb5a39477d56b55c0824200008-Paper-Conference.pdf)
- **RestBench** (measurements) — *measured_by*
  - [JMMMU: AJapanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.44.pdf)
- **BFCL-v2** (measurements) — *measured_by*
  > We evaluated TOOLFLOW’s tool-calling ability on the BFCL. This dataset contains questions from four categories.
  - [PROMPTEVALS: A Dataset of Assertions and Guardrails for Custom Production Large Language Model Pipelines](https://aclanthology.org/2025.naacl-long.214.pdf)
- **ToolAlpaca** (measurements) — *measured_by*
  - [PROMPTEVALS: A Dataset of Assertions and Guardrails for Custom Production Large Language Model Pipelines](https://aclanthology.org/2025.naacl-long.214.pdf)
- **ToolQuery** (measurements) — *measured_by*
  - [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.578.pdf)
- **MMAU** (measurements) — *measured_by*
  > MMAU (Yin et al., 2024) evaluates agent capabilities across five domains—tool use, graph-based reasoning, data science, programming, and mathematics.
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **Affinity methods** (measurements) — *measured_by*
  - [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.113.pdf)

### → Tool use
- **In-context learning** (constructs) — *causes*
  - [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf)
- **Planning** (constructs) — *causes*
  - [GuideBench: Benchmarking Domain-Oriented Guideline Following forLLMAgents](https://aclanthology.org/2025.acl-long.558.pdf)
- **Instruction following** (constructs) — *causes*
  - [JMMMU: AJapanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.44.pdf)

### Associated with
- **In-context learning** (constructs)
  - [Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf)
- **Planning** (constructs)
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Chain-of-thought reasoning** (constructs)
  > we opt for the framework of the ReAct agent that performs step-by-step reasoning for tool usage based on observations of previous steps.
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Grounding** (constructs)
  - [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)
- **Reversal curse** (constructs)
  - [The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://proceedings.iclr.cc/paper_files/paper/2024/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf)
- **Code execution** (behaviors tasks)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Web navigation** (behaviors tasks)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Compositional reasoning** (constructs)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  - [Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf)
- **Refusal** (constructs)
  - [Robust Function-Calling for On-Device Language Model via Function Masking](https://proceedings.iclr.cc/paper_files/paper/2025/file/d45e0bfb5a39477d56b55c0824200008-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
- **Structured output generation** (behaviors tasks)
  > Model Compression Significantly Impacts Structured Output Generation. Our experimental results in Table 8 demonstrate significant performance variations between JSON and string format outputs under different compression techniques. The analysis reveals that model performance consistently degrades more severely when generating JSON-structured outputs compared to string formats.
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **BFCL** (measurements)
  - [PAPILLON: Privacy Preservation fromInternet-based and Local Language Model Ensembles](https://aclanthology.org/2025.naacl-long.174.pdf)
- **Prompt compression** (behaviors tasks)
  > “In agent, API documentation can be compressed to enable more efficient tool use”
  - [Yeah, Un, Oh: Continuous and Real-time Backchannel Prediction with Fine-tuning of Voice Activity Projection](https://aclanthology.org/2025.naacl-long.368.pdf)
- **Task execution** (constructs)
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
