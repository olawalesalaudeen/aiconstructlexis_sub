# Creativity
**Type:** Construct  
**Referenced in:** 54 papers  
**Also known as:** Creative thinking, Creative problem-solving, H-creativity, P-creativity, Creative intelligence, Creative reasoning, Creative quality  

## State of the Field

Across the surveyed literature, the prevailing usage of Creativity refers to a latent ability in language models to generate novel, diverse, and original content that goes beyond existing examples or straightforward solutions. This concept is applied across various domains, from generating new robotic tasks and imaginative text to proposing "out-of-the-box" solutions for social problems. While the emphasis on novelty is widespread, a smaller line of work introduces more specific framings, such as distinguishing between P-creativity (novelty to the agent) and H-creativity (novelty to human history), or defining "creative reasoning" as the ability to repurpose tools in unfamiliar environments. The operationalization of this construct relies heavily on subjective assessment, with papers frequently measuring it using both `Human evaluation` through methods like pairwise preferences and Likert scales, and automated `LLM-as-a-judge` systems. Specific measurement instruments are also cited, including `WildBench`, which assesses creativity through constrained writing tasks, and the `Consensual Assessment Technique`, a method based on holistic judgments from domain experts. The construct is consistently studied alongside `Divergent thinking` and `Divergent reasoning`, which some sources describe as a core characteristic of creativity, and is also related to `Originality`, which is explicitly used as a dimension for scoring.

## Sources

**[GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf)**
> The latent ability of an LLM to generate novel, diverse, and previously unseen robotic tasks that go beyond the scope of existing human-curated benchmarks.

**[THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS](https://proceedings.iclr.cc/paper_files/paper/2024/file/2dae7d1ccf1edf76f8ce7c282bdf4730-Paper-Conference.pdf) (as "Creative thinking")**
> The ability to generate coherent, novel text under constraints that require imaginative planning and composition.

**[The Impact of Domain-Specific Terminology on Machine Translation for Finance inEuropean Languages](https://aclanthology.org/2025.naacl-long.141.pdf) (as "H-creativity")**
> The quality of an idea being novel in the context of all of human history, meaning no one else has had the idea before.

**[The Impact of Domain-Specific Terminology on Machine Translation for Finance inEuropean Languages](https://aclanthology.org/2025.naacl-long.141.pdf) (as "P-creativity")**
> The quality of an idea being novel to the individual agent that produced it, regardless of whether others have had the idea before.

**[Superlatives in Context: Modeling the Implicit Semantics of Superlatives](https://aclanthology.org/2025.naacl-long.161.pdf) (as "Creative problem-solving")**
> The ability to solve complex problems that require novel, intelligent, or non-obvious steps, rather than just following a straightforward procedure.

**[Evaluation ofLLMVulnerabilities to Being Misused for Personalized Disinformation Generation](https://aclanthology.org/2025.acl-long.39.pdf) (as "Creative intelligence")**
> A broad latent trait encompassing the capacity to think innovatively, adapt observations to new contexts, and generate original strategies in unstructured scenarios, as part of a triarchic model of intelligence.

**[Evaluation ofLLMVulnerabilities to Being Misused for Personalized Disinformation Generation](https://aclanthology.org/2025.acl-long.39.pdf) (as "Creative reasoning")**
> The latent ability of a language model agent to generate novel, adaptive solutions to problems by repurposing tools, identifying implicit goals, and solving puzzles in unfamiliar environments.

**[On the Same Wavelength? Evaluating Pragmatic Reasoning in Language Models across Broad Concepts](https://aclanthology.org/2025.emnlp-main.1009.pdf) (as "Creative quality")**
> A latent trait reflecting the overall perceived creativity of an idea, as judged by human raters on dimensions such as cleverness, remoteness, and uncommonness.

## Relationships

### Creativity →
- **Human evaluation** (measurements) — *measured_by*
  > "We evaluate system output by soliciting pairwise preferences ... along four dimensions"
  - [MetaDesigner: Advancing Artistic Typography through AI-Driven, User-Centric, and Multilingual WordArt Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/a10c3d85879c29331ba4d73ede56c7d3-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > In addition, we develop a LLM-based evaluator (Liusie et al., 2023; Liu et al., 2024; Zheng et al., 2024; Bohnet et al., 2024) to perform side-by-side comparisons of system output. We design prompts targeting the same dimensions of story quality adopted in our human evaluation (Section 6.2).
  - [Agents' Room:  Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf)
- **WildBench** (measurements) — *measured_by*
  > “The tasks in WILDBENCH typically demand higher-order reasoning, such as writing and/or debugging code with specific constraints, creative writing with multiple constraints on the style and content”
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Consensual Assessment Technique** (measurements) — *measured_by*
  > The Consensual Assessment Technique (CAT) (Amabile, 1983) is a method for evaluating creative products by asking experts in the domain to provide their own holistic judgments of creativity, without being given explicit criteria to follow.
  - [Enhancing Logical Reasoning in Language Models via Symbolically-GuidedMonteCarlo Process Supervision](https://aclanthology.org/2025.emnlp-main.1625.pdf)

### → Creativity
- **Bias amplification** (behaviors tasks) — *causes*
  - [Bias Amplification in Language Model Evolution: An Iterated Learning Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/4418f6a54f4314202688d77956e731ce-Paper-Conference.pdf)
- **Domain knowledge** (constructs) — *causes*
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Social and emotional intelligence** (constructs) — *causes*
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Imagination** (constructs) — *causes*
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Divergent thinking** (constructs)
  > From cognitive science, creativity consists of at least two key characteristics: convergent thinking (purposefulness to achieve a given goal) and divergent thinking (adaptability to explore new environments or constraints) (Runco, 2003).
  - [Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps](https://proceedings.iclr.cc/paper_files/paper/2025/file/6794f555524c9069e26970a408d353cc-Paper-Conference.pdf)
- **Creative writing** (behaviors tasks)
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Generation diversity** (constructs)
  - [Diversity-Rewarded CFG Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a59a11e8580a7ac850cb792f6179c7a0-Paper-Conference.pdf)
- **Coherence** (constructs)
  - [Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs](https://proceedings.iclr.cc/paper_files/paper/2025/file/afa5f124e36bed5cc2125067005d43f5-Paper-Conference.pdf)
- **Originality** (constructs)
  > “Creativity scoring broadly considers two complementary dimensions: the intrinsic qualities of ideas ... and their extrinsic statistical infrequency within a population (i.e., original ideas do not appear very often)”
  - [A Sequential Multi-Stage Approach for Code Vulnerability Detection via Confidence- and Collaboration-based Decision Making](https://aclanthology.org/2025.emnlp-main.1072.pdf)
- **Helpfulness** (constructs)
  > Figure 4: Analysis results of the primary value of evaluation metric: ... the PL model prioritizes Empathy, Actionability, and Creativity. Being trained on the threads of AdvisorQA, the PL model reflects the Reddit forum’s source, valuing advice that resonates empathetically with the given situation, is actionable, and creative, as preferred by the majority. (Section 4.1)
  - [TRANSIENTTABLES: EvaluatingLLMs’ Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.333.pdf)
- **Divergent reasoning** (constructs)
  > The ability to generate diverse solutions to a given problem is a hallmark of human creativity. This divergent reasoning is also crucial for machines, enhancing their robustness and enabling them to assist humans in many applications such as scientific discovery. (Abstract)
  - [Flow of Reasoning: Training LLMs for Divergent Reasoning with Minimal Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25k/yu25k.pdf)
- **Associative reasoning** (constructs)
  > A key aspect of evaluating creativity lies in assessing associative ability, which plays a central role in creativity by driving generative processes (Section 1).
  - [Understanding the Modality Gap: An Empirical Study on the Speech-Text Alignment Mechanism of Large Speech Language Models](https://aclanthology.org/2025.emnlp-main.263.pdf)
