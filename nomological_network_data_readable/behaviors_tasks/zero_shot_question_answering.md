# Zero-shot question answering
**Type:** Behavior  
**Referenced in:** 8 papers  
**Also known as:** Zero-shot Question Answering  

## State of the Field

Across the surveyed literature, zero-shot question answering is characterized as the behavior of a model performing tasks without any task-specific training, fine-tuning, or examples provided in the prompt or context. The most common definition specifies this as "generating correct answers to multiple-choice questions," while other papers adopt a broader framing that includes general question answering on downstream tasks or other natural language understanding and reasoning tasks. This behavior is consistently operationalized by measuring a model's performance, typically reported as "zero-shot accuracy," across a wide array of evaluation benchmarks. The most frequently cited instruments for this purpose are PIQA, BoolQ, and WinoGrande. Other benchmarks commonly used to measure this behavior include HellaSwag, ARC, MMLU, and LAMBADA. As one study notes, evaluation involves reporting "the zero-shot accuracy on various benchmarks, including PIQA, ARC, HellaSwag, and WinoGrande" (QLLM: Accurate and Efficient Low-Bitwidth Quantization for Large Language Models). The consistent focus is on assessing a model's capabilities on unseen tasks without task-specific adaptation.

## Sources

**[PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)**
> Generating correct answers to multiple-choice questions without any task-specific training examples provided in context.

**[ShiftAddLLM: Accelerating Pretrained LLMs via Post-Training Multiplication-Less Reparameterization](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c30a37c75f062e0bf79297c73db8c6c-Paper-Conference.pdf) (as "Zero-shot Question Answering")**
> The observable behavior of answering questions on downstream tasks without fine-tuning or additional training.

## Relationships

### Zero-shot question answering →
- **BoolQ** (measurements) — *measured_by*
  > “For zero-shot evaluation, we employ BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), WinoGrande (Keisuke et al., 2019), and TruthfulQA (Lin et al., 2022).” (Section 5.4)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > “we also examined the zero-shot capabilities of pruned models. In detail, we report the accuracy in six zero-shot tasks including PIQA”
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  > “For zero-shot evaluation, we employ BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), WinoGrande (Keisuke et al., 2019), and TruthfulQA (Lin et al., 2022).” (Section 5.4)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Discovering Sparsity Allocation for  Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **OBQA** (measurements) — *measured_by*
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
