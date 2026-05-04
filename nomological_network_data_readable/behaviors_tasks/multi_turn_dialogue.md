# Multi-turn dialogue
**Type:** Behavior  
**Referenced in:** 38 papers  
**Also known as:** Multi-turn conversation  

## State of the Field

Across the surveyed literature, multi-turn dialogue is predominantly defined as the behavior of maintaining a coherent and contextually relevant conversation over multiple exchanges. This interaction is frequently contrasted with "single-round Q&A sessions" (PROMPTEVALS), with definitions emphasizing the need to maintain context and statefulness across turns. While the most common framing involves a user and an AI, some papers study this behavior in agent-agent simulations where agents "take turns (in a round-robin fashion...)" to act in a shared context (SOTOPIA). A smaller line of work also conceptualizes it as a reinforcement learning problem requiring "multiple rounds of language interaction" to achieve a goal (LMRL Gym). To measure this behavior, papers commonly use the MT-Bench benchmark, which is described as containing "80 multi-turn questions spanning eight distinct knowledge domains". Other approaches to studying this behavior include analyzing large-scale interaction logs, as seen with the WildChat dataset, or using simulation frameworks. The provided data also shows multi-turn dialogue is studied in relation to long-context processing and safety, though the nature of these connections is not specified.

## Sources

**[Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)**
> The behavior of maintaining a coherent and contextually relevant conversation over multiple exchanges with a user.

**[#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf) (as "Multi-turn conversation")**
> Responding coherently across multiple dialogue turns in a conversational benchmark setting.

## Relationships

### Multi-turn dialogue →
- **MT-Bench** (measurements) — *measured_by*
  > To further validate the improvements of ICON2 in overall capabilities and multi-turn dialogue, we conducted evaluations on MT-Bench, with the results shown in Table 2 (Section 4.3).
  - [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf)

### Associated with
- **Dialogue** (behaviors tasks)
  - [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf)
- **Long-context understanding** (constructs)
  - [LLM-Guided Co-Training for Text Classification](https://aclanthology.org/2025.emnlp-main.1584.pdf)
