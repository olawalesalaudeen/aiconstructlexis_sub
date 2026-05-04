# Emergent abilities
**Type:** Construct  
**Referenced in:** 16 papers  
**Also known as:** Emergent capabilities, Emergence, Emergent ability  

## State of the Field

Across the surveyed literature, "Emergent abilities" are most frequently defined as a phenomenon where a model's performance on specific tasks improves dramatically and unpredictably after surpassing a certain scale threshold, manifesting capabilities not observed in smaller models. This dominant framing often specifies that performance remains near random chance until a sharp improvement occurs with increased pretraining compute. A smaller body of work offers alternative definitions; one paper provides a three-part characterization involving discontinuous improvement, simultaneous improvement across multiple tasks, and the learning of underlying data regularities. Another distinct framing, present in a few papers, describes emergence as new capabilities arising from the collaboration of multiple models, where a system can solve problems that individual models cannot. The primary driver for this construct is reported to be model scalability. These abilities are described as "qualitatively new," with cited examples including complex reasoning, abstract language comprehension, instruction following, and in-context few-shot learning. To operationalize this construct, researchers measure model performance on benchmarks such as MMLU and BIG-Bench. The concept is also studied in relation to text generation, with one paper noting that emergence may be more prevalent on string-match and multiple-choice tasks. Finally, one study suggests the phenomenon can disappear if the model is trained on the test task, pointing to a potential confound in its evaluation.

## Sources

**[Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)**
> The phenomenon where a model's performance on specific tasks appears to improve dramatically and unpredictably once it surpasses a certain size threshold, manifesting capabilities not observed in smaller models.

**[Training on the Test Task Confounds Evaluation and Emergence](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab8c971c2ccd12bac0ab249f75e2c16d-Paper-Conference.pdf) (as "Emergent capabilities")**
> The phenomenon where a model's performance on a task remains near random chance up to a certain scale of pretraining compute, after which it improves sharply.

**[A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cd2b0a6b7423af6369cbdbbb228e8d0-Paper-Conference.pdf) (as "Emergence")**
> A phenomenon characterized by sudden performance improvement on a task, simultaneous improvement across multiple tasks, and a correlation with the model learning underlying data-generating regularities.

**[CoPL: Collaborative Preference Learning for PersonalizingLLMs](https://aclanthology.org/2025.emnlp-main.651.pdf) (as "Emergent ability")**
> The phenomenon where a system of collaborating models demonstrates capabilities not present in any of the individual models.

## Relationships

### Emergent abilities →
- **MMLU** (measurements) — *measured_by*
  > "the MMLU benchmark ... evaluated using 56 LLMs" and "Fig. 1a–3a show the scaling trend of accuracy on the MMLU" (Fig. 1 caption; Sec. 2.3)
  - [U-shaped and Inverted-U Scaling behind Emergent Abilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f696200311b445af686c3ebd87ade1d7-Paper-Conference.pdf)
- **BIG-Bench** (measurements) — *measured_by*
  > "Fig. 4 shows U-shaped vs. inverted-U scaling of Hindu knowledge, conceptual combinations, and analogical similarity datasets in Big-Bench ... totaling 6 datasets" (Sec. 2.3)
  - [U-shaped and Inverted-U Scaling behind Emergent Abilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f696200311b445af686c3ebd87ade1d7-Paper-Conference.pdf)

### → Emergent abilities
- **Scalability** (constructs) — *causes*
  - [Neural Residual Diffusion Models for Deep Scalable Vision Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/d51ceadaf09a4699f18986702df24987-Paper-Conference.pdf)

### Associated with
- **In-context learning** (constructs)
  - [Lines of Thought in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/649f080d8891ab4d4b262cb9cd52e69a-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [U-shaped and Inverted-U Scaling behind Emergent Abilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f696200311b445af686c3ebd87ade1d7-Paper-Conference.pdf)
- **Zero-shot learning** (constructs)
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.354.pdf)
