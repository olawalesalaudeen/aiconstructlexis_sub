# Memory management
**Type:** Construct  
**Referenced in:** 4 papers  
**Also known as:** Context management, Sustained context management  

## State of the Field

The most common framing of memory management is an agent's ability to store, retrieve, summarize, and update past experiences to inform later decisions. Some work uses the term "sustained context management" to emphasize maintaining relevant information across multiple conversational turns, while a more specialized view of "context management" focuses on filtering irrelevant data during code exploration to prevent misleading the agent. This construct is primarily operationalized and measured using the Berkeley Function Calling Leaderboard (BFCL), which assesses it through multi-turn queries. The evaluation specifically probes a model's ability to "accurately retrieve, add, overwrite, or delete information" from a stored snapshot, independent of the immediate chat history. This is presented as a difficult task, with one paper noting that current models achieve low accuracy. Memory management is studied alongside information retrieval and is reported in one paper to be a cause of self-correction. Within some agent frameworks, it is described as the "foundation" for accumulating historical experience.

## Sources

**[Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](https://proceedings.neurips.cc/paper_files/paper/2024/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)**
> The ability to store, retrieve, summarize, and update past experiences so they can inform later decisions.

**[The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf) (as "Sustained context management")**
> The ability to maintain relevant conversational or task context across multiple turns and use it correctly in later actions.

**[OrcaLoca: An LLM Agent Framework for Software Issue Localization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25x/yu25x.pdf) (as "Context management")**
> The ability of an LLM agent to maintain a relevant and concise working context during code exploration by filtering out irrelevant or redundant information that could mislead the localization process.

## Relationships

### Memory management →
- **Self-correction** (behaviors tasks) — *causes*
  - [Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](https://proceedings.neurips.cc/paper_files/paper/2024/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
- **BFCL** (measurements) — *measured_by*
  > "the ‘multi-turn’ featuring eight curated API suites and 1000 queries, assessing sustained context management and dynamic decision-making"
  - [The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)

### Associated with
- **Information retrieval** (behaviors tasks)
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
