# Graph reasoning
**Type:** Construct  
**Referenced in:** 13 papers  
**Also known as:** Graph reasoning ability, Graph isomorphism detection, Hamiltonian cycle detection, Hamiltonian path detection, Biggest chordless cycle identification  

## State of the Field

Across the surveyed literature, graph reasoning is most commonly defined as a specific facet of algorithmic reasoning that focuses on solving problems involving graph-structured data. A recurring, complementary view treats it as a latent capacity to understand, retain, and manipulate graph-structured information, often presented in natural language or visual formats. The field operationalizes this construct through a range of specific behaviors. One line of work measures it using tasks such as "graph connectivity, shortest path, and cycle detection" (Mixture of Parrots: Experts improve memorization more than reasoning), while another proposes "graph recall" as a "simple yet fundamental task" for its assessment (Microstructures and Accuracy of Graph Recall by Large Language Models). A distinct set of studies evaluates graph reasoning from visual inputs, using tasks like graph isomorphism detection, Hamiltonian path and cycle detection, and identifying the biggest chordless cycle. The presentation of the graph is noted as a factor, with one study observing that "the order of graph descriptions significantly affects the graph reasoning performance of LLMs" (Evaluating Language Models as Synthetic Data Generators). Graph reasoning is studied in relation to problem-solving and pathfinding, and is sometimes contrasted with inductive reasoning.

## Sources

**[Understanding Transformer Reasoning Capabilities via Graph Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f395480c04ac6dfb2c2326a639df88e-Paper-Conference.pdf)**
> A specific facet of algorithmic reasoning focused on solving problems on graph-structured data.

**[Microstructures and Accuracy of Graph Recall by Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77e6814d32a86b76123bd10aa7e2ad81-Paper-Conference.pdf) (as "Graph reasoning ability")**
> The latent capacity to understand, retain, and manipulate graph-structured information across tasks that involve relations among entities.

**[Visual Graph Arena: Evaluating Visual Conceptualization of Vision and Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/babaiee25a/babaiee25a.pdf) (as "Graph isomorphism detection")**
> The task of determining whether two visually distinct graph representations share the same underlying structure, including the same number of vertices, edges, and connectivity patterns.

**[Visual Graph Arena: Evaluating Visual Conceptualization of Vision and Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/babaiee25a/babaiee25a.pdf) (as "Hamiltonian path detection")**
> Identifying whether a graph contains a path that visits each node exactly once, based on visual input.

**[Visual Graph Arena: Evaluating Visual Conceptualization of Vision and Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/babaiee25a/babaiee25a.pdf) (as "Hamiltonian cycle detection")**
> Determining whether a graph contains a cycle that visits each node exactly once, based on visual input.

**[Visual Graph Arena: Evaluating Visual Conceptualization of Vision and Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/babaiee25a/babaiee25a.pdf) (as "Biggest chordless cycle identification")**
> Identifying the size of the largest cycle in a graph where no two non-consecutive nodes are connected by an edge not in the cycle.

## Relationships

### Associated with
- **Algorithmic reasoning** (constructs)
  - [Understanding Transformer Reasoning Capabilities via Graph Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f395480c04ac6dfb2c2326a639df88e-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks)
  > We define the length-2 path problem on a graph, and use it as a means to understand other graph reasoning tasks such as graph connectivity, shortest path, and cycle detection. (Section 3.2)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **Pathfinding** (behaviors tasks)
  > We define the length-2 path problem on a graph, and use it as a means to understand other graph reasoning tasks such as graph connectivity, shortest path, and cycle detection. (Section 3.2)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **Inductive reasoning** (constructs)
  > We combine the complementary strengths of a lightweight KG-specialized LLM with a powerful general LLM to enhance reasoning performance by leveraging their respective graph-based reasoning and inductive reasoning capabilities. (Section 1)
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
