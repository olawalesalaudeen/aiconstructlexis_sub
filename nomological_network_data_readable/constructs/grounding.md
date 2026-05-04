# Grounding
**Type:** Construct  
**Referenced in:** 54 papers  
**Also known as:** Grounding ability, Grounding capability, Groundedness, Visual localization, Attribution groundedness, Grounded understanding, Argument groundedness, Evidence attribution, Factual reliability, Context utilisation, Region understanding, Framing divergence, Caption alignment, Temporal referring expression, Accident temporal localization, Temporal referring, Moment retrieval, Temporal action localization  

## State of the Field

Across the provided literature, the construct of Grounding is predominantly framed in two distinct ways: connecting language to visual or spatial information, and connecting language to textual evidence. The most prevalent usage defines Grounding as a model's ability to connect high-level concepts to fine-grained visual details, such as localizing objects in an image or video from a textual description. This includes producing precise spatial outputs like bounding boxes for user interface elements, as seen in definitions of 'Grounding ability' and 'Grounding capability'. A specific line of this research extends this to the temporal domain, where grounding involves identifying specific timestamps or video segments corresponding to a natural language query, a task referred to as 'Moment retrieval' or 'Temporal action localization'. This form of temporal grounding is operationalized using benchmarks like Charades-STA, which is used to measure moment retrieval performance. A separate body of work, often in the context of retrieval-augmented generation (RAG), treats Grounding as the extent to which a model's response is derived from provided documents rather than its internal parametric knowledge. In this context, also termed 'Groundedness' or 'Argument groundedness', the focus is on ensuring responses are factually supported by and consistent with retrieved evidence, with one study defining 'Attribution Groundedness' as the quality of citations supporting generated claims. The provided data also shows that Grounding is studied alongside other constructs like Temporal reasoning and Mathematical reasoning.

## Sources

**[Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)**
> The model's ability to connect high-level concepts and reasoning processes to fine-grained, low-level visual details in a video, such as object identities, motion, and interactions.

**[VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Grounding ability")**
> The capacity to produce precise spatial outputs for GUI elements, such as coordinates or bounding boxes, from screenshots.

**[Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf) (as "Grounding capability")**
> The latent ability to accurately associate textual references with specific visual locations or bounding boxes in a UI.

**[Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf) (as "Groundedness")**
> The extent to which an LLM's response is derived solely from the information within provided documents rather than its internal parametric knowledge.

**[MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf) (as "Visual localization")**
> The latent ability to identify where in an image the relevant subject or evidence for a question is located.

**[Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf) (as "Attribution groundedness")**
> The quality of an LLM's generated citations in a RAG context, specifically whether the citations are relevant and sufficiently support the claims they are attached to.

**[CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf) (as "Grounded understanding")**
> The ability to connect language expressions to specific image regions or objects with precise spatial localization.

**[RAGLLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.282.pdf) (as "Evidence attribution")**
> The latent ability of a model to correctly and faithfully link statements in its explanations to the supporting source evidence, ensuring that citations reflect actual content and context from the provided passages.

**[Waste Not, Want Not; RecycledGumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.293.pdf) (as "Argument groundedness")**
> The extent to which a generated argument is factually supported by and consistent with the retrieved evidence, minimizing hallucination or contradiction.

**[LoGU: Long-form Generation with Uncertainty Expressions](https://aclanthology.org/2025.acl-long.929.pdf) (as "Factual reliability")**
> The degree to which the retrieval and reasoning process avoids hallucinated or factually inaccurate content by grounding in document-derived knowledge.

**[Adversarial Alignment with Anchor Dragging Drift (A3D2): Multimodal Domain Adaptation with Partially Shifted Modalities](https://aclanthology.org/2025.acl-long.968.pdf) (as "Context utilisation")**
> The latent ability of a language model to effectively leverage retrieved external information when generating responses, reflecting how well it integrates evidence into its predictions.

**[CPCF: A Cross-Prompt Contrastive Framework for Referring Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25h/zhu25h.pdf) (as "Region understanding")**
> The latent ability of a referring MLLM to accurately interpret and generate responses based on a specific visual region indicated by a prompt, distinguishing it from surrounding or similar regions.

**[learnable soft visual prompt](https://aclanthology.org/2025.emnlp-main.996.pdf) (as "Framing divergence")**
> The latent tendency of an LLM to generate conflicting narrative interpretations of the same event when conditioned on different personas, reflecting epistemic contradictions shaped by perspective.

**[TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac3af725ae398b6184faae0828bdbd6c-Paper-Conference.pdf) (as "Temporal referring expression")**
> Identifying the specific image or images in a sequence where a described change occurred.

**[TAU-106K: A New Dataset for Comprehensive Understanding of Traffic Accident](https://proceedings.iclr.cc/paper_files/paper/2025/file/b33ad9d46ab2a23b6783d954121d26e3-Paper-Conference.pdf) (as "Accident temporal localization")**
> The task of identifying the precise start and end timestamps of a traffic accident event within a video clip.

**[Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf) (as "Temporal referring")**
> The observable behavior of formulating or answering questions that refer to particular temporal positions within the content.

**[YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf) (as "Caption alignment")**
> The task of synchronizing text captions with the corresponding segments of a sign language video.

**[TRACE: Temporal Grounding Video LLM  via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf) (as "Moment retrieval")**
> The task of identifying the start and end timestamps of a video segment that corresponds to a given natural language query.

**[Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf) (as "Temporal action localization")**
> The task of identifying the start and end times of specific actions within a longer, untrimmed video.

## Relationships

### Grounding →
- **Visual reasoning** (constructs) — *causes*
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **Charades-STA** (measurements) — *measured_by*
  > We utilize test set of Charades-STA (Gao et al., 2017) for the moment retrieval task and report the recall at IOU thresholds of 0.5 and 0.7.
  - [TRACE: Temporal Grounding Video LLM  via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
- **FLEURS-ASL** (measurements) — *measured_by*
  - [Examining and Adapting Time for Multilingual Classification via Mixture of Temporal Experts](https://aclanthology.org/2025.naacl-long.314.pdf)
- **ScreenSpot** (measurements) — *measured_by*
  - [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf)
- **InfiniBench** (measurements) — *measured_by*
  - [3DS: Medical Domain Adaptation ofLLMs via Decomposed Difficulty-based Data Selection](https://aclanthology.org/2025.emnlp-main.984.pdf)

### → Grounding
- **Visual grounding** (constructs) — *measured_by*
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)

### Associated with
- **Temporal reasoning** (constructs)
  - [TRACE: Temporal Grounding Video LLM  via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Tool use** (behaviors tasks)
  - [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)
- **Spatial understanding** (constructs)
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **Temporal video grounding** (behaviors tasks)
  - [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf)
