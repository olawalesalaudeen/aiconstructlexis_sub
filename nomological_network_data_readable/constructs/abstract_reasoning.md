# Abstract reasoning
**Type:** Construct  
**Referenced in:** 48 papers  
**Also known as:** Abstract visual reasoning, Abstract thinking, Analogical reasoning, Problem abstraction, High-level reasoning, Analogy-making, Advanced abstract reasoning, Case-based reasoning, Algebraic rule induction, Letter string analogy solving, Verbal analogy solving  

## State of the Field

Across the surveyed literature, the prevailing view of abstract reasoning is as a high-level cognitive ability to identify and operate on patterns, concepts, and principles independent of concrete instances or surface-level details. This is frequently contrasted with precise, step-by-step formal deduction or direct computation, with some papers noting it is required for problems that are difficult to formalize as programs ("ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving"). The construct is multifaceted, with some work focusing on "abstract visual reasoning" in visual puzzles, while a prominent line of inquiry investigates "analogical reasoning," defined as transferring relational patterns to new domains. The field most commonly operationalizes and measures abstract reasoning using the Abstraction and Reasoning Corpus (ARC), a set of visual puzzles designed to evaluate this capability. Other measurement approaches include the use of Bongard Problems and, in one study, causal mediation analysis to probe the internal mechanisms that support the construct. Abstract reasoning is studied alongside and often linked to systematic generalization, relational reasoning, and logical reasoning. One paper explicitly defines it as a synergy between two processes: "abstraction, the extraction of common features from concrete entities... and reasoning, the derivation of new knowledge from existing information" ("Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance"). A few papers also suggest directional relationships, reporting that visual perception can impact abstract reasoning and that abstract reasoning may in turn influence complex reasoning.

## Sources

**[Lemur: Integrating Large Language Models in Automated Program Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c86142265c5e2c900613dd1d031cb90-Paper-Conference.pdf)**
> The ability to reason about program properties and logic at a conceptual level, distinct from precise, step-by-step formal deduction.

**[MARVEL: Multidimensional Abstraction and Reasoning through Visual Evaluation and Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/529d8b3a23991e83db07f21727256374-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Abstract visual reasoning")**
> The ability to identify high-level, abstract patterns governing relationships between visual shapes and their attributes in a specific task configuration.

**[ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf) (as "Abstract thinking")**
> The cognitive ability to work with concepts and principles independent of concrete instances, which is considered a prerequisite for demanding tasks like code generation.

**[VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf) (as "Analogical reasoning")**
> The cognitive ability to identify, map, and transfer relational patterns from a known domain (a reference pair) to a new one (an application pair).

**[Intelligence at the Edge of Chaos](https://proceedings.iclr.cc/paper_files/paper/2025/file/d791394d32c428aecc7a5b101fb47799-Paper-Conference.pdf) (as "Abstraction")**
> The model's ability to identify and operate on high-level patterns and concepts, independent of specific surface-level details.

**[GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf) (as "Problem abstraction")**
> A higher-order reasoning skill involving the simplification and conceptual representation of a problem's core components.

**[CanLLMs Convert Graphs to Text-Attributed Graphs?](https://aclanthology.org/2025.naacl-long.66.pdf) (as "High-level reasoning")**
> The latent ability of a model to reason from abstract, conceptual representations of a problem rather than from low-level details, enabling more robust and semantically precise inference.

**[Reasoning Limitations of Multimodal Large Language Models. A case study of Bongard Problems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/malkinski25a/malkinski25a.pdf) (as "Analogy-making")**
> The cognitive process of identifying and applying structural correspondences between different situations or representations.

**[D-RAG: Differentiable Retrieval-Augmented Generation for Knowledge Graph Question Answering](https://aclanthology.org/2025.emnlp-main.1794.pdf) (as "Advanced abstract reasoning")**
> The capacity to handle difficult combinatorial or other non-routine mathematical problems that require deeper abstraction and problem solving.

**[Refining Attention for Explainable and Noise-Robust Fact-Checking with Transformers](https://aclanthology.org/2025.emnlp-main.1296.pdf) (as "Case-based reasoning")**
> The tendency of LLMs to rely on surface-level patterns and pre-trained representations rather than generalizing well to novel input encodings, making them vulnerable to symbolic obfuscation.

**[Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25c/yang25c.pdf) (as "Algebraic rule induction")**
> Generating the next token in a sequence by inferring an abstract identity rule (e.g., ABA or ABB) from in-context examples using arbitrary tokens.

**[Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25c/yang25c.pdf) (as "Letter string analogy solving")**
> Solving analogical reasoning problems over letter sequences involving successor or predecessor relations (e.g., abc is to abd as xyz is to xya).

**[Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25c/yang25c.pdf) (as "Verbal analogy solving")**
> Solving analogical reasoning problems involving semantic relations such as synonymy or antonymy (e.g., hot is to cold as up is to down).

## Relationships

### Abstract reasoning →
- **ARC** (measurements) — *measured_by*
  > The Abstraction and Reasoning Corpus (ARC) aims to evaluate the abstract reasoning capabilities of language models through their ability to solve visual puzzles. (Section 4.1)
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
- **Complex reasoning** (behaviors tasks) — *causes*
  - [THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS](https://proceedings.iclr.cc/paper_files/paper/2024/file/2dae7d1ccf1edf76f8ce7c282bdf4730-Paper-Conference.pdf)
- **Causal mediation analysis** (measurements) — *measured_by*
  > The causal mediation analyses in section 3.1 demonstrate that the identified attention heads are causally sufficient, in the sense that perturbing their outputs alters the model’s responses in a predictable manner. (Section 3.4)
  - [Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25c/yang25c.pdf)
- **Bongard Problems** (measurements) — *measured_by*
  > Analogy-making is a critical aspect of human cognition, tightly linked with fluid intelligence, the capacity to apply learned skills in novel settings (Lake et al., 2017). Several approaches have been proposed to build systems capable of making analogies. Notably, the structure-mapping theory explores methods for discovering structural correspondences between pre-existing object representations... However, these approaches often overlook the perceptual aspect... (Introduction)
  - [Bongard in Wonderland: Visual Puzzles that Still Make AI Go Mad?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wust25a/wust25a.pdf)
- **Spatial reasoning** (constructs) — *causes*
  - [Conan-Embedding-v2: Training anLLMfrom Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.759.pdf)

### → Abstract reasoning
- **Visual perception** (constructs) — *causes*
  > A single error in visual feature perception can impact reasoning since the correct pattern must apply to all puzzle shapes. (Section 6)
  - [MARVEL: Multidimensional Abstraction and Reasoning through Visual Evaluation and Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/529d8b3a23991e83db07f21727256374-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **In-context learning** (constructs)
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **General reasoning** (constructs)
  - [Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf)
- **Compositional generalization** (constructs)
  - [Attention as a Hypernetwork](https://proceedings.iclr.cc/paper_files/paper/2025/file/abfa542f546df3c6c35695ec8d5bf4b9-Paper-Conference.pdf)
- **Perception** (constructs)
  > Analogical reasoning consists of diverse atomic abilities; perceptual understanding, mapping abstract relationships between visual contents (Gentner, 1983), and transferring relational patterns to novel cases. (Section 1)
  - [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf)
- **Relational reasoning** (constructs)
  > Analogical reasoning consists of diverse atomic abilities; perceptual understanding, mapping abstract relationships between visual contents... and transferring relational patterns to novel cases.
  - [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf)
- **Geometric reasoning** (constructs)
  - [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf)
- **Logical reasoning** (constructs)
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Reasoning Limitations of Multimodal Large Language Models. A case study of Bongard Problems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/malkinski25a/malkinski25a.pdf)
- **Reasoning** (constructs)
  > abstract reasoning involves two core processes: abstraction, the extraction of common features from concrete entities (Murphy, 2004), and reasoning, the derivation of new knowledge from existing information (Holyoak & Morrison, 2012).
  - [Benchmarking Abstract and Reasoning Abilities Through A Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25u/ma25u.pdf)
