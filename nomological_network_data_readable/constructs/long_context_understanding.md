# Long-context understanding
**Type:** Construct  
**Referenced in:** 167 papers  
**Also known as:** Long context understanding, Long text understanding, Long-context comprehension, Long-text understanding, Cross-page comprehension, Long Context, Long-context capabilities, Long-context capability, Long-document understanding, Long-context processing capability, Long-form video understanding, Long video understanding, Long image-sequence understanding, Long-context visual processing, Egocentric video understanding, Long-context modeling capability, Long-context modeling, Long-context Modeling Capacity, Recall ability, Long-range dependency understanding, Long sequence comprehension, Context memory, Long-range modeling, Long-range ability, Long-range context understanding, Long-form video-language understanding, Long document understanding, Long-range information access, Long-context ability, Long-context performance, Multi-modal long-context learning, Long-range capabilities, Long context reasoning, Long-term reasoning, Long-range dependency capture, Long-range reasoning, Long-range interaction reasoning, Long-distance dependency capture, Long-context problem solving, Long-range dependency handling, Long-range sequential reasoning, Long-horizon reasoning  

## State of the Field

Across the surveyed literature, "Long-context understanding" is predominantly framed as a latent ability of models to effectively process, comprehend, and utilize information from extended input sequences, often far exceeding their original training context windows. This construct is referred to by various names, including "long-context comprehension," "long-range reasoning," and "long-context capability," all pointing to the challenge of maintaining performance and coherence over lengthy inputs. The scope of "long context" is broad, encompassing single documents exceeding a page, conversational histories, and inputs spanning from 16K to 128K tokens. While most definitions focus on textual data, a notable subset extends the concept to multi-modal scenarios, defining specific facets like "long-form video understanding," "long image-sequence understanding," and the comprehension of documents containing text, tables, and images. A recurring theme across definitions is the model's capacity to not only process but also integrate relevant information, maintain coherence, and capture what some papers term "long-range dependencies" between distant elements in a sequence. The field operationalizes and measures this construct primarily through performance on specialized benchmarks. The most prevalent measurement instruments cited are LongBench, described as a "comprehensive, bilingual, multitask benchmark," and RULER, a synthetic benchmark for evaluating long-context models. Other frequently used benchmarks for textual understanding include InfiniteBench, L-Eval, and BABILong, while multi-modal abilities are assessed using instruments like EgoSchema for video and MMLongBench-Doc for visually-rich documents. This construct is studied alongside several related concepts, including length generalization, planning, and complex reasoning, and some work suggests that deficits in long-range reasoning can contribute to model hallucination.

## Sources

**[SmartPlay : A Benchmark for LLMs as Intelligent Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/063d1fadbde557466bf5bcffe814a64e-Paper-Conference.pdf) (as "Long text understanding")**
> The latent ability to comprehend and process lengthy or syntactically complex textual inputs, ranging from short lines to documents exceeding one page.

**[Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)**
> The latent ability of a language model to maintain coherence, relevance, and performance when processing input sequences far exceeding its original context window.

**[A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf) (as "Long context understanding")**
> The latent ability of a model to effectively process and utilize information across extended input sequences, integrating relevant content despite length and noise.

**[MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Long-context comprehension")**
> The capacity of a model to process, retain, and utilize information from extended conversational histories or long input sequences.

**[InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf) (as "Long-text understanding")**
> The model's comprehensive ability to read, process, and reason about information presented in extremely long documents or sequences.

**[MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Cross-page comprehension")**
> The ability to collect, synthesize, and reason over information and evidence distributed across multiple different pages of a document.

**[SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf) (as "Long-document understanding")**
> The latent ability to comprehend and answer questions about lengthy, multi-page documents containing mixed modalities such as text, tables, charts, and images.

**[LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf) (as "Long-context capability")**
> The latent ability of a model to effectively process, understand, and perform tasks requiring information from extended textual contexts.

**[Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf) (as "Long Context")**
> The latent ability to process, comprehend, and synthesize information to generate responses from extensive textual inputs.

**[Forgetting Transformer: Softmax Attention with a Forget Gate](https://proceedings.iclr.cc/paper_files/paper/2025/file/add3d389197ad2267f660ad060ef61f4-Paper-Conference.pdf) (as "Long-context capabilities")**
> The model's ability to effectively process, understand, and utilize information from very long sequences of text.

**[OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf) (as "Long-context processing capability")**
> The ability of a model to effectively process, understand, and utilize information from very long input sequences to perform complex tasks.

**[Streaming Video Question-Answering with In-context Video KV-Cache Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/67a9b444cbcd647572c88194619f72d5-Paper-Conference.pdf) (as "Long-form video understanding")**
> A specific facet of video understanding focused on comprehending videos of extended duration, often requiring the integration of information over many minutes.

**[LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf) (as "Long video understanding")**
> A specific facet of multi-modal understanding focused on the model's ability to comprehend and reason about the content and temporal dynamics of extended video sequences.

**[mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf) (as "Long image-sequence understanding")**
> The model's latent ability to process and comprehend information from extended sequences of images, such as those found in lengthy videos or multi-image documents.

**[Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf) (as "Long-context visual processing")**
> The ability of a model to effectively process and utilize information from a large number of visual inputs presented simultaneously in its context window.

**[MMEgo: Towards Building Egocentric Multimodal LLMs for Video QA](https://proceedings.iclr.cc/paper_files/paper/2025/file/b29a95e7d9f1e1a6dfc567b556733744-Paper-Conference.pdf) (as "Egocentric video understanding")**
> The latent capability to comprehend first-person videos by recognizing activities, objects, and other visual details from a self-centered viewpoint.

**[Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf) (as "Long-context modeling capability")**
> The latent ability of a model to capture long-range dependencies and process extended input sequences effectively.

**[DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.504.pdf) (as "Long-context Modeling Capacity")**
> The ability of an LLM to retain and effectively utilize information from extended dialogue histories, despite the constraints of finite context length.

**[Beyond Logits: Aligning Feature Dynamics for Effective Knowledge Distillation](https://aclanthology.org/2025.acl-long.1126.pdf) (as "Long-context modeling")**
> The latent ability of a language model to effectively process and retain information across very long input sequences, maintaining coherence and performance over thousands of tokens.

**[VMLUBenchmarks: A comprehensive benchmark toolkit forVietnameseLLMs](https://aclanthology.org/2025.acl-long.564.pdf) (as "Recall ability")**
> The model's underlying capacity to retrieve specific, relevant information from long input contexts, especially in information-sparse scenarios.

**[HyKGE: A Hypothesis Knowledge Graph EnhancedRAGFramework for Accurate and Reliable MedicalLLMs Responses](https://aclanthology.org/2025.acl-long.581.pdf) (as "Long-range dependency understanding")**
> The model's capacity to capture and utilize relationships between distant tokens in a sequence, crucial for coherent processing of long texts.

**[The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.591.pdf) (as "Long sequence comprehension")**
> The latent ability of LLMs to maintain understanding and retain information across extended input sequences, particularly challenged by structural complexity and length.

**[Analyzing and Mitigating Inconsistency in Discrete Speech Tokens for Neural Codec Language Models](https://aclanthology.org/2025.acl-long.1499.pdf) (as "Context memory")**
> The model's ability to retain and correctly use information across long or multi-step planning tasks, particularly in handling user profiles and extended task descriptions without losing critical details.

**[Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1603.pdf) (as "Long-range modeling")**
> The latent ability of a VLM to maintain coherent understanding and performance across extended sequences of multimodal inputs, particularly over long videos or interleaved images.

**[The Hidden Attention of Mamba Models](https://aclanthology.org/2025.acl-long.77.pdf) (as "Long-range ability")**
> The latent capacity of a model to maintain coherent and accurate representations over long input sequences, particularly in preserving positional information across distant tokens.

**[How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf) (as "Long-range context understanding")**
> The capacity to synthesize information across multiple documents or abstracts that are distantly related in the input sequence, maintaining coherence and relevance in the output.

**[HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Long-form video-language understanding")**
> The comprehensive ability to process, comprehend, and reason about visual and linguistic information presented in videos spanning long durations, typically an hour or more.

**[LV-XAttn: Distributed Cross-Attention for Long Visual Inputs in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25c/chang25c.pdf) (as "Long document understanding")**
> The task of processing and comprehending lengthy text documents to extract information or answer questions.

**[MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dihan25a/dihan25a.pdf) (as "Long-context reasoning")**
> The ability to effectively process, understand, and draw inferences from extended passages of text or data.

**[Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf) (as "Long-range information access")**
> The latent ability to access and utilize information from distant parts of the input sequence, beyond the immediate attention window.

**[Puzzle: Distillation-Based NAS for Inference-Optimized LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bercovich25a/bercovich25a.pdf) (as "Long-context performance")**
> The model's ability to maintain accuracy and coherence when processing and generating text with very long input sequences.

**[Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf) (as "Multi-modal long-context learning")**
> The ability of a multi-modal model to improve its performance on a downstream task by conditioning on a long context of many demonstration examples.

**[LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf) (as "Long-range capabilities")**
> The latent ability of a model to process and maintain dependencies across extensive input contexts.

**[XAttention: Block Sparse Attention with Antidiagonal Scoring](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ag/xu25ag.pdf) (as "Long-context ability")**
> The capacity to process and use information across very long input sequences without losing task performance.

**[Efficient Long Context Fine-tuning with Chunk Flow](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25m/yuan25m.pdf) (as "Long-context processing")**
> The model's ability to effectively process and utilize information from extensive input sequences.

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf) (as "Long context reasoning")**
> The ability to synthesize and reason over information distributed across extended input sequences, integrating distant pieces of information to form coherent responses.

**[AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf) (as "Long-term reasoning")**
> The latent ability to maintain coherent and effective reasoning over multiple interaction rounds to achieve a distant goal.

**[Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf) (as "Long-range dependency capture")**
> The model's capacity to model relationships and dependencies between elements that are far apart in a sequence.

**[Theoretical Foundations of Deep Selective State-Space Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6231c5f46598cfd09ff1970524e0436-Paper-Conference.pdf) (as "Long-range reasoning")**
> The ability to model and reason over long sequences of information, capturing dependencies between distant elements.

**[BehaviorGPT: Smart Agent Simulation for Autonomous Driving with Next-Patch Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9144c7c014bf4c30e88f650bef8f68dd-Paper-Conference.pdf) (as "Long-range interaction reasoning")**
> The ability to capture dependencies and interactions across extended spatial and temporal horizons in traffic trajectories.

**[InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf) (as "Long-distance dependency capture")**
> The model's ability to identify and utilize relationships between pieces of information that are far apart within a long sequence of text.

**[MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf) (as "Long-range dependency modeling")**
> The ability of a model to capture, represent, and utilize relationships between elements that are far apart in a sequence.

**[WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf) (as "Long-context problem solving")**
> The ability to handle extended conversation histories and long queries when generating useful responses.

**[Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf) (as "Long-range dependency handling")**
> The ability of a model to capture and utilize relationships between elements that are far apart in a sequence.

**[Can Large Language Models Understand Symbolic Graphics Programs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41bd71e7bf7f9fe68f1c936940fd06bd-Paper-Conference.pdf) (as "Long-range sequential reasoning")**
> The capacity to process and understand the procedural steps in a program where the order of operations significantly affects the final semantic meaning.

**[SAFE: Schema-Driven Approximate Distance Join for Efficient Knowledge Graph Querying](https://aclanthology.org/2025.emnlp-main.884.pdf) (as "Long-horizon reasoning")**
> The ability of a model to generate and maintain a coherent, multi-step plan to achieve a complex goal over an extended sequence of actions.

## Relationships

### Long-context understanding →
- **LongBench** (measurements) — *measured_by*
  > "we use the LongBench benchmark (Bai et al., 2023) to evaluate the long context prompt and decoding performance of HiP"
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **RULER** (measurements) — *measured_by*
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **Needle-in-a-haystack test** (measurements) — *measured_by*
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
- **L-Eval** (measurements) — *measured_by*
  > “LongBench, L-eval and LooGLE serve as multitask benchmarks, providing a comprehensive evaluation of long-context understanding”
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **LongBench-E** (measurements) — *measured_by*
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **LooGLE** (measurements) — *measured_by*
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
- **MLVU** (measurements) — *measured_by*
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **LongVideoBench** (measurements) — *measured_by*
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **ZeroSCROLLS** (measurements) — *measured_by*
  - [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)
- **LongEval** (measurements) — *measured_by*
  - [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **EgoSchema** (measurements) — *measured_by*
  > Table 3: Performance comparisons on 9 video benchmarks, including ActivityNet-QA (Yu et al., 2019), EgoSchema (Mangalam et al., 2023), EventBench (Du et al., 2024), LongVideoBench (Wu et al., 2024), PerceptionTest (Patraucean et al., 2023), MVBench (Li et al., 2024b), NExT-QA (Xiao et al., 2021), VNBench (Zhao et al., 2024), and VideoMME (Fu et al., 2024a). (Table 3)
  - [MMEgo: Towards Building Egocentric Multimodal LLMs for Video QA](https://proceedings.iclr.cc/paper_files/paper/2025/file/b29a95e7d9f1e1a6dfc567b556733744-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
- **OK-VQA** (measurements) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **TextVQA** (measurements) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **VizWiz** (measurements) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **VQA-v2** (measurements) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **In-context learning** (constructs) — *causes*
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
- **Speech classification** (behaviors tasks) — *measured_by*
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
- **MMLongBench-Doc** (measurements) — *measured_by*
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **DUDE** (measurements) — *measured_by*
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SlideVQA** (measurements) — *measured_by*
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **FinanceBench** (measurements) — *measured_by*
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **HELMET** (measurements) — *measured_by*
  - [Enhancing Transformers for Generalizable First-Order Logical Entailment](https://aclanthology.org/2025.acl-long.275.pdf)
- **WildBench** (measurements) — *measured_by*
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  - [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *causes*
  - [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf)
- **Document summarization** (behaviors tasks) — *causes*
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
- **The Pile** (measurements) — *measured_by*
  - [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf)
- **PG-19** (measurements) — *measured_by*
  - [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf)
- **Video-MME** (measurements) — *measured_by*
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **LOFT** (measurements) — *measured_by*
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **SWDE** (measurements) — *measured_by*
  - [VMLUBenchmarks: A comprehensive benchmark toolkit forVietnameseLLMs](https://aclanthology.org/2025.acl-long.564.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  - [VMLUBenchmarks: A comprehensive benchmark toolkit forVietnameseLLMs](https://aclanthology.org/2025.acl-long.564.pdf)
- **Code understanding** (constructs) — *measured_by*
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **LongGenBench** (measurements) — *measured_by*
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **MM-NIAH** (measurements) — *measured_by*
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **MileBench** (measurements) — *measured_by*
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **WikiText-2** (measurements) — *measured_by*
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)

### → Long-context understanding
- **Information retrieval** (behaviors tasks) — *causes*
  - [Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf)
- **Coreference resolution** (behaviors tasks) — *causes*
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)

### Associated with
- **Length generalization** (constructs)
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  - [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)
- **Question answering** (behaviors tasks)
  > ...achieving substantial progress on tasks such as summarization and question answering that emphasize the effective utilization and understanding of long inputs.
  - [SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
- **Planning** (constructs)
  - [Leveraging Environment Interaction for Automated PDDL Translation and Planning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/44af065477781e7f8a8589b14a62c489-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf)
- **Long-context processing** (constructs)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **Text summarization** (behaviors tasks)
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **Contextual understanding** (constructs)
  - [From Unaligned to Aligned: Scaling MultilingualLLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.375.pdf)
- **Document understanding** (constructs)
  - [LLM-Guided Co-Training for Text Classification](https://aclanthology.org/2025.emnlp-main.1584.pdf)
- **Personalized response generation** (behaviors tasks)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.504.pdf)
- **Video understanding** (constructs)
  - [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
- **Scientific question answering** (behaviors tasks)
  - [How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf)
- **Structural understanding** (constructs)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.591.pdf)
- **Document summarization** (behaviors tasks)
  - [CanLLMs Generate and Solve Linguistic Olympiad Puzzles?](https://aclanthology.org/2025.emnlp-main.970.pdf)
- **Complex reasoning** (behaviors tasks)
  - [LLM-Guided Co-Training for Text Classification](https://aclanthology.org/2025.emnlp-main.1584.pdf)
- **Attention sparsity** (constructs)
  - [SEAL: Structure and Element Aware Learning Improves Long Structured Document Retrieval](https://aclanthology.org/2025.emnlp-main.430.pdf)
- **Multi-turn dialogue** (behaviors tasks)
  - [LLM-Guided Co-Training for Text Classification](https://aclanthology.org/2025.emnlp-main.1584.pdf)
- **ArgKP21** (measurements)
  - [Does Localization Inform Unlearning? A Rigorous Examination of Local Parameter Attribution for Knowledge Unlearning in Language Models](https://aclanthology.org/2025.emnlp-main.1110.pdf)
