# Ethical reasoning
**Type:** Construct  
**Referenced in:** 11 papers  
**Also known as:** Machine ethics, Ethical consideration, Deontological morality, Utilitarian morality, Ethical considerations, Ethics, Morality  

## State of the Field

Across the surveyed literature, ethical reasoning is predominantly framed as a latent ability for models to understand, adhere to, and make judgments based on moral principles, particularly in complex or conflicting scenarios. Definitions vary in terminology, using phrases like "machine ethics," "moral reasoning," and "morality," but generally converge on this core concept of navigating situations involving right and wrong. A few papers offer more specific or alternative framings; one line of work analyzes the construct through distinct philosophical lenses, such as Deontological (rule-based) and Utilitarian (consequence-based) morality. A different, more behavioral definition treats "ethical consideration" not as an internal capacity but as an observable "tendency for outputs to comment on ethics, limitations, or responsible use," as noted in one study where "GPT and Claude comment much more on ethics and limitations than Llama" (VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models). The most common method for operationalizing this construct is through the ETHICS benchmark, which is frequently cited as a tool for its measurement, probing a model's understanding of concepts like justice, well-being, and commonsense morality. Failures in ethical reasoning are sometimes characterized as "causal reasoning gaps" or "ethical blind spots" where a model fails to "fully realize the consequences of its actions" (BadRobot: Jailbreaking Embodied LLM Agents in the Physical World). The construct is studied alongside Faithfulness and Safety, and human preference alignment is reported to improve this ability, with one paper finding that RLHF leads to a "substantial average improvement... on the machine ethics benchmark" (More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness).

## Sources

**[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf)**
> The latent ability to evaluate the moral and consequential implications of actions, beyond superficial rule-following.

**[More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf) (as "Machine ethics")**
> The model's adherence to ethical principles and its ability to recognize actions that are against human morality.

**[DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life](https://proceedings.iclr.cc/paper_files/paper/2025/file/8587069d00a69d0ea498d547fffad6dd-Paper-Conference.pdf) (as "Moral reasoning")**
> The cognitive ability to navigate and make judgments in situations involving complex and often conflicting ethical principles.

**[VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/acbfe708197ff78ad04cc1beb1710979-Paper-Conference.pdf) (as "Ethical consideration")**
> A tendency for outputs to comment on ethics, limitations, or responsible use in addition to providing factual content.

**[Moral Alignment for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2b1bad4756ceee8f408e16b8e6e4383-Paper-Conference.pdf) (as "Deontological morality")**
> A moral framework where the morality of an action is judged based on its adherence to a set of rules or norms, such as not defecting against a cooperator.

**[Moral Alignment for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2b1bad4756ceee8f408e16b8e6e4383-Paper-Conference.pdf) (as "Utilitarian morality")**
> A moral framework where the morality of an action is judged based on its consequences, specifically its ability to maximize the collective welfare or payoff for all agents.

**[Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf) (as "Ethics")**
> The model's capacity to adhere to moral principles and make ethically sound judgments, particularly in complex dilemmas.

**[MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf) (as "Ethical considerations")**
> The adherence of a model's responses to ethical principles, including safety, privacy, fairness, and the avoidance of harmful or biased content.

**[ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf) (as "Morality")**
> The model's latent adherence to ethical principles and commonsense moral judgments when presented with scenarios involving right and wrong.

## Relationships

### Ethical reasoning →
- **ETHICS** (measurements) — *measured_by*
  - [ALI-Agent: Assessing LLMs'  Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)

### → Ethical reasoning
- **Human preference alignment** (constructs) — *causes*
  > RLHF applied to a general-purpose preference dataset leads to a substantial average improvement of 31% on the machine ethics benchmark. (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)

### Associated with
- **Trustworthiness** (constructs)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Safety** (constructs)
  - [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf)
