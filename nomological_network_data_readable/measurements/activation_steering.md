# Activation steering
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** Inference-time intervention (ITI), Model steering  

## State of the Field

Across the provided literature, Activation steering is predominantly characterized as a causal intervention technique used to modify a language model's behavior at inference time. This is achieved by directly altering the model's internal representations, specifically by shifting or adding to the hidden activations of targeted neurons during a forward pass. The terms "Inference-time intervention (ITI)" and "Model steering" are also used to describe this process of intervening on generations to produce a "counterfactual generation conditioned on the concept-based intervention" (AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders). The stated goals of this technique vary, with some work aiming to steer models toward abstract behaviors like memorization versus generalization, while other papers focus on eliciting or suppressing specific concepts in the generated output. The effectiveness of these interventions is operationalized in multiple ways, including using an LLM-as-a-judge to rate steered outputs and analyzing increases in likelihood for texts aligned with the desired behavior. Activation steering is positioned as a "practical application of various interpretability methods" and is studied in conjunction with concept detection. As one study notes, it has emerged as a "potential alternative to finetuning and prompting" due to its potential for "lightweight and interpretable control" (AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders).

## Sources

**[ESC-Judge: A Framework for Comparing Emotional Support Conversational Agents](https://aclanthology.org/2025.emnlp-main.812.pdf) (as "Inference-time intervention (ITI)")**
> An experimental procedure where the hidden activations of specific, targeted neurons are shifted during a model's forward pass to causally steer its behavior toward a desired outcome like memorization or generalization.

**[Neuron-Level Differentiation of Memorization and Generalization in Large Language Models](https://aclanthology.org/2025.emnlp-main.813.pdf)**
> A causal intervention technique that modifies a model's hidden activations at inference time to alter its behavior along a desired direction, such as from direct answering to abstention.

**[AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf) (as "Model steering")**
> The observable act of modifying a language model's internal representations during generation to produce outputs that incorporate a target concept while following instructions.

## Relationships

### Activation steering →
- **LLM-as-a-judge** (measurements) — *measured_by*
  > For the latter, we use an LLM judge to rate steered outputs on three relevant axes (see §3.3). (Section 3)
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Harmlessness** (constructs) — *causes*
  - [StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1501.pdf)

### Associated with
- **Interpretability and explainability** (constructs)
  > Since steering may enable lightweight and interpretable control over model outputs, it has emerged as a potential alternative to finetuning and prompting
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Concept detection** (constructs)
  > our results suggest that joint learning of concept detection and steering (as in ReFT-r1) may be the key to advancement.
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
