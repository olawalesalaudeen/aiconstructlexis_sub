# Data analysis
**Type:** Behavior  
**Referenced in:** 18 papers  
**Also known as:** Data preprocessing, Shape and trend analysis, Log analysis, Data analysis ability, Descriptive analytics, Diagnostic analytics, End-to-end data analytics, Predictive analytics, Prescriptive analytics, Comparison and trend analysis, Comprehensive analysis, Event-centric analysis, Image quality analysis, Inter-relationship analysis  

## State of the Field

The prevailing view across the surveyed literature defines data analysis as the process of systematically applying statistical and logical reasoning to comprehend data, answer questions, and derive insights from a database. A more holistic framing describes it as an "end-to-end" workflow that includes formulating questions, interpreting answers, and generating summaries, with insights categorized as descriptive, diagnostic, predictive, or prescriptive. This behavior is most commonly operationalized and measured using benchmarks such as LiveBench, InfiAgent-DABench, WildBench, and TableEval. For instance, LiveBench evaluates data analysis through practical data-wrangling tasks like "table reformatting, predicting which columns can be used to join two tables, and predicting the correct column type annotation." While frequently associated with tabular data, the concept is also applied in other domains, including the analysis of visual information like movement trajectories, events in videos, and image quality, as well as log files and text for sentiment analysis. A few papers offer alternative conceptualizations, framing it as a "latent capacity" to understand data-centric problems or as an internal model mechanism of "data preprocessing." Data analysis is studied in relation to mathematical, logical, and strategic reasoning, and is also reported to correlate with natural language understanding.

## Sources

**[DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The process of systematically applying statistical and logical reasoning to comprehend data and derive insights from a database.

**[How Transformers Utilize Multi-Head Attention in In-Context Learning? A Case Study on Sparse Linear Regression](https://proceedings.neurips.cc/paper_files/paper/2024/file/d83d04f40961442fa31dd2552debd0e9-Paper-Conference.pdf) (as "Data preprocessing")**
> An internal process where the model transforms or reweights input data features based on correlations computed from in-context examples before further processing.

**[TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/16ba99f25a235f1100a4014d71d34ad8-Paper-Conference.pdf) (as "Shape and trend analysis")**
> The observable task of analyzing a subject's trajectory to determine the shape or general trend of its movement.

**[Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf) (as "Log analysis")**
> The observable behavior of processing and interpreting information from long log files.

**[InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "End-to-end data analytics")**
> The ability to conduct a complete data analysis workflow, from understanding a high-level goal to formulating questions, extracting insights, and summarizing findings with actionable recommendations.

**[InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "Descriptive analytics")**
> The ability to generate insights that summarize and describe what has happened in a dataset.

**[InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "Diagnostic analytics")**
> The ability to generate insights that explain the causes or reasons behind observed data trends.

**[InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "Predictive analytics")**
> The ability to forecast future outcomes from past data and current trends.

**[InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "Prescriptive analytics")**
> The ability to generate insights that suggest specific actions to address issues or capitalize on opportunities identified in the data.

**[DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50e9ad960ae78b741a6b4fea533f2eaf-Paper-Conference.pdf) (as "Data analysis ability")**
> The latent capacity to understand data-centric questions, inspect relevant files and tables, and derive correct answers from complex real-world data analysis settings.

**[SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/693ce820ea7e0f0c70a2a833cbdf7ccc-Paper-Conference.pdf) (as "Comparison and trend analysis")**
> The ability to compare different entities or events and analyze emerging patterns or trends over the course of a video.

**[RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf) (as "Comprehensive analysis")**
> The ability to thoroughly examine and understand the components and structure of a query and response to form a judgment.

**[SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/693ce820ea7e0f0c70a2a833cbdf7ccc-Paper-Conference.pdf) (as "Event-centric analysis")**
> The ability to focus on and conduct an in-depth examination of significant events that occur within a video.

**[An Intelligent Agentic System for Complex Image Restoration Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/921ac785fa9edc73cacaf2664f43d234-Paper-Conference.pdf) (as "Image quality analysis")**
> The ability of a vision-language model to understand, recognize, and assess the quality of an image, including identifying specific types of degradation.

**[Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf) (as "Inter-relationship analysis")**
> The ability to identify and describe the connections, interactions, or spatial dynamics between multiple specified objects or regions within an image.

**[Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf) (as "Sentiment analysis")**
> The latent ability to infer emotional polarity or affective labels from text.

## Relationships

### Data analysis →
- **LiveBench** (measurements) — *measured_by*
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **WildBench** (measurements) — *measured_by*
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *correlates*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Data transformation** (behaviors tasks) — *measured_by*
  > “Data Analysis: three tasks using recent datasets from Kaggle and Socrata, specifically, table reformatting ...”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Schema linking** (behaviors tasks) — *measured_by*
  > “Data Analysis: three tasks using recent datasets from Kaggle and Socrata, specifically, ... predicting which columns can be used to join two tables”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Data annotation** (behaviors tasks) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **InfiAgent-DABench** (measurements) — *measured_by*
  > (1) Data Analysis: InfiAgent-DABench (Hu et al., 2024b) contains 257 challenges with CSV inputs and multi-level (easy/medium/hard) analysis questions. (Section 4.1)
  - [Weight-Aware Activation Sparsity with ConstrainedBayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.58.pdf)
- **TableEval** (measurements) — *measured_by*
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Logical reasoning** (constructs)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Strategic reasoning** (constructs)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Task decomposition** (behaviors tasks)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
