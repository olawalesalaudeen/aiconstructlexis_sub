# Prompt sensitivity
**Type:** Construct  
**Referenced in:** 23 papers  
**Also known as:** Input saliency, Prompt brittleness, Prompt influence, Instruction sensitivity  

## State of the Field

The most prevalent definition of "Prompt sensitivity" across the provided literature is the tendency for a model's performance and output to vary based on different, often semantically similar, wordings of a prompt. This is frequently framed as a form of instability, with one paper noting that "slight variations in input prompts can lead to significant differences in output quality" (GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers). Related terms like "prompt brittleness" and "instruction sensitivity" are also used, focusing on specific variations such as formatting, example order, or instruction phrasing. A less common framing, seen in the concepts of "prompt influence" and "input saliency," treats this as the "latent influence of individual input tokens" on model generation, connecting it to interpretability (Unveiling and Manipulating Prompt Influence in Large Language Models). This construct is operationalized by observing model responses to prompt modifications like paraphrasing or reordering. The effects are measured through changes in task performance or shifts in model behavior, such as when "bias patterns frequently shift or reverse direction entirely" due to minimal prompt changes (Invisible Entropy: Towards Safe and Efficient Low-EntropyLLMWatermarking). One paper also links the phenomenon to the conditional accessibility of "Prompt-Sensitive Known Knowledge (PSK)" (GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models).

## Sources

**[Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf) (as "Prompt brittleness")**
> The tendency of model predictions to change substantially under small changes in prompt formatting, verbalizers, example choice, or example order.

**[Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf) (as "Input saliency")**
> The latent influence of individual input tokens in a prompt on the generation of specific output tokens by an LLM, reflecting their causal contribution to model decisions.

**[Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf) (as "Prompt influence")**
> The latent extent to which prompt tokens shape or steer the model's generated outputs.

**[Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/a8de97fa77a09258b22880c230a83445-Paper-Conference.pdf)**
> The tendency for a model's performance and output to vary based on different wordings of a prompt, even when the prompts are semantically similar.

**[What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf) (as "Instruction sensitivity")**
> The degree to which a model's performance is affected by variations in the textual phrasing or ordering of an instruction, even when the semantic meaning is identical.
