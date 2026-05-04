# Molecule understanding
**Type:** Behavior  
**Referenced in:** 18 papers  
**Also known as:** Molecular property prediction, Functional group detection, Molecular structure elucidation, Spectrum interpretation, Molecule construction, Saturation identification, Aromatic ring identification, Functional group identification, Saturation degree calculation, Molecular toxicity prediction, Binding prediction, Binding affinity prediction, Molecular description generation, Property prediction, IUPAC name prediction, Forward reaction prediction, Retrosynthesis, Molecular graph extension, Pharmaceutical property prediction, Reaction prediction  

## State of the Field

Across the provided literature, molecule understanding is not a single, unified task but a broad category of behaviors related to analyzing, predicting, and generating information about chemical structures. The most prevalent usage involves molecular property prediction, where models generate numerical values for physical properties, predict biophysical attributes like toxicity, or perform classifications such as antibody-antigen binding. A second major line of work frames it as molecular structure elucidation, an overarching task of deducing a molecule's structure from its formula and spectral data. This elucidation process is further broken down into sub-tasks, including an initial 'molecule understanding' stage for inferring properties from a formula, 'spectrum interpretation', and a final 'molecule construction' stage, as detailed in 'Can LLMs Solve Molecule Puzzles?'. Other related tasks include generating natural language descriptions, predicting systematic IUPAC names, and forecasting chemical reactions through forward reaction prediction or retrosynthesis. To operationalize these behaviors, researchers employ a range of benchmarks, with MoleculeNet being frequently used for property prediction, alongside others like QM9, CheBI-20, and Mol-Instructions. This set of tasks is studied in conjunction with Chemical reasoning and Planning, and performance on them is reported to be influenced by Chain-of-thought reasoning.

## Sources

**[3D-MolT5: Leveraging Discrete Structural Information for Molecule-Text Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d4dc72d715bd6415d356293079adf3d-Paper-Conference.pdf) (as "Molecular property prediction")**
> The task of generating a numerical value or a textual description for a specific chemical or physical property of a given molecule.

**[Hierarchical Graph Tokenization for Molecule-Language Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cf/chen25cf.pdf) (as "Functional group detection")**
> Determining whether a specific functional group (e.g., hydroxide, carboxylic acid) is present in a given molecular structure, typically in response to a yes/no question.

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Molecular structure elucidation")**
> The overarching task of deducing a molecule's complete chemical structure by integrating clues from various types of spectral data and a molecular formula.

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The initial sub-task of analyzing a given molecular formula to infer foundational properties such as the degree of saturation, the presence of aromatic rings, and potential functional groups.

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Spectrum interpretation")**
> The sub-task of analyzing multimodal spectral data, including images of IR, MASS, H-NMR, and C-NMR spectra, to confirm or revise hypotheses about a molecule's structural components.

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Molecule construction")**
> The final sub-task of iteratively selecting and assembling molecular fragments into a complete and valid structure that is consistent with all provided NMR data and other evidence.

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Saturation identification")**
> Determining whether a molecule has a given degree of saturation from its formula or structural clues.

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Aromatic ring identification")**
> The specific, observable task of identifying the presence of aromatic rings within a molecule based on its chemical formula.

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Functional group identification")**
> The specific, observable task of identifying potential functional groups within a molecule based on its chemical formula and spectral data.

**[Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Saturation degree calculation")**
> The specific, observable task of quantitatively calculating the degree of unsaturation for a molecule from its chemical formula.

**[UniTox: Leveraging LLMs to Curate a Unified Dataset of Drug-Induced Toxicity from FDA Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/16659e412de3965fa195ddb9f2c4b356-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Molecular toxicity prediction")**
> Predicting drug toxicity from molecular structure using machine learning models trained on UniTox labels.

**[A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Binding prediction")**
> The task of classifying whether a given antibody sequence will bind to a specific antigen, typically framed as a binary or multi-class classification problem.

**[A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Binding affinity prediction")**
> The task of predicting a continuous value representing the strength or affinity of the binding interaction between an antibody and an antigen.

**[LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf) (as "Molecular description generation")**
> The task of generating a natural language text that accurately describes the properties, structure, and function of a given molecule.

**[LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf) (as "Property prediction")**
> The task of predicting specific numerical chemical or physical properties of a molecule, such as orbital energies.

**[LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf) (as "IUPAC name prediction")**
> The task of generating the standard, systematic IUPAC nomenclature for a given molecular structure.

**[LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf) (as "Forward reaction prediction")**
> The task of determining the potential products of a chemical reaction given a set of reactants and reagents.

**[LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf) (as "Retrosynthesis")**
> The task of identifying potential reactant molecules required to synthesize a target chemical compound.

**[A new framework for evaluating model out-of-distribution generalisation for the biochemical domain](https://proceedings.iclr.cc/paper_files/paper/2025/file/b84adff45775e92a45f0cd87c37f5ce9-Paper-Conference.pdf) (as "Pharmaceutical property prediction")**
> The task of predicting biophysical attributes of small molecules, such as their absorption, distribution, metabolism, excretion, and toxicity (ADMET).

**[Conformal Generative Modeling with Improved Sample Efficiency through Sequential Greedy Filtering](https://proceedings.iclr.cc/paper_files/paper/2025/file/c2a96d676ac2716615bf1ab7edd3f3d3-Paper-Conference.pdf) (as "Molecular graph extension")**
> Generating a single-atom extension of an incomplete molecular graph so that it matches the target molecule.

**[Multimodal Large Language Models for Inverse Molecular Design with Retrosynthetic Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6739d8df16b5bce3587ca5f18662a6aa-Paper-Conference.pdf) (as "Reaction prediction")**
> Predicting a reaction template or one-step retrosynthetic reaction from a product molecule and text context.

## Relationships

### Molecule understanding →
- **MoleculeNet** (measurements) — *measured_by*
  - [SMI-Editor: Edit-based SMILES Language Model with Fragment-level Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/b0b750c4189f19d0cd71375e9e17f83f-Paper-Conference.pdf)
- **CheBI-20** (measurements) — *measured_by*
  - [LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf)
- **Mol-Instructions** (measurements) — *measured_by*
  - [TreeReview: A Dynamic Tree of Questions Framework for Deep and EfficientLLM-based Scientific Peer Review](https://aclanthology.org/2025.emnlp-main.791.pdf)
- **QM9** (measurements) — *measured_by*
  - [3D-MolT5: Leveraging Discrete Structural Information for Molecule-Text Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d4dc72d715bd6415d356293079adf3d-Paper-Conference.pdf)

### → Molecule understanding
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [Learning Together to Perform Better: Teaching Small-ScaleLLMs to Collaborate via Preferential Rationale Tuning](https://aclanthology.org/2025.acl-long.755.pdf)

### Associated with
- **Expressive power** (constructs)
  - [A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Planning** (constructs)
  - [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Chemical reasoning** (constructs)
  - [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf)
