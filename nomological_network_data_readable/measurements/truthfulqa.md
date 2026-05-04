# TruthfulQA
**Type:** Measurement  
**Referenced in:** 205 papers  
**Also known as:** Truthful QA, Truthful-QA, TRUTHFULQA  

## State of the Field

Across the surveyed literature, TruthfulQA is consistently described as a benchmark designed to measure a model's truthfulness. Its primary feature, noted in multiple papers, is a set of questions (over 800 according to some sources) specifically crafted to elicit false answers based on common human misconceptions, thereby testing a model's ability to avoid generating imitative falsehoods. The most prevalent use of TruthfulQA is to operationalize and measure the constructs of faithfulness and hallucination. It is also frequently employed to evaluate behaviors such as question answering, text generation, and commonsense understanding. A smaller set of studies uses it to assess safety, informativeness, and human preference alignment. The benchmark is versatile in its application, being used for both multiple-choice and open-ended generative tasks, as noted in papers like "Tool-Augmented Reward Modeling" and "SALMON". Furthermore, it is often included as a component in broader evaluation suites, such as the Open LLM Leaderboard.

## Sources

**[Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf)**
> Benchmark containing over 800 questions designed to elicit false answers based on common misconceptions, evaluating a model's ability to avoid generating false information.

**[Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf) (as "Truthful QA")**
> A benchmark designed to measure a model's ability to generate truthful answers and avoid generating common falsehoods.

**[Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf) (as "Truthful-QA")**
> The Truthful-QA benchmark, designed to measure a model's tendency to generate truthful answers and avoid generating common falsehoods.

**[ManaTTSPersian: a recipe for creatingTTSdatasets for lower resource languages](https://aclanthology.org/2025.naacl-long.465.pdf) (as "TRUTHFULQA")**
> Benchmark designed to evaluate factual accuracy and truthfulness in AI-generated responses across multiple-choice and generative tasks.

## Relationships

### TruthfulQA →
- **Text generation** (behaviors tasks) — *measured_by*
  > "we use the over 800 closed-book questions in TruthfulQA ... corresponding to whole sentence answers"
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)

### → TruthfulQA
- **Truthfulness** (constructs) — *measured_by*
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  > TruthfulQA (Lin et al., 2022) and HaluEval (Li et al., 2023) for factual reasoning and ARC-Challenge (Clark et al., 2018) for scientific reasoning (Section 4.1, Datasets).
  - [Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > For short-form Q&A scenarios evaluation, we adopt the open-ended generation task of TruthfulQA (Lin et al., 2022), Entity Questions (Sciavolino et al., 2021), SciQ(Welbl et al., 2017) and StrategyQA (Geva et al., 2021). (Section 4.1)
  - [On the Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/c48dcd605cfb17d5b4f94ce106a915f7-Paper-Conference.pdf)
- **Factuality** (constructs) — *measured_by*
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > two generation datasets (TruthfulQA (Lin et al., 2022) and GSM8K (Cobbe et al., 2021)) (Section 4)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Reliability** (constructs) — *measured_by*
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
- **Informativeness** (constructs) — *measured_by*
  > In TruthfulQA, factuality is evaluated by two fine-tuned GPT-3 models, each focusing on truthfulness and informativeness (Section 4.3).
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **Long-form question answering** (behaviors tasks) — *measured_by*
  > To assess long-form generation capabilities, we utilized TruthfulQA (Lin et al., 2022), which requires the model to produce truthful answers when faced with questions to elicit false or misleading responses. (Section 4)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Decoupling Angles and Strength in Low-rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3379ce104189b72d5f7baaa03ae81329-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [LACA: Improving Cross-lingual Aspect-Based Sentiment Analysis withLLMData Augmentation](https://aclanthology.org/2025.acl-long.42.pdf)
- **Factual question answering** (behaviors tasks) — *measured_by*
  - [WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines](https://aclanthology.org/2025.naacl-long.168.pdf)
- **Factual accuracy** (constructs) — *measured_by*
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **Generative capability** (constructs) — *measured_by*
  > the results on two generation datasets (TruthfulQA, GSM8K) of all three baselines when compression ratios are 60% and above are zero, meaning that the compressed LLMs totally lose their generation ability. (Section 4.1)
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **Knowledge transferability** (constructs) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **Knowledge awareness** (constructs) — *measured_by*
  - [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.52.pdf)
- **Hallucination detection** (behaviors tasks) — *measured_by*
  > On the challenging TruthfulQA benchmark (Lin et al., 2022a), our approach achieves a significant +12.8% improvement in hallucination detection accuracy (AUROC) compared to state-of-the-art methods. (Section 1. Introduction)
  - [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf)
- **Contextual understanding** (constructs) — *measured_by*
  > Moreover, to demonstrate contextual understanding and general effectiveness of each model variant, we assess their performance using HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2020), and TruthfulQA (Lin et al., 2021b) benchmarks. (Section 4.2)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **Error handling** (constructs) — *measured_by*
  > We evaluate our method on LLMs and show significant perplexity improvements over baselines. This is particularly noteworthy at high sparsity levels, maintaining robust improvements even as high as 70% sparsity. Benchmark results. In Table 3, we evaluate the performance of our method on several benchmark datasets.
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)

### Associated with
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
- **OpenLLM Leaderboard** (measurements)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
