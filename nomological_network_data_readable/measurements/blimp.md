# BLiMP
**Type:** Measurement  
**Referenced in:** 15 papers  

## State of the Field

Across the provided literature, BLiMP (Benchmark of Linguistic Minimal Pairs) is consistently characterized as an instrument for evaluating a model's knowledge of linguistic phenomena, particularly English grammar. The prevailing operationalization involves presenting models with "minimal pairs" of sentences—one grammatical or acceptable and the other not—to test the model's ability to distinguish between them. One paper specifies this is done by measuring whether the model "assigns lower perplexity to the grammatical sentences" ("Follow the Beaten Path..."). While its most common application is evaluating "syntactic phenomena," a number of sources describe its scope more broadly, noting that its 67 subtasks test contrasts across "syntax, morphology, and semantics" ("HIGGS..."). Consequently, BLiMP is used to measure a range of constructs, most frequently "linguistic knowledge," "syntactic competence," and "formal linguistic competence." It is also used to assess "language proficiency" and, in one instance, the "faithfulness" of explanations. The benchmark is described as "extensively utilised" and is typically evaluated in a "zero-shot setting" ("HIGGS...").

## Sources

**[Sudden Drops in the Loss: Syntax Acquisition, Phase Transitions, and Simplicity Bias in MLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e8df255a03b383f30abe09203770213-Paper-Conference.pdf)**
> Benchmark of Linguistic Minimal Pairs, a corpus of minimal-pair sentence judgments used here to evaluate syntactic phenomena such as agreement.

## Relationships

### → BLiMP
- **Language proficiency** (constructs) — *measured_by*
  > To assess the significance of the localized units on the models’ linguistic abilities, we utilize three widely used benchmarks that measure formal linguistic competence (Mahowald et al., 2024). ... Second, BLiMP...
  - [HIGGS: Pushing the Limits of Large Language Model Quantization via the Linearity Theorem](https://aclanthology.org/2025.naacl-long.544.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf)
- **Syntactic competence** (constructs) — *measured_by*
  - [Follow the Beaten Path: The Role of Route Patterns on Vision-Language Navigation Agents Generalization Abilities](https://aclanthology.org/2025.naacl-long.407.pdf)
- **Linguistic knowledge** (constructs) — *measured_by*
  > As a control, we evaluate TopoLM's performance on linguistic knowledge (BLiMP), downstream task (GLUE), and brain alignment benchmarks (Brain-Score), compared to the non-topographic baseline model.
  - [TopoLM: brain-like spatio-functional organization in a topographic language model](https://proceedings.iclr.cc/paper_files/paper/2025/file/4f7f521c08b5e0cd9931e74fa353b59b-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > "All models were evaluated on a common evaluation measure: BLiMP (Warstadt et al., 2020)."
  - [TopoNets: High performing vision and language models with brain-like topography](https://proceedings.iclr.cc/paper_files/paper/2025/file/6191ab7080c840f67eaf5dff7d5edfcb-Paper-Conference.pdf)
- **Syntactic ability** (constructs) — *measured_by*
  - [Search Wisely: Mitigating Sub-optimal Agentic Searches By Reducing Uncertainty](https://aclanthology.org/2025.emnlp-main.999.pdf)
- **Formal linguistic competence** (constructs) — *measured_by*
  - [Sketch-of-Thought: EfficientLLMReasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1237.pdf)
- **Plausibility** (constructs) — *measured_by*
  - [The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology](https://aclanthology.org/2025.emnlp-main.1769.pdf)
