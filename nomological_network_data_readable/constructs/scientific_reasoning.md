# Scientific reasoning
**Type:** Construct  
**Referenced in:** 45 papers  
**Also known as:** Fact reasoning, Scientific problem solving, Scientific question answering, Science question answering, STEM question answering  

## State of the Field

Across the surveyed literature, scientific reasoning is most commonly defined as the ability to reason about scientific concepts, data, and figures, often in academic contexts involving complex visualizations. This construct is frequently described as requiring multi-step inference, the application of domain-specific knowledge, and the interpretation of multimodal information. A smaller line of work frames it as an observable task, such as "scientific problem solving" or various forms of "science question answering." The field operationalizes and measures this construct primarily through performance on question-answering benchmarks. The most frequently cited instruments for this purpose are ScienceQA, used to assess multimodal reasoning, and ARC (including its ARC-Challenge and ARC-Easy subsets). Other benchmarks reported to evaluate scientific reasoning include SciQ, MT-Bench, ScienceWorld, and OpenBookQA, which is used for a related concept termed "fact reasoning." Some research extends the concept to include the scientific process itself, such as hypothesis formulation, while another study highlights the ability to correctly interpret evidence and avoid unjustified conclusions. Scientific reasoning is also studied alongside other constructs like commonsense understanding, knowledge acquisition, and task decomposition.

## Sources

**[At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)**
> The ability to reason about scientific concepts, data, and figures, particularly in academic or research contexts involving complex visualizations.

**[Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf) (as "Fact reasoning")**
> The latent ability to reason based on factual knowledge and open-book information.

**[AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment](https://aclanthology.org/2025.emnlp-main.329.pdf) (as "Scientific problem solving")**
> The task of addressing complex problems from scientific domains that require structured reasoning and domain knowledge.

**[What Do Indonesians Really Need from Language Technology? A Nationwide Survey](https://aclanthology.org/2025.emnlp-main.368.pdf) (as "Scientific question answering")**
> The task of answering questions related to scientific concepts, often requiring interpretation of diagrams or data presented visually.

**[Primus: A Pioneering Collection of Open-Source Datasets for CybersecurityLLMTraining](https://aclanthology.org/2025.emnlp-main.528.pdf) (as "Science question answering")**
> The task of answering questions related to elementary school science.

**[s3: You Don’t Need That Much Data to Train a Search Agent viaRL](https://aclanthology.org/2025.emnlp-main.1096.pdf) (as "STEM question answering")**
> Answering questions related to science, technology, engineering, and mathematics.

## Relationships

### Scientific reasoning →
- **ScienceQA** (measurements) — *measured_by*
  > We use the ScienceQA dataset (Lu et al., 2022) to evaluate the scientific reasoning ability of the model. (Section 3.1)
  - [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [DREAM: Improving Video-Text Retrieval Through Relevance-Based Augmentation Using Large Foundation Models](https://aclanthology.org/2025.naacl-long.157.pdf)
- **SciQ** (measurements) — *measured_by*
  > SciQ measures scientific reasoning, challenging models to apply scientific concepts beyond mere fact recall. (Section 4.2)
  - [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  > Scientific reasoning is evaluated on SciQ (Welbl et al., 2017), Sci-Eval (Sun et al., 2024), and ARC (Clark et al., 2018) for English science
  - [InductionBench:LLMs Fail in the Simplest Complexity Class](https://aclanthology.org/2025.acl-long.1288.pdf)
- **MT-Bench** (measurements) — *measured_by*
  > “The second benchmark, MT-Bench (Zheng et al., 2024), consists of 80 multi-turn dialogues spanning various domains, including writing, roleplay, reasoning, math, coding, extraction, STEM, and humanities.”
  - [s3: You Don’t Need That Much Data to Train a Search Agent viaRL](https://aclanthology.org/2025.emnlp-main.1096.pdf)
- **SciBench** (measurements) — *measured_by*
  - [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf)
- **SciEval** (measurements) — *measured_by*
  - [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf)
- **ScienceWorld** (measurements) — *measured_by*
  > ScienceWorld... is an interactive benchmark designed for embodied science experiments... The aim is to assess whether AI models can apply scientific knowledge.
  - [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  > OpenBookQA (Mihaylov et al., 2018) for fact reasoning (Section 3.1)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)

### Associated with
- **Task decomposition** (behaviors tasks)
  - [PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf)
- **Commonsense reasoning** (constructs)
  - [PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf)
- **Knowledge acquisition** (constructs)
  > suggesting a successful internalization of scientific reasoning processes and domain-specific knowledge, primarily through the WKL component (Section 5.4).
  - [Adapting While Learning: Grounding LLMs for Scientific Problems with Tool Usage Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lyu25a/lyu25a.pdf)
