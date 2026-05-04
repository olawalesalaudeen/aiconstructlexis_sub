# Misclassification
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Label misidentification, Triggered misclassification  

## State of the Field

Across the provided literature, misclassification is most commonly defined as an observable failure mode where a model produces an incorrect class label for a given input. This behavior is observed in various contexts, from text classification where an input is assigned to a wrong category, to vision-language models where it is framed as “tricking VLMs into misidentifying class labels” (Shadowcast: Stealthy Data Poisoning Attacks Against Vision-Language Models). A more specific variant is “triggered misclassification,” which describes incorrect classification specifically in response to inputs containing a backdoor trigger. The provided research identifies several conditions that can lead to this behavior. One paper reports that `Backdoor vulnerability` causes misclassification, noting that when a “poisoned trigger” is present, the model is induced to produce an adversarial response. Other work states that “even slight perturbations to input data can result in misclassification” (Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models). The behavior is operationalized by measuring the rate at which a model produces a targeted adversarial output or an incorrect label under these conditions.

## Sources

**[Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf)**
> An observable failure mode where the model produces an incorrect class label for a given input.

**[Shadowcast: Stealthy Data Poisoning Attacks Against Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a2e30664b9647f97d7b9275358d083c-Paper-Conference.pdf) (as "Label misidentification")**
> Responding to an image with the wrong class label or identity, such as naming one person or object as another.

**[Backdoor Attacks in Token Selection of Attention Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25c/wang25c.pdf) (as "Triggered misclassification")**
> The observable behavior in which a model incorrectly classifies inputs that contain a backdoor trigger, producing a targeted adversarial output.

## Relationships

### → Misclassification
- **Backdoor vulnerability** (constructs) — *causes*
  > “backdoor attacks are particularly insidious: they introduce ‘poisoned triggers’ ... When a trigger is present, the model produces an adversarial response; otherwise, it behaves normally.”
  - [Backdoor Attacks in Token Selection of Attention Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25c/wang25c.pdf)
