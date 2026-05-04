# Knowledge acquisition
**Type:** Construct  
**Referenced in:** 9 papers  
**Also known as:** Background Knowledge, Preliminary knowledge grasp, Knowledge internalization, Fact learning  

## State of the Field

Across the surveyed literature, knowledge acquisition is most commonly defined as a latent ability for models to retrieve and utilize factual or contextual knowledge to support decision-making. This framing positions it as a core capability, evaluated alongside logical reasoning and coding. A smaller set of papers offers more process-oriented definitions, such as "fact learning," which describes the encoding of information into model weights during training, or "knowledge internalization," the incorporation of knowledge from external tools. In a domain-specific context, it is also framed as "preliminary knowledge grasp," the memorization of foundational facts without complex application. This construct is operationalized and measured using benchmarks like AgentBench, while its foundational aspect is assessed in the medical domain via question-answering tasks on MedQA and MedMCQA. The ability is described as involving the learning of "simple associations" like "capital cities of countries," though one paper notes this process can be "data-inefficient." Knowledge acquisition is studied in relation to faithfulness, text generation, and scientific reasoning, and is reported in some work to be influenced by self-reflection and to influence commonsense knowledge.

## Sources

**[AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)**
> The latent ability to retrieve and utilize relevant factual or contextual knowledge from external sources or internal representations to support decision-making.

**[FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf) (as "Background Knowledge")**
> The capacity to generate responses by accessing a broad repository of general and domain-specific factual and commonsense information.

**[Extractive Structures Learned in Pretraining Enable Generalization on Finetuned Facts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25m/feng25m.pdf) (as "Fact learning")**
> The process by which a language model encodes and stores factual information from training data into its weights.

**[Adapting While Learning: Grounding LLMs for Scientific Problems with Tool Usage Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lyu25a/lyu25a.pdf) (as "Knowledge internalization")**
> The process by which a model incorporates external, tool-generated solutions into its parametric knowledge, allowing it to solve problems without relying on tool calls.

**[Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf) (as "Preliminary knowledge grasp")**
> The latent ability to memorize and initially understand foundational medical knowledge, such as facts and definitions, without requiring complex reasoning or application.

## Relationships

### Knowledge acquisition →
- **AgentBench** (measurements) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf)
- **MedQA** (measurements) — *measured_by*
  > most medical benchmarks (Jin et al., 2021; Pal et al., 2022; Wang et al., 2024; Cai et al., 2024; Qiu et al., 2024) evaluate LLMs’ capabilities through question-answering (QA) tasks, which mainly focus on assessing LLMs’ preliminary knowledge grasp (Section 1)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **MedMCQA** (measurements) — *measured_by*
  > most medical benchmarks (Jin et al., 2021; Pal et al., 2022; Wang et al., 2024; Cai et al., 2024; Qiu et al., 2024) evaluate LLMs’ capabilities through question-answering (QA) tasks, which mainly focus on assessing LLMs’ preliminary knowledge grasp (Section 1)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)

### → Knowledge acquisition
- **Self-reflection** (behaviors tasks) — *causes*
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf)

### Associated with
- **Multiple-choice question answering** (behaviors tasks)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **Factuality** (constructs)
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
- **Scientific reasoning** (constructs)
  > suggesting a successful internalization of scientific reasoning processes and domain-specific knowledge, primarily through the WKL component (Section 5.4).
  - [Adapting While Learning: Grounding LLMs for Scientific Problems with Tool Usage Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lyu25a/lyu25a.pdf)
