# 2WikiMultihopQA
**Type:** Measurement  
**Referenced in:** 72 papers  
**Also known as:** 2WikiMultiHopQA, 2wikimultihopqa, 2WIKIMULTIHOPQA, 2WikiMQA, 2WikiMHQA, 2WikiMulti-hopQA, 2Wikimultihop, 2Wiki, 2Wiki-MultiHopQA  

## State of the Field

Across the provided literature, 2WikiMultihopQA is consistently characterized as a multi-hop question-answering dataset derived from Wikipedia. Its prevailing use is to evaluate a model's ability to reason by integrating information across multiple documents to find an answer. The benchmark is most frequently used to measure the behavior of `Multi-hop question answering` and the construct of `Complex reasoning`, with some studies also using it to assess `Document question answering` and `Long-context understanding`. The nature of the required reasoning is described with some variation, from involving "two linked facts" to "up to 5-hop questions," and is noted by one paper to include "comparison and composition" tasks. Several papers operationalize it as an evaluation task for retrieval-augmented generation (RAG) systems, sometimes as an "unseen" dataset. It is also frequently identified as a component of the `LongBench` benchmark suite. In practice, it is often studied alongside other multi-hop QA datasets such as HotpotQA and Musique to assess model performance.

## Sources

**[Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf)**
> A multi-document, multi-hop question-answering dataset involving up to 5-hop questions synthesized from Wikipedia passages.

**[Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c27bf8d56d3d50c7aeaf7535dee975-Paper-Conference.pdf) (as "2WikiMultiHopQA")**
> A dataset used for evaluating retrieval-augmented generation performance on question-answer pairs.

**[Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf) (as "2wikimultihopqa")**
> A multi-hop question-answering dataset derived from Wikipedia, used as an unseen evaluation task for RAG-tuned models.

**[SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf) (as "2WIKIMULTIHOPQA")**
> A multi-hop question answering dataset that requires reasoning over multiple documents to find the answer.

**[OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf) (as "2WikiMQA")**
> A multi-hop question answering benchmark used to assess multi-step reasoning over long contexts.

**[Delving into Multilingual Ethical Bias: TheMSQADwith Statistical Hypothesis Tests for Large Language Models](https://aclanthology.org/2025.acl-long.16.pdf) (as "2WikiMHQA")**
> A multi-hop question answering dataset built from Wikipedia, requiring reasoning over multiple evidence documents.

**[Generalized Attention Flow: Feature Attribution for Transformer Models via Maximum Flow](https://aclanthology.org/2025.acl-long.981.pdf) (as "2WikiMulti-hopQA")**
> Multi-hop question answering dataset requiring reasoning over two linked facts, built from Wikipedia.

**[ALGEN: Few-shot Inversion Attacks on Textual Embeddings via Cross-Model Alignment and Generation](https://aclanthology.org/2025.acl-long.1186.pdf) (as "2Wikimultihop")**
> A challenging benchmark for multi-hop question answering where the knowledge graph is constructed from provided text passages and a large proportion of questions require reasoning types like comparison and composition.

**[ViClaim: A Multilingual Multilabel Dataset for Automatic Claim Detection in Videos](https://aclanthology.org/2025.emnlp-main.22.pdf) (as "2Wiki")**
> The 2WikiMultiHopQA (2Wiki) benchmark, a multi-hop open-domain question answering dataset used for in-domain evaluation.

**[RICO: Improving Accuracy and Completeness in Image Recaptioning via Visual Reconstruction](https://aclanthology.org/2025.emnlp-main.1106.pdf) (as "2Wiki-MultiHopQA")**
> A multi-hop question answering benchmark dataset designed to test reasoning over multiple documents from Wikipedia.

## Relationships

### → 2WikiMultihopQA
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  - [ImgTrojan: Jailbreaking Vision-Language Models withONEImage](https://aclanthology.org/2025.naacl-long.361.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Document question answering** (behaviors tasks) — *measured_by*
  > Performance comparison on eight LongBench datasets evaluating single/multi-document QA, summarization, and retrieval tasks... (Table 3)
  - [HVGuard: Utilizing Multimodal Large Language Models for Hateful Video Detection](https://aclanthology.org/2025.emnlp-main.457.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [DoLLMs Encode Frame Semantics? Evidence from Frame Identification](https://aclanthology.org/2025.emnlp-main.1500.pdf)
- **Information synthesis** (behaviors tasks) — *measured_by*
  - [From Scores to Steps: Diagnosing and ImprovingLLMPerformance in Evidence-Based Medical Calculations](https://aclanthology.org/2025.emnlp-main.549.pdf)
- **Long-context reasoning** (constructs) — *measured_by*
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)

### Associated with
- **LongBench** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
