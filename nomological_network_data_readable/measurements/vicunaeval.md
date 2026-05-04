# VicunaEval
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** Vicuna Eval, Vicuna Evaluation  

## State of the Field

VicunaEval is consistently characterized across the provided literature as a measurement instrument, described as both an "evaluation dataset" and a "benchmark." The prevailing usage is to assess model performance on instruction-following tasks, with one paper defining its purpose as evaluating "the quality of model responses across diverse prompts" ("TUNA: Comprehensive Fine-grained Temporal Understanding Evaluation on Dense Dynamic Videos"). A more specific framing notes it was designed to evaluate the Vicuna model in particular, using "80 challenging questions" ("OneQuantLLMforALL: Fine-tuning QuantizedLLMs Once for Efficient Deployments"). Its use is situated alongside other evaluation tools, as one study includes it in a list of "wide-used instruction datasets for assessment" ("TUNA..."). In practice, researchers use VicunaEval to operationalize and measure specific latent constructs. The provided data shows it is used as an instrument to assess both `Commonsense knowledge` and `Faithfulness` in models.

## Sources

**[TUNA: Comprehensive Fine-grained Temporal Understanding Evaluation on Dense Dynamic Videos](https://aclanthology.org/2025.acl-long.92.pdf) (as "Vicuna Eval")**
> An instruction-following evaluation dataset used to assess the quality of model responses across diverse prompts.

**[OneQuantLLMforALL: Fine-tuning QuantizedLLMs Once for Efficient Deployments](https://aclanthology.org/2025.acl-long.1125.pdf) (as "Vicuna Evaluation")**
> Benchmark comprising 80 challenging questions designed to evaluate the Vicuna model's performance on complex instruction-following tasks.

## Relationships

### → VicunaEval
- **Instruction following** (constructs) — *measured_by*
  - [A Grounded Typology of Word Classes](https://aclanthology.org/2025.naacl-long.522.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
