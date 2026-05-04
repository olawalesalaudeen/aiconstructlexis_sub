# Quantization robustness
**Type:** Construct  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, quantization robustness is consistently defined as the degree to which a model maintains its performance when its weights and activations are represented in low-precision formats. The concept is most frequently discussed in the context of extreme, low-bitwidth scenarios, such as 4-bit or 8-bit quantization, where models often suffer from what one paper calls "significant performance degradation." This construct is operationalized by measuring the change in model accuracy or performance after quantization, with one study noting a successful outcome as "less than 1% accuracy loss." The motivation for studying this property is to "reduce model size and computational latency." A specific challenge to achieving robustness is the presence of "activation outliers," which are identified as a "performance bottleneck." While the core definition is shared, one paper frames it more abstractly as a "latent ability" of a model, emphasizing resilience across diverse quantization settings.

## Sources

**[OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)**
> The degree to which a model maintains performance when weights and activations are represented in low-precision formats, particularly under extreme conditions like 4-bit quantization.

## Relationships

### Quantization robustness →
- **C4** (measurements) — *measured_by*
  - [SKIM: Any-bit Quantization Pushing The Limits of Post-Training Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25c/bai25c.pdf)
- **WikiText-2** (measurements) — *measured_by*
  - [SKIM: Any-bit Quantization Pushing The Limits of Post-Training Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25c/bai25c.pdf)
