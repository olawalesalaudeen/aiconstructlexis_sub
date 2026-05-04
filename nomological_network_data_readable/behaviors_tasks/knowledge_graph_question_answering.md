# Knowledge graph question answering
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Graph question answering  

## State of the Field

Across the provided literature, Knowledge graph question answering (KGQA) is consistently defined as the task of answering natural language questions by retrieving and reasoning over structured facts from a knowledge graph. This process is formalized in one paper as finding the correct answer `a*` given a question `q` and a graph `G`. A less common framing, termed "Graph question answering," describes a similar task involving a "textual graph." The provided sources state that KGQA requires a "deep understanding of natural language questions" and is thus related to `Natural language understanding`. This behavior is operationalized and measured using several benchmark datasets. The most frequently mentioned instruments are `WebQSP` and `CWQ`, which are described as "widely used" and "classical benchmarks for complex logical reasoning in KGQA." Other benchmarks cited for evaluating this task, though less often in this set of papers, include `GrailQA`, `MedQA`, and `Text2Cypher`.

## Sources

**[Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf)**
> The observable task of answering a natural language question by retrieving and reasoning over structured facts from a knowledge graph.

**[G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf) (as "Graph question answering")**
> The task of generating a natural language answer to a question based on the information contained within a provided textual graph.

## Relationships

### Knowledge graph question answering →
- **WebQSP** (measurements) — *measured_by*
  > We evaluate reasoning performance on benchmark KGQA datasets used by: WebQSP (Yih et al., 2016)... (Section 4.1)
  - [Personalized Generation In Large Model Era: A Survey](https://aclanthology.org/2025.acl-long.1202.pdf)
- **CWQ** (measurements) — *measured_by*
  > "We evaluate reasoning performance on benchmark KGQA datasets used by: WebQSP (Yih et al., 2016) includes 4,737 questions involving simple and two-hop reasoning, while CWQ (Talmor and Berant, 2018) features 34,689 questions requiring complex 2-4 hop reasoning."
  - [Efficient Long Context Language Model Retrieval with Compression](https://aclanthology.org/2025.acl-long.741.pdf)
- **GrailQA** (measurements) — *measured_by*
  > We assess the performance of SAFE on three widely-used multi-hop KGQA benchmarks: CWQ (Talmor and Berant, 2018), WebQSP (Yih et al., 2016), and GrailQA (Gu et al., 2021) (Section 5).
  - [PreP-OCR: A Complete Pipeline for Document Image Restoration and EnhancedOCRAccuracy](https://aclanthology.org/2025.acl-long.750.pdf)
- **WebQuestions** (measurements) — *measured_by*
  - [PreP-OCR: A Complete Pipeline for Document Image Restoration and EnhancedOCRAccuracy](https://aclanthology.org/2025.acl-long.750.pdf)
- **MedQA** (measurements) — *measured_by*
  > We evaluate KGQA benchmarks spanning different backbone KGs. ... MedQA (Jin et al., 2021) consists of questions extracted from USMLE exams. (Section 4.1)
  - [Social Bias in Multilingual Language Models: A Survey](https://aclanthology.org/2025.emnlp-main.1417.pdf)
- **Text2Cypher** (measurements) — *measured_by*
  > We evaluate KGQA benchmarks spanning different backbone KGs. ... The Text2cypher dataset (Ozsoy et al., 2024) emulates text2cypher queries encountered in enterprise KGs... (Section 4.1)
  - [Social Bias in Multilingual Language Models: A Survey](https://aclanthology.org/2025.emnlp-main.1417.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [PreP-OCR: A Complete Pipeline for Document Image Restoration and EnhancedOCRAccuracy](https://aclanthology.org/2025.acl-long.750.pdf)
- **Natural language understanding** (constructs)
  > KGQA poses challenges to existing approaches, as it requires a deep understanding of natural language questions and the ability to perform complex reasoning over KGs. (Section 1)
  - [Evaluating Large Language Models for Detecting Antisemitism](https://aclanthology.org/2025.emnlp-main.1793.pdf)
