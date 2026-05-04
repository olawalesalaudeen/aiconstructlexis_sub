# Trustworthiness and reliability
**Type:** Construct  
**Referenced in:** 16 papers  
**Also known as:** Prediction reliability, Reasoning reliability, Reward model reliability, Tool reliability, Verifier reliability, Trust and safety  

## State of the Field

Across the provided literature, trustworthiness and reliability are not treated as a single, unified concept but are multifaceted constructs applied to specific components and outputs of language model systems. The most prevalent usage frames reliability as the consistency and accuracy of a particular function. This includes the reliability of reward models, which is noted to be higher for high or low rewards than for moderate ones; the reliability of verifiers for evaluating reasoning paths; and the reliability of scaling law estimations in forecasting model performance. Another common application of reliability concerns the correctness of model behaviors, such as consistently producing a target answer after an edit, accurately interacting with external tools, or generating logically valid reasoning rationales. A distinct, human-centric framing is also present, where trustworthiness is defined as the confidence human experts have in a system's outputs, which one paper suggests can be enhanced by interpretability. This is related to the concept of trust and safety, which is defined as a system property that protects users from harm and fosters their confidence in the technology.

## Sources

**[A Hitchhiker’s Guide to Scaling Law Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/choshen25a/choshen25a.pdf) (as "Prediction reliability")**
> The degree to which estimated scaling laws consistently and accurately forecast the performance of target models, accounting for variability across seeds and training dynamics.

**[BalancEdit: Dynamically Balancing the Generality-Locality Trade-off in Multi-modal Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25e/guo25e.pdf) (as "Reliability")**
> The latent ability of a model to consistently produce the target answer for the specific input-question pair being edited, ensuring the edit is successfully applied.

**[Code-Generated Graph Representations Using Multiple LLM Agents for Material Properties Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25an/huang25an.pdf) (as "Trustworthiness")**
> The degree to which human experts can be confident in the outputs of the LLM system, often enhanced by the interpretability of its results.

**[Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf) (as "Tool reliability")**
> The ability of a large language model to accurately and effectively interact with external tools throughout a task, maximizing successful outcomes while minimizing errors and hallucinations.

**[Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf) (as "Reward model reliability")**
> The degree to which a reward model's assigned rewards align with the actual performance of model responses, varying across reward ranges.

**[BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf) (as "Reasoning reliability")**
> The consistency and trustworthiness of a model's reasoning outputs, such that generated rationales are valid and lead to correct conclusions across diverse problems.

**[From Passive to Active Reasoning: Can Large Language Models Ask the Right Questions under Incomplete Information?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25e/zhou25e.pdf) (as "Verifier reliability")**
> The consistency and accuracy with which a model component evaluates and selects promising reasoning paths during search-based active reasoning, affecting the overall effectiveness of strategies like tree-of-thought.

**[Position: Generative AI Regulation Can Learn from Social Media Regulation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/appel25a/appel25a.pdf) (as "Trust and safety")**
> The latent property of a system that ensures user protection from harm, including misinformation, abuse, and unsafe content, while fostering user confidence in the technology.
