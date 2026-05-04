# Personalization
**Type:** Construct  
**Referenced in:** 47 papers  
**Also known as:** Personalization capability  

## State of the Field

The most prevalent definition of personalization across the provided literature is the ability to tailor responses and content to a user's unique needs and preferences, often by understanding their historical interactions. While this core idea is widespread, its application varies; some work frames it as adapting predictions based on demographic attributes, while other papers define it as adapting to user-specific subjects or community-level norms. A more specific framing, found in one paper, defines it for multimodal models as the "latent ability... to conduct personalized conversations that correctly identify and reference specific individuals presented in context" (Personalized Visual Instruction Tuning). Across these uses, personalization is consistently treated as an adaptive capability, with one paper noting that by default, large models "lack personalization primarily due to the nature of their training data."

To operationalize this construct, researchers employ several measurement approaches. A common method is automated evaluation using an "LLM as a judge," where a model like GPT-4 rates responses on their "relevance to users' preferences." Human evaluation is also used, with participants directly rating the extent to which a response is personalized. Specific benchmarks are reported to assess personalization, including OpinionQA and GlobalOpinionQA for aligning with user opinions, and Caltech101 in studies that investigate the balance between personalization and other model properties. Personalization is frequently studied in relation to generalization, with some papers aiming to "balance" these two goals, and is also associated with safety and catastrophic forgetting. Additionally, some work suggests that a model's expressive power can improve its personalization.

## Sources

**[Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)**
> The ability to tailor responses and content to a user's unique needs and preferences by understanding their historical interactions.

**[Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf) (as "Personalization capability")**
> The latent ability of a multimodal model to conduct personalized conversations that correctly identify and reference specific individuals presented in context.

## Relationships

### Personalization →
- **LLM-as-a-judge** (measurements) — *measured_by*
  > “We further explore whether we can employ language models to automate the evaluation... we ask GPT-4 to rate the responses based on their helpfulness and relevance to users’ preferences.”
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *causes*
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > “We then ask the participant to rate the extent to which the LLM response is personalized to the given context, Ci.”
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
- **Caltech101** (measurements) — *measured_by*
  > We select four visual classification datasets to investigate the task of balancing personalization, generalization and privacy: Caltech101 (Fei-Fei et al., 2004) (Section 4.1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **OpinionQA** (measurements) — *measured_by*
  > For OpinionQA, we use a subsampled split released by Hwang et al. (2023), which consists of 10.5k and 15.8k training and test QA pairs across 525 users and 15 topics, respectively. For GlobalOpinionQA, since the dataset originally included the answer distribution by multiple respondents in the same country, we converted it to have a single answer by selecting the choice with the highest probability. It results in 920 training and 1,317 test QA pairs across 46 countries. We consider each country as a specific user. (Section 4.1)
  - [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.598.pdf)
- **GlobalOpinionQA** (measurements) — *measured_by*
  > For GlobalOpinionQA, since the dataset originally included the answer distribution by multiple respondents in the same country, we converted it to have a single answer by selecting the choice with the highest probability. It results in 920 training and 1,317 test QA pairs across 46 countries. We consider each country as a specific user. (Section 4.1)
  - [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.598.pdf)

### → Personalization
- **Expressive power** (constructs) — *causes*
  > The residual term is crucial for retaining the expressiveness lost during the factorization process, thereby preserving the client-specific learning and improving personalization (Section 1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)

### Associated with
- **Generalization** (constructs)
  > FedPGP (Cui et al., 2024): Incorporate a low-rank adaptation term with an additional contrastive loss to balance generalization and personalization.
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf)
- **Safety** (constructs)
  - [Retrospective Learning from Interactions](https://aclanthology.org/2025.acl-long.1201.pdf)
