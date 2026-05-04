# Safe-RLHF
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** SafeRLHF  

## State of the Field

Across the provided literature, Safe-RLHF is most commonly described as a human-annotated, pairwise preference dataset used for both alignment tuning and evaluation of language models. Papers consistently use this instrument to measure the constructs of `Helpfulness` and `Harmlessness`. A specific feature noted in the data is that it "ranks two responses in each datum for helpfulness and harmlessness independently." In practice, it is used as a training set for alignment methods and as a benchmark for LM alignment experiments, where one paper specifies that trained models are evaluated against a gold reward model and a reference model. The dataset's scale is described with some variation across papers, with one source citing "83.4K preference entries" and another "1 million human-labeled data points." Its application is also situated alongside other alignment datasets, as it is used in experiments with HH-RLHF.

## Sources

**[On Positional Bias of Faithfulness for Long-form Summarization](https://aclanthology.org/2025.naacl-long.443.pdf) (as "SafeRLHF")**
> Human-annotated pairwise preference dataset that independently ranks responses for helpfulness and harmlessness, used for alignment tuning and evaluation.

**[The Crucial Role of Samplers in Online Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/62133b95efaa6f10a5395eb10ca087cd-Paper-Conference.pdf)**
> A dataset used for LM alignment experiments in which trained models are evaluated against a gold reward model and a reference model.

## Relationships

### → Safe-RLHF
- **Helpfulness** (constructs) — *measured_by*
  - [PromptRefine: Enhancing Few-Shot Performance on Low-ResourceIndic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.18.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [PromptRefine: Enhancing Few-Shot Performance on Low-ResourceIndic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.18.pdf)
