# BIG-Bench
**Type:** Measurement  
**Referenced in:** 32 papers  
**Also known as:** BIG-BENCH, Big-Bench, BIG-bench, Big-bench  

## State of the Field

Across the surveyed literature, BIG-Bench is consistently characterized as a large, collaborative, and diverse evaluation suite designed to probe the capabilities and limitations of language models. Several papers refer to it by its full name, the 'Beyond the Imitation Game benchmark', and note its composition of over 200 distinct tasks. The benchmark is most frequently used to measure a wide range of reasoning abilities, with papers using it to operationalize constructs such as logical deduction, commonsense reasoning, mathematical reasoning, and date reasoning. Beyond this focus, it is also reported as a tool for assessing in-context learning, emergent abilities, societal bias, and safety. A prevalent usage pattern involves researchers selecting specific subsets or individual tasks from the larger suite, such as the 'BIG-BENCH LITE' subset for QA and classification, the 'date understanding' task for commonsense reasoning, or tasks targeting 'Unnatural In-context Learning'. As one paper notes, its tasks cover domains including "math, coding, and human understanding, scientific knowledge, and prosocial behavior" (Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks). Some work also frames BIG-Bench as a leaderboard for ranking the overall capabilities of different models.

## Sources

**[Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)**
> Comprehensive evaluation suite containing diverse reasoning tasks such as logical deduction, temporal sequences, and formal fallacies, designed to test a wide range of cognitive abilities in language models.

**[Predicting Emergent Abilities with Infinite Resolution Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e6d14709eae0cbc49a1d19d87fb8b21-Paper-Conference.pdf) (as "BigBench")**
> A diverse evaluation suite for large language models that includes a wide range of challenging tasks, used here to study in-context learning and emergent abilities.

**[Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf) (as "BIG-BENCH")**
> Beyond the Imitation Game benchmark, a collaboratively built benchmark of 204 diverse tasks from various domains; the paper uses the BIG-BENCH LITE subset focusing on QA, classification, and translation tasks.

**[Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf) (as "Big-Bench")**
> A benchmark suite containing a wide range of challenging tasks designed to measure the capabilities of large language models, including reasoning and comprehension.

**[PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf) (as "BIG-bench")**
> Beyond the Imitation Game benchmark (BIG-bench) is a collaborative benchmark comprising 204 diverse tasks designed to probe the capabilities and limitations of large language models.

**[Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf) (as "Big-bench")**
> A large, collaborative benchmark suite for language models, from which the 'date understanding' task is used as a testbed for commonsense reasoning.

## Relationships

### → BIG-Bench
- **Societal bias** (constructs) — *measured_by*
  - [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Table question answering** (behaviors tasks) — *measured_by*
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
- **Date reasoning** (behaviors tasks) — *measured_by*
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
- **Stability** (constructs) — *measured_by*
  - [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Seq-VCR: Preventing  Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)
- **Emergent abilities** (constructs) — *measured_by*
  > "Fig. 4 shows U-shaped vs. inverted-U scaling of Hindu knowledge, conceptual combinations, and analogical similarity datasets in Big-Bench ... totaling 6 datasets" (Sec. 2.3)
  - [U-shaped and Inverted-U Scaling behind Emergent Abilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f696200311b445af686c3ebd87ade1d7-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)

### Associated with
- **Object counting** (behaviors tasks)
  - [The Validation Gap: A Mechanistic Analysis of How Language Models Compute Arithmetic but Fail to Validate It](https://aclanthology.org/2025.emnlp-main.1496.pdf)
