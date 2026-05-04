# zs-RE
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** ZsRE  

## State of the Field

Across the provided literature, zs-RE is consistently defined as a benchmark or dataset for zero-shot relation extraction, where models must identify relations between entities without prior examples. A prevalent application of zs-RE is in the evaluation of knowledge editing, with multiple papers citing it as a "representative benchmark in the field of model editing" used to assess a model's ability to update its knowledge. This evaluation is frequently operationalized as a question answering task, as several sources describe zs-RE as a "closed-book question answering (QA) dataset." One definition explicitly links these uses, framing the instrument as a tool to "evaluate the ability of models to update knowledge based on single-relation prompts without prior examples." In addition to knowledge editing, the benchmark is also used to measure information extraction capabilities more broadly. The provided data also indicates that zs-RE is used to assess other model properties, including locality, generality, factuality, hallucination, and faithfulness.

## Sources

**[PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf)**
> zs-RE is a benchmark for zero-shot relation extraction, where models must identify relations between entities without prior examples for those specific relations.

**[Identification of Multiple Logical Interpretations in Counter-Arguments](https://aclanthology.org/2025.emnlp-main.327.pdf) (as "ZsRE")**
> Zero-shot Relation Extraction dataset used to evaluate the ability of models to update knowledge based on single-relation prompts without prior examples.

## Relationships

### → zs-RE
- **Question answering** (behaviors tasks) — *measured_by*
  > "ZsRE is a closed-book question answering (QA) dataset derived from zero-shot relation extraction."
  - [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf)
- **Knowledge editing** (behaviors tasks) — *measured_by*
  > "We adopted two representative benchmarks in the field of model editing: Counterfact(Meng et al., 2022) and ZsRE(Levy et al., 2017)." (Section 4.1) and "we adopt the metrics for evaluating knowledge updating ability: Efficacy (efficiency success) and Generalization (paraphrase success)" (Section 4.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **Locality** (constructs) — *measured_by*
  > Results on three metrics for the two datasets using LLAMA2-7B and LLAMA-7B. (Table 1)
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Generality** (constructs) — *measured_by*
  > Results on three metrics for the two datasets using LLAMA2-7B and LLAMA-7B. (Table 1)
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Factual knowledge** (constructs) — *measured_by*
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks) — *measured_by*
  > “zs-RE (Levy et al., 2017), Relation extraction”
  - [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  - [Stealth edits to large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c8168a8eca2eb23f6b1f5019371043e-Paper-Conference.pdf)
- **Reliability** (constructs) — *measured_by*
  - [Investigating Pedagogical Teacher and StudentLLMAgents: Genetic Adaptation Meets Retrieval-Augmented Generation Across Learning Styles](https://aclanthology.org/2025.emnlp-main.676.pdf)
