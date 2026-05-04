# Document understanding
**Type:** Construct  
**Referenced in:** 25 papers  
**Also known as:** Document comprehension, Document reasoning  

## State of the Field

Across the provided literature, Document Understanding is most commonly defined as the ability to extract and use information from a document to answer a question. A smaller set of papers uses the related term "document comprehension" to emphasize the interpretation of content, structure, and layout, while a single source introduces "document reasoning" to describe inference across heterogeneous document types like text and tables. The construct is described as a "foundational AI capability" applicable to complex, unstructured, and often multimodal documents containing text, images, and figures. To operationalize this construct, papers commonly use question-answering tasks; Document Question Answering (DocQA) and Document Visual Question Answering (DocVQA) are explicitly named as evaluation methods. Other tasks reported to assess it include document classification and information extraction. One paper notes that there is an "absence of well-defined standards for direct quality assessment" for this capability.

## Sources

**[xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)**
> The ability to extract and use relevant information from a retrieved document to answer a question.

**[UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Document comprehension")**
> The latent ability to understand and interpret the content, structure, and context of complex, unstructured documents.

**[2025.emnlp-main.710.checklist](https://aclanthology.org/attachments/2025.emnlp-main.710.checklist.pdf) (as "Document reasoning")**
> The latent ability to draw inferences and synthesize information across heterogeneous document types, such as text and structured tables.

## Relationships

### Document understanding →
- **DocVQA** (measurements) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **OCR-VQA** (measurements) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **ChartQA** (measurements) — *measured_by*
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
- **InfoVQA** (measurements) — *measured_by*
  - [CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eb/wang25eb.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
- **AI2D** (measurements) — *measured_by*
  - [CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eb/wang25eb.pdf)
- **SROIE** (measurements) — *measured_by*
  - [Deriving Strategic Market Insights with Large Language Models: A Benchmark for Forward Counterfactual Generation](https://aclanthology.org/2025.emnlp-main.576.pdf)

### → Document understanding
- **Visual perception** (constructs) — *causes*
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)

### Associated with
- **Optical character recognition** (behaviors tasks)
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **Long-context understanding** (constructs)
  - [LLM-Guided Co-Training for Text Classification](https://aclanthology.org/2025.emnlp-main.1584.pdf)
