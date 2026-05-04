# HotpotQA
**Type:** Measurement  
**Referenced in:** 181 papers  
**Also known as:** HotPotQA, HOTPOTQA, Hotpot-QA, Hotpot_QA, HotpotwikiQA  

## State of the Field

Across the provided literature, HotpotQA is consistently defined as a benchmark for question answering that requires multi-hop reasoning. The core task involves finding and integrating evidence from multiple supporting documents, which are frequently specified as originating from Wikipedia. Papers use HotpotQA to measure several capabilities, most prevalently multi-hop question answering, but also complex reasoning, information retrieval, and document question answering. The benchmark is applied in various settings, including open-domain, closed-book, and a "distractor setting" where irrelevant paragraphs are mixed with relevant ones. While most descriptions are consistent, there is some variation in how its outputs are characterized; one paper notes it involves "long answers containing many tokens," whereas another describes answers as "typically being short entities or yes/no responses." Its use extends beyond direct evaluation, as it is included within other benchmarks like LongBench and is sometimes used to generate synthetic training data or as a probing set for model analysis.

## Sources

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)**
> HotpotQA is a multi-hop question answering benchmark used to evaluate answering questions that require combining multiple pieces of evidence.

**[DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf) (as "HotPotQA")**
> A question answering benchmark that requires an agent to find and reason over multiple supporting documents from Wikipedia to answer complex questions.

**[SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf) (as "HOTPOTQA")**
> A question answering dataset that requires finding and reasoning over multiple supporting documents to answer complex questions.

**[RNNs are not Transformers (Yet):  The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf) (as "Hotpot-QA")**
> A multi-document question answering dataset in which the model answers a question using multiple related Wikipedia paragraphs, with retrieval difficulty manipulated by paragraph ordering.

**[iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.761.pdf) (as "Hotpot_QA")**
> A question answering dataset that requires multi-hop reasoning across multiple supporting documents to find the answer.

**[Behavioural vs. Representational Systematicity in End-to-End Models: An Opinionated Survey](https://aclanthology.org/2025.acl-long.1538.pdf) (as "HotpotwikiQA")**
> Multi-hop QA dataset derived from Wikipedia, combining elements of HotpotQA with long-context requirements.

## Relationships

### → HotpotQA
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  > Reasoning, including ... multi-hop question answering (HotpotQA)... (Section 2.2)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > “Complex Reasoning (HotpotQA (Yang et al., 2018)) is a multi-turn QA dataset.”
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > “For more complex tasks, such as multi-hop QA and dialogue, we use HotpotQA dataset (Yang et al., 2018) and Wikipedia of Wizard (WoW) (Dinan et al., 2019) for evaluation.”
  - [ESE: Espresso Sentence Embeddings](https://proceedings.iclr.cc/paper_files/paper/2025/file/60dc26558762425a465cb0409fc3dc52-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > Moreover, the choice of the four datasets, which include short- and long-form generation, question answering, summarization, and multi-hop reasoning, demonstrates the generalizability of the Sparse RAG approach. (Section 1)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *measured_by*
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  - [SmartRAG: Jointly Learn RAG-Related Tasks From the Environment Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/83ccb398f3ce9c4d137011f36a03c7d4-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > “Experiments are conducted on five widely used benchmarks: GSM8K (Cobbe et al., 2021), MATH, HumanEval, Trivia Creative Writing, and HotpotQA”
  - [From Personas to Talks: Revisiting the Impact of Personas onLLM-Synthesized Emotional Support Conversations](https://aclanthology.org/2025.emnlp-main.278.pdf)
- **Document question answering** (behaviors tasks) — *measured_by*
  > Performance comparison on eight LongBench datasets evaluating single/multi-document QA, summarization, and retrieval tasks... (Table 3)
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Continual learning** (constructs) — *measured_by*
  > “Continual Fine-Tuning: (a) SQuAD (Rajpurkar et al., 2016) paired with HotpotQA to inject more complex, multi-hop reasoning data after simpler QA”
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **Long-context reasoning** (constructs) — *measured_by*
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Fact-seeking question answering** (behaviors tasks) — *measured_by*
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **Text-based question answering** (behaviors tasks) — *measured_by*
  > we apply this intervention to ... two QA tasks, Natural Questions (NQ) and HotpotQA... By contrast, on the QA tasks, masking RH leads to a substantial performance decrease. These results confirm that ... retrieval heads play a more pivotal role in text-based QA. (Section 5.2)
  - [Please Translate Again: Two Simple Experiments on Whether Human-Like Reasoning Helps Translation](https://aclanthology.org/2025.emnlp-main.1032.pdf)

### Associated with
- **LongBench** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
- **HELMET** (measurements)
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf)
