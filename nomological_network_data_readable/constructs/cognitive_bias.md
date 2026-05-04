# Cognitive bias
**Type:** Construct  
**Referenced in:** 10 papers  
**Also known as:** Long context bias, Counterfactual bias, Acquiescence bias, Present bias, Authority bias, Bandwagon bias, Compassion-fade bias, Distraction bias, Positive bias, Limited cognitive ability, Attention bias, Interpretation bias, Memory bias  

## State of the Field

Across the surveyed literature, cognitive bias is most commonly framed as a systematic pattern of deviation from norm or rationality in judgment. This general construct is used to characterize a wide variety of specific phenomena in LLMs, including biases related to judgment (e.g., `Authority bias`, `Bandwagon bias`), context processing (`Long context bias`, `Distraction bias`), and social factors (`Counterfactual bias`). Operationalization of the construct is diverse and tailored to the specific bias under investigation. For example, `Counterfactual bias` is measured by assessing semantic differences in responses when demographic attributes in prompts are altered, while `Long context bias` is identified through degraded performance as input sequence length increases. In studies of 'LLM-as-a-Judge' systems, biases are frequently operationalized by manipulating prompts with elements like fake authoritative sources or emotional content to observe their influence. A less common framing defines cognitive bias as a model's tendency to generate linguistically plausible but perceptually inconsistent answers. The construct is studied in relation to `Attention sink` and `Knowledge forgetting`, and specific forms like `Attention bias` and `Interpretation bias` are examined as cognitive dimensions that are reported to correlate with depression relapse.

## Sources

**[Can LLMs Understand Time Series Anomalies?](https://proceedings.iclr.cc/paper_files/paper/2025/file/05774fb74e863308c4b460c9f49f6918-Paper-Conference.pdf) (as "Long context bias")**
> A model's tendency to exhibit degraded performance on time series analysis tasks as the length of the input sequence (number of tokens) increases.

**[Certifying Counterfactual Bias in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c6decac1477fbcc2cbf12d314ce0133-Paper-Conference.pdf) (as "Counterfactual bias")**
> The tendency of an LLM to produce semantically different or biased responses when only demographic-sensitive attributes in otherwise matched prompts are changed.

**[ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf) (as "Acquiescence bias")**
> A tendency to preferentially give affirmative responses even when uncertainty or inconsistency would warrant other answers.

**[Exploring Prosocial Irrationality for LLM Agents: A Social Cognition View](https://proceedings.iclr.cc/paper_files/paper/2025/file/65b4e84b66ed049f8066919a803e3942-Paper-Conference.pdf)**
> A systematic pattern of deviation from norm or rationality in judgment, often stemming from subjective processing of information.

**[Language Models Trained to do Arithmetic Predict Human Risky and Intertemporal Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3372a60f76e0acce756cb24deead020-Paper-Conference.pdf) (as "Present bias")**
> The tendency to overvalue immediate rewards compared to future rewards, leading to time-inconsistent preferences.

**[Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf) (as "Authority bias")**
> A tendency for an LLM judge to assign greater credibility to statements that appear to come from authoritative sources.

**[Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf) (as "Bandwagon bias")**
> A tendency for an LLM judge to prefer the majority view regardless of whether it is correct.

**[Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf) (as "Compassion-fade bias")**
> The latent tendency of an LLM judge to evaluate responses differently when they are attributed to a well-known model versus an anonymized or less-known source.

**[Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf) (as "Distraction bias")**
> A tendency for an LLM judge to be influenced by irrelevant or unimportant details in the prompt or response.

**[Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf) (as "Positive bias")**
> A learned tendency for a model to avoid generating responses that fall outside of categories provided in a prompt, possibly due to training on positive image-text pairs.

**[Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf) (as "Sentiment bias")**
> A tendency for an LLM judge to prefer or be influenced by positive or negative emotional expression in the content being judged.

**[The Pursuit of Empathy: Evaluating Small Language Models forPTSDDialogue Support](https://aclanthology.org/2025.emnlp-main.1574.pdf) (as "Limited cognitive ability")**
> A constraint in the model’s capacity to correctly comprehend or reason about visual content, leading to hallucinated or incorrect cognitive responses despite accurate perception.

**[Moral Framing in Politics (MFiP): A new resource and models for moral framing](https://aclanthology.org/2025.emnlp-main.1758.pdf) (as "Attention bias")**
> The latent tendency to preferentially focus on specific types of information, such as negative or positive content, while ignoring others, reflecting a persistent cognitive vulnerability in depression.

**[Moral Framing in Politics (MFiP): A new resource and models for moral framing](https://aclanthology.org/2025.emnlp-main.1758.pdf) (as "Interpretation bias")**
> The latent tendency to perceive ambiguous situations or information in a systematically biased way, particularly toward negative interpretations, which persists after remission and predicts relapse risk.

**[Moral Framing in Politics (MFiP): A new resource and models for moral framing](https://aclanthology.org/2025.emnlp-main.1758.pdf) (as "Memory bias")**
> The latent tendency to recall past experiences in a way that is disproportionately influenced by current emotional states, especially favoring negative memories, serving as a cognitive marker for depression relapse.

## Relationships

### Associated with
- **Attention sink** (constructs)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Knowledge forgetting** (constructs)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
