# Causal inference
**Type:** Behavior  
**Referenced in:** 10 papers  
**Also known as:** Causal discovery, Cause attribution, Causal effect estimation, Causal graph discovery, Causal graph construction, Causal relationship classification, Effect inference, Causal identification  

## State of the Field

In the surveyed literature, "Causal inference" is treated as a broad category of behaviors rather than a single, uniformly defined task. A prevalent framing, articulated in "Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?", organizes the concept into three core activities: causal discovery, cause attribution, and causal effect estimation. Causal discovery, which also appears as causal graph discovery or construction, is commonly described as recovering latent causal structures from data, text, or agent interactions. Other definitions focus more narrowly on identifying specific relationships, such as selecting the most plausible cause for a premise or classifying a sentence as describing a causal link. A third cluster of work defines the behavior as estimating or quantifying the effects of variables on one another, sometimes framed as predicting future states after an action. This behavior is operationalized and measured using benchmarks like COPA and ACRE, and in simulated environments including AI2-THOR and Gridworld. Some research reports that performing causal inference can enable interpretability and continual learning. The behavior is also studied alongside language proficiency and hypothesis formulation.

## Sources

**[Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf) (as "Causal discovery")**
> The task of recovering the latent causal structure of variables from data or text.

**[Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf) (as "Cause attribution")**
> The task of uncovering the potential causes behind a given process or observed outcome.

**[Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf) (as "Causal effect estimation")**
> The task of investigating and quantifying the effect of specific cause variables on outcome variables.

**[CausalStock: Deep End-to-end Causal Discovery for News-driven Multi-stock Movement Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/54d689d58fe54c92aee2d732fc49fca8-Paper-Conference.pdf) (as "Causal graph discovery")**
> Inferring a temporal directed graph over stocks that represents lagged causal links between variables.

**[Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)**
> The task of selecting the most plausible cause or effect for a given premise from a set of alternatives.

**[ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf) (as "Causal graph construction")**
> Building a directed structure of item-action dependencies from interaction records and interventions.

**[Causal Order: The Key to Leveraging Imperfect Experts in Causal Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/edcbd38b2509b57954d38de6cd9c05b3-Paper-Conference.pdf) (as "Effect inference")**
> Estimating causal effects of one variable on another from an inferred adjustment set or causal structure.

**[Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf) (as "Causal relationship classification")**
> The task of identifying whether a sentence describes a causal link between events or is merely coincidental noise.

**[LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf) (as "Causal identification")**
> Determining which objects can activate a machine based on observed outcomes.

## Relationships

### Causal inference →
- **Interpretability and explainability** (constructs) — *causes*
  > "ADAM constructs a nearly perfect causal graph from scratch, enabling efficient task decomposition and execution with strong interpretability."
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)
- **COPA** (measurements) — *measured_by*
  - [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.622.pdf)
- **Continual learning** (constructs) — *causes*
  > Newly discovered items enable the execution of new unknown actions and the CD on these actions. This iterative process ensures the lifelong learning through continuous engagement and adaptation.
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)
- **AI2-THOR** (measurements) — *measured_by*
  > We evaluate our framework using two distinct environments: a dynamic 8 × 8 GridWorld and a static 3D-rendered kitchen (AI2-THOR)... Our experiments focus on three key aspects: the effectiveness of text-based action representations, causal inference, and planning.
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **Gridworld** (measurements) — *measured_by*
  > We evaluate our framework using two distinct environments: a dynamic 8 × 8 GridWorld and a static 3D-rendered kitchen (AI2-THOR)... Our experiments focus on three key aspects: the effectiveness of text-based action representations, causal inference, and planning.
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **ACRE** (measurements) — *measured_by*
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)

### Associated with
- **Causal reasoning** (constructs)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
- **Hypothesis generation** (behaviors tasks)
  - [Causal Modelling Agents: Causal Graph Discovery through Synergising Metadata- and Data-driven Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe90657b12193c7b52a3418bdc351807-Paper-Conference.pdf)
