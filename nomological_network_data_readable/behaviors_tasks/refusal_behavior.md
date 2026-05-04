# Refusal behavior
**Type:** Behavior  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, refusal behavior is consistently defined as the observable act of a model declining to respond to prompts identified as harmful, unsafe, or policy-violating. This behavior is treated as an indicator of intact safety mechanisms and is described in one paper as a "safety-critical function" (NUTMEG: Separating Signal From Noise in Annotator Disagreement). The measurement of this behavior is operationalized through specific evaluation setups. For instance, one study mentions a "focused evaluation of binary refusal behavior" using a balanced set of one-line prompts (NUTMEG: Separating Signal From Noise in Annotator Disagreement). Additionally, the JailbreakBench benchmark is used to assess this behavior by measuring the "jailbreak Attack Success Rate (ASR)", where a successful attack represents a failure of the model to refuse (The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence). Refusal behavior is studied alongside concepts like "attack success rate" and "safety risk index" and is also noted as being related to "Helpful response generation".

## Sources

**[Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)**
> The observable act of a model declining to respond to a harmful or unsafe prompt, indicating intact safety mechanisms.

## Relationships

### Refusal behavior →
- **JailbreakBench** (measurements) — *measured_by*
  > We evaluate the jailbreak Attack Success Rate (ASR) on JAILBREAKBENCH (Chao et al., 2024) using the STRONGREJECT fine–tuned judge (Souly et al., 2024).
  - [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wollschlager25a/wollschlager25a.pdf)

### Associated with
- **Helpful response generation** (behaviors tasks)
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
