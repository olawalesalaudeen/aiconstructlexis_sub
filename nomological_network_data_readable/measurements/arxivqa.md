# ArXivQA
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** arXiVQA, ArxiVQA  

## State of the Field

ArXivQA is a measurement instrument built from academic papers on ArXiv, with a consistent focus on questions related to scientific figures. Across the provided sources, it is most commonly used to evaluate `Visual question answering` and general `Question answering` capabilities. The format is described in multiple ways; one paper defines it as a "visual question answering (VQA) dataset" ("VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents"), while another specifies it is a "multiple-choice question answering dataset" where performance is measured by accuracy. A different operationalization frames ArXivQA as a "page-level retrieval task" used to measure `Information retrieval`. In this framing, a model uses "the question as the query, and the associated page as the gold document" ("ColPali: Efficient Document Retrieval with Vision Language Models"). The dataset's components are described as including "questions, context images, and gold answers" or "page-question-answer triplet[s]". Thus, while its prevailing use is for evaluating VQA, its structure also supports its application as a retrieval benchmark.

## Sources

**[VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)**
> A visual question answering (VQA) dataset consisting of questions about figures from ArXiv academic papers.

**[ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf) (as "arXiVQA")**
> A page-level retrieval task built from scientific figures from arXiv, using the question as the query and the associated page as the target.

**[On the Relation Between Fine-Tuning, Topological Properties, and Task Performance in Sense-Enhanced Embeddings](https://aclanthology.org/2025.acl-long.1152.pdf) (as "ArxiVQA")**
> A multiple-choice question answering dataset derived from academic papers, used to evaluate document visual question answering performance in both closed- and open-domain settings.

## Relationships

### → ArXivQA
- **Question answering** (behaviors tasks) — *measured_by*
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We collect question-document pairs from a series of VQA datasets, targeting different document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024b), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for various figure types, and SlideVQA (Tanaka et al., 2023) for presentation slides.
  - [VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [Enhancing Machine Translation with Self-Supervised Preference Data](https://aclanthology.org/2025.acl-long.1166.pdf)
