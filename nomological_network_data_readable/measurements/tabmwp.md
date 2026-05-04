# TabMWP
**Type:** Measurement  
**Referenced in:** 14 papers  

## State of the Field

Across the provided sources, TabMWP is consistently described as a benchmark for evaluating mathematical reasoning, specifically in contexts involving tabular data. The dataset's structure consists of samples each containing a math word problem in natural language and an accompanying table, sometimes described as semi-structured. To succeed on this benchmark, models are expected to perform joint reasoning over text and structured information, a process one paper outlines as understanding the problem, extracting relevant information from the table, and then performing calculations. Consequently, TabMWP is most frequently used to measure and operationalize mathematical reasoning, with some sources using the more specific terms 'arithmetic reasoning' or 'numerical reasoning'. A secondary framing, present in a smaller number of papers, characterizes it as a 'tabular question-answering' or 'structured reasoning' task. Overall, the benchmark is used to assess an LLM's ability to apply reasoning skills to tabular contexts to solve quantitative problems.

## Sources

**[CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)**
> A benchmark for mathematical reasoning that requires processing information from tables to solve math word problems.

## Relationships

### → TabMWP
- **Mathematical reasoning** (constructs) — *measured_by*
  > We evaluate our LLM cascade approaches on six datasets, covering (1) mathematical reasoning, including GSM8k (Cobbe et al., 2021), ASDIV (Ling et al., 2017), and TabMWP (Lu et al., 2023); (2) symbolic reasoning from BIG-Bench Hard (bench authors, 2023), including DATE and Navigate; and (3) causal reasoning, including CREPE (Zhang et al., 2023). (Section 3.1)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > "Lastly, we also test on a popular tabular question-answering dataset, TabMWP (Lu et al., 2023), that requires LLMs to use reasoning skills over tabular contexts."
  - [Ethical Concern Identification inNLP: A Corpus ofACLAnthology Ethics Statements](https://aclanthology.org/2025.naacl-long.581.pdf)
