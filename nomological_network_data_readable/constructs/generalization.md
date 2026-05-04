# Generalization
**Type:** Construct  
**Referenced in:** 1205 papers  
**Also known as:** Generalizability, Generalization ability, Generalization capability, Generalization performance, Generalisation, Cross-lingual generalisation, Cross-lingual transfer, Cross-lingual transferability, Generalisability, Size generalisation, Task-agnostic generalizability, Temporal generalizability, Domain-generality, Architectural generalizability  

## State of the Field

Across the surveyed literature, generalization is consistently defined as a model's ability to maintain strong performance on new, unseen data, tasks, or conditions that differ from its training distribution. While this core definition is widely shared, some papers adopt more specific framings such as cross-lingual, temporal, or task-agnostic generalization to denote performance across linguistic, time-based, or task-type boundaries. Researchers operationalize and measure this construct by evaluating model performance on a wide array of out-of-distribution (OOD) benchmarks, with MMLU, GSM8k, HellaSwag, and ARC-Challenge being among the most frequently used instruments. A recurring theme is the explicit contrast between generalization and memorization, with one study noting that "Disentangling the effects of generalization and test set memorization is critical" ("Proving Test Set Contamination in Black-Box Language Models"). This is often studied alongside overfitting, where methods are assessed on their ability to improve generalization without simply memorizing training data. The construct is a common target for improvement in various contexts, including instruction tuning, which one paper describes as having the "primary purpose" of expanding generalization abilities ("OctoPack: Instruction Tuning Code Large Language Models"), as well as in research on alignment, knowledge editing, and embodied agents.

## Sources

**[$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf)**
> The ability of a model or fusion method to maintain strong performance across different conditions, datasets, or tasks, such as clean vs. noisy speech or audio-visual settings.

**[An interpretable error correction method for enhancing code-to-code translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e01f4ef7ffeedf3317a44461d18df9d-Paper-Conference.pdf) (as "Generalizability")**
> The extent to which a model maintains useful performance across diverse domains, entity types, and evaluation settings beyond the specific data it was trained on.

**[KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf) (as "Generalization ability")**
> The model's capacity to perform effectively on new, unseen data and tasks that differ from its training distribution.

**[AffineQuant: Affine Transformation Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/ddfb58b61e7213dfb9e06c695475b2bd-Paper-Conference.pdf) (as "Generalization capability")**
> The ability of the quantized model to preserve performance across different datasets, model sizes, and evaluation settings.

**[Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf) (as "Generalization performance")**
> The latent tendency of a trained reflector or system to transfer effectively across different actor models or settings.

**[Model merging with SVD to tie the Knots](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4f8a5109c5083b5307fcd0bddae7a7-Paper-Conference.pdf) (as "Generality")**
> The ability of a merged model to preserve the union of all skills from its base models and correctly classify inputs from any of the source tasks into a unified label space.

**[Procedural Knowledge in Pretraining Drives Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/482847908fd916b5b6b9e82525c773ad-Paper-Conference.pdf) (as "Generalisation")**
> The model's underlying strategy for applying knowledge learned from pretraining data to new, unseen problems.

**[CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf) (as "Cross-lingual transferability")**
> The degree to which a model's capability learned in one language can be applied to another language without additional training, reflecting the generalization of skills across linguistic boundaries.

**[DETQUS: Decomposition-Enhanced Transformers forQUery-focused Summarization](https://aclanthology.org/2025.naacl-long.139.pdf) (as "Cross-lingual transfer")**
> The ability to apply knowledge learned from data in one language (typically high-resource) to perform tasks in another language (typically low-resource).

**[Learning to Substitute Words with Model-based Score Ranking](https://aclanthology.org/2025.naacl-long.577.pdf) (as "Cross-lingual generalisation")**
> The ability of a model trained or tuned in one language to effectively apply reasoning skills to other languages, especially low-resource ones, without performance degradation.

**[ImpliHateVid: A Benchmark Dataset and Two-stage Contrastive Learning Framework for Implicit Hate Speech Detection in Videos](https://aclanthology.org/2025.acl-long.843.pdf) (as "Generalisability")**
> The ability of a reasoning method to transfer effectively across different tasks, models, and problem domains without significant reconfiguration.

**[DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf) (as "Temporal generalizability")**
> The ability to accurately verify claims that occur after the model's knowledge cutoff by relying on external evidence rather than parametric memory.

**[Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf) (as "Task-agnostic generalizability")**
> The capacity of a model or method to maintain performance across diverse tasks without requiring task-specific fine-tuning or retraining.

**[Softmax is not Enough (for Sharp Size Generalisation)](https://raw.githubusercontent.com/mlresearch/v267/main/assets/velickovic25a/velickovic25a.pdf) (as "Size generalisation")**
> The ability of a model to maintain performance on tasks when the number of input items exceeds the maximum seen during training, particularly relevant for reasoning tasks over variable-length sequences.

**[Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf) (as "Domain-generality")**
> The capacity to apply a cognitive skill across diverse contexts and stimulus types, rather than relying on narrow, task-specific patterns or priors.

**[slow-reconvergence phase](https://aclanthology.org/2025.emnlp-main.1676.pdf) (as "Architectural generalizability")**
> The extent to which statistical patterns in response length, such as GEV distribution fit, hold across different LLM architectures and scales, indicating a fundamental property of transformer-based generation.

## Relationships

### Generalization →
- **MMLU** (measurements) — *measured_by*
  > Multi-task Language Understanding: MMLU (Hendrycks et al.), C-Eval (Huang et al., 2023); (Section 3.1)
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  > Figure 4 shows the downstream performance on HellaSwag, MMLU Var3, ARC-Challenge, and SciQ. PolyNorm outperforms SwiGLU on all tasks, with notable improvements, demonstrating superior generalization capabilities.
  - [Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/725f5e8036cc08adeba4a7c3bcbc6f2c-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  > Moreover, the choice of the four datasets, which include short- and long-form generation, question answering, summarization, and multi-hop reasoning, demonstrates the generalizability of the Sparse RAG approach. (Section 1)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  > Additionally, we evaluate the model’s generalization performance across six out-of-domain tasks, including MT-Bench (Zheng et al., 2024), ARC-Challenge (25-shot) (Clark et al., 2018), GSM8K (8-shot) (Cobbe et al., 2021), HellaSwag (8-shot) (Zellers et al., 2019), GPQA (0-shot) (Rein et al., 2023), and MMLU (0-shot) (Hendrycks et al., 2020).
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
- **ALFWorld** (measurements) — *measured_by*
  - [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > We examine how wrong-over-wrong alignment can generalize to other unseen tasks in the same domain. We employ Hellaswag (Zellers et al., 2019) ... as two unseen datasets (Section 5)
  - [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf)
- **GrailQA** (measurements) — *measured_by*
  > We experiment on GrailQA to compare the performance on different generalization levels (preliminary in Appendix D). (Section 4.3.3)
  - [Context-Aware Sentiment Forecasting viaLLM-based Multi-Perspective Role-Playing Agents](https://aclanthology.org/2025.acl-long.137.pdf)
- **MATH** (measurements) — *measured_by*
  > We evaluate these verifiers on the GSM8K test set as well as their easy-to-hard generalization on much harder MATH dataset (Hendrycks et al., 2021) (Section 4)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  > "Additional evaluation of SMAAT on language understanding benchmarks, including GLUE and advGLUE are reported in Appendix E."
  - [Soft Syntactic Reinforcement for Neural Event Extraction](https://aclanthology.org/2025.naacl-long.480.pdf)
- **VirtualHome** (measurements) — *measured_by*
  > For the last two crossover tests, TWOSOME agent trained in Food Preparation is tested in Entertainment and TWOSOME trained in Entertainment is tested in Food Preparation. (Figure 6)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  > In this section, we investigate whether our method is generally applicable beyond the medical domain. We use two general domain datasets, CommonsenseQA (CSQA) (Talmor et al., 2018) and OpenbookQA (OBQA) (Mihaylov et al., 2018)... (Section 4.5)
  - [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  > In this section, we investigate whether our method is generally applicable beyond the medical domain. We use two general domain datasets, CommonsenseQA (CSQA) (Talmor et al., 2018) and OpenbookQA (OBQA) (Mihaylov et al., 2018)... (Section 4.5)
  - [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf)
- **MBPP** (measurements) — *measured_by*
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **C-Eval** (measurements) — *measured_by*
  > Multi-task Language Understanding: MMLU (Hendrycks et al.), C-Eval (Huang et al., 2023); (Section 3.1)
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
- **ScienceWorld** (measurements) — *measured_by*
  > Comprehensive studies on ScienceWorld and ALFWorld benchmarks show that our method consistently improves performance and generalization capacity, surpassing a range of baselines by a significant margin. (Summary of Contributions)
  - [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  > Figure 8 presents the rate-accuracy performance of our re-trained scheme applied to two MLLMs that do not use the pre-trained CLIP ViT visual encoder: (1) mPLUG-Owl2 (Ye et al., 2024) on MMBench and Osprey (Yuan et al., 2024) on POPE (popular setting). Our method under all three settings clearly outperforms the Reconstruction baseline, confirming the generalizability of the proposed framework.
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **POPE** (measurements) — *measured_by*
  > Figure 8 presents the rate-accuracy performance of our re-trained scheme applied to two MLLMs that do not use the pre-trained CLIP ViT visual encoder: (1) mPLUG-Owl2 (Ye et al., 2024) on MMBench and Osprey (Yuan et al., 2024) on POPE (popular setting). Our method under all three settings clearly outperforms the Reconstruction baseline, confirming the generalizability of the proposed framework.
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **WebArena** (measurements) — *measured_by*
  > To further measure the generalizability of our method, we also evaluate on other popular benchmarks such as OSWorld and relevant domains from WebArena.
  - [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c995a913bc20ca39ce2231b8973be90a-Paper-Conference.pdf)
- **HaluEval** (measurements) — *measured_by*
  > "we directly apply the directions and hyperparameters learned from TruthfulQA to HaluEval (Li et al., 2023) and TrivialQA (Joshi et al., 2017) to validate the generalizability of TAE."
  - [ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > The GPT-4 judgment results between the generations of different methods and Llama-3-Base are provided in Figure 3... This confirms the superiority of PAD in generalizing to unseen personalized preferences.
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  > HumanEval evaluates code generation capabilities, while GSM8k assesses multistep mathematical reasoning skills. (Section 5.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  > For the OOD evaluation, we test each approach’s generalization ability on Deepmind Math (Saxton et al., 2019), MMLU-pro (Wang et al., 2024), strategyQA (Geva et al., 2021), and DROP (Dua et al., 2019). (Section 3.1)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  > We found that LASER outperforms with upto 3.38% difference and 1% difference on average in accuracy.
  - [GuideLLM: ExploringLLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.288.pdf)
- **MuSiQue** (measurements) — *measured_by*
  > For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022)... These datasets test the model’s generalization ability beyond the training domain. (Section 4.2.1)
  - [ViClaim: A Multilingual Multilabel Dataset for Automatic Claim Detection in Videos](https://aclanthology.org/2025.emnlp-main.22.pdf)
- **Functional MATH** (measurements) — *measured_by*
  > The performance of the models trained with the synthetic data from the MATH data at high sampling budget on the Functional MATH dataset. The results suggest that training with WC data enhances the generalization capabilities over the SE data, at a fixed sampling budget. (Figure 6)
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
- **PopQA** (measurements) — *measured_by*
  > Moreover, the choice of the four datasets, which include short- and long-form generation, question answering, summarization, and multi-hop reasoning, demonstrates the generalizability of the Sparse RAG approach. (Section 1)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  > Moreover, the choice of the four datasets, which include short- and long-form generation, question answering, summarization, and multi-hop reasoning, demonstrates the generalizability of the Sparse RAG approach. (Section 1)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **FLAN** (measurements) — *measured_by*
  > To demonstrate the generalizability and robustness of our method, we include FLAN (Chung et al., 2024) (a mix of multiple NLP tasks) as reference datasets .
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **OSWORLD** (measurements) — *measured_by*
  - [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > While humans can recognize frames from movies they’ve seen (avg. accuracy 0.19), their accuracy drops sharply (0.02) on unseen titles, highlighting that generalization alone cannot explain the VLMs performance on the same task. (Figure 8).
  - [DIS-CO: Discovering Copyrighted Content in VLMs Training Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duarte25a/duarte25a.pdf)
- **miniF2F** (measurements) — *measured_by*
  > The FORMALALIGN model exhibits consistent performance across four diverse datasets, demonstrating its ability to generalize its autoformalization evaluation capabilities. Particularly noteworthy are the model's AS scores of 66.39% and 64.61% on the challenging MiniF2F-Valid and MiniF2F-Test datasets, respectively.
  - [FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf)
- **OlympiadBench** (measurements) — *measured_by*
  > We also incorporate two more challenging datasets, Olympiad-Bench (He et al., 2024) and CollegeMath (Tang et al., 2024), to further test our model’s generalizability on out-of-distribution challenging problems. (Section 4.1)
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
- **BEIR** (measurements) — *measured_by*
  > We conducted experiments on DL19, DL20, and BEIR, and show the results in Table 2. (Section 4.4)
  - [VISA: Retrieval Augmented Generation with Visual Source Attribution](https://aclanthology.org/2025.acl-long.1457.pdf)
- **WikiText** (measurements) — *measured_by*
  > We evaluate LENSLLM’s effectiveness for LLM selection through three analyses: (1) comparing its curve-fitting accuracy during fine-tuning against Rectified Scaling Law... across FLAN, Wikitext, and Gigaword datasets. (Section 4.2)
  - [LensLLM: Unveiling Fine-Tuning Dynamics for LLM Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25g/zeng25g.pdf)
- **SVAMP** (measurements) — *measured_by*
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **GAIA** (measurements) — *measured_by*
  > "We validated OSCAR’s effectiveness and generalizability across diverse benchmarks involving both desktop and smartphone OS environments. On the GAIA (Mialon et al., 2023) benchmark, OSCAR outperformed previous methods"
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **APIBench** (measurements) — *measured_by*
  - [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://proceedings.iclr.cc/paper_files/paper/2024/file/28e50ee5b72e90b50e7196fde8ea260e-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **CIFAR-10** (measurements) — *measured_by*
  > Extensive experiments demonstrate its superior performance and generalization to various categories and types of dirty samples. The results on CIFAR-10, ImageNet-100 and ImageNet-Dog with different poisoning ratios are presented in Tables 1,2,13,14.
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **CIFAR-100** (measurements) — *measured_by*
  > In this section, we evaluate the generalization of discrete prompts generated by Greedy on CIFAR-10, CIFAR-100, ImageNet as well as domain generalization datasets fMoW (Christie et al., 2018) and OfficeHome (Venkateswara et al., 2017) (Section 5)
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **ImageNet-1k** (measurements) — *measured_by*
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **FMOW** (measurements) — *measured_by*
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **Linear probing** (measurements) — *measured_by*
  > "we present a standard linear probe (on top of CLIP’s features), which achieves slightly better accuracy but a vacuous generalization bound"
  - [Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/9e79aefb538d02a7c0610fa43bdb0d0f-Paper-Conference.pdf)
- **SST-2** (measurements) — *measured_by*
  - [CSR-Bench: BenchmarkingLLMAgents in Deployment of Computer Science Research Repositories](https://aclanthology.org/2025.naacl-long.634.pdf)
- **IMDb** (measurements) — *measured_by*
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
- **MNLI** (measurements) — *measured_by*
  > “we assess its performance on paraphrase detection using the QQP dev set, natural language inference (NLI) using both the MNLI matched and mismatched dev sets, and commonsense reasoning using the SWAG dev set.”
  - [MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval](https://aclanthology.org/2025.emnlp-main.1583.pdf)
- **Agi-Eval** (measurements) — *measured_by*
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **VTAB-1k** (measurements) — *measured_by*
  > We select a pre-trained ViT/16 (Dosovitskiy et al., 2020) as the vision model and evaluate on VTAB-1k (Zhai et al., 2019) benchmark, which contains 19 visual tasks with three domains: Natural, Specialized, and Structured. (Section 4.4)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **FLORES-200** (measurements) — *measured_by*
  - [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf)
- **Dialogue generation** (behaviors tasks) — *measured_by*
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  > We evaluated the trained models on public benchmarks (Fourrier et al., 2023; OpenCompass Contributors, 2023). Table 1 presents the evaluation results. ... These results demonstrate that both EDiT and A-EDiT exhibit strong convergence and generalization capabilities. (Section 4.2)
  - [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf)
- **PKU-SafeRLHF** (measurements) — *measured_by*
  > We evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH) (Bai et al., 2022), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU) (Ji et al., 2024), Reward3, UltraFeedback(UltraF) (Cui et al., 2024), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
- **InfoSeek** (measurements) — *measured_by*
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **MathVerse** (measurements) — *measured_by*
  > To verify the generalization ability of G-LLaVA, we also conduct evaluation on the newly introduced MathVerse benchmark (Zhang et al., 2024b). (Section 5.1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **ASDIV** (measurements) — *measured_by*
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **OpenWebText** (measurements) — *measured_by*
  - [Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/11715d433f6f8b9106baae0df023deb3-Paper-Conference.pdf)
- **Harmbench** (measurements) — *measured_by*
  - [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf)
- **Reward-Bench** (measurements) — *measured_by*
  > We employ the primary dataset from RewardBench to evaluate the out-of-domain generalization capabilities of our reward models. (Section 4.3)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
- **Caltech101** (measurements) — *measured_by*
  > We select four visual classification datasets to investigate the task of balancing personalization, generalization and privacy: Caltech101 (Fei-Fei et al., 2004) (Section 4.1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **CollegeMath** (measurements) — *measured_by*
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **TheoremQA** (measurements) — *measured_by*
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **Clotho** (measurements) — *measured_by*
  - [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf)
- **OBQA** (measurements) — *measured_by*
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
- **CMMLU** (measurements) — *measured_by*
  - [Maximizing Intermediate Checkpoint Value in LLM Pretraining with Bayesian Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bv/liu25bv.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **Model collapse** (constructs) — *correlates*
  - [Linguistic Collapse: Neural Collapse in (Large) Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f88cc8930b47a45ec4733123bf3039b9-Paper-Conference.pdf)
- **LLaVA-Bench** (measurements) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **TextVQA** (measurements) — *measured_by*
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf)
- **2WikiMultihopQA** (measurements) — *measured_by*
  - [DoLLMs Encode Frame Semantics? Evidence from Frame Identification](https://aclanthology.org/2025.emnlp-main.1500.pdf)
- **MGSM** (measurements) — *measured_by*
  > we include (6) MGSM (Shi et al., 2022), a structured math reasoning task where predefined logic may suffice, to evaluate generalization to template-compatible domains. (Section 5.1)
  - [Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.93.pdf)
- **FollowBench** (measurements) — *measured_by*
  > FollowBench is a fine-grained constraint-following benchmark with five levels of difficulty. It contains diverse and open-ended instructions requiring evaluation by strong LLMs, such as GPT-4, which can fully examine the generalization of AUTOIF to more general instructions not verifiable by simple code executions. (Section 4).
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **InfoBench** (measurements) — *measured_by*
  > "we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation."
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **Arena-Hard** (measurements) — *measured_by*
  > "we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation."
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **MathOdyssey** (measurements) — *measured_by*
  > As can be seen in Figure 5, our method outperforms COT & TIR-ToRA... in all the individual topics and across all the 4 datasets, thereby proving beneficial for all topics. This highlights the generalisation ability of our approach...
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
- **Multimodal Mind2Web** (measurements) — *measured_by*
  > Second, Multimodal-Mind2Web (Deng et al., 2024; Zheng et al., 2024) extends the Mind2Web benchmark to evaluate generalization across three increasingly challenging settings: cross-task, cross-website, and cross-domain. (Section 3.1)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  > PolyNorm outperforms SwiGLU on all tasks, with notable improvements, demonstrating superior generalization capabilities. (Section 4.3)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Dynamath** (measurements) — *measured_by*
  - [DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/78b248ea6f627431bba5029d92be8a3d-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eedf422d321a20b2bd5e947c57c82e96-Paper-Conference.pdf)
- **WebVoyager** (measurements) — *measured_by*
  - [AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2c6e459b95694a24ac69c469a4ee746-Paper-Conference.pdf)
- **LogiQA** (measurements) — *measured_by*
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **LogiQA 2.0** (measurements) — *measured_by*
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Bamboogle** (measurements) — *measured_by*
  > “For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2022), and PopQA (Mallen et al., 2022). These datasets test the model’s generalization ability beyond the training domain.”
  - [ViClaim: A Multilingual Multilabel Dataset for Automatic Claim Detection in Videos](https://aclanthology.org/2025.emnlp-main.22.pdf)
- **DROP** (measurements) — *measured_by*
  > For the OOD evaluation, we test each approach’s generalization ability on Deepmind Math (Saxton et al., 2019), MMLU-pro (Wang et al., 2024), strategyQA (Geva et al., 2021), and DROP (Dua et al., 2019). (Section 3.1)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **SNLI** (measurements) — *measured_by*
  > We then assessed the performance of the merged LoRA on these in-domain tasks as well as on two additional out-of-domain tasks, SNLI and WNLI, to evaluate its adaptability and generalization capabilities.
  - [Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b54e0146a82945f01e69c2e3309ba925-Paper-Conference.pdf)
- **WNLI** (measurements) — *measured_by*
  > We then assessed the performance of the merged LoRA on these in-domain tasks as well as on two additional out-of-domain tasks, SNLI and WNLI, to evaluate its adaptability and generalization capabilities.
  - [Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b54e0146a82945f01e69c2e3309ba925-Paper-Conference.pdf)
- **Out-of-distribution evaluation** (measurements) — *measured_by*
  > “Generalization refers to the model’s ability to perform well on out-of-distribution (OOD) data, whether in-domain or out-of-domain. We assess in-domain generalization by evaluating the perplexity of a model on the test set of each training data source, while OOD generalization is evaluated with unseen datasets.”
  - [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
- **CoLA** (measurements) — *measured_by*
  - [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf)
- **Reddit TL;DR dataset** (measurements) — *measured_by*
  > To evaluate the generalization ability of the aligned models on out-of-distribution data, we fine-tune the models using only posts from the relationship and relationship advice subreddits of the Reddit TL;DR (Stiennon et al., 2020) dataset. (Section 6)
  - [Variational Best-of-N Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/402542c2341e5d2eadc1dd0891275901-Paper-Conference.pdf)
- **QMSum** (measurements) — *measured_by*
  > Moreover, the choice of the four datasets, which include short- and long-form generation, question answering, summarization, and multi-hop reasoning, demonstrates the generalizability of the Sparse RAG approach. (Section 1)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **ConceptARC** (measurements) — *measured_by*
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
- **ContextHub** (measurements) — *measured_by*
  > TypedThinker generalizes well to the unseen domain. We use a new propositional logic benchmark Contexthub (Hua et al., 2024) for evaluation. (Section 4.5)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **API-Bank** (measurements) — *measured_by*
  > To evaluate the generality of MTU-LLaMA, we measure its performance on the OOD test split of MTU-Bench and two other OOD tool-use benchmarks, i.e., API-Bank (Li et al., 2023) and ToolTalk (Farn & Shin, 2023)... which show strong generalizability of MTU-LLaMA.
  - [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf)
- **PartNet-Mobility** (measurements) — *measured_by*
  > For a more systematic evaluation, we validate the performance of Real2Code on the well-established PartNet-Mobility dataset (Mo et al., 2019), using an extensive test set of unseen objects that contain various numbers of articulated parts.
  - [Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf)
- **SWAG** (measurements) — *measured_by*
  - [MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval](https://aclanthology.org/2025.emnlp-main.1583.pdf)
- **Super-Natural Instructions** (measurements) — *measured_by*
  > Experiments on synthetic pre-training and real-world instruction tuning tasks demonstrate that PEARL effectively mitigates permutation attacks and enhances performance. Notably, despite being trained on fewer shots and shorter contexts, PEARL achieves performance gains of up to 40% when scaled to many-shot and long-context scenarios, highlighting its efficiency and generalization capabilities.
  - [PEARL: Towards Permutation-Resilient LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fad8e1915f66161581bb127ccf01092e-Paper-Conference.pdf)
- **AndroidControl** (measurements) — *measured_by*
  - [Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://aclanthology.org/2025.acl-long.277.pdf)
- **StableToolBench** (measurements) — *measured_by*
  > We comprehensively validate the superiority of DTA-Llama in real-world tool benchmarks, evaluating its performance from three aspects: effectiveness, computational cost, and generalization ability. (Section 1)
  - [LLMs Trust Humans More, That’s a Problem! Unveiling and Mitigating the Authority Bias in Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.1401.pdf)
- **LEMON** (measurements) — *measured_by*
  > To further assess the generalization ability of our models, we evaluated them on the LEMON dataset, which contains longer and more complex sentences.
  - [MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis](https://aclanthology.org/2025.acl-long.678.pdf)
- **MTEB** (measurements) — *measured_by*
  > To validate the effectiveness and generalization ability of our proposed method, we followed the data selection strategy of e5-mistral-7b-instruct (Wang et al., 2023) and used only a small portion of the MTEB training dataset for zero-shot training. (Section 4.3)
  - [CoEvo: Coevolution ofLLMand Retrieval Model for Domain-Specific Information Retrieval](https://aclanthology.org/2025.emnlp-main.758.pdf)
- **TopiOCQA** (measurements) — *measured_by*
  - [Model Unlearning via Sparse Autoencoder Subspace Guided Projections](https://aclanthology.org/2025.emnlp-main.1349.pdf)
- **AIME 2024** (measurements) — *measured_by*
  > Among these, AIME-2024, HumanEval, HumanEval+, GPQA, and SciBench are from a totally different distributions compared to training data, serving to verify the generalization capability of MAS-GPT. (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **SciBench** (measurements) — *measured_by*
  > Among these, AIME-2024, HumanEval, HumanEval+, GPQA, and SciBench are from a totally different distributions compared to training data, serving to verify the generalization capability of MAS-GPT. (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **Image captioning** (behaviors tasks) — *measured_by*
  > Meanwhile, image captioning is conducted on the unseen BLIP-2 (OPT-2.7b) (Li et al., 2023), to demonstrate the generalization capacity. (Section 4.1)
  - [Privacy-Shielded Image Compression: Defending Against Exploitation from Vision-Language Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25k/shen25k.pdf)
- **ProofNet** (measurements) — *measured_by*
  > We also report the performance of the model trained only on LeanWorkbook for 24 iterations, excluding miniF2F-valid and proofnet-valid, demonstrating that the model trained with STP also generalizes to out-of-domain theorems. (Section 4.2)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **FreshQA** (measurements) — *measured_by*
  - [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf)
- **MultiHop-RAG** (measurements) — *measured_by*
  - [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  > To understand the effect of α on model generalization, we measure the AE2 performance of various models with changing α. (Section 4.2. Results)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
- **OCRVQA** (measurements) — *measured_by*
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
- **UltraFeedback** (measurements) — *measured_by*
  > We evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH) (Bai et al., 2022), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU) (Ji et al., 2024), Reward3, UltraFeedback(UltraF) (Cui et al., 2024), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
- **FineWeb** (measurements) — *measured_by*
  > We evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH) (Bai et al., 2022), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU) (Ji et al., 2024), Reward3, UltraFeedback(UltraF) (Cui et al., 2024), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
- **MineDojo** (measurements) — *measured_by*
  > We validate our method in both MineDojo (Fan et al., 2022) and Mineflayer (PrismarineJS., 2013) environments. The experimental results suggest that our method completes diverse challenging tasks with a single model, indicating its promising generalization. (Section 1)
  - [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dj/li25dj.pdf)
- **GPQA-Diamond** (measurements) — *measured_by*
  > we use GSM8K and MATH500, along with an additional dataset to assess how well our transferring-then-finetuning approach generalizes to the unseen task GPQADiamond (Rein et al., 2024). (Section 5.1).
  - [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence inLLMs](https://aclanthology.org/2025.emnlp-main.131.pdf)
- **MME-RealWorld** (measurements) — *measured_by*
  > After creating an Error-book based on MME-RealWorld-Lite (Reasoning) subset, we applied it directly to the remaining MME-RealWorld Reasoning subset, excluding the Lite portion to rigorously test generalization (Section 4.1).
  - [TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning](https://aclanthology.org/2025.emnlp-main.711.pdf)
- **QQP** (measurements) — *measured_by*
  > The first five datasets are used to evaluate performance against SSL baselines, while the remaining three assess generalization on NLU tasks. (Section 4.1)
  - [MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval](https://aclanthology.org/2025.emnlp-main.1583.pdf)
- **DynamicNER** (measurements) — *measured_by*
  > To address these limitations, we propose DynamicNER, the first NER dataset designed for LLM-based methods with dynamic categorization, introducing various entity types and entity type lists for the same entity in different context, leveraging the generalization of LLM-based NER better.
  - [TurBLiMP: ATurkish Benchmark of Linguistic Minimal Pairs](https://aclanthology.org/2025.emnlp-main.835.pdf)
- **NLGraph** (measurements) — *measured_by*
  - [Multi-Document Event Extraction Using Large and Small Language Models](https://aclanthology.org/2025.emnlp-main.973.pdf)
- **YAGS** (measurements) — *measured_by*
  > To assess generalization beyond the training distribution, we evaluated the FN 1.7 fine-tuned model (§3.2) on the two established out-of-domain datasets. YAGS (Hartmann et al., 2017) is a benchmark annotated with FN 1.5 frames... (Section 4.2)
  - [FISTAPruner: Layer-wise Post-training Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.1499.pdf)
- **FewEvent** (measurements) — *measured_by*
  > Through extensive evaluations across six datasets, five domains, and nine LLMs, we demonstrate the generalizability and efficacy of DICORE... (Introduction)
  - [LILaC: Late Interacting in Layered Component Graph for Open-domain Multimodal Multihop Retrieval](https://aclanthology.org/2025.emnlp-main.1038.pdf)
- **ACE** (measurements) — *measured_by*
  > Through extensive evaluations across six datasets, five domains, and nine LLMs, we demonstrate the generalizability and efficacy of DICORE... (Introduction)
  - [LILaC: Late Interacting in Layered Component Graph for Open-domain Multimodal Multihop Retrieval](https://aclanthology.org/2025.emnlp-main.1038.pdf)
- **SPEED** (measurements) — *measured_by*
  > Through extensive evaluations across six datasets, five domains, and nine LLMs, we demonstrate the generalizability and efficacy of DICORE... (Introduction)
  - [LILaC: Late Interacting in Layered Component Graph for Open-domain Multimodal Multihop Retrieval](https://aclanthology.org/2025.emnlp-main.1038.pdf)
- **CASIE** (measurements) — *measured_by*
  > Through extensive evaluations across six datasets, five domains, and nine LLMs, we demonstrate the generalizability and efficacy of DICORE... (Introduction)
  - [LILaC: Late Interacting in Layered Component Graph for Open-domain Multimodal Multihop Retrieval](https://aclanthology.org/2025.emnlp-main.1038.pdf)
- **ToxiCloakCN** (measurements) — *measured_by*
  > To further evaluate the generalization capacity of our homophone-aware training strategy under cross-domain settings, we conduct experiments on the ToxiCloakCN dataset as an external benchmark (Xiao et al., 2024). (Section 5.5.5)
  - [MiLQ: BenchmarkingIRModels for Bilingual Web Search with Mixed Language Queries](https://aclanthology.org/2025.emnlp-main.1154.pdf)

### → Generalization
- **In-context learning** (constructs) — *causes*
  > In standard ICL (which we will refer to as prequential ICL), the query xq is a novel input that does not appear in the context. In the alternative form of ICL (which we will call train-risk ICL), the query xq is a randomly-selected input that appeared previously in the context x1:j.
  - [Probing the Decision Boundaries of In-context Learning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb5dd4476448c44e55a759a985b3bbec-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *causes*
  > catastrophic forgetting (CF) is still an unavoidable problem during CIT, which refers to the forgetting of previously learned tasks and the deterioration of original generalization ability (Section 1).
  - [Beyond Text Compression: Evaluating Tokenizers Across Scales](https://aclanthology.org/2025.acl-long.1547.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [KptLLM: Unveiling the Power of Large Language Model for Keypoint Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe692980c5d9732cf153ce27947653a7-Paper-Conference.pdf)
- **Memorization** (constructs) — *causes*
  > Recent advances in grokking have demonstrated that neural networks can transition from memorizing to perfectly generalizing once they detect underlying logical patterns – yet these studies have primarily used small, synthetic tasks. (Abstract)
  - [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](https://proceedings.neurips.cc/paper_files/paper/2024/file/f5198bc255e1d5f959edd6d1d1a86fab-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Overfitting** (constructs) — *causes*
  > Over-personalization can lead to overfitting, reducing generalizability (Abstract).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks) — *causes*
  > VGD enhances the interpretability, generalization, and flexibility of prompt generation without the need for additional training. (Section 1)
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **Model collapse** (constructs) — *causes*
  > Consequently, the model’s ability to generalize to real-world data is compromised, as it increasingly relies on the distorted distribution provided by prior AI generations rather than learning accurate representations of the real world. (Section 1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- **Code editing** (behaviors tasks) — *causes*
  > Reasoning over the differences between the two states admits a more local task (as evidenced by our data efficient learning), and this property can aid in generalization. (Appendix B.1)
  - [Learning to Edit Visual Programs with Self-Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/c585301e1c4b7c50039de5413ef585b5-Paper-Conference.pdf)
- **Inductive bias** (constructs) — *causes*
  > This suggests a desirable inductive bias of RAPTR that improves its generalization abilities beyond perplexity. (Section 4)
  - [Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *causes*
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
- **Generation diversity** (constructs) — *causes*
  - [Towards Few-Shot Adaptation of Foundation Models via Multitask Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d9a0718883f4a2eecee3c69c7213b05-Paper-Conference.pdf)
- **Consistency** (constructs) — *causes*
  - [Towards Few-Shot Adaptation of Foundation Models via Multitask Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d9a0718883f4a2eecee3c69c7213b05-Paper-Conference.pdf)
- **Continual learning** (constructs) — *causes*
  - [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf)
- **Inductive reasoning** (constructs) — *causes*
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **World knowledge** (constructs) — *causes*
  - [FakeShield: Explainable Image Forgery Detection and Localization via Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d4e0ab9d8ff180bf5b95c258842d16e-Paper-Conference.pdf)
- **Shortcut learning** (constructs) — *causes*
  - [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.416.pdf)
- **Commonsense reasoning** (constructs) — *causes*
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **Few-shot prompting** (measurements) — *causes*
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
- **Knowledge transfer** (constructs) — *causes*
  - [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf)
- **Safety** (constructs) — *causes*
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **Spatial reasoning** (constructs) — *causes*
  > state-of-the-art VLMs have exhibited strong spatial reasoning and temporal understanding capabilities across various vision tasks (Nag et al., 2022; Chen et al., 2024; Hong et al., 2023; Gao et al., 2024), allowing them to generalize to novel scenarios. (Section 1)
  - [Vision Language Models are In-Context Value Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/54854cf15a24fff9f5134a8641136fe4-Paper-Conference.pdf)
- **Disentanglement** (constructs) — *causes*
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *causes*
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)
- **Abstraction** (constructs) — *causes*
  - [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf)
- **Planning** (constructs) — *causes*
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *causes*
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **Temporal understanding** (constructs) — *causes*
  > state-of-the-art VLMs have exhibited strong spatial reasoning and temporal understanding capabilities across various vision tasks (Nag et al., 2022; Chen et al., 2024; Hong et al., 2023; Gao et al., 2024), allowing them to generalize to novel scenarios. (Section 1)
  - [Vision Language Models are In-Context Value Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/54854cf15a24fff9f5134a8641136fe4-Paper-Conference.pdf)
- **Spatiotemporal reasoning** (constructs) — *causes*
  > VLA models enhanced with visual traces exhibit improved spatial-temporal awareness. This visual trace prompting technique enables better adaptation to variations in manipulation tasks and improves overall generalization.
  - [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Representation learning** (constructs) — *causes*
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Compositional generalization** (constructs) — *causes*
  - [MapNav: A Novel Memory Representation via Annotated Semantic Maps forVLM-based Vision-and-Language Navigation](https://aclanthology.org/2025.acl-long.639.pdf)
- **Robustness** (constructs) — *causes*
  - [Promoting Ensemble Diversity with Interactive Bayesian Distributional Robustness for Fine-tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pham25b/pham25b.pdf)
- **Pattern recognition** (constructs) — *causes*
  > PM enhances the model’s ability to recognize relationships between nodes of the same type, improving its understanding of circuit structures and generalizability. (Section 3.2)
  - [Position: General Intelligence Requires Reward-based Pretraining](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25n/han25n.pdf)
- **Flatness** (constructs) — *correlates*
  > We attend to recent studies that have demonstrated that the generalization performance of a model is closely linked to the flatness of the solution landscape (Keskar et al., 2017; Jiang et al., 2020a). (1. Introduction)
  - [SAFE: Finding Sparse and Flat Minima to Improve Pruning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25s/lee25s.pdf)
- **Meta-learning** (constructs) — *causes*
  > This intrinsic capacity allows agents to autonomously and adaptively refine their learning strategies in response to shifting tasks and domains, reducing dependence on human-programmed meta-processes (Section 1).
  - [Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cw/liu25cw.pdf)

### Associated with
- **Memorization** (constructs)
  > Disentangling the effects of generalization and test set memorization is critical to our understanding of language model performance, but this is becoming increasingly difficult as the pretraining datasets are rarely public for many of the LMs deployed today. (Section 1)
  - [AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7641940c7dd9e5de58c20e39586eb64-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Towards Understanding How Transformers Learn In-context Through a Representation Learning Lens](https://proceedings.neurips.cc/paper_files/paper/2024/file/01a8d63f9cb6dcbaa3092ccddd2075ac-Paper-Conference.pdf)
- **Overfitting** (constructs)
  > This indicated less overfitting and better generalization when NEFTune is used. (Section 5.1)
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
- **Knowledge transferability** (constructs)
  - [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf)
- **Adaptability** (constructs)
  > "we investigate whether ASPRM demonstrates model transferability and rating position, in-domain, and cross-domain generalization capability"
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **Instruction following** (constructs)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **Personalization** (constructs)
  > FedPGP (Cui et al., 2024): Incorporate a low-rank adaptation term with an additional contrastive loss to balance generalization and personalization.
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Data contamination** (constructs)
  > “the contamination of evaluation metrics through direct memorization of test samples, which undermines the assessment of a model’s capabilities by allowing it to succeed through recall rather than by applying intended skills (Dataset Contamination).”
  - [Towards Efficient and Multifaceted Computer-assisted Pronunciation Training Leveraging Hierarchical Selective State Space Model and Decoupled Cross-entropy Loss](https://aclanthology.org/2025.naacl-long.99.pdf)
- **Specialization** (constructs)
  > Specialization trades generality for inference efficiency: a small model trained on data close to the targeted domain can be strong on this domain. (Section 4)
  - [Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf)
- **Training stability** (constructs)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Factuality** (constructs)
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Few-shot learning** (measurements)
  > Humans exhibit remarkable few-shot learning capabilities, rapidly generalizing from a single task demonstration to related conditions by integrating the observed behavior with their internal world model.
  - [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ac50fd0a4eeeb1f077b17bb7c5353c3-Paper-Conference.pdf)
- **Expressive power** (constructs)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
- **Reversal curse** (constructs)
  - [The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://proceedings.iclr.cc/paper_files/paper/2024/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf)
- **Expert specialization** (constructs)
  > We also observe that after instruction-tuning, the MoE models exhibit better expert usage, which may help prevent the expert collapse for generalization after instruction-tuning as in Zuo et al. (2021). (Section 4.3)
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **Fairness** (constructs)
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  > Unlike prior studies that primarily focus on tasks from a single domain, our method demonstrates strong generalizability across web agents, mathematical reasoning, and scientific discovery domains, further proving its effectiveness. (Section 2)
  - [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Reliability** (constructs)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Locality** (constructs)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Knowledge editing** (behaviors tasks)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **Weak-to-strong generalization** (constructs)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Scalability** (constructs)
  > This paper aims to evaluate and rethink the generalization capability of the SKP paradigm from four perspectives including Granularity, Transferability, Scalability, and Universality. (Abstract)
  - [Multimodal Transformers are Hierarchical Modal-wise Heterogeneous Graphs](https://aclanthology.org/2025.acl-long.110.pdf)
- **Code generation** (behaviors tasks)
  > ...the generalization abilities of the pre-trained model (i.e., code comprehension, instruction-following, code generation, etc.). (Section 4)
  - [Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dt/li25dt.pdf)
- **Hallucination** (behaviors tasks)
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Constrained Human-AI Cooperation: An Inclusive Embodied Social Intelligence Challenge](https://proceedings.neurips.cc/paper_files/paper/2024/file/4eb8e997fc91086225b7484cf8eac341-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  > The first limitation is that TPO may introduce a stronger form of “catastrophic forgetting”. The results in Sec. 4.2 indicate that while TPO exhibits excellent performance on in-distribution datasets, it may suffer from performance degradation on out-of-distribution datasets.
  - [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf)
- **Specificity** (constructs)
  > Generalization and specificity are tied together by an inherent trade-off: abstaining from everything achieves perfect generalization but no specificity, and not abstaining at all results in perfect specificity rates but no generalization. (Section 5.1)
  - [DrawEduMath: Evaluating Vision Language Models with Expert-Annotated Students’ Hand-Drawn Math Images](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Image restoration** (behaviors tasks)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Image editing** (behaviors tasks)
  > To further demonstrate the generalization and applicability of ELM, we evaluate its ability to generate samples from novel classes and perform image editing tasks, with the results in Appendix A.2. (Section 4.4)
  - [Elucidating the design space of language models for image generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25w/liu25w.pdf)
- **Pattern recognition** (constructs)
  - [LICO: Large Language Models for In-Context Molecular Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/84b16af3773fc5825ddb64996190289a-Paper-Conference.pdf)
- **Abstraction** (constructs)
  - [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf)
- **Synthetic data generation** (behaviors tasks)
  - [Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e0bfe8bbaa0e70809f0a8ccd9c2ff3e-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements)
  > However, these judge models demonstrate poor generalization when evaluating different LLMs and benchmarks (Laskar et al., 2023; Huang et al., 2024). (Section 2)
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks)
  - [DrawEduMath: Evaluating Vision Language Models with Expert-Annotated Students’ Hand-Drawn Math Images](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Universality** (constructs)
  - [Multimodal Transformers are Hierarchical Modal-wise Heterogeneous Graphs](https://aclanthology.org/2025.acl-long.110.pdf)
- **Self-correction** (behaviors tasks)
  - [UniRAG: Unified Query Understanding Method for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.694.pdf)
- **Inductive bias** (constructs)
  > Our results indicate that common LLM architectures and training setups might encode very similar inductive biases, freeing practitioners to optimize them for training efficiency without adversely affecting downstream generalization. (Section 1)
  - [LLMs on the Line: Data Determines Loss-to-Loss Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mayilvahanan25a/mayilvahanan25a.pdf)
- **In-context classification** (behaviors tasks)
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
- **Transitive reasoning** (constructs)
  - [Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf)
- **Reward overoptimization** (constructs)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
- **Code debugging** (behaviors tasks)
  > "Our algorithm yields a significant boost in performance compared to best-of-N and self-repair, and also exhibits strong generalisation across datasets and models."
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **MIND** (measurements)
  > However, its accuracy drops significantly when tested on other datasets, indicating its inability to generalize well. (Section 4.1)
  - [One Planner To Guide Them All ! Learning Adaptive Conversational Planners for Goal-oriented Dialogues](https://aclanthology.org/2025.emnlp-main.1124.pdf)
- **Long-form text generation** (behaviors tasks)
  - [Unveiling Internal Reasoning Modes inLLMs: A Deep Dive into Latent Reasoning vs. Factual Shortcuts with Attribute Rate Ratio](https://aclanthology.org/2025.emnlp-main.112.pdf)
