# Knowledge awareness
**Type:** Construct  
**Referenced in:** 11 papers  
**Also known as:** Knowledge comprehension, Knowledge understanding, Knowledge and understanding  

## State of the Field

Across the surveyed literature, "Knowledge awareness" is most commonly framed as a latent ability for models to acquire, represent, and apply factual world knowledge when processing inputs and generating outputs. This general capability is described as encompassing the use of both domain-specific information and general knowledge from training data to perform diverse cognitive tasks, and is often studied alongside reasoning. A more specific, and less common, definition treats it as the ability to recognize when a question requires external knowledge or common sense that is "not directly visible in the image" ("CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness"). Another paper defines it as the ability to apply factual information that is explicitly "presented in a question" ("xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation"). The construct is operationalized and measured using a range of evaluation instruments, including MMLU, TruthfulQA, the LLM Evaluation Harness, and the HuggingFace Open LLM Leaderboard 2. In the context of spoken language, one paper uses VoxEval to "assess SLMs’ knowledge understanding through pure speech interactions" ("SimulS2S-LLM: Unlocking Simultaneous Inference of SpeechLLMs for Speech-to-Speech Translation"). The concept is also studied in relation to "Knowledge memorization".

## Sources

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)**
> The ability to recognize that answering a question requires external knowledge or common sense not directly visible in the image.

**[xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf) (as "Knowledge comprehension")**
> The ability of a model to understand and correctly apply factual or conceptual information presented in a question.

**[Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf) (as "Knowledge understanding")**
> The latent ability to represent and use factual or domain knowledge when processing inputs and generating outputs.

**[Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.52.pdf) (as "Knowledge and understanding")**
> The latent ability of a model to acquire, retain, and apply general world knowledge and domain-specific information from training data to perform well on diverse cognitive tasks.

## Relationships

### Knowledge awareness →
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Open LLM Leaderboard 2** (measurements) — *measured_by*
  - [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.52.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.52.pdf)
- **VoxEval** (measurements) — *measured_by*
  - [SimulS2S-LLM: Unlocking Simultaneous Inference of SpeechLLMs for Speech-to-Speech Translation](https://aclanthology.org/2025.acl-long.818.pdf)

### Associated with
- **Knowledge memorization** (constructs)
  - [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks)
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
- **Uncertainty quantification** (constructs)
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
