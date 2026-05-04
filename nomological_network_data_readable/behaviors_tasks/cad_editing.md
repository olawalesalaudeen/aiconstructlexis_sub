# CAD editing
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Masked CAD sequence generation, Modeling command generation, Text-to-CAD generation, CAD sequence infilling  

## State of the Field

Across the provided literature, "CAD editing" is a behavior centered on generating or modifying Computer-Aided Design (CAD) models from natural language instructions, with several distinct operationalizations presented. One common framing is "Text-to-CAD generation," defined as the end-to-end task of converting a textual description into a complete CAD model, often represented as a "CAD parametric sequence." A different approach, termed "Modeling command generation," focuses more narrowly on producing specific, executable CAD commands from instructions, which one paper describes as translating an "intention" into a "sequence of modeling commands." A more specific, two-stage operationalization of editing is also proposed in a single study. In this framework, a model first performs "Masked CAD sequence generation" to identify and mask the parts of a CAD sequence that require modification. Subsequently, the model engages in "CAD sequence infilling" to generate the precise modifications for these masked regions, resulting in the final edited model.

## Sources

**[Targeted control of fast prototyping through domain-specific interface](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25h/shi25h.pdf) (as "Modeling command generation")**
> The production of executable CAD modeling commands (e.g., Boolean union, surface lofting) from interpreted natural language instructions.

**[Text-to-CAD Generation Through Infusing Visual Feedback in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eg/wang25eg.pdf) (as "Text-to-CAD generation")**
> The end-to-end task of converting a natural language textual description into a complete Computer-Aided Design (CAD) model.

**[CAD-Editor: A Locate-then-Infill Framework with Automated Training Data Synthesis for Text-Based CAD Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25g/yuan25g.pdf) (as "Masked CAD sequence generation")**
> Identifying regions in a CAD sequence that require modification by replacing them with <mask> tokens while preserving unmodified parts.

**[CAD-Editor: A Locate-then-Infill Framework with Automated Training Data Synthesis for Text-Based CAD Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25g/yuan25g.pdf) (as "CAD sequence infilling")**
> Generating precise modifications to fill in masked regions of a CAD sequence to produce a fully edited CAD model.
