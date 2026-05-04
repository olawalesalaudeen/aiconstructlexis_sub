# Knowledge graph construction
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Semantic network construction, Factual entity graph construction, Textual entity graph construction, Temporal knowledge graph update  

## State of the Field

Across the provided literature, knowledge graph construction is most commonly described as the automatic extraction of entities and their relationships from unstructured text to form a structured graph. One paper frames this as the "text-to-graph generation (T2G) task," aiming to create a knowledge representation without manual intervention. While this core idea is consistent, different papers introduce specific nuances. For instance, one study distinguishes between "textual entity graph construction," which represents relationships solely as expressed in the input text, and "factual entity graph construction," which validates these relationships against an external knowledge base like Wikipedia. A different line of work focuses on the temporal dimension, defining the task as updating a knowledge graph over time by integrating new information as "short-term memory" while preserving historical structure. Another paper describes a related process, "Semantic Network Analysis," as transforming text into networks of concepts to unify lexical, syntactic, and semantic information. To evaluate this behavior, researchers use datasets with ground truth knowledge graphs; the provided data shows that the SciERC dataset is used for this purpose.

## Sources

**[Sali4Vid: Saliency-Aware Video Reweighting and Adaptive Caption Retrieval for Dense Video Captioning](https://aclanthology.org/2025.emnlp-main.1309.pdf) (as "Semantic network construction")**
> Transforming textual data into a graph of nodes (concepts) and edges (relations) to represent knowledge structure.

**[T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.186.pdf) (as "Textual entity graph construction")**
> Building a graph representation of entities and their relationships as expressed in the input text, where nodes represent entities and edges represent extracted relations.

**[T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.186.pdf) (as "Factual entity graph construction")**
> Constructing a knowledge-based entity graph by querying a knowledge base (e.g., Wikipedia) to determine whether real-world relationships exist between linked entities.

**[LLMs cannot spot math errors, even when allowed to peek into the solution](https://aclanthology.org/2025.emnlp-main.554.pdf)**
> The process of automatically extracting entities and their relationships from unstructured text to create a structured knowledge graph.

**[RewardDS: Privacy-Preserving Fine-Tuning for Large Language Models via Reward Driven Data Synthesis](https://aclanthology.org/2025.emnlp-main.224.pdf) (as "Temporal knowledge graph update")**
> Updating a knowledge graph over time by incorporating new scene information while preserving historical structure, enabling long-term reasoning.

## Relationships

### Knowledge graph construction →
- **SciERC** (measurements) — *measured_by*
  > In our study, we conduct experiments on two general datasets (REBEL-Sub (Huguet Cabot and Navigli, 2021) and GenWiki (Jin et al., 2020)) and two domain-specific datasets (SCIERC (Luan et al., 2018) and the Windows-centric subset of Re-DocRED (Tan et al., 2022)) with golden ground truth KGs (Section 5.1.1).
  - [LLMs cannot spot math errors, even when allowed to peek into the solution](https://aclanthology.org/2025.emnlp-main.554.pdf)
