# GPQA
**Type:** Measurement  
**Referenced in:** 86 papers  

## State of the Field

Across the provided literature, GPQA is consistently characterized as a benchmark of graduate-level, multiple-choice questions written by domain experts in biology, physics, and chemistry. Its most frequently stated purpose is to evaluate advanced model capabilities, specifically "scientific domain expertise" and what some papers call "deep" or "graduate-level reasoning." A prevalent use of GPQA is to measure `Generalization`; several studies employ it as an out-of-domain task to test if "the learned reasoning capability can be generalized across different tasks." The benchmark is also used to operationalize a range of other constructs, including `Logical reasoning` and `Natural language understanding`, as well as behaviors like `Question answering`. Some papers highlight its design as being "google-proof" and challenging for both AI systems and human experts. One study leverages its recent release date to use it as an "uncontaminated dataset," noting it was released "beyond the knowledge cutoff of the target models."

## Sources

**[CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf)**
> A benchmark of graduate-level questions in biology, physics, and chemistry, used for comparison to evaluate scientific domain expertise.

## Relationships

### → GPQA
- **Generalization** (constructs) — *measured_by*
  > Additionally, we evaluate the model’s generalization performance across six out-of-domain tasks, including MT-Bench (Zheng et al., 2024), ARC-Challenge (25-shot) (Clark et al., 2018), GSM8K (8-shot) (Cobbe et al., 2021), HellaSwag (8-shot) (Zellers et al., 2019), GPQA (0-shot) (Rein et al., 2023), and MMLU (0-shot) (Hendrycks et al., 2020).
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > ...language understanding (HellaSwag (Zellers et al., 2019), BoolQ (Clark et al., 2019), OpenbookQA (Mihaylov et al., 2018), SQuAD (Rajpurkar et al., 2016), MMLU (Hendrycks et al., 2021), MMLU-Pro (Wang et al., 2024), GPQA(Rein et al., 2023)) (Section 3).
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1453.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [TheUD-NewsCrawl Treebank: Reflections and Challenges from a Large-scaleTagalog Syntactic Annotation Project](https://aclanthology.org/2025.acl-long.358.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [R-Bind: Unified Enhancement of Attribute and Relation Binding in Text-to-Image Diffusion Models](https://aclanthology.org/2025.emnlp-main.350.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > For logical reasoning, we evaluate the PrOntoQA (Saparov & He, 2022) dataset for logical deduction in a 5-shot setting and the GPQA (Rein et al., 2023) dataset for graduate-level multiple-choice questions in a 0-shot setting (Section 4).
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
- **Understanding** (constructs) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Iterative refinement** (behaviors tasks) — *measured_by*
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Resource-Rational Noisy-Channel Language Processing: Testing the Effect of Algorithmic Constraints on Inferences](https://aclanthology.org/2025.emnlp-main.1208.pdf)
- **Task generalization** (constructs) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > Safety and helpfulness results for different fine-tuning strategies across three LLMs. ... higher helpfulness values reflect better benchmark performance. (Table 2 Caption)
  - [TokenSelect: Efficient Long-Context Inference and Length Extrapolation forLLMs via Dynamic Token-LevelKVCache Selection](https://aclanthology.org/2025.emnlp-main.1080.pdf)
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1041.pdf)
