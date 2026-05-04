# Weather
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, the Weather dataset is consistently used as a standard benchmark for evaluating models on time series forecasting tasks. It is explicitly employed to measure the performance of time series forecasting and, in one instance, in-context learning. The dataset is broadly defined as containing climate or weather-related time series, with one paper specifying it includes "meteorological variables such as temperature, humidity, and wind speed" (Time-LLM: Time Series Forecasting by Reprogramming Large Language Models). A recurring application mentioned in the definitions is the evaluation of "long-term forecasting performance in zero-shot settings." In practice, it is frequently evaluated alongside a suite of other time series datasets, most commonly the ETT family (ETTh1, ETTh2, ETTm1, ETTm2), Electricity (ECL), and Traffic.

## Sources

**[TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting](https://proceedings.iclr.cc/paper_files/paper/2024/file/5132940b1bced8a7b28e9695d49d435a-Paper-Conference.pdf)**
> A climate time series dataset used for evaluating long-term forecasting performance in zero-shot settings.

## Relationships

### → Weather
- **Time series forecasting** (behaviors tasks) — *measured_by*
  > “The datasets we evaluate on are ETTh1, ETTh2, ETTm1, ETTm2, Weather, Traffic, ECL, Solar and US Weather”
  - [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
