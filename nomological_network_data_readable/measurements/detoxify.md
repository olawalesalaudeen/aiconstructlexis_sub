# Detoxify
**Type:** Measurement  
**Referenced in:** 15 papers  

## State of the Field

Across the provided literature, Detoxify is consistently described as a model-based tool used to evaluate and score the toxicity of generated text. It is most frequently used to operationalize the construct of Harmlessness, and in one instance, Harmful content generation. The instrument functions by assigning a numerical toxicity score, where a higher value indicates more toxic content, and researchers sometimes apply a threshold to this score for classification. One paper specifies that Detoxify evaluates six distinct attributes: "toxicity, severe toxicity, obscene, threat, insult, identity attack." In practice, it is used as an automated evaluation procedure for LLM outputs, sometimes alongside other tools like the OpenAI Moderation API and Perspective API. One study compares its detection rate on harmful instructions to other APIs, finding it flagged 6% of cases with a threshold of ≥0.7. The data also shows that researchers may use different scoring thresholds or even retrain the model on custom datasets for specific applications.

## Sources

**[Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf)**
> Model-based toxicity scoring system that assigns a toxicity score to generated text.

## Relationships

### → Detoxify
- **Harmlessness** (constructs) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
