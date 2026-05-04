# Confidence estimation
**Type:** Construct  
**Referenced in:** 36 papers  
**Also known as:** Probability estimation, Confidence Expression, Expressing uncertainty, Confidence score generation, Step correctness prediction, Confidence correction, Verbalized confidence, Nuanced uncertainty expression, Linguistic uncertainty expression, Natural language uncertainty expression, Self-knowledge estimation, Model confidence  

## State of the Field

Across the surveyed literature, confidence estimation is predominantly characterized as the observable behavior of a model articulating its certainty, which is operationalized in two primary ways: through numerical scores and through natural language expressions. The most frequent numerical approach involves the model generating an explicit confidence score, often as a probability or percentage, representing its certainty in an answer's correctness or its alignment with human preferences. Other numerical methods infer confidence from internal model states, such as by "extracting the probability of the 'yes' token" to verify a prediction ("CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness") or by using signals like perplexity and token entropy. The second major operationalization involves linguistic expressions of uncertainty, where models generate text to qualify their answers with phrases ranging from direct statements like "I am unsure" ("Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration") to more nuanced hedging. The target of this estimation varies; while most work focuses on the final output, some papers measure confidence in intermediate steps, such as "scoring the correctness of reasoning steps" ("AROMA: Autonomous Rank-one Matrix Adaptation"). A less common framing treats confidence as an internal state inferred from the stability of representations or as a dynamic process, with one paper describing "confidence correction" as a recalibration pattern observed across model layers. In the provided literature, confidence estimation is also studied alongside self-consistency.

## Sources

**[Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf)**
> The model generates a numerical score representing its certainty that its judgment aligns with human preferences.

**[BIRD: A Trustworthy Bayesian Inference Framework for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/19452e14fe6e0a8ac00410f1eebcbded-Paper-Conference.pdf) (as "Probability estimation")**
> The observable act of assigning a numerical probability or confidence score to a potential outcome given a context.

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf) (as "Confidence Expression")**
> Providing probability estimates or confidence levels for predictions, often by verifying if a predicted answer is correct via token probability.

**[Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf) (as "Expressing uncertainty")**
> The observable behavior of a model explicitly stating its lack of confidence or knowledge in its response, such as by outputting phrases like 'I am unsure'.

**[Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf) (as "Confidence score generation")**
> The action of producing numerical confidence values for each potential class in a classification task, expressed within a natural language response.

**[AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.171.pdf) (as "Step correctness prediction")**
> The observable task of assigning a confidence score to each reasoning step indicating whether it is correct or incorrect, based on internal model states.

**[AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.171.pdf) (as "Self-evaluation")**
> The observable behavior of an LLM producing internal confidence signals about its own reasoning steps without external feedback.

**[2025.emnlp-main.530.checklist](https://aclanthology.org/attachments/2025.emnlp-main.530.checklist.pdf) (as "Confidence expression")**
> The model's output of a probability or likelihood score associated with its generated response or prediction.

**[WISE: Weak-Supervision-Guided Step-by-Step Explanations for MultimodalLLMs in Image Classification](https://aclanthology.org/2025.emnlp-main.742.pdf) (as "Confidence correction")**
> The observable pattern in which a model's confidence increases beyond accuracy (overconfidence) and then decreases to better align with accuracy in later layers, indicating active recalibration of confidence.

**[VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.73.pdf) (as "Verbalized confidence")**
> The observable expression of a model's certainty in its answer, typically in the form of a percentage or probability statement.

**[Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.187.pdf) (as "Nuanced uncertainty expression")**
> The generation of text that qualifies an answer with expressions of doubt or uncertainty, such as "I am not sure but..." or "maybe".

**[Multilingual Pretraining for Pixel Language Models](https://aclanthology.org/2025.emnlp-main.1505.pdf) (as "Linguistic uncertainty expression")**
> The observable use of words, phrases, and hedging language to convey a degree of confidence or doubt in a generated response.

**[2025.emnlp-main.1505.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1505.checklist.pdf) (as "Natural language uncertainty expression")**
> The model generates explicit statements about its confidence or uncertainty using natural language (e.g., 'I'm not sure' or 'I'm highly confident').

**[Your Language Model Can Secretly Write Like Humans: Contrastive Paraphrase Attacks onLLM-Generated Text Detectors](https://aclanthology.org/2025.emnlp-main.434.pdf) (as "Self-knowledge estimation")**
> The observable task of assigning a score to a model's own generated answer that reflects the model's confidence in its factual correctness, framed as a binary classification problem.

**[Your Language Model Can Secretly Write Like Humans: Contrastive Paraphrase Attacks onLLM-Generated Text Detectors](https://aclanthology.org/2025.emnlp-main.434.pdf) (as "Uncertainty estimation")**
> The model's generation of confidence or uncertainty signals (e.g., perplexity, token entropy) in response to input questions, used to infer implicit awareness of evergreen-ness.

**[MentalGLMSeries: Explainable Large Language Models for Mental Health Analysis onChinese Social Media](https://aclanthology.org/2025.emnlp-main.687.pdf) (as "Confidence scoring")**
> Assigning a numerical confidence level to a diagnostic decision based on factual consistency and evidence from a reasoning subgraph.

**[Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.276.pdf) (as "Model confidence")**
> The degree to which a model's internal representations reflect certainty in its predictions, inferred from stability of outputs and embedding dynamics.

## Relationships

### Associated with
- **Self-consistency** (measurements)
  - [Self-Consistency Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/prasad25a/prasad25a.pdf)
- **Reasoning** (constructs)
  - [E](https://aclanthology.org/2025.acl-long.417.pdf)
