# Modularity
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** Circuit reuse, Module reuse, Module transfer  

## State of the Field

Across the surveyed literature, Modularity is predominantly framed as a quality of a model's generated output, particularly in domains like code generation and theorem proving. The most common definitions describe it as the extent to which a generated program or proof is structured into distinct, logical, and reusable sub-components, a characteristic often compared to the practices of experienced human programmers. For instance, in theorem proving, it is conceptualized as decomposing complex problems into reusable lemmas that can be added to a growing library. A distinct, less frequent framing treats modularity as an internal property of the model's architecture, focusing on the reuse of computational sub-circuits, such as attention heads, across different tasks. This is also described as the decomposability of a model's processes into "self-contained, independently functional sub-networks." The concept is closely associated with reusability and transferability, with definitions for "module reuse" and "module transfer" emphasizing the ability to apply learned components to new instances or entirely different task domains. To operationalize the construct, one study reports using GPT-4 to rate the reusability of generated code on a Likert scale, while another mentions a framework for extracting and analyzing internal functional sub-networks within models.

## Sources

**[GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf) (as "Module reuse")**
> The tendency to apply previously learned modules to new instances or tasks rather than regenerating task-specific solutions from scratch.

**[GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf) (as "Module transfer")**
> The ability of learned modules to remain useful when applied in a different task domain or evaluation setting.

**[Circuit Component Reuse Across Tasks in Transformer Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ffbfbcf4ad7304d57158b046525e46c-Paper-Conference.pdf) (as "Circuit reuse")**
> The degree to which a language model repurposes learned subcircuits—comprising attention heads and algorithmic steps—across different tasks that share underlying computational demands.

**[CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)**
> The latent quality of a generated program being structured into distinct, logical, and often reusable sub-components or modules, which is a hallmark of experienced programming.

**[CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf) (as "Reusability")**
> The latent capacity of a model to generate code components that can be adapted or reused across different solution attempts or problems, reflecting generalization at the sub-task level.
