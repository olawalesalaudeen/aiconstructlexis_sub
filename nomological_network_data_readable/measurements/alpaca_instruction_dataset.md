# Alpaca instruction dataset
**Type:** Measurement  
**Referenced in:** 56 papers  
**Also known as:** Alpaca, Alpaca dataset, Alpaca Instruction Tuning Dataset, Alpaca-GPT4  

## State of the Field

Across the provided literature, the Alpaca instruction dataset is predominantly characterized as an instruction-following dataset used for fine-tuning and calibrating language models. Many studies employ it to adapt pretrained models to follow instructions, with one paper specifying it contains "52K instruction-following data generated from text-davinci-003" (QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models). A common application, particularly in model compression research, is using the dataset for "calibration and recovery fine-tuning" to assess and restore performance. Several papers also treat it as a source of "benign" data, using it to test for safety degradation after fine-tuning or as a control set to calibrate probes on neutral chat data. Another frequent use is as a source of prompts for evaluation, where it provides "out-of-domain queries" to detect model infringement or to test prompt inversion. The dataset is positioned to measure a variety of constructs and behaviors, including helpfulness, commonsense knowledge, text generation, and question answering. It is also used to evaluate model attributes like faithfulness and consistency.

## Sources

**[Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf) (as "Alpaca")**
> Instruction-following dataset used for calibration and recovery fine-tuning, serving as a basis for assessing model performance post-compression.

**[Can Watermarks be Used to Detect LLM IP Infringement For Free?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8fba406323cb3930aeaccc9aa64c83a8-Paper-Conference.pdf) (as "Alpaca dataset")**
> A dataset of instruction-following examples, used in the paper as a source of out-of-domain queries for detecting model infringement.

**[Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf) (as "Alpaca Instruction Tuning Dataset")**
> An instruction dataset used here as a source of prompts for hallucination-related editing and evaluation setup.

**[TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf) (as "Alpaca-GPT4")**
> An instruction-tuning dataset used as a fine-tuning corpus and also as benign data in red-teaming-related experiments.

## Relationships

### → Alpaca instruction dataset
- **Instruction following** (constructs) — *measured_by*
  - [Towards Optimal Multi-draft Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0907335ecf28faf15be54485dbcbe70e-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  - [Beware of Calibration Data for Pruning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ede933e10afa991a10b6f36b6522129-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Semantic consistency** (constructs) — *measured_by*
  - [Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.292.pdf)
