# Trustworthiness
**Type:** Construct  
**Referenced in:** 94 papers  
**Also known as:** Scoring reliability, Trustfulness, Trust, Credibility, Clinical trustworthiness, Trust and safety  

## State of the Field

Across the surveyed literature, Trustworthiness is a broad construct, frequently used interchangeably with Reliability, that concerns the dependability, consistency, and accuracy of a model's outputs. The prevailing definitions describe it as a multifaceted property encompassing factual accuracy, safety, and robustness, with unreliable generations viewed as a risk for practical deployment in critical domains like medicine. This construct is most commonly operationalized through measures of consistency; as one paper notes, "Failure to preserve self-consistency... undermines the trustworthiness of a model." Other papers operationalize it by assessing a model's capacity to avoid hallucinations, its honesty in tool use, or, in the case of reward models, its ability to "select the correct solution more often." The concept is frequently linked to a model's suitability for high-stakes applications, with some work specifying framings like "Clinical trustworthiness." A distinct and less common perspective defines "Trust" as a latent disposition developed between agents based on historical performance, which can influence social behaviors like conformity. Ultimately, many sources connect the construct to user confidence, noting that without it, models "risk undermining the foundation of long-term trust with humans."

## Sources

**[An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf) (as "Reliability")**
> A broad property of a large language model concerning its trustworthiness and consistency, encompassing aspects like factual accuracy, safety, and robustness.

**[Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf)**
> The quality of a model being reliable and consistent in its understanding and generation, as evidenced by properties like self-consistency.

**[Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf) (as "Scoring reliability")**
> The degree to which a reward model consistently and accurately assigns scores that reflect true human preferences, enhanced by access to external verification tools.

**[Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf) (as "Trustfulness")**
> The reliability and credibility of the model's output results, often compromised by the generation of false or unsupported content.

**[Do as We Do, Not as You Think: the Conformity of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1da9ca7e9cef4b1af63913f05d1630a4-Paper-Conference.pdf) (as "Trust")**
> A latent positive disposition developed by an agent towards its peers based on their historical accuracy, which can increase its propensity to conform to their subsequent judgments.

**[CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/70fa5df8e3300dc30bf19bee44a56155-Paper-Conference.pdf) (as "Credibility")**
> The degree to which a model's answers are based on a genuine understanding of relevant evidence within the video content, rather than relying on shortcuts or biases.

**[Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.548.pdf) (as "Clinical trustworthiness")**
> The degree to which model outputs are reliable and safe for clinical use, especially when intermediate reasoning errors could lead to misjudgments.

**[Position: Generative AI Regulation Can Learn from Social Media Regulation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/appel25a/appel25a.pdf) (as "Trust and safety")**
> The latent property of a system that ensures user protection from harm, including misinformation, abuse, and unsafe content, while fostering user confidence in the technology.

## Relationships

### Trustworthiness →
- **Human evaluation** (measurements) — *measured_by*
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **DecodingTrust** (measurements) — *measured_by*
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **ASQA** (measurements) — *measured_by*
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **QAMPARI** (measurements) — *measured_by*
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **ELI5** (measurements) — *measured_by*
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **FINTRUST** (measurements) — *measured_by*
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.512.pdf)

### → Trustworthiness
- **Faithfulness** (constructs) — *causes*
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Alignment** (constructs) — *causes*
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
- **Semantic uncertainty** (constructs) — *causes*
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **Uncertainty quantification** (constructs) — *causes*
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1543.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26d4fbaf7dfa115f1d4b3f104e26bce-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs)
  - [A Concept-Based Explainability Framework for Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f4fba41b554f9aaa013c4062a1c40518-Paper-Conference.pdf)
- **Truthfulness** (constructs)
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Safety** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Privacy** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-consistency** (measurements)
  - [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks)
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
- **Fairness** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmlessness** (constructs)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Validity** (constructs)
  - [Large language model validity via enhanced conformal prediction methods](https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Social bias** (constructs)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Ethical reasoning** (constructs)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Transparency** (constructs)
  - [Decision Information Meets Large Language Models: The Future of Explainable Operations Research](https://proceedings.iclr.cc/paper_files/paper/2025/file/a48e5877c7bf86a513950ab23b360498-Paper-Conference.pdf)
