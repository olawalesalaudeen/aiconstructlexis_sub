# Beavertails
**Type:** Measurement  
**Referenced in:** 21 papers  
**Also known as:** BeaverTails, BeaverTails-Evaluation  

## State of the Field

Across the provided literature, Beavertails is predominantly described as a benchmark dataset for evaluating the safety and alignment of language models. The most frequent definition characterizes it as a tool for "response safety classification," while other papers frame it as a dataset for assessing "safety-related responses" and "harmlessness." Papers use Beavertails to operationalize and measure several constructs, most commonly `Harmlessness`, but also `Helpfulness`, `Safety`, and `Harmful content generation`. For instance, some studies explicitly measure `Harmful content generation` by sampling "1000 harmful instructions from the testing set of BeaverTails" to compute a score. The dataset is described as containing human annotations, with multiple sources noting it is structured around a "safety taxonomy of 14 categories." It is characterized as both a "human-annotated preference dataset" and a "question answering dataset containing advice queries and candidate answers," and is also used to test "safety filtering and jailbreak resistance." One study reports that models trained on the dataset "surpass their baselines in both helpfulness and harmlessness evaluations."

## Sources

**[Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf)**
> A dataset used to evaluate alignment and safety-related responses of finetuned language models.

**[BingoGuard: LLM Content Moderation Tools with Risk Levels](https://proceedings.iclr.cc/paper_files/paper/2025/file/782b6152c04e9948c2cb3833e9a288ef-Paper-Conference.pdf) (as "BeaverTails")**
> A benchmark dataset used for evaluating the performance of models on response safety classification.

**[Performance Gap in Entity Knowledge Extraction Across Modalities in Vision Language Models](https://aclanthology.org/2025.acl-long.1412.pdf) (as "BeaverTails-Evaluation")**
> A benchmark for evaluating the harmlessness of LLM responses to harmful instructions, assessing both content safety and refusal behavior.

## Relationships

### → Beavertails
- **Harmlessness** (constructs) — *measured_by*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > “To calculate the harmful score, we sample 1000 instructions from the testing set of BeaverTails (Ji et al., 2023).”
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Powerformer: Efficient and High-Accuracy Privacy-Preserving Language Model with Homomorphic Encryption](https://aclanthology.org/2025.acl-long.544.pdf)
- **Harmful content detection** (behaviors tasks) — *measured_by*
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Adversarial attacks** (behaviors tasks) — *measured_by*
  > BeaverTails (Ji et al., 2024) is the benchmark used by Rosati et al. (2024) to evaluate RepNoise; we adopt the same evaluation setup, reporting the average harmfulness scores (ranging from 0 to 1) as assessed by their harmfulness score. (Section 2.2)
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
