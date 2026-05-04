# WMT14 en-de
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** WMT14 En-De, WMT-14 en-de, WMT14 DE-EN  

## State of the Field

Across the provided literature, WMT14 en-de is described as both a benchmark and a dataset used to operationalize and measure the behavior of machine translation. Its most common application is for evaluation, specifically to assess the "translation quality" of language models, including finetuned LLMs. The prevailing usage defines the task as translating from English to German, with one paper noting its use for "translating English to German using WMT14 en-de" (On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes). However, a minority framing exists, with one source defining it for German-to-English translation. While primarily positioned as an evaluation instrument, a smaller line of work also utilizes it as a dataset for training models, particularly within "distillation experiments" (On Teacher Hacking in Language Model Distillation).

## Sources

**[On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)**
> WMT14 en-de is a machine translation benchmark for translating English to German, used to evaluate translation quality.

**[When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf) (as "WMT14 En-De")**
> WMT14 English-German machine translation benchmark used to evaluate finetuned LLMs on translation.

**[On Teacher Hacking in Language Model Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tiapkin25a/tiapkin25a.pdf) (as "WMT-14 en-de")**
> An English-to-German translation dataset used for training and evaluation in the distillation experiments.

**[polybasic Speculative Decoding Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25az/wang25az.pdf) (as "WMT14 DE-EN")**
> A dataset from the Workshop on Machine Translation (WMT) 2014 for evaluating German-to-English machine translation.

## Relationships

### → WMT14 en-de
- **Machine translation** (behaviors tasks) — *measured_by*
  > To evaluate GKD beyond summarization, we consider the task on translating English to German using WMT14 en-de (Bojar et al., 2014). (Section 4.2).
  - [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf)
