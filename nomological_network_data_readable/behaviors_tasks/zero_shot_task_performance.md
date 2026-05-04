# Zero-shot task performance
**Type:** Behavior  
**Referenced in:** 17 papers  

## State of the Field

Across the surveyed literature, Zero-shot task performance is consistently defined as the observable ability of a model to complete language understanding, question answering, or commonsense reasoning tasks when given no in-context examples. The operationalization of this behavior appears highly standardized in the provided papers. Performance is almost universally measured using the `LLM Evaluation Harness` framework, which facilitates evaluation on a variety of downstream tasks. The primary metric reported is accuracy, which one study specifies is calculated as the "average accuracy over five runs in each table" (Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models). This evaluation is conducted on a suite of standardized benchmarks, with `HellaSwag`, `PIQA`, and `ARC` appearing as frequently used examples. Other datasets such as `WinoGrande`, `BoolQ`, and `MMLU` are also commonly part of the evaluation set to assess this capability.

## Sources

**[CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)**
> The observable performance of a model on various language understanding tasks, such as question answering and commonsense reasoning, when given no in-context examples.

## Relationships

### Zero-shot task performance →
- **LLM Evaluation Harness** (measurements) — *measured_by*
  > zero-shot tasks implemented in Language Model Evaluation Harness (18)
  - [A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/db6ccc979860d7a233ecaf588bb23512-Paper-Conference.pdf)
- **MNLI** (measurements) — *measured_by*
  - [Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/db6ccc979860d7a233ecaf588bb23512-Paper-Conference.pdf)
- **RTE** (measurements) — *measured_by*
  - [Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/db6ccc979860d7a233ecaf588bb23512-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > For a fair comparison, we evaluate the models on MMLU (23), Arc Challenge (6), and OpenBookQA (35) zero-shot tasks implemented in Language Model Evaluation Harness (18).
  - [SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3504a4fa45685d668ce92797fbbf1895-Paper-Conference.pdf)
- **Mutual** (measurements) — *measured_by*
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
- **ETHICS** (measurements) — *measured_by*
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)

### → Zero-shot task performance
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [SliceGPT: Compress Large Language Models by Deleting Rows and Columns](https://proceedings.iclr.cc/paper_files/paper/2024/file/316648eb8b4ffb6010f531b07848c300-Paper-Conference.pdf)
