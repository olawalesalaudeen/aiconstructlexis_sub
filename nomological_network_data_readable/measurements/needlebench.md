# Needlebench
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** NeedleBench  

## State of the Field

Across the provided literature, Needlebench is consistently defined as a benchmark for evaluating how well long-context models can comprehend and retrieve information from long input sequences. The prevailing usage is to test recall-intensive information finding, with papers using it to measure constructs such as information retrieval, long-context reasoning, and knowledge recall. One paper specifies that the benchmark operationalizes these assessments through three subtasks: Single-Needle Retrieval, Multi-Needle Retrieval, and Multi-Needle Reasoning. It is characterized as a synthetic benchmark, which, as one study notes, offers "better control over variables such as sequence length and complexity" (LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs). The benchmark is used to assess and compare the retrieval capabilities of different models, with one paper describing it as "a suite of recall-intensive tasks where recurrent models typically underperform" (Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions).

## Sources

**[LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)**
> A benchmark that evaluates long-context models on their ability to comprehend and retrieve information from long input sequences.

**[Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf) (as "NeedleBench")**
> A suite of recall-intensive tasks designed to test long-context retrieval and information finding in large language models.

## Relationships

### → Needlebench
- **Information retrieval** (behaviors tasks) — *measured_by*
  > “For NeedleBench, both Rodimus and Rodimus+ even exceed the performance of Pythia”
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
- **Long-context reasoning** (constructs) — *measured_by*
  > "NeedleBench (Li et al., 2024a): Tests retrieval and reasoning in complex contexts through three subtasks: Single-Needle Retrieval, Multi-Needle Retrieval, and Multi-Needle Reasoning."
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  > Furthermore, Rodimus* achieves a performance improvement of up to 7.21% over Mamba2, and outperforms even softmax attention-based Pythia on NeedleBench—a suite of recall-intensive tasks where recurrent models typically underperform (Waleffe et al., 2024). (Section 1)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
