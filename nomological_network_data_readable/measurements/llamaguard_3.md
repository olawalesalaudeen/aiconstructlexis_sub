# LlamaGuard 3
**Type:** Measurement  
**Referenced in:** 14 papers  
**Also known as:** Llama-Guard-3-8B, Llama-Guard-3, Llama-Guardv3-8B  

## State of the Field

Across the provided literature, LlamaGuard 3 is consistently characterized as a safety classifier or automated evaluator designed to classify content, such as prompts and model responses, as safe or unsafe. It is explicitly used to measure constructs like 'Harmful content generation', 'Safety alignment', and 'Harmlessness'. The instrument is operationalized in several ways: as a judge in red-teaming experiments, as a tool to assess refusal behavior and jailbreak resistance, and as an 'external guardrail' within evaluation frameworks like JailbreakBench. Multiple sources specify that it is a Llama-3.1-8B-based model that has been fine-tuned for content safety classification. One paper notes its adoption as a safety evaluator is due to its 'strong alignment with human judgment and effectiveness in evaluating long-form, reasoning-based outputs' (MAKAR: a Multi-Agent framework based Knowledge-Augmented Reasoning for Grounded Multimodal Named Entity Recognition).

## Sources

**[Neural Genetic Search in Discrete Spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25b/kim25b.pdf) (as "Llama-Guard-3-8B")**
> A safety classifier used to score whether generated responses are toxic in the red-teaming experiment.

**[Activation Space Interventions Can Be Transferred Between Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oozeer25a/oozeer25a.pdf) (as "Llama-Guard-3")**
> A safety classifier model that evaluates whether a prompt or response is safe or unsafe, used to assess refusal behavior and jailbreak resistance.

**[ConCISE](https://aclanthology.org/2025.emnlp-main.406.pdf)**
> A Llama-3.1-8B-based model fine-tuned for content safety classification, used as an automated evaluator to assess the harmfulness of model outputs.

**[PACHAT: Persona-Aware Speech Assistant for Multi-party Dialogue](https://aclanthology.org/2025.emnlp-main.1493.pdf) (as "Llama-Guardv3-8B")**
> A specific language model used as an external guardrail or automated judge to classify the safety of responses within the JailbreakBench evaluation framework.

## Relationships

### → LlamaGuard 3
- **Harmful content generation** (behaviors tasks) — *measured_by*
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **Safety alignment** (constructs) — *measured_by*
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.239.pdf)
