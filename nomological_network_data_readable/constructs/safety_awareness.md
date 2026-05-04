# Safety awareness
**Type:** Construct  
**Referenced in:** 10 papers  

## State of the Field

Across the surveyed literature, Safety awareness is predominantly framed as a latent construct related to a model's capacity to recognize and manage potentially harmful situations. The most common definition describes it as a disposition to identify sensitive or harmful actions and seek user confirmation before execution, with one study noting this is operationalized as a "safeguard mechanism". Other definitions characterize it as a model's general sensitivity to risks and tendency to avoid unsafe outputs, or more specifically as the ability to recognize and avoid harmful interactions like clicking on pop-ups. A smaller line of work treats it as an internal property, defining it by the degree to which a model's representations contain "clear and consistent distinctions between safe and toxic content." The construct is operationalized in several ways: one paper uses `Human evaluation` to assess a "safeguard rate," while others employ benchmarks like `SIUO` or measure it through `Harmfulness detection` tasks. Safety awareness is also positioned as a component of the broader concept of `Safety alignment`.

## Sources

**[A Survey ofQUDModels for Discourse Processing](https://aclanthology.org/2025.naacl-long.85.pdf)**
> The latent disposition to recognize and handle sensitive or potentially harmful actions by seeking user confirmation before execution.

## Relationships

### Safety awareness →
- **Human evaluation** (measurements) — *measured_by*
  > The safeguard rate measures how often UFO requests user confirmation when the request involves sensitive actions. All metrics are assessed through human evaluation. (Section 4.1)
  - [WebQuality: A Large-scale Multi-modal Web Page Quality Assessment Dataset with Multiple Scoring Dimensions](https://aclanthology.org/2025.naacl-long.26.pdf)
- **SIUO** (measurements) — *measured_by*
  > For assessment of safety-awareness, we employ SIUO (Wang et al., 2025) and MSS-Bench (Zhou et al., 2024) datasets... (Section 2.1).
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)

### Associated with
- **Harmfulness detection** (behaviors tasks)
  > “we define two security evaluation metrics: Safety Awareness, measured by accuracy on the binary classification task, and Risk Resistance, measured by accuracy on the 11-class risk identification task”
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **Safety alignment** (constructs)
  > These tasks pose significant challenges to the multimodal reasoning and safety alignment capabilities of models (Section 2.1).
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)
