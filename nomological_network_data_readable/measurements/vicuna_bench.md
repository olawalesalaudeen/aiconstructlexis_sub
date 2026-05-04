# Vicuna-Bench
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** Vicuna Bench, Vicuna-bench, Vicuna bench  

## State of the Field

Vicuna-Bench is a benchmark commonly used to evaluate the performance of Large Language Models, with a prevailing focus on conversational and instruction-following abilities. Across the provided literature, a recurring feature of its operationalization is the use of an automated judge, most frequently identified as GPT-4, to assess model responses to user prompts. One paper specifies that this evaluation involves comparing a model's output against a reference model such as gpt-3.5-turbo. The benchmark's data is described as consisting of user prompts, with sources mentioning "user-shared conversations" or a specific set of "80 single-turn chat prompts." While some definitions frame its purpose broadly, the more specific and common descriptions state it measures "chatbot capability" and "response quality on short-text, conversational tasks." The provided work also shows Vicuna-Bench being used to measure constructs such as `Commonsense knowledge`, `Evaluation`, and `Text generation`. In practice, it is frequently employed alongside other evaluation tools, with several papers mentioning it in conjunction with MT-Bench and AlpacaEval. The benchmark is also referred to as VicunaEval in some contexts.

## Sources

**[Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) (as "Vicuna Bench")**
> A benchmark for assessing LLM responses to user prompts, used to evaluate the correlation between evaluator models and human or GPT-4 scores.

**[SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)**
> Chatbot benchmark using user-shared conversations evaluated by GPT-4 to assess model performance in open-ended dialogue.

**[OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf) (as "Vicuna-bench")**
> A benchmark used to evaluate a model's instruction-following and conversational abilities, where model outputs are compared against a reference model (gpt-3.5-turbo) using GPT-4 as the judge.

**[SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf) (as "Vicuna bench")**
> A benchmark used to evaluate the performance of LLMs on a variety of tasks.

**[RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf) (as "VicunaEval")**
> A benchmark dataset used to evaluate an LLM's performance and response quality on short-text, conversational tasks.

## Relationships

### → Vicuna-Bench
- **Instruction following** (constructs) — *measured_by*
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
