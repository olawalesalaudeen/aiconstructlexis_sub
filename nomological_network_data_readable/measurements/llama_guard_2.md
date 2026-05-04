# Llama Guard 2
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** Llama-Guard-2, Llama-Guard-2-8B  

## State of the Field

Across the provided literature, Llama Guard 2 is predominantly characterized as an automated safety evaluation tool, frequently employed as an "LLM-as-a-judge." It is consistently defined as a safety classifier fine-tuned from Llama-3-8B. The instrument is used to measure constructs such as `Safety` and the behavior of `Harmful content generation`. Papers operationalize this by having Llama Guard 2 classify the harmfulness, toxicity, or safety of various outputs, including model responses, conversations, and documents. This classification is then used to compute metrics like Attack Success Rate, as noted in one study, or the percentage of unsafe responses. Its application appears in contexts like safety red-teaming evaluations, data filtering, and alignment training, where it is sometimes used alongside other evaluators like GPT-4. A less common application mentioned in one paper is using its feature layer as a source for semantic embeddings.

## Sources

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf) (as "Llama-Guard-2")**
> A safety classifier model fine-tuned from Llama-3-8B, used as an LLM-as-a-judge to evaluate the harmfulness of model responses.

**[Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf)**
> A model used as the semantic embedding source and to measure how safe or harmful a conversation is.

**[Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf) (as "Llama-Guard-2-8B")**
> A specialized language model used as an automated judge to classify the toxicity of model outputs for safety red-teaming evaluations.

## Relationships

### → Llama Guard 2
- **Safety** (constructs) — *measured_by*
  - [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: ... the Llama-Guard-2 safety classifier... (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
