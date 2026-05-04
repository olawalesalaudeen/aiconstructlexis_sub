# Parameter sensitivity
**Type:** Construct  
**Referenced in:** 9 papers  
**Also known as:** Hyper-parameter sensitivity, Numeric precision sensitivity, Progressive sensitivity, Quantization sensitivity, Weight sensitivity  

## State of the Field

Across the provided literature, parameter sensitivity is most commonly framed as the degree to which specific model parameters disproportionately influence optimization outcomes during fine-tuning. This construct is operationalized by identifying parameters with maximized "coordinate-wise gradient square values" or by using the "empirical Fisher information matrix," with one study noting that as few as "0.1%-1% parameters contribute about 50% gradient norm square" (Zeroth-Order Fine-Tuning of LLMs with Transferable Static Sparsity). Another paper characterizes this phenomenon as being marked by "high Hessian values" during the initial phases of adaptation. While this is the prevailing usage, the concept is also applied to other contexts, such as 'quantization sensitivity,' where different model components show varied accuracy loss from reduced precision, and 'numeric precision sensitivity,' which concerns a model's response to small changes in input specifications. A specific framing, 'progressive sensitivity,' posits that models become more sensitive to parameter modifications with more pre-training. This particular form of sensitivity is reported to cause greater 'knowledge forgetting' when the model is subsequently modified.

## Sources

**[Zeroth-Order Fine-Tuning of LLMs with Transferable Static Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/266983d0949aed78a16fa4782237dea7-Paper-Conference.pdf)**
> The extent to which particular parameters contribute disproportionately to optimization progress or loss change during fine-tuning.

**[LaMAGIC2: Advanced Circuit Formulations for Language Model-Based Analog Topology Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25b/chang25b.pdf) (as "Numeric precision sensitivity")**
> The model's ability to detect and respond accurately to small differences in numeric input specifications, such as voltage conversion ratio or efficiency targets.

**[MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duanmu25a/duanmu25a.pdf) (as "Quantization sensitivity")**
> The degree to which different components of a model are affected by reduced numerical precision, influencing the accuracy loss when quantized.

**[Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf) (as "Hyper-parameter sensitivity")**
> A property of a defense mechanism where its effectiveness is highly dependent on the specific hyper-parameters, such as learning rate and training epochs, used during the fine-tuning process.

**[Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf) (as "Progressive sensitivity")**
> The latent tendency of pre-trained models to become increasingly sensitive to parameter modifications—such as fine-tuning or noise—as the amount of pre-training data increases, leading to greater forgetting of pre-trained knowledge.

**[Radio: Rate–Distortion Optimization for Large Language Model Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/young25b/young25b.pdf) (as "Weight sensitivity")**
> The degree to which perturbations in a model's specific weights affect the overall output distortion and final prediction accuracy.

## Relationships

### Parameter sensitivity →
- **Knowledge forgetting** (constructs) — *causes*
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
