# Watermark removal
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Watermark neutralization  

## State of the Field

Across the provided literature, watermark removal is consistently defined as an adversarial behavior aimed at eliminating or neutralizing embedded statistical signals from a language model or its output. The stated goal is to revert a watermarked model to an unwatermarked state or, in the context of knowledge distillation, to enable "untraceable knowledge distillation." This behavior is operationalized through several distinct methods. One paper proposes a taxonomy of approaches, distinguishing between "pre-distillation removal" via data paraphrasing and "post-distillation removal" through techniques like "inference-time watermark neutralization," which applies inverse rules to the model's logits. Another paper discusses a method named DE-MARK for performing this task. The behavior is studied in relation to the robustness of watermarking schemes, where it is described as a "critical vulnerability" that can "strip or alter the embedded watermark, undermining its intended protection" in adversarial settings.

## Sources

**[𝜙-Decoding: Adaptive Foresight Sampling for Balanced Inference-Time Exploration and Exploitation](https://aclanthology.org/2025.acl-long.648.pdf)**
> The act of eliminating or neutralizing watermark signals from training data or model outputs to prevent detection during knowledge distillation.

**[𝜙-Decoding: Adaptive Foresight Sampling for Balanced Inference-Time Exploration and Exploitation](https://aclanthology.org/2025.acl-long.648.pdf) (as "Watermark neutralization")**
> A post-distillation watermark removal method that counteracts an inherited watermark by applying inverted watermark rules directly to the student model's logits during its decoding phase.

## Relationships

### Associated with
- **Watermark robustness** (constructs)
  - [De-mark: Watermark Removal in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bq/chen25bq.pdf)
