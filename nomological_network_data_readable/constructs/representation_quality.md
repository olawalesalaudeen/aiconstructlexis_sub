# Representation quality
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Embedding capability, Task vector quality, Visual feature quality, Feature representation capability, Hierarchical concept representation  

## State of the Field

Across the surveyed literature, representation quality is a latent construct referring to the effectiveness of a model's internal representations in encoding and preserving task-relevant information. The most detailed definition frames it as the ability to retain useful information while discarding noise, which is reflected in downstream performance and structural properties like compression, geometry, and invariance. Other papers offer more specific framings, such as the ability to distinguish between tasks and knowledge domains, the decodability of task vectors for in-context learning, or the capacity to capture semantic meaning in text embeddings. A recurring theme is the geometric structure of these representations; one study notes that models can encode high- and low-level concepts in an "approximately orthogonal manner." The concept also extends to vision, where "visual feature quality" is defined by the preservation of semantic, structural, and pixel-level details from an input image. To operationalize this construct, researchers measure downstream performance using benchmarks like the Massive Text Embedding Benchmark (MTEB), evaluating on its text similarity and text-embedding tasks. In the visual domain, one paper reports that image reconstruction can be used to enhance representation quality.

## Sources

**[Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf) (as "Hierarchical concept representation")**
> The organization of knowledge in LLMs such that high-level task concepts (e.g., 'capital') are encoded in directions orthogonal to low-level, task-specific features, enabling selective attention and compositionality.

**[Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf) (as "Feature representation capability")**
> The inherent ability of a pre-trained model to encode data into a feature space that can be used to distinguish and categorize different tasks and knowledge domains.

**[Emergence and Effectiveness of Task Vectors in In-Context Learning: An Encoder Decoder Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25h/han25h.pdf) (as "Task vector quality")**
> The degree to which a model's internal representation of a task is distinct and decodable, determining the effectiveness of triggering correct in-context learning behavior.

**[What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf) (as "Embedding capability")**
> The latent ability of a model to produce high-quality text representations that capture semantic meaning, enhanced by bidirectional modeling but typically at the cost of generative performance in unidirectional models.

**[Layer by Layer: Uncovering Hidden Representations in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/skean25a/skean25a.pdf)**
> The latent property of a model's internal representations that determines their effectiveness in preserving task-relevant information while discarding noise, as reflected in downstream performance and structural properties like compression, geometry, and invariance.

**[DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf) (as "Visual feature quality")**
> The degree to which visual encoder outputs preserve semantic, structural, and pixel-level details from the input image, enabling accurate multimodal alignment and reasoning.

## Relationships

### Representation quality →
- **MTEB** (measurements) — *measured_by*
  > we conduct experiments on ten text similarity (STS) tasks in MTEB (Muennighoff et al., 2022) (Section 5.1)
  - [Layer by Layer: Uncovering Hidden Representations in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/skean25a/skean25a.pdf)

### → Representation quality
- **Image reconstruction** (behaviors tasks) — *causes*
  - [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf)
