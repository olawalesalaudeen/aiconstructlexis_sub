# Electricity dataset
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** ECL, ECL dataset  

## State of the Field

The Electricity dataset is predominantly used as a benchmark for evaluating time series forecasting models, often under the name ECL. It is consistently defined as capturing hourly electricity consumption data from a number of clients, though the specific version varies, with one paper citing 321 clients and another using a subset of 19. One source explicitly clarifies this relationship, stating, "The ECL dataset is a subset of the Electricity dataset" (FSTLLM: Spatio-Temporal LLM for Few Shot Time Series Forecasting). The most common application across the provided papers is to assess long-term and few-shot forecasting performance. A less frequent use case positions the dataset as a tool to evaluate the performance of "self-healing adaptation strategies across different data distributions" (Self-Healing Machine Learning: A Framework for Autonomous Adaptation in Real-World Environments). In practice, it is frequently studied alongside other time series datasets like Weather, Traffic, and Solar-Energy.

## Sources

**[Self-Healing Machine Learning: A Framework for Autonomous Adaptation in Real-World Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a86ec12e94ef1fe306362e7bdcd5894-Paper-Conference.pdf)**
> Electricity [55] is a dataset used to evaluate the performance of self-healing adaptation strategies across different data distributions.

**[AutoTimes: Autoregressive Time Series Forecasters via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf) (as "ECL")**
> A real-world benchmark dataset for long-term time series forecasting that captures hourly electricity consumption data from 321 clients.

**[FSTLLM: Spatio-Temporal LLM for Few Shot Time Series Forecasting](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25a/jiang25a.pdf) (as "ECL dataset")**
> Subset of the Electricity dataset comprising hourly electricity consumption from 19 clients, used for evaluating forecasting accuracy in a different domain.
