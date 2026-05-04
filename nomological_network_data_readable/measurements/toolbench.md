# ToolBench
**Type:** Measurement  
**Referenced in:** 22 papers  
**Also known as:** Toolbench  

## State of the Field

ToolBench is predominantly characterized across the provided literature as a large-scale benchmark or dataset for evaluating large language models. Its most common application is to measure the construct of "Tool use," with papers using it to assess behaviors like API-calling accuracy, function calling, and multi-turn tool usage. The benchmark is also used, though less frequently, to evaluate an agent's "Decision-making" and "Information retrieval" capabilities. Operationally, ToolBench is consistently described as containing a massive set of over 16,000 real-world APIs, often sourced from RapidAPI, paired with diverse user requests, instructions, and in some cases, expert trajectories. While its prevailing use is for evaluation—with some papers reporting metrics like "pass rate, win rate, and success rate" ("JMMMU...")—a notable subset of papers also defines and uses ToolBench as an "instruction-tuning dataset" for training models. A few sources offer more specific framings, describing it as a "workload" with tool demonstrations ("Preble...") or a suite with environments like "Home Search, Trip Booking, Google Sheets, and Virtual Home" ("ToolChain*...").

## Sources

**[ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf)**
> A benchmark suite for evaluating the tool-use capabilities of LLM agents across various environments, including Home Search, Trip Booking, Google Sheets, and Virtual Home.

**[Preble: Efficient Distributed Prompt Scheduling for LLM Serving](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc342f48de8264779952fac378f96dc-Paper-Conference.pdf) (as "Toolbench")**
> A workload used to evaluate an LLM's ability to use tools, characterized by prompts that include tool demonstrations and calls.

## Relationships

### → ToolBench
- **Tool use** (behaviors tasks) — *measured_by*
  > Projects like the Berkeley Function Calling Leaderboard (BFCL), ToolBench and MetaTool test tool use/function calling in multiple programming languages and propose various methods for evaluating the accuracy of function calls. (Section 2)
  - [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://proceedings.iclr.cc/paper_files/paper/2024/file/28e50ee5b72e90b50e7196fde8ea260e-Paper-Conference.pdf)
- **Decision-making** (constructs) — *measured_by*
  > "we conduct extensive experiments on Game of 24 (Yao et al., 2023), WebShop (Yao et al., 2022a), ToolBench (Qin et al., 2023c) and RestBench (Song et al., 2023) datasets"
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **Planning** (constructs) — *measured_by*
  - [ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > Our experiments are based on ToolBench, a real-world tool benchmark containing more 16k tool collections... Our retrieval and end-to-end agent-tuning data are converted from the original data in ToolBench. (Section 4.1)
  - [ToolGen: Unified Tool Retrieval and Calling via Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b646bdebeb87dfafe2c6f77a63b564e1-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.578.pdf)
