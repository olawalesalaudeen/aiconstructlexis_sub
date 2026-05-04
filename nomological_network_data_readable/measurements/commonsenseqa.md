# CommonsenseQA
**Type:** Measurement  
**Referenced in:** 130 papers  
**Also known as:** CommonSenseQA, CSQA, Commonsense QA, Commonsense-QA, CommonSense-QA, CommonsenseQA (CSQA)  

## State of the Field

Across the surveyed literature, CommonsenseQA is consistently described as a multiple-choice question-answering benchmark. Its most frequently stated purpose is to evaluate a model's commonsense reasoning and commonsense understanding, though a notable subset of papers frames its use more broadly as assessing general understanding or general knowledge. The benchmark operationalizes these constructs through questions about everyday situations, with several sources specifying it uses a five-option format designed to be difficult for models that rely on "superficial cues" by including plausible distractors. Papers use CommonsenseQA to measure a range of capabilities beyond its primary target, including question answering, generalization, and reasoning. More specific applications include assessing zero-shot generalization, checking for data contamination, and evaluating the locality of model edits. It is frequently deployed alongside other reasoning benchmarks such as StrategyQA, ARC, and OpenBookQA. One paper notes that the dataset is built upon ConceptNet.

## Sources

**[Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf)**
> A commonsense question answering benchmark used to evaluate commonsense reasoning.

**[Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf) (as "CommonSenseQA")**
> CommonSenseQA is a commonsense question-answering benchmark used here to evaluate general understanding.

**[In-the-wild Audio Spatialization with Flexible Text-guided Localization](https://aclanthology.org/2025.acl-long.99.pdf) (as "CSQA")**
> A benchmark named Commonsense QA that evaluates a model's commonsense reasoning capabilities through a collection of multiple-choice question-answering tasks.

**[Did Translation Models Get More Robust Without AnyoneEven Noticing?](https://aclanthology.org/2025.acl-long.123.pdf) (as "Commonsense QA")**
> A multiple-choice question answering dataset that requires commonsense knowledge to predict the correct answers.

**[Understanding Overadaptation in Supervised Fine-Tuning: The Role of Ensemble Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25d/hao25d.pdf) (as "Commonsense-QA")**
> Question-answering dataset with over 10,000 real-world commonsense questions requiring models to identify relevant knowledge and distinguish plausible distractors.

**[EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf) (as "CommonSense-QA")**
> A multiple-choice question answering dataset that requires commonsense knowledge to predict the correct answer, with questions designed to be difficult for models that rely on superficial cues.

**[Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf) (as "CommonsenseQA (CSQA)")**
> A multiple-choice question answering benchmark designed to evaluate a model's commonsense reasoning and general knowledge.

## Relationships

### → CommonsenseQA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > "We evaluate our proposed method on several question-answering benchmarks, including ScienceQA (Lu et al., 2022), CommonsenseQA (Talmor et al., 2019), OpenBookQA (Mihaylov et al., 2018) and SIQA (Sap et al., 2019)."
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Commonsense question answering** (behaviors tasks) — *measured_by*
  > We consider nine varied downstream tasks: ... (c) general understanding (CommonSenseQA (Talmor et al., 2019), PhysicalIQA (Bisk et al., 2020))
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > In this section, we investigate whether our method is generally applicable beyond the medical domain. We use two general domain datasets, CommonsenseQA (CSQA) (Talmor et al., 2018) and OpenbookQA (OBQA) (Mihaylov et al., 2018)... (Section 4.5)
  - [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [Condor: EnhanceLLMAlignment with Knowledge-Driven Data Synthesis and Refinement](https://aclanthology.org/2025.acl-long.1092.pdf)
- **Short-context capability** (constructs) — *measured_by*
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Knowledge reasoning** (constructs) — *measured_by*
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Out-of-distribution detection** (behaviors tasks) — *measured_by*
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  > To evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three unseen KGQA datasets: FreebaseQA (Jiang et al., 2019), CSQA (Talmor et al., 2019) and MedQA (Jin et al., 2021). (Section 5.4)
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **Locality** (constructs) — *measured_by*
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [Taming Overconfidence in LLMs: Reward Calibration in RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/29fb6e1456b3d8b57ede5c45aa2c6537-Paper-Conference.pdf)
