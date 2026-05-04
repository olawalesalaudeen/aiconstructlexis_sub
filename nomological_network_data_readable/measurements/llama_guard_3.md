# Llama Guard 3
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** Llama-Guard-3, Llama-Guard-3-8B, Llama-guard-3, Llama-Guard3-8B  

## State of the Field

Across the provided literature, Llama Guard 3 is predominantly characterized as an automated tool for evaluating the safety of language model outputs, frequently described as a "safety classifier," "automated judge," or "content safety classification LLM." Its primary documented use is to measure `Harmful content generation` by classifying model responses as "harmful or safe." Papers specify that it is capable of identifying various types of harmful content, such as "violence, self-harm, illegal activities, and inappropriate sexual content." It is operationalized as a "discriminator in attack evaluation" and as an "auxiliary detection tool," with one source noting the "close alignment of Llama-guard-3 and human evaluations" ("Measuring memorization in language models via probabilistic extraction"). While most sources focus on this safety classification role, a few papers describe more specific or distinct applications. For example, one study employs it to "evaluate the fairness of model outputs," and another uses it to assess safety by measuring a model's "refusal rate to harmful queries." A different framing appears in one paper that characterizes Llama Guard 3 not just as a post-hoc evaluation instrument but as an active "neural defense model" designed to "detect and block jailbreak attempts and unsafe content."

## Sources

**[FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf) (as "Llama-Guard-3")**
> An open-source content safety classification LLM used as an auxiliary detection tool to evaluate the fairness of model outputs.

**[Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory](https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf) (as "Llama-Guard-3-8B")**
> Safety classifier used to judge whether model responses are safe in the alignment experiment.

**[Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion](https://aclanthology.org/2025.naacl-long.88.pdf)**
> A semantic classifier capable of identifying various types of harmful content, including violence, self-harm, illegal activities, and inappropriate sexual content, used as a discriminator in attack evaluation.

**[Measuring memorization in language models via probabilistic extraction](https://aclanthology.org/2025.naacl-long.470.pdf) (as "Llama-guard-3")**
> Automated content moderation system used as a judge to classify model-generated responses as harmful or safe based on predefined safety policies.

**[M³GQA: A Multi-Entity Multi-Hop Multi-Setting Graph Question Answering Benchmark](https://aclanthology.org/2025.acl-long.1479.pdf) (as "Llama-Guard3-8B")**
> A specialized language model used as an evaluation tool to assess the safety of other models' outputs by measuring their refusal rate to harmful queries.

## Relationships

### → Llama Guard 3
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > Then evaluate the harmfulness score on its responses with the Llama-Guard-3-8B (Llama Team, 2024). We use 70% harmful prompts in the AdvBench dataset (Zou et al., 2023b) for InferAligner, Vaccine, and our SaLoRA. (Section 5.1).
  - [Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion](https://aclanthology.org/2025.naacl-long.88.pdf)
