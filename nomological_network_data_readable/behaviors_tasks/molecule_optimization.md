# Molecule optimization
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Molecular optimization  

## State of the Field

Across the provided literature, molecule optimization is consistently defined as the task of generating or searching for molecules to optimize specific, desirable properties. The goal, as one paper states, is to "design new molecules with desired properties such as high chemical stability, low toxicity, or selective inhibition against a target disease" (LICO: Large Language Models for In-Context Molecular Optimization). Other commonly targeted properties include drug-likeness, binding affinity, and synthesis difficulty. The task is described as either an iterative search of the chemical space or the generation of chemical structures, such as SMILES. This behavior is operationalized and measured using specific benchmarks and scoring systems. For instance, papers evaluate performance on the Practical Molecular Optimization (PMO) benchmark, which is referred to as a "standard benchmark for molecular optimization." Another approach involves using metrics like SCScore to assess whether generated molecules have successfully reduced synthesis difficulty.

## Sources

**[LICO: Large Language Models for In-Context Molecular Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/84b16af3773fc5825ddb64996190289a-Paper-Conference.pdf) (as "Molecular optimization")**
> The task of iteratively searching the chemical space to find molecules that maximize a specific desired property, such as drug-likeness or bioactivity.

**[Searching for Optimal Solutions with LLMs via Bayesian Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/a79237d6c47feef24c1df723cb41f674-Paper-Conference.pdf)**
> The generation of chemical structures (SMILES) to optimize specific properties like druglikeness and binding affinity.

## Relationships

### Molecule optimization →
- **PMO** (measurements) — *measured_by*
  > We evaluate LICO on Practical Molecular Optimization (PMO) (Gao et al., 2022), a standard benchmark for molecular optimization with a focus on sample efficiency. (Section 5.1)
  - [LICO: Large Language Models for In-Context Molecular Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/84b16af3773fc5825ddb64996190289a-Paper-Conference.pdf)
- **SCScore** (measurements) — *measured_by*
  > The results indicate that our OSDA Agent successfully generated optimized versions of these molecules, reducing the SCScore and thereby lowering the synthesis difficulty, while preserving the functional characteristics necessary for zeolite templating. (Section 5.3)
  - [OSDA Agent: Leveraging Large Language Models for De Novo Design of Organic Structure Directing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f38fbf326eb71f4749d04102323f7f79-Paper-Conference.pdf)
