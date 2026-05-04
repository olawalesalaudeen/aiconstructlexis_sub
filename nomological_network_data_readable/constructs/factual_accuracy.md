# Factual accuracy
**Type:** Construct  
**Referenced in:** 55 papers  
**Also known as:** Fact-checking capability, Correctness, Factual reasoning, Sincerity, Fact discernment, Factual consistency, Factuality preservation  

## State of the Field

Across the provided literature, 'Factual accuracy' is predominantly characterized as the alignment between a model's generated output and a source of truth, which can be external evidence, a source document, or real-world facts. The most common framing, often termed 'factual consistency' or 'factuality,' centers on a model's ability to generate correct, verifiable statements while avoiding errors such as 'hallucinations' or outputs that 'diverge from real-world facts' (GradOT). A smaller set of papers conceptualizes this as a more active capacity, using terms like 'fact-checking capability' or 'fact discernment' to describe the ability to assess truthfulness, verify claims, and distinguish correct from incorrect information. A few specific framings also appear, such as 'sincerity,' which introduces the dimension of avoiding deception, and 'correctness,' which applies the concept narrowly to the accuracy of generated training data. While a standard operationalization is not detailed, some papers mention specific instruments; for instance, one study uses 'FActScore to assess the rate of factuality degradation' ("Data Quality Issues..."), while others reference 'FactVC' and 'HHEM-2.1-Open' for evaluating 'factual consistency'. The study of this construct is frequently linked to enhancing model trustworthiness, as noted in discussions of auditing 'fact-checking capacities' and 'factual reasoning capabilities' ("ReSCORE...").

## Sources

**[ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.17.pdf) (as "Fact-checking capability")**
> The overall capacity of an LLM to correctly verify claims and produce sound justifications across diverse and complex real-world scenarios.

**[ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.17.pdf) (as "Factual reasoning")**
> The latent ability of an LLM to assess the truthfulness of claims by integrating knowledge and generating valid justifications, beyond mere verdict prediction.

**[Capture the Key in Reasoning to EnhanceCoTDistillation Generalization](https://aclanthology.org/2025.acl-long.22.pdf) (as "Sincerity")**
> The latent tendency of a model to provide truthful and evidence-backed responses without deception during cooperation with humans.

**[JuStRank: BenchmarkingLLMJudges for System Ranking](https://aclanthology.org/2025.acl-long.35.pdf) (as "Correctness")**
> The latent accuracy of generated training samples in correctly representing the intended relation between entities without factual or labeling errors.

**[ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.53.pdf)**
> The latent trait reflecting a model's ability to generate responses that are factually correct and grounded in reliable external evidence.

**[400B](https://aclanthology.org/2025.acl-long.250.pdf) (as "Fact discernment")**
> The ability to accurately distinguish between correct factual information and incorrect or counterfactual statements, especially when both are present in the context.

**[GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models](https://aclanthology.org/2025.acl-long.256.pdf) (as "Factuality")**
> The extent to which an LLM's outputs align with real-world facts, particularly in avoiding hallucinations and maintaining truthfulness even under misleading or ambiguous prompts.

**[HD-NDEs: Neural Differential Equations for Hallucination Detection inLLMs](https://aclanthology.org/2025.acl-long.310.pdf) (as "Factual consistency")**
> The degree to which the model's generated summary aligns with factually accurate content from the source video, avoiding hallucinations or incorrect claims.

**[Data Quality Issues in Multilingual Speech Datasets: The Need for Sociolinguistic Awareness and Proactive Language Planning](https://aclanthology.org/2025.acl-long.371.pdf) (as "Factuality preservation")**
> The degree to which generated text remains faithful to the factual information contained in the original source text across iterations.

## Relationships

### Factual accuracy →
- **Human evaluation** (measurements) — *measured_by*
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf)
- **ASQA** (measurements) — *measured_by*
  - [Exploring Large Language Models for Detecting Mental Disorders](https://aclanthology.org/2025.emnlp-main.1753.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
