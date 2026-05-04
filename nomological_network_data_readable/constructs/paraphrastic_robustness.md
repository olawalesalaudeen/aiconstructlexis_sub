# Paraphrastic robustness
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Robustness to paraphrases, Robustness to spurious features  

## State of the Field

Across the provided literature, paraphrastic robustness is most commonly defined as a model's ability to maintain stable performance or produce consistent behavior when an input like a question or instruction is rephrased without changing its underlying semantic meaning. A related but broader conceptualization, termed 'robustness to spurious features' in one paper, extends this to include stability against any meaning-preserving variations, such as changes in prompt formatting. The construct is operationalized by evaluating whether a model can produce the same correct output or behavior across multiple linguistic variations of the same prompt. For instance, one study measures this by using the CounterFact dataset and "computing the percentage of datapoints where the model gets all paraphrases of a given question correct." This form of robustness is treated as a specific type of generalization, with another paper using "unseen instruction datasets" for its measurement. The stability of model behavior under these variations is presented as a consideration when making claims about a model's general abilities.

## Sources

**[The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf) (as "Robustness to paraphrases")**
> The stability of a model's performance when a question or prompt is rephrased without changing its semantic meaning.

**[Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf) (as "Robustness to spurious features")**
> The ability of a model to maintain stable performance despite the presence of irrelevant or meaning-preserving variations in the input, such as prompt formatting.

**[Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf)**
> The latent ability of a model to produce consistent, correct behavior despite linguistic variations in task instructions, such as rephrasing or indirect object references, when the underlying intention remains unchanged.

## Relationships

### Paraphrastic robustness →
- **CounterFact** (measurements) — *measured_by*
  > We evaluate the model’s robustness to paraphrases by computing the percentage of datapoints where the model gets all paraphrases of a given question correct. (Section 5.1)
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
