# AddSub
**Type:** Measurement  
**Referenced in:** 16 papers  
**Also known as:** AddSub+  

## State of the Field

Across the provided literature, AddSub is consistently defined as a dataset composed of arithmetic word problems that involve addition and subtraction. Its most common application is to measure or evaluate the mathematical and arithmetic reasoning capabilities of language models, with multiple papers using it to "assess the model’s performance on arithmetic reasoning tasks." A recurring, though not universal, framing positions AddSub as an out-of-distribution benchmark; one paper explicitly calls it a "near-shift out-of-distribution benchmark," while another lists it among several OOD datasets. A single study also discusses a variant named "AddSub+", which is used to explore problems with different digit lengths. In practice, AddSub is frequently used in evaluation suites alongside other mathematical reasoning datasets such as GSM8K, SVAMP, and SingleEq.

## Sources

**[Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)**
> A dataset of arithmetic word problems involving addition and subtraction, used as a near-shift out-of-distribution benchmark.

**[Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://proceedings.iclr.cc/paper_files/paper/2024/file/72679d76c80e079c70fe5977d21ed1e4-Paper-Conference.pdf) (as "AddSub+")**
> A dataset for arithmetic reasoning that involves addition and subtraction problems, used here with variants of different digit lengths.

## Relationships

### → AddSub
- **Mathematical reasoning** (constructs) — *measured_by*
  > we ... test on six different math reasoning datasets: MultiArith (Roy and Roth, 2016), GSM8K (Cobbe et al., 2021), AddSub (Hosseini et al., 2014), AQuA (Ling et al., 2017), SingleEq (Koncel-Kedziorski et al., 2015) and SVAMP (Patel et al., 2021). (Section 4.1)
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
