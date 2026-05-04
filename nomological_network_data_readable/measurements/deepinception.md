# DeepInception
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, DeepInception is consistently characterized as a jailbreak attack method, operationalized as a "manually crafted jailbreak prompt template." Its mechanism, as described in multiple sources, involves using "imaginary scenes and characters to attack target LLMs," with one paper elaborating that it is a "meticulously crafted manual prompt template." The primary application of DeepInception is to evaluate model safety. Specifically, it is used to measure `Harmlessness` by functioning as an adversarial attack to test the robustness of an LLM's safety defenses. Within this context, it is frequently evaluated as a state-of-the-art technique alongside other jailbreak methods such as GCG, PAIR, AutoDAN, and ReNeLLM.

## Sources

**[CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)**
> A manually crafted jailbreak prompt template that uses imaginary scenes and characters to attack target LLMs.

## Relationships

### → DeepInception
- **Harmlessness** (constructs) — *measured_by*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
