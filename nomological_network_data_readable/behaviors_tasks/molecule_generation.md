# Molecule generation
**Type:** Behavior  
**Referenced in:** 8 papers  
**Also known as:** Molecular generation, Multi-conditional molecular generation, Molecule synthesis  

## State of the Field

Across the provided literature, molecule generation is predominantly described as the task of producing novel molecular structures from a given prompt, context, or objective. The generated output is typically a molecular representation, with several papers specifying string-based formats such as SMILES or SELFIES. A recurring theme is that this generation is guided by specific goals, with one paper framing it as "multi-conditional molecular generation" that must satisfy constraints like property values and structural features. Other work operationalizes the task as generating molecules with specific "target properties" or meeting pharmaceutical criteria such as "binding affinity and drug-likeness." While most commonly termed 'molecule generation', the task is also referred to as 'molecule synthesis' in one paper, with a similar definition focused on generating valid structures from examples. One study notes the use of a specific tool, Pocket2Mol, to execute the generation action. This behavior is also presented as a domain-specific task requiring knowledge not typically found in general-purpose datasets.

## Sources

**[Multimodal Large Language Models for Inverse Molecular Design with Retrosynthetic Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6739d8df16b5bce3587ca5f18662a6aa-Paper-Conference.pdf) (as "Multi-conditional molecular generation")**
> The observable task of generating a molecular graph that simultaneously satisfies multiple constraints, such as specific property values and structural features.

**[Efficient Evolutionary Search Over Chemical Space with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/804b5e300c9ed4e3ea3b073f186f4adc-Paper-Conference.pdf) (as "Molecular generation")**
> The task of producing novel molecular structures, often represented as SMILES or SELFIES strings, based on a given prompt or objective.

**[SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cb240de90aa20207db944c6c88a7cc0-Paper-Conference.pdf)**
> Generating a molecular representation from a prompt or chemical context.

**[Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf) (as "Molecule synthesis")**
> The task of generating valid molecular structures in a specified format, such as SMILES, based on examples.
