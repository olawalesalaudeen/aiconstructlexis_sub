# Protein understanding
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Protein sequence generation, Protein contact prediction, Protein fold classification, Fluorescence prediction, Fitness prediction, Metal ion binding prediction, Solubility prediction, Stability prediction, Paratope prediction, Secondary structure prediction, Contact map prediction, Distance map prediction, Folding, Inverse folding, Mutation effect prediction, Protein variant fitness prediction, Zero-shot fitness prediction, Motif-scaffolding, Biophysical property prediction, Protein-protein interface prediction, Remote homology prediction, Protein fitness prediction, Protein sequence design, Mammalian cell expression prediction, Subcellular localization prediction, Thermostability prediction, Protein function prediction  

## State of the Field

In the surveyed literature, 'Protein understanding' represents a broad collection of behaviors centered on predicting protein structure, function, and generating novel sequences. A prevalent theme across papers is the prediction of functional and biophysical properties, with 'fitness prediction' being a frequently documented task, defined variously as predicting the impact of mutations or assigning a functional score to a sequence. These property prediction tasks are commonly operationalized as either regression (e.g., for fluorescence, stability) or binary classification (e.g., for metal ion binding, solubility). The behavior of protein fitness prediction is explicitly measured using the ProteinGym benchmark. Another major group of tasks involves structure, including predicting 3D structure from a sequence ('folding'), the reverse ('inverse folding'), and identifying internal features like residue contacts and secondary structure. The scope of tasks sometimes extends to other biomolecules, with some papers defining RNA-related prediction tasks such as contact and distance map prediction. A final set of behaviors involves generation, from creating plausible new protein sequences to targeted 'protein sequence design' for enhanced stability.

## Sources

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Protein sequence generation")**
> The task of creating novel amino acid sequences that are plausible or functional proteins.

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Protein contact prediction")**
> The task of predicting whether two amino acids in a protein sequence are close to each other in the folded 3D structure.

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Protein fold classification")**
> The task of assigning a protein sequence to one of a predefined set of structural fold classes.

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Fluorescence prediction")**
> A regression task to predict the fluorescence intensity of a protein.

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Fitness prediction")**
> A regression task to predict a protein's fitness, a measure of its functional performance.

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Metal ion binding prediction")**
> A binary classification task to determine whether a protein sequence binds to metal ions.

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Solubility prediction")**
> A binary classification task to predict whether a protein will be soluble when expressed.

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Stability prediction")**
> A regression task to predict the thermostability of a protein.

**[A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Paratope prediction")**
> The task of identifying the specific residues in an antibody's sequence that constitute the binding site (paratope) for an antigen.

**[BEACON: Benchmark for Comprehensive RNA Tasks and Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/a8ea503d91320fcfe12cba61c8a6d285-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Secondary structure prediction")**
> The task of identifying and predicting the base-pairing interactions within a single RNA molecule to determine its two-dimensional structure.

**[BEACON: Benchmark for Comprehensive RNA Tasks and Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/a8ea503d91320fcfe12cba61c8a6d285-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Contact map prediction")**
> The task of identifying which pairs of nucleotides in an RNA sequence are in close physical proximity in the molecule's three-dimensional structure.

**[BEACON: Benchmark for Comprehensive RNA Tasks and Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/a8ea503d91320fcfe12cba61c8a6d285-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Distance map prediction")**
> The task of estimating the physical, three-dimensional distances between all pairs of nucleotides within an RNA molecule.

**[DPLM-2: A Multimodal Diffusion Protein Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/57c30b677add9aa78e1745f0643104d0-Paper-Conference.pdf) (as "Folding")**
> Predicting a 3D protein structure from an amino-acid sequence.

**[DPLM-2: A Multimodal Diffusion Protein Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/57c30b677add9aa78e1745f0643104d0-Paper-Conference.pdf) (as "Inverse folding")**
> Generating an amino-acid sequence that is compatible with a given backbone structure.

**[DPLM-2: A Multimodal Diffusion Protein Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/57c30b677add9aa78e1745f0643104d0-Paper-Conference.pdf) (as "Motif-scaffolding")**
> Generating scaffold regions around a fixed motif while preserving the motif’s structure and function.

**[Bio-xLSTM: Generative modeling, representation and in-context learning of biological and chemical sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/60cefc59610f8f59ea10099f99a36726-Paper-Conference.pdf) (as "Protein variant fitness prediction")**
> The task of predicting the functional effect or fitness impact of amino acid substitutions (mutations) in a protein sequence.

**[Protein Language Model Fitness is a Matter of Preference](https://proceedings.iclr.cc/paper_files/paper/2025/file/62cf81a87f367758cebabce08e8d40d8-Paper-Conference.pdf) (as "Zero-shot fitness prediction")**
> The observable task of assigning a score to a mutated protein sequence relative to a wild type sequence to predict its functional fitness, without any fine-tuning on labeled fitness data.

**[Protein Language Model Fitness is a Matter of Preference](https://proceedings.iclr.cc/paper_files/paper/2025/file/62cf81a87f367758cebabce08e8d40d8-Paper-Conference.pdf) (as "Mutation effect prediction")**
> The specific task of predicting the functional outcome of one or more mutations in a protein sequence, often as a log odds ratio.

**[A new framework for evaluating model out-of-distribution generalisation for the biochemical domain](https://proceedings.iclr.cc/paper_files/paper/2025/file/b84adff45775e92a45f0cd87c37f5ce9-Paper-Conference.pdf) (as "Biophysical property prediction")**
> The task of predicting physical or chemical properties of proteins based on their sequence, such as the optimal temperature for catalysis.

**[The OMG dataset: An Open MetaGenomic corpus for mixed-modality genomic language modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/dbb40375daa3c39f1c098b12608aed12-Paper-Conference.pdf) (as "Protein-protein interface prediction")**
> The task of identifying specific amino acid residues that are in close proximity and form the interaction surface between two or more proteins.

**[The OMG dataset: An Open MetaGenomic corpus for mixed-modality genomic language modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/dbb40375daa3c39f1c098b12608aed12-Paper-Conference.pdf) (as "Remote homology prediction")**
> The task of identifying evolutionary relationships between proteins that have low sequence similarity.

**[Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf) (as "Protein fitness prediction")**
> The task of assigning a scalar value or a relative ranking to protein sequences based on their predicted biophysical or functional properties.

**[From Mechanistic Interpretability to Mechanistic Biology: Training, Evaluating, and Interpreting Sparse Autoencoders on Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/adams25a/adams25a.pdf) (as "Subcellular localization prediction")**
> Predicting the cellular compartment (e.g., nucleus, extracellular space) where a protein is localized based on its sequence.

**[From Mechanistic Interpretability to Mechanistic Biology: Training, Evaluating, and Interpreting Sparse Autoencoders on Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/adams25a/adams25a.pdf) (as "Thermostability prediction")**
> Predicting the melting temperature of a protein based on its sequence, used as a continuous regression task.

**[From Mechanistic Interpretability to Mechanistic Biology: Training, Evaluating, and Interpreting Sparse Autoencoders on Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/adams25a/adams25a.pdf) (as "Mammalian cell expression prediction")**
> A binary classification task to determine whether a given protein can be successfully expressed in a specific host cell line (e.g., Chinese hamster ovary cells).

**[Learning Extrapolative Sequence Transformations from Markov Chains](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hager25a/hager25a.pdf) (as "Protein sequence design")**
> The task of generating mutant protein sequences (specifically ACE2) with higher stability, measured by lower free energy (ddG), than the original wildtype sequence.

**[Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sculley25a/sculley25a.pdf) (as "Protein function prediction")**
> Predicting the biological function of proteins based on their amino acid sequences, in the absence of experimentally verified annotations during training.

## Relationships

### Protein understanding →
- **ProteinGym** (measurements) — *measured_by*
  > Specifically, we take the wild type proteins in 217 DMS studies from ProteinGym (Notin et al., 2023) and calculating PLLs for each of them. (Section 4.3)
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)

### → Protein understanding
- **Tool use** (behaviors tasks) — *causes*
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)
