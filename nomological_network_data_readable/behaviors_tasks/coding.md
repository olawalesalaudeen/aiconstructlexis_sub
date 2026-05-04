# Coding
**Type:** Behavior  
**Referenced in:** 10 papers  
**Also known as:** Coding assistance  

## State of the Field

Across the provided literature, the behavior of 'Coding' is consistently defined as a task involving computer programming, encompassing activities like writing, debugging, and providing code-related solutions. The most common definition describes it as "responding to prompts that require code-related solutions or programming assistance" (Instruct-SkillMix; Position: AI Should Not Be An Imitation Game), with a related framing of "coding assistance" that focuses on helping users (Position: AI Scaling). One paper provides a concrete example of this behavior, citing a study that measured the speed of "coding a functional HTTP server" (Position: AI Should Not Be An Imitation Game). While the provided data does not detail a full evaluation procedure, one source mentions that the instructions for the WildBench benchmark cover coding tasks. In the surveyed work, coding is frequently presented as a distinct task category for LLMs, often studied alongside creative writing. It is also described as a function performed by specialized sub-models derived from a foundation model (Position: AI Scaling).

## Sources

**[Instruct-SkillMix: A Powerful Pipeline for LLM Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)**
> Responding to prompts that require code-related solutions or programming assistance.

**[Position: AI Scaling: From Up to Down and Out](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25fh/wang25fh.pdf) (as "Coding assistance")**
> The task of helping users write, debug, or complete computer code.

## Relationships

### Coding →
- **MBPP** (measurements) — *measured_by*
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **CodeContests** (measurements) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)

### Associated with
- **Code generation** (behaviors tasks)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Code debugging** (behaviors tasks)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
