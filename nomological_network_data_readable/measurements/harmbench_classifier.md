# HarmBench classifier
**Type:** Measurement  
**Referenced in:** 2 papers  
**Also known as:** HarmBench Classifier  

## State of the Field

An LLM-as-a-judge safety classifier fine-tuned to assess whether model outputs are harmful.

## Sources

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)**
> An LLM-as-a-judge safety classifier fine-tuned to assess whether model outputs are harmful.

**[SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf) (as "HarmBench Classifier")**
> A specific classifier from the HarmBench benchmark, used as a baseline safety evaluator in the meta-evaluation.

## Relationships

### → HarmBench classifier
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: the official HarmBench classifier... (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
