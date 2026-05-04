# Privacy preservation
**Type:** Construct  
**Referenced in:** 18 papers  

## State of the Field

Across the surveyed literature, privacy preservation is a construct concerned with minimizing data exposure and memorization risk from private data used in LLM training, fine-tuning, and prompting. The common goal is to prevent models from leaking, regurgitating, or otherwise disclosing sensitive information, such as "private user information found in the training corpus." This construct is studied in multiple contexts, including federated learning where clients train on local data, and in-context learning where there is a risk that models "may leak or regurgitate the private examples demonstrated in the prompt." The most prevalent method for operationalizing this construct is through formal mathematical guarantees, with multiple papers defining it via differential privacy (DP). This involves ensuring that model parameters, outputs, or generated prompts satisfy a formal `(ε, δ)-DP` guarantee with respect to the private dataset. Other techniques mentioned include generating synthetic data or prompts with DP guarantees. To empirically assess the degree of privacy preservation, the provided literature indicates the use of both `LLM-as-a-judge` and `Human evaluation`, with one paper stating its use of human evaluation to assess a model's "capability in generating private summaries."

## Sources

**[Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e9034dd5420660d86c8c360c35a895e-Paper-Conference.pdf)**
> The extent to which a model training process minimizes data exposure and memorization risk, particularly in federated settings with decentralized data.

## Relationships

### Privacy preservation →
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [LLMThe Genius Paradox: A Linguistic and Math Expert’s Struggle with Simple Word-based Counting Problems](https://aclanthology.org/2025.naacl-long.173.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > We further evaluate the LMs capability in generating private summaries by conducting a human evaluation. (Section 4.5)
  - [FinetuningLLMs for Human Behavior Prediction in Social Science Experiments](https://aclanthology.org/2025.emnlp-main.1531.pdf)
