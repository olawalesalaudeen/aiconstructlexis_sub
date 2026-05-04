# MSR-VTT-QA
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** MSRVT-QA  

## State of the Field

Across the provided literature, MSR-VTT-QA is consistently defined and used as a benchmark to measure the behavior of video question answering. All definitions state that it is based on the MSR-VTT (Microsoft Research Video to Text) dataset. The instrument is also used to evaluate the broader construct of video understanding, with one paper including it in a "comprehensive suite of video understanding benchmarks." Several sources specify that the benchmark uses "open-ended" questions to assess model performance. One definition further characterizes its goal as evaluating the "open-ended comprehension of video semantics" on "diverse video content." In practice, MSR-VTT-QA is frequently deployed alongside other video QA benchmarks, most commonly MSVD-QA, TGIF-QA, and ActivityNet-QA, to form evaluation suites for video-language models.

## Sources

**[Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf) (as "MSRVTT-QA")**
> Video question answering benchmark based on the Microsoft Research Video to Text dataset, evaluating open-ended comprehension of video semantics.

**[$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)**
> Video question answering benchmark based on the MSR-VTT dataset, assessing model performance on diverse video content with open-ended questions.

**[CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eb/wang25eb.pdf) (as "MSRVT-QA")**
> A benchmark for video question answering based on the MSR-VTT (Microsoft Research Video to Text) dataset.

## Relationships

### → MSR-VTT-QA
- **Video question answering** (behaviors tasks) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)
