# Bamboogle
**Type:** Measurement  
**Referenced in:** 14 papers  

## State of the Field

Across the provided literature, Bamboogle is characterized as a question answering dataset used for evaluating models, often as an "unseen evaluation task" or for "out-of-domain evaluation." Its most prevalent application is to measure multi-hop question answering, with several papers explicitly grouping it with other datasets of this type. It is also used to assess a model's generalization ability beyond its training domain. A less common, single-paper claim is that it measures compositional reasoning. The dataset is consistently defined as containing "complex or adversarial questions." One source specifies that answering these questions "requires knowledge beyond Wikipedia’s coverage," while another notes they are questions that "Google answers incorrectly."

## Sources

**[Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf)**
> A dataset of complex or adversarial questions, used as an unseen evaluation task for RAG-tuned models.

## Relationships

### → Bamboogle
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  > We conduct experiments on five multi-hop QA datasets: HotPotQA (Yang et al., 2018), 2WikiMultiHopQA (2Wiki) (Ho et al., 2020), MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2023) and WebQuestions (WebQA) (Berant et al., 2013). (Section 4.1)
  - [Evaluating Sequence Labeling on the basis of Information Theory](https://aclanthology.org/2025.acl-long.1352.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > “For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2022), and PopQA (Mallen et al., 2022). These datasets test the model’s generalization ability beyond the training domain.”
  - [ViClaim: A Multilingual Multilabel Dataset for Automatic Claim Detection in Videos](https://aclanthology.org/2025.emnlp-main.22.pdf)
- **Compositional reasoning** (constructs) — *measured_by*
  > Bamboogle (Press et al., 2023) includes complex questions that Google answers incorrectly, assessing compositional reasoning. (Section 4.1)
  - [CLIP-MoE: Towards Building Mixture of Experts forCLIPwith Diversified Multiplet Upcycling](https://aclanthology.org/2025.emnlp-main.276.pdf)
