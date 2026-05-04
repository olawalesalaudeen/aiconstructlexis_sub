# UltraFeedback
**Type:** Measurement  
**Referenced in:** 66 papers  
**Also known as:** Ultrafeedback, Ultra-Feedback  

## State of the Field

Across the surveyed literature, UltraFeedback is framed in two primary ways: as a public benchmark for evaluation and as a high-quality dataset for model tuning. It is consistently described as a preference dataset composed of instruction-response pairs, with a recurring detail being that its preference labels are annotated by GPT-4, which some papers contrast with human-annotated datasets. As a measurement instrument, papers use UltraFeedback to assess a range of model capabilities, including `Helpfulness`, `Commonsense knowledge`, `Instruction following`, `Faithfulness`, and `Dialogue generation`. The scores within the dataset are noted to be a weighted combination of "instruction-following, truthfulness, honesty, and helpfulness" (ReFT: Representation Finetuning for Language Models). In its role as a benchmark, it is frequently used to evaluate "generative judges on preference prediction" (Learning LLM-as-a-Judge for Preference Alignment) and general "alignment performance" (ProcessBench: Identifying Process Errors in Mathematical Reasoning). As a training resource, it is employed for "instruction tuning" and for training reward models. More specific applications include using its prompts for "best-of-n alignment experiments" and leveraging its development set for hyperparameter tuning.

## Sources

**[ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf) (as "Ultrafeedback")**
> A high-quality instruction dataset built from scored candidate responses and used for instruction tuning.

**[Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf)**
> A public benchmark used to evaluate generative judges on preference prediction.

**[Towards Cost-Effective Reward Guided Text Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rashid25a/rashid25a.pdf) (as "Ultra-Feedback")**
> Ultra-Feedback dataset used for additional fine-grained text generation experiments.

## Relationships

### UltraFeedback →
- **Critique** (behaviors tasks) — *causes*
  - [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)

### → UltraFeedback
- **Instruction following** (constructs) — *measured_by*
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **Truthfulness** (constructs) — *measured_by*
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **Dialogue generation** (behaviors tasks) — *measured_by*
  - [MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ddab70bf41ffe5d423840644d3357f4-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH) (Bai et al., 2022), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU) (Ji et al., 2024), Reward3, UltraFeedback(UltraF) (Cui et al., 2024), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)

### Associated with
- **Instruction following** (constructs)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
