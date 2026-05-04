# Ambiguity handling
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Ambiguity awareness, Ambiguity understanding, Task ambiguity  

## State of the Field

Across the surveyed literature, ambiguity handling is predominantly framed as a model's capacity to manage user inputs that are open to multiple interpretations. Definitions vary slightly in focus, describing it as "ambiguity awareness"—the ability to recognize when a situation "admits multiple plausible interpretations"—or "ambiguity understanding," which involves correctly interpreting vague or incomplete instructions. A more technical and less common framing defines ambiguity at the tokenization level, where "multiple token sequences can correspond to the same text." The construct is operationalized through several behaviors; one paper suggests that an effective response to ambiguity is to "ask clarifying questions" rather than assuming a single interpretation. Another line of work measures this ability by evaluating whether models can "correctly understand the instructions and produce the right answers" on benchmarks like VISUAL-O1, which was designed to test the disambiguation of instructions. One paper notes that "weak reasoning abilities of disambiguation can lead to catastrophic errors." The construct is studied alongside `Uncertainty quantification` and is proposed to be caused by `Commonsense knowledge`.

## Sources

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf) (as "Ambiguity awareness")**
> The ability to recognize when a question, object, or situation admits multiple plausible interpretations and therefore cannot be answered with certainty.

**[Visual-O1: Understanding Ambiguous Instructions via Multi-modal Multi-turn Chain-of-thoughts Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3769fddee1b20552d2490c4ff18b136-Paper-Conference.pdf) (as "Ambiguity understanding")**
> The ability of a model to correctly interpret language instructions that are vague, incomplete, or contain colloquialisms by integrating visual context and common sense.

**[Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf)**
> The general capacity of a model to respond effectively to highly ambiguous user requests rather than presupposing a single interpretation.

**[The Foundations of Tokenization: Statistical and Computational Concerns](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3748cdac932d91f0a51a37db90dec50-Paper-Conference.pdf) (as "Ambiguity")**
> The extent to which multiple token sequences can correspond to the same text, creating uncertainty in decoding or in the induced language model.

**[Eliciting Human Preferences with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf) (as "Task ambiguity")**
> The degree to which a user's intended task specification is underspecified or open to multiple interpretations.

## Relationships

### Ambiguity handling →
- **Human evaluation** (measurements) — *measured_by*
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **G-Eval** (measurements) — *measured_by*
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)

### Associated with
- **Prompt engineering** (behaviors tasks)
  - [Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf)
- **Uncertainty quantification** (constructs)
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
