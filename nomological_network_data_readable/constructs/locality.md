# Locality
**Type:** Construct  
**Referenced in:** 19 papers  

## State of the Field

Across the provided literature, Locality is consistently defined as a property of knowledge editing that measures the extent to which an edit is localized, ensuring a model's behavior on unrelated inputs remains unchanged. The prevailing framing emphasizes preventing unintended side effects, with one paper noting that a successful edit should "adjust the targeted knowledge locally while leaving unrelated knowledge unaffected." The field operationalizes this construct by evaluating an edited model's performance on a wide array of general benchmarks to detect degradation in areas untargeted by the edit. For instance, one study explicitly uses this method to "assess this, we evaluate the model on general benchmarks, including CommonsenseQA..., BigBench-Hard..., MMLU..., and GSM8k." Other measurement instruments frequently used to assess Locality include CounterFact, zs-RE, Natural Questions, and RedPajama. This evaluation is also applied to the Visual question answering task, and one source describes the underlying procedure as "comparing the outputs of the unedited and edited models" on unrelated knowledge. In the context of knowledge editing research, Locality is studied alongside other constructs such as Faithfulness and Generalization.

## Sources

**[VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The extent to which a knowledge edit is localized, ensuring the model's behavior on unrelated inputs remains unchanged.

## Relationships

### Locality →
- **zs-RE** (measurements) — *measured_by*
  > Results on three metrics for the two datasets using LLAMA2-7B and LLAMA-7B. (Table 1)
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **CounterFact** (measurements) — *measured_by*
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)
- **RedPajama** (measurements) — *measured_by*
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WikiDatarecent** (measurements) — *measured_by*
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **WikiDatacounterfact** (measurements) — *measured_by*
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **BBH** (measurements) — *measured_by*
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **MMLU** (measurements) — *measured_by*
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf)

### Associated with
- **Knowledge editing** (behaviors tasks)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **Reliability** (constructs)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Length generalization** (constructs)
  - [The Role of Sparsity for Length Generalization in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/golowich25a/golowich25a.pdf)
