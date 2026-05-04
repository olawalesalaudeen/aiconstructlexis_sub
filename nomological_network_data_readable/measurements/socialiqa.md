# SocialIQA
**Type:** Measurement  
**Referenced in:** 30 papers  
**Also known as:** Social IQa, Social-I-QA  

## State of the Field

Across the provided literature, SocialIQA is predominantly described as a benchmark for evaluating commonsense reasoning, specifically concerning social situations and human motivations. It is consistently operationalized as a dataset of questions about social interactions, with some sources specifying a multiple-choice answer format. A recurring, more specific theme is its use in assessing social and emotional capabilities. For instance, one paper states it "measures social and emotional intelligence through questions about social interactions," while another includes it in a "socio-emotional-skills" evaluation subset. Reflecting these dual framings, SocialIQA is most frequently used to measure `Commonsense understanding`, but is also employed to assess constructs like `Social reasoning`, `Social intelligence`, and `Social competence`. Beyond these primary uses, it also serves to evaluate general `Question answering` capabilities and model performance under specific conditions like data contamination. In practice, it is often evaluated alongside a suite of other commonsense reasoning benchmarks, such as ARC-Easy, WinoGrande, and CommonsenseQA.

## Sources

**[EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf) (as "Social IQa")**
> Social IQA, a benchmark using questions about social interactions to assess social and emotional intelligence.

**[Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf) (as "SIQA")**
> Social IQa benchmark testing commonsense reasoning about social situations and human motivations.

**[Emergent Response Planning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25p/dong25p.pdf)**
> A dataset of social interaction questions requiring commonsense reasoning, used to assess multiple-choice answer prediction as a content planning attribute.

**[How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf) (as "Social-I-QA")**
> Commonsense reasoning benchmark involving social interactions, used to assess model performance under contamination and forgetting conditions.

## Relationships

### → SocialIQA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
- **Social intelligence** (constructs) — *measured_by*
  - [Divergences between Language Models and Human Brains](https://proceedings.neurips.cc/paper_files/paper/2024/file/f96839fc751b67492e17e70f5c9730e4-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > OLMo-30M models trained on various pre-training token budgets are fine-tuned on downstream tasks using fixed hyperparameters: math (GSM8k), code (Starcoder-Python), and QA (SIQA). (Figure 4)
  - [Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf)
- **Social and emotional intelligence** (constructs) — *measured_by*
  > "Social IQA measures social and emotional intelligence through questions about social interactions."
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
- **Overfitting** (constructs) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **Functional linguistic competence** (constructs) — *measured_by*
  - [Sketch-of-Thought: EfficientLLMReasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1237.pdf)
