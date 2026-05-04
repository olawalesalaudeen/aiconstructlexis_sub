# Humor understanding
**Type:** Construct  
**Referenced in:** 14 papers  
**Also known as:** Humor recognition, Humor, Affiliative humor, Aggressive humor, Self-defeating humor, Self-enhancing humor, Humor style  

## State of the Field

Across the surveyed literature, humor understanding is most commonly defined as a latent ability to comprehend the nuances, context, and contradictory elements that create humor, such as juxtaposition and puns. A smaller body of work frames it more simply as "humor recognition," or the ability to detect humor, while several papers treat "humor" not as an understanding construct but as a generative quality—a stylistic tendency to produce amusing responses. The construct is operationalized and measured using instruments including the Anthropic HHH dataset and the ArmoRM reward model. The Humor Style Questionnaire (HSQ) is also used to assess specific dimensions, namely affiliative, self-enhancing, aggressive, and self-defeating humor styles. Humor understanding is frequently studied alongside helpfulness and harmlessness as multi-dimensional alignment objectives. Some research suggests that this understanding is a foundational skill that can improve a model's ability to generate humorous text. However, multiple papers note that current models' grasp of the concept remains "shallow," as they "struggle with understanding the nuances of human humor through juxtaposition" (Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions).

## Sources

**[Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf)**
> The latent ability to comprehend and interpret the nuances of humor, particularly when it arises from the juxtaposition of contradictory elements.

**[Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e297fb6cd1690ee5b39c5bb4c58ad801-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Humor recognition")**
> The ability of a model to identify or detect humor in a given piece of content.

**[Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf) (as "Humor")**
> The tendency of a model to produce amusing or humorous responses when such style is desired.

**[Preemptive Detection and Correction of Misaligned Actions inLLMAgents](https://aclanthology.org/2025.emnlp-main.13.pdf) (as "Affiliative humor")**
> A style of humor characterized by its use to enhance social relationships and build rapport with others.

**[Preemptive Detection and Correction of Misaligned Actions inLLMAgents](https://aclanthology.org/2025.emnlp-main.13.pdf) (as "Aggressive humor")**
> A style of humor characterized by its use to criticize or disparage others, often through sarcasm or teasing.

**[Preemptive Detection and Correction of Misaligned Actions inLLMAgents](https://aclanthology.org/2025.emnlp-main.13.pdf) (as "Self-defeating humor")**
> A style of humor characterized by making jokes at one's own expense to gain approval from others.

**[Preemptive Detection and Correction of Misaligned Actions inLLMAgents](https://aclanthology.org/2025.emnlp-main.13.pdf) (as "Self-enhancing humor")**
> A style of humor characterized by its use as a coping mechanism to deal with stress and maintain a positive outlook.

**[2025.emnlp-main.13.checklist](https://aclanthology.org/attachments/2025.emnlp-main.13.checklist.pdf) (as "Humor style")**
> A latent dispositional trait reflecting an individual's or model's characteristic way of engaging with humor, such as preference for certain types of jokes or comedic expression.

## Relationships

### Humor understanding →
- **Anthropic HHH** (measurements) — *measured_by*
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *causes*
  > Finally, with these two basic skills, humor understanding and judgment, the ability to generate humor can be improved. (Section 1)
  - [Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps](https://proceedings.iclr.cc/paper_files/paper/2025/file/6794f555524c9069e26970a408d353cc-Paper-Conference.pdf)
- **ArmoRM** (measurements) — *measured_by*
  > For the evaluation of 'harmless', 'helpful', and 'humor' dimensions... Additionally, we employ the ArmoRM (Wang et al., 2024b), a multi-dimension reward model... For these reward models, we report their scores assessing LLM responses from various perspectives.
  - [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)
- **Humor Style Questionnaire** (measurements) — *measured_by*
  > “The HSQ measures four distinct dimensions of humor: Affiliative humor ...”
  - [2025.emnlp-main.13.checklist](https://aclanthology.org/attachments/2025.emnlp-main.13.checklist.pdf)

### Associated with
- **Helpfulness** (constructs)
  > In practice, human preferences are multi-dimensional and we often need to align LLMs to balance multiple, sometimes conflicting, preference dimensions such as helpfulness, harmlessness, and humor (Section 2. Related Work)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
- **Harmlessness** (constructs)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
