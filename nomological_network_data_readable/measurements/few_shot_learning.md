# Few-shot learning
**Type:** Measurement  
**Referenced in:** 12 papers  

## State of the Field

Across the provided sources, few-shot learning is consistently framed as an evaluation procedure and a form of prompt engineering. The single available definition describes it as a method where a model is provided with a small number of task examples within the prompt to guide its response. One paper offers a concrete operationalization, specifying the use of "three examples for tasks 1 and 2, and one example for task 3." This evaluation procedure is applied across a range of benchmarks, including LongBench, MMLU, HellaSwag, ARC, LongBench-E, and GLUE. The concept is also studied in relation to generalization, with one source noting that humans use this capability for "rapidly generalizing from a single task demonstration." Additionally, few-shot learning is studied alongside continual learning, information extraction, and time series forecasting.

## Sources

**[Retrieval over Classification: Integrating Relation Semantics for Multimodal Relation Extraction](https://aclanthology.org/2025.emnlp-main.944.pdf)**
> An evaluation procedure where the model is provided with a small number of examples of the task within the prompt to guide its response.

## Relationships

### Few-shot learning →
- **LongBench** (measurements) — *measured_by*
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **LongBench-E** (measurements) — *measured_by*
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  - [On the Crucial Role of Initialization for Matrix Factorization](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d67ec04032cccf4a21d04c0ae4ab268-Paper-Conference.pdf)

### Associated with
- **Generalization** (constructs)
  > Humans exhibit remarkable few-shot learning capabilities, rapidly generalizing from a single task demonstration to related conditions by integrating the observed behavior with their internal world model.
  - [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ac50fd0a4eeeb1f077b17bb7c5353c3-Paper-Conference.pdf)
- **Time series forecasting** (behaviors tasks)
  - [TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
- **Continual learning** (constructs)
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Information extraction** (behaviors tasks)
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)
