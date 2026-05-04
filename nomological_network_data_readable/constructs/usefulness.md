# Usefulness
**Type:** Construct  
**Referenced in:** 20 papers  
**Also known as:** Downstream task performance, Model usefulness, Model utility, Utility, General utility  

## State of the Field

Across the provided literature, "Usefulness," often termed "model utility," is predominantly characterized as a model's ability to maintain its general performance and capabilities after undergoing some form of modification. The most frequent contexts for this construct are procedures like unlearning, model compression, or the application of safety mechanisms, where usefulness must be preserved. This is commonly framed as a balancing act, with one paper noting "a trade-off between unlearning effectiveness and model utility" ("KMMLU: Measuring Massive Multitask Language Understanding inKorean"). The prevailing definitions describe it as performance on tasks and data that were not targeted for modification or the ability to remain effective on legitimate tasks. Operationalization of this construct varies: some work measures it as the "aggregated performance of the model on retained data" ("Evaluating Morphological Compositional Generalization in Large Language Models"), while others assess it via performance on a range of downstream tasks after model compression. A distinct line of work defines "utility" in the context of synthetic data, where it refers to the data's value for a downstream task, often weighed against privacy guarantees. Less common are broader definitions, such as the general capability to satisfy human instructions, or highly specific ones, like the effectiveness of a diagram description as a textual aid for blind and low-vision users.

## Sources

**[Evaluating Morphological Compositional Generalization in Large Language Models](https://aclanthology.org/2025.naacl-long.60.pdf) (as "Model utility")**
> The overall performance and general capabilities of a model on tasks and data that were not targeted for unlearning.

**[BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.444.pdf) (as "Model usefulness")**
> The latent capacity of a model to maintain general language understanding and generation quality during and after unlearning procedures.

**[AutoEval-ToD: Automated Evaluation of Task-oriented Dialog Systems](https://aclanthology.org/2025.naacl-long.509.pdf) (as "Downstream task performance")**
> The ability of a language model to maintain its effectiveness on a range of evaluation tasks after undergoing compression techniques like quantization or pruning.

**[Causally Modeling the Linguistic and Social Factors that Predict Email Response](https://aclanthology.org/2025.naacl-long.595.pdf) (as "Utility")**
> The degree to which synthetically generated data is useful for a downstream task, often evaluated in contrast to the privacy guarantees provided.

**[FOCUS: Evaluating Pre-trained Vision-Language Models on Underspecification Reasoning](https://aclanthology.org/2025.acl-long.1338.pdf)**
> The degree to which a diagram description serves as an effective textual aid for BLV users in educational contexts, particularly in summarization, multiple-choice question solving, and open-ended question answering.

**[Knowledge Graph Retrieval-Augmented Generation forLLM-based Recommendation](https://aclanthology.org/2025.acl-long.1318.pdf) (as "General utility")**
> The model's ability to maintain high performance on general tasks and benchmarks regardless of the presence or activation of the SUDO key.

## Relationships

### Usefulness →
- **Human evaluation** (measurements) — *measured_by*
  - [TinySQL: A Progressive Text-to-SQLDataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1490.pdf)

### Associated with
- **Safety** (constructs)
  - [Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats](https://proceedings.iclr.cc/paper_files/paper/2025/file/699c5a2bb87a8aa32c4ad541d9997361-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)
