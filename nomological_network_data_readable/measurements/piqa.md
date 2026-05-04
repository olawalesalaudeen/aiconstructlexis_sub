# PIQA
**Type:** Measurement  
**Referenced in:** 267 papers  
**Also known as:** PiQA, Piqa  

## State of the Field

Across the provided literature, PIQA (Physical Interaction: Question Answering) is a benchmark consistently used to measure commonsense reasoning, with a specific focus on the understanding of physical interactions and situations. The prevailing operationalization involves evaluating models in a zero-shot setting, where they must answer multiple-choice questions about how to interact with everyday objects or determine the most physically plausible solution to a problem. Papers frequently use PIQA to assess a model's `Commonsense understanding` and `Natural language understanding`, often grouping it with other benchmarks like HellaSwag, WinoGrande, and ARC to form a suite for evaluating general model capabilities. Beyond this primary use, some studies employ PIQA to evaluate more specific abilities such as `Logical reasoning`, `Generalization`, and `Natural language inference`. The evaluation is commonly conducted using standardized frameworks, with several papers explicitly mentioning the `LLM Evaluation Harness` or `OpenCompass` to report accuracy scores. While the dominant format is multiple-choice question answering, a few papers describe its use for generative QA tasks or, in one instance, for "grounding and abstractive summarization." In at least one case, PIQA is also used to measure `Catastrophic forgetting` after fine-tuning.

## Sources

**[AffineQuant: Affine Transformation Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/ddfb58b61e7213dfb9e06c695475b2bd-Paper-Conference.pdf)**
> Physical Interaction: Question Answering, a commonsense reasoning benchmark that tests understanding of physical interactions.

**[SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf) (as "PiQA")**
> Benchmark for physical commonsense reasoning, assessing a model's ability to answer questions about everyday physical interactions.

**[Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf) (as "Piqa")**
> The Physical Interaction: Question Answering benchmark, which tests commonsense reasoning about how to interact with everyday objects.

## Relationships

### → PIQA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [Divergences between Language Models and Human Brains](https://proceedings.neurips.cc/paper_files/paper/2024/file/f96839fc751b67492e17e70f5c9730e4-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > The four benchmarks are ARC_C, HellaSwag, PIQA and MMLU... Results of the zero-shot performance are displayed in Table 1, which demonstrates that there is no significant loss of the ability of the language understanding of LLMs after the aligning with embodied environments (Section 5.5)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  > “we also examined the zero-shot capabilities of pruned models. In detail, we report the accuracy in six zero-shot tasks including PIQA”
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **Language proficiency** (constructs) — *measured_by*
  - [NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/db6461eaf0eaeaad1d9c4a70e4818cbd-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > We conducted experiments on a series of language modeling and understanding tasks, including PiQA (Bisk et al., 2020), ARC-easy (ARC-e), ARC-challenge (ARC-c) (Clark et al., 2018), HellaSwag (Hella.) (Zellers et al., 2019), Winogrande (Wino.) (Sakaguchi et al., 2019) and MMLU (Li et al., 2023). The results are reported in Table 2 and all evaluations were done using lm-evaluation-harness (Gao et al., 2024). (Section 4.2)
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > We use 12 natural language understanding benchmarks for evaluation: CMNLI (Xu et al., 2020), HellaSwag(HeSw) (Zellers et al., 2019), PIQA (Bisk et al., 2020),CHID (Zheng et al., 2019), WSC (Levesque et al., 2012),CommonSenseQA(CoQA) (Talmor et al., 2018), BoolQ (Clark et al., 2019),MMLU (Hendrycks et al., 2020), CMMLU (Li et al., 2023),Race-High/Middle (Lai et al., 2017), C3 (Sun et al., 2020). (Section 4.2)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Commonsense question answering** (behaviors tasks) — *measured_by*
  - [Radio: Rate–Distortion Optimization for Large Language Model Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/young25b/young25b.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *measured_by*
  > The fine-tuned models under MDS are evaluated on the general tasks including MMLU (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), and PIQA (Bisk et al., 2020) to measure the catastrophic forgetting of the PEFT approaches. (Section 4.1)
  - [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.246.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Diff-eRank: A Novel Rank-Based Metric for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/45cc967d7899616f51993b7b363d35b5-Paper-Conference.pdf)
- **Zero-shot classification** (behaviors tasks) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > We utilize validation sets from six benchmarks: PIQA (Bisk et al., 2020), HellaSwag (Zellers et al., 2019), ARC-E (Clark et al., 2018), ARC-C (Clark et al., 2018), COPA (Roemmele et al., 2011), Winograd (Levesque et al., 2012), and MathQA (Amini et al., 2019). (Section 4.2.3)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > Notably, Figure 8 shows significant gains in categories like MBPP (programming) and PIQA (physical commonsense reasoning), reflecting enhanced logical reasoning and problem-solving skills. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **Natural language inference** (behaviors tasks) — *measured_by*
  > Natural Language Inference (NLI) using PIQA (Bisk et al., 2020) and WinoGrande (Sakaguchi et al., 2020) (Section 4).
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
- **Task generalization** (constructs) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
- **Overfitting** (constructs) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **Functional linguistic competence** (constructs) — *measured_by*
  > “To assess this, we use six benchmarks covering world knowledge (ARC-EASY, ARC-CHALLENGE (Clark et al., 2018)), social reasoning (SOCIAL IQA (Sap et al., 2019)), physical reasoning (PIQA (Bisk et al., 2019))”
  - [Sketch-of-Thought: EfficientLLMReasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1237.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  > Therefore, we only test on tasks (ARC-easy, Hellaswag, PIQA, SciQ, LAMBADA) in lm-evaluation-harness. (Section 4.1)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **OpenCompass** (measurements)
  > We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA (Bisk et al., 2019), ARC-challenge (ARC-C) (Clark et al., 2018), ARC-easy (ARC-E) (Clark et al., 2018), WinoGrande (WG) (Sakaguchi et al., 2019), HellaSwag (HLSG) (Zellers et al., 2019), and CommonSenseQA (CSQA) (Talmor et al., 2019). (Section 5.1)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
