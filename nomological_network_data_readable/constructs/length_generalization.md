# Length generalization
**Type:** Construct  
**Referenced in:** 64 papers  
**Also known as:** Length generalizability, Length extrapolation, Context Length Generalizability, Sequence generalization, Generative length extrapolation  

## State of the Field

Length generalization is predominantly defined as a model's ability to be trained on shorter sequences and then perform effectively on sequences longer than those seen during training, without performance degradation. This concept is frequently referred to using interchangeable terms like "length extrapolation" and "long-context generalization." A recurring theme is that this ability serves as a proxy for whether a model has learned a scalable, algorithmic solution rather than memorizing training data; as one paper states, it "is used as a proxy for whether the model has learned the correct problem-solving strategy for the given task" (What Algorithms can Transformers Learn? A Study in Length Generalization). A few papers offer more specific framings, such as for program synthesis (producing longer code) or generative tasks (maintaining quality in long-form speech generation).

To operationalize this construct, researchers employ a "training on short, testing on long" evaluation paradigm across a wide array of benchmarks. Commonly used instruments mentioned in the provided data include LongBench, InfiniteBench, PG-19, The Pile, and C4. The ability is also assessed through performance on downstream tasks like text summarization and information retrieval. The provided literature suggests several factors that influence length generalization. For instance, some work reports that a limited effective receptive field can hinder it, while adaptive computation is reported to improve it. The construct is also studied in relation to other concepts such as systematic generalization, mathematical reasoning, and long-context understanding.

## Sources

**[ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/c43b2989b1ba055aa713a4abbe4a8b05-Paper-Conference.pdf)**
> The ability of a model to be trained on shorter sequences and then be applied to longer sequences without performance degradation.

**[InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf) (as "Length generalizability")**
> The ability of a large language model to effectively process sequences that are longer than those it was exposed to during its pre-training phase.

**[Can LLMs Solve Longer Math Word Problems Better?](https://proceedings.iclr.cc/paper_files/paper/2025/file/474ada926b331d78f06d95e8913111cc-Paper-Conference.pdf) (as "Context Length Generalizability")**
> The ability of a Large Language Model to solve math word problems with extended narratives or lengthy contexts.

**[Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf) (as "Length extrapolation")**
> The ability to effectively process sequences that are longer than any seen during the training phase.

**[MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf) (as "Long-context generalization")**
> The ability of a model to maintain its performance and effectiveness when processing input sequences that are significantly longer than those it was exposed to during its pre-training phase.

**[Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eedf422d321a20b2bd5e947c57c82e96-Paper-Conference.pdf) (as "Sequence generalization")**
> The ability to handle new sequences within seen topics after learning from many training sequences.

**[Long-Form Speech Generation with Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25k/park25k.pdf) (as "Generative length extrapolation")**
> The ability to maintain high-quality and coherent generation for durations significantly longer than those seen during training.

## Relationships

### Length generalization →
- **InfiniteBench** (measurements) — *measured_by*
  > We compare our method with existing length extrapolation approaches...on LongBench (Bai et al., 2023) and InfiniteBench (Zhang et al., 2024), evaluating them on Llama2-7B-chat-hf... (Section 5.1)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **PG-19** (measurements) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Books3** (measurements) — *measured_by*
  - [Scaling Laws of RoPE-based Extrapolation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d33b741600f100b31256c70a46f66ec9-Paper-Conference.pdf)
- **NarrativeQA** (measurements) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  > We compare our method with existing length extrapolation approaches...on LongBench (Bai et al., 2023) and InfiniteBench (Zhang et al., 2024), evaluating them on Llama2-7B-chat-hf... (Section 5.1)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Needle-in-a-haystack test** (measurements) — *measured_by*
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **RULER** (measurements) — *measured_by*
  - [To Mask or to Mirror: Human-AIAlignment in Collective Reasoning](https://aclanthology.org/2025.emnlp-main.123.pdf)
- **GovReport** (measurements) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **QMSum** (measurements) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Qasper** (measurements) — *measured_by*
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **CodeParrot** (measurements) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eedf422d321a20b2bd5e947c57c82e96-Paper-Conference.pdf)
- **The Pile** (measurements) — *measured_by*
  > To assess their capability for length extrapolation, we evaluated the implicit models on the test split of the D-PILE, which was packed with longer sequences consisting of 4096, 8192, and 16384 tokens. (Section 5)
  - [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf)
- **Sparsity** (constructs) — *correlates*
  > our experiments adjust the sparsity of several synthetic tasks, and we observe that length generalization improves monotonically with decreasing sparsity. (Section 1)
  - [The Role of Sparsity for Length Generalization in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/golowich25a/golowich25a.pdf)
- **C4** (measurements) — *measured_by*
  > Finally, we study the interplay between sparsity and length generalization in natural language. ... We trained our models using the OLMo codebase (Groeneveld et al., 2024) on the C4 dataset (Raffel et al., 2019). (Section 5.3)
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
- **Memorization** (constructs) — *measured_by*
  - [Understanding and Improving Length Generalization in Recurrent Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/buitrago25a/buitrago25a.pdf)
- **LongMemEval** (measurements) — *measured_by*
  - [ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **HELMET** (measurements) — *measured_by*
  - [ProbingLLMWorld Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.235.pdf)

### → Length generalization
- **Effective receptive field** (constructs) — *causes*
  > Through a series of visualizations, analyses, and empirical measures, recognize that although Mamba can theoretically capture global interactions via the recurrent state, its limited ERF prevents significant length-extrapolation; (Section 1)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
- **Adaptive computation** (constructs) — *causes*
  > In this work, we demonstrate that looped Transformers with an adaptive number of steps significantly improve length generalization. (ABSTRACT)
  - [Looped Transformers for Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf)
- **Permutation invariance** (constructs) — *causes*
  - [Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf)

### Associated with
- **Long-context understanding** (constructs)
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  > We propose a new theoretical framework to study length generalization for the next-token prediction task, as performed by decoder-only transformers. (Abstract)
  - [The Role of Sparsity for Length Generalization in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/golowich25a/golowich25a.pdf)
- **Systematic generalization** (constructs)
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
- **Long-context processing** (constructs)
  - [Long-Short Alignment for Effective Long-Context Modeling in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25a/du25a.pdf)
- **Long-form text generation** (behaviors tasks)
  - [DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f050fa9f0d898e3f265d515f50ae8f9-Paper-Conference.pdf)
- **Extrapolation ability** (constructs)
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **Inductive bias** (constructs)
  > The short validation set reveals an architecture’s inductive bias in the absence of any disambiguating information about how it should generalize to longer lengths, as in the experiments of Del´etang et al. (2023). (Section 4)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Generalizing Reasoning Problems to Longer Lengths](https://proceedings.iclr.cc/paper_files/paper/2025/file/abcbdf504b621b4d1213aa7a5c489f8a-Paper-Conference.pdf)
- **Locality** (constructs)
  - [The Role of Sparsity for Length Generalization in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/golowich25a/golowich25a.pdf)
- **Easy-to-hard generalization** (constructs)
  > Our findings suggest that self-improvement is not limited to length generalization but also enables easy-to-hard generalization, where a model trained on simpler tasks successfully learns harder tasks without additional supervision. (Section 1)
  - [Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25j/park25j.pdf)
- **Attention sink** (constructs)
  > most training-free extrapolation methods are not only severely limited by memory bottlenecks, but also suffer from the attention sink, which restricts their scalability and effectiveness in practice. (Abstract)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Information retrieval** (behaviors tasks)
  - [Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning](https://aclanthology.org/2025.emnlp-main.1545.pdf)
