# LiveBench
**Type:** Measurement  
**Referenced in:** 16 papers  

## State of the Field

Across the provided literature, LiveBench is characterized as a dynamic benchmark designed to mitigate data contamination by regularly updating its dataset with questions from recent sources. Several papers specify its method, noting it "collects questions based on the latest information source, e.g., math competitions from the past 12 months, with new questions added and updated every few months" (Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models). The benchmark is consistently defined as an evaluation from Abacus AI that uses a large test set of questions with ground truth answers. Papers use LiveBench to measure a wide range of model capabilities, including mathematical reasoning, programming ability, data analysis, natural language understanding, commonsense knowledge, faithfulness, and instruction following. It is studied alongside other evaluation tools and is reported to be "strongly correlated" with HELM (Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking). Additionally, its reasoning and mathematics datasets are used by JudgeBench, and it is shown to correlate with LMSYS Chatbot Arena and Arena-Hard.

## Sources

**[Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)**
> A benchmark from Abacus AI that evaluates models on a large test set of questions with ground truth answers.

## Relationships

### → LiveBench
- **Mathematical reasoning** (constructs) — *measured_by*
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Data analysis** (behaviors tasks) — *measured_by*
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **LMSYS Chatbot Arena** (measurements) — *correlates*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Arena-Hard** (measurements) — *correlates*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [PicPersona-TOD: A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.404.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **HELM** (measurements) — *correlates*
  > LiveBench and HELM are strongly correlated
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [PicPersona-TOD: A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.404.pdf)
- **Consistency** (constructs) — *measured_by*
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)

### Associated with
- **JudgeBench** (measurements)
  > For the Reasoning and Mathematics categories, we use the corresponding LiveBench datasets. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **BBH** (measurements)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **IFEval** (measurements)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
