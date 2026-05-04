# Time series forecasting
**Type:** Behavior  
**Referenced in:** 22 papers  
**Also known as:** Binary forecasting, Time-series forecasting, Long-term forecasting, Probabilistic forecasting, Short-term forecasting, Degradation trend inference  

## State of the Field

Across the provided literature, time series forecasting is consistently defined as the task of predicting future data points in a sequence based on historical observations. This behavior is operationalized and evaluated using several real-world datasets, with papers frequently citing the use of `Weather`, `ETTh1`, `ETTm1`, and `Traffic` benchmarks. The general task is further specified into several sub-types, including `long-term` and `short-term` forecasting, which differ by their prediction horizons, as well as `probabilistic forecasting`, which aims to produce a distribution over future values rather than a single point estimate. A few papers also define more specialized variants, such as `binary forecasting` for events with True/False outcomes and `degradation trend inference` for analyzing system trajectories. In the context of large language models, this task is often framed as a sequence continuation problem, where a model is prompted to "continue the following sequence" (Enhancing LLM Reasoning via Vision-Augmented Prompting) or "forecast the next value" (TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series). Some papers propose that successful performance on this task is influenced by underlying constructs, with `commonsense knowledge`, `logical reasoning`, and `structural understanding` being reported as causes of forecasting ability. The task is also studied in the context of `few-shot learning`.

## Sources

**[TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting](https://proceedings.iclr.cc/paper_files/paper/2024/file/5132940b1bced8a7b28e9695d49d435a-Paper-Conference.pdf)**
> The observable task of predicting future data points in a sequence based on historical observations.

**[Density estimation with LLMs: a geometric investigation of in-context learning trajectories](https://proceedings.iclr.cc/paper_files/paper/2025/file/380afe1a245a3b2134010620eae88865-Paper-Conference.pdf) (as "Time-series forecasting")**
> The task of predicting future values in a sequence of numerical data points based on past observations provided in context.

**[Consistency Checks for Language Model Forecasters](https://proceedings.iclr.cc/paper_files/paper/2025/file/5107a33432b9a5cffafd0a53ef6c6a18-Paper-Conference.pdf) (as "Binary forecasting")**
> The observable task of assigning a probability between 0 and 1 to a question about a future event that has a binary (True/False) outcome.

**[Fourier Head: Helping Large Language Models Learn Complex Probability Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/d3e38662377dcce6203f4bb91b2a9b03-Paper-Conference.pdf) (as "Probabilistic forecasting")**
> Producing a distribution over future numerical values in a time series rather than a single point estimate.

**[Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf) (as "Long-term forecasting")**
> The task of predicting time series values over a long future horizon based on a historical sequence.

**[Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf) (as "Short-term forecasting")**
> The task of predicting time series values over a short future horizon based on a historical sequence.

**[ITFormer: Bridging Time Series and Natural Language for Multi-Modal QA with Large-Scale Multitask Dataset](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25av/wang25av.pdf) (as "Degradation trend inference")**
> The task of analyzing signal variations across multiple time periods to infer the trajectory of system degradation.

## Relationships

### Time series forecasting →
- **Weather** (measurements) — *measured_by*
  > “The datasets we evaluate on are ETTh1, ETTh2, ETTm1, ETTm2, Weather, Traffic, ECL, Solar and US Weather”
  - [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf)
- **ETTh1** (measurements) — *measured_by*
  - [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf)
- **ETTm1** (measurements) — *measured_by*
  - [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf)
- **Traffic** (measurements) — *measured_by*
  - [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf)

### → Time series forecasting
- **Reasoning** (constructs) — *causes*
  - [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *causes*
  > FSCA can be flexibly and repeatedly integrated into various layers of pre-trained LLMs to improve awareness of logic and structure, thereby enhancing performance.
  - [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf)
- **Structural understanding** (constructs) — *causes*
  - [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf)

### Associated with
- **Few-shot learning** (measurements)
  - [TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
