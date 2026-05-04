# Aggregative question answering
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Aggregation question answering  

## State of the Field

The provided literature presents two distinct conceptualizations of aggregative question answering. One framing defines the behavior as a statistical task of "counting or summing entities or attributes that meet a certain criteria," with examples like "How many ACM fellow are from MIT?" ("LLMBias Detection and Mitigation through the Lens of Desired Distributions"). This view of the task is explicitly related to mathematical reasoning. A different paper describes it as a "novel task requiring models to reason over thousands of user-chatbot interactions to answer aggregative queries" ("5.8%"). In this context, the goal is to synthesize information to identify phenomena such as "emerging concerns among specific demographics" or "tracking changes in societal sentiment." This latter version of the task is operationalized and measured by the WildChat-AQA benchmark, which was introduced "to facilitate research into Aggregative Question Answering."

## Sources

**[LLMBias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.77.pdf) (as "Aggregation question answering")**
> Answering a question by counting or summing entities or attributes that meet a certain criteria.

**[5.8%](https://aclanthology.org/2025.emnlp-main.1667.pdf)**
> Generating answers to questions that require synthesizing information across thousands of conversations, such as identifying trends, demographic concerns, or sentiment shifts.

## Relationships

### Aggregative question answering →
- **WildChat-AQA** (measurements) — *measured_by*
  > To facilitate research into Aggregative Question Answering, we introduce WildChat-AQA, a benchmark constructed from the WildChat dataset (Zhao et al., 2024b; Deng et al., 2024). (Section 1)
  - [5.8%](https://aclanthology.org/2025.emnlp-main.1667.pdf)

### Associated with
- **Statistical reasoning** (constructs)
  - [LLMBias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.77.pdf)
