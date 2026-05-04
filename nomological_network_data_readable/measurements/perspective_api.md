# Perspective API
**Type:** Measurement  
**Referenced in:** 37 papers  
**Also known as:** PERSPECTIVE API, PerspectiveAPI  

## State of the Field

Across the provided literature, Perspective API is consistently characterized as an external tool or automated service used to evaluate text for harmful content. It is prevalently used to measure the construct of `Harmlessness` and the behavior of `Harmful content generation`. Researchers operationalize this measurement by using the API to generate a toxicity score, which is often a probability between 0 and 1 indicating the likelihood of text being toxic; some studies apply a specific threshold to this score to make a binary classification. The tool is noted for providing both an overall toxicity score and scores for more fine-grained attributes, with definitions frequently listing dimensions like severe toxicity, threat, profanity, and identity attack. Beyond evaluating model outputs, it is also employed for data filtering and as a baseline for comparison against other harm classification models. One paper describes its standing in the field as "a widely recognized automated toxicity detection tool... and the de facto benchmark" (Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs).

## Sources

**[Controlled Text Generation via Language Model Arithmetic](https://proceedings.iclr.cc/paper_files/paper/2024/file/96aad3299d18497e2bea4fc20b949b81-Paper-Conference.pdf)**
> An external tool used to classify text along multiple dimensions of toxicity, including severe toxicity, threat, profanity, and identity attack.

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf) (as "PERSPECTIVE API")**
> External tool that provides fine-grained toxicity scoring for text, including attributes like insult, profanity, and identity attack.

**[SynergizingLLMs with Global Label Propagation for Multimodal Fake News Detection](https://aclanthology.org/2025.acl-long.73.pdf) (as "PerspectiveAPI")**
> Automated content safety evaluation tool that scores text outputs on dimensions such as toxicity, insult, profanity, severe toxicity, and threat to assess model safety alignment.

## Relationships

### → Perspective API
- **Harmlessness** (constructs) — *measured_by*
  - [Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > For toxicity evaluation, we utilize the PERSPECTIVE API (Lees et al., 2022) for REALTOXICITYPROMPTS and the ToxiGen RoBERTa model for the ToxiGen benchmark, both designed to measure the generation of toxic content.
  - [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf)
