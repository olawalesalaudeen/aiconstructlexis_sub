# AlpacaFarm
**Type:** Measurement  
**Referenced in:** 10 papers  
**Also known as:** Alpacafarm  

## State of the Field

Across the surveyed literature, AlpacaFarm is most commonly described as an evaluation framework for assessing open-ended conversation models, with some papers also referring to it as a benchmark, test set, or dataset. Its primary stated purpose is to evaluate a model's 'instructability' or instruction-following capabilities, and the provided data also indicates it is used to measure the constructs of 'helpfulness' and 'commonsense knowledge'. The evaluation is typically operationalized through pairwise comparisons of two model outputs for a given instruction. These comparisons are conducted using either human preference annotations—with one paper noting a 66% inter-annotator agreement—or model-based evaluators. For instance, one study employs GPT-4 as an evaluator to determine a model's win rate against a baseline. The dataset component contains a set of instructions, with one paper specifying a test set of 805 instructions, and is described as providing specific data splits for different stages of RLHF. In addition to being a dataset, one paper refers to the 'AlpacaFarm codebase' for judging model responses, indicating it is also a software tool.

## Sources

**[Evaluating Large Language Models at Evaluating Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/afc8b034823271816d14f7c1aefe1dff-Paper-Conference.pdf)**
> Evaluation framework for open-ended conversation models, using human or model-based comparisons to assess response quality and instructability.

**[RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf) (as "Alpacafarm")**
> A benchmark for evaluating instruction-following models, which includes human preference annotations for pairwise comparisons.

## Relationships

### → AlpacaFarm
- **Helpfulness** (constructs) — *measured_by*
  - [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)
