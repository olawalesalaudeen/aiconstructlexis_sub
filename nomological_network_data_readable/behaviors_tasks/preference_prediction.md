# Preference prediction
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Recipe preference prediction, Preference score prediction  

## State of the Field

Across the provided literature, preference prediction is a behavior centered on forecasting which items or responses will be favored by a user, population, or other mechanism. The most common framing of this task involves predicting a binary choice between two options, such as which of two recipes a population will rate more highly or which of two responses a reward model will select. A different line of work defines it as predicting a continuous "scalar preference score" that indicates the degree to which a response aligns with a specific user's preferences. This behavior is operationalized using datasets of paired items, for instance, one study created "a set of 500 recipe pairs with similar ingredients but significantly different average ratings" to evaluate models. The task is also approached by training a model to "predict the decisions of a given mechanism," which could be a human, an LLM-as-a-judge, or a reward model. Preference prediction is studied in relation to the Bradley-Terry model and is also connected to social bias. As one study notes, model performance on recipe prediction can reflect an "omnivore bias," where accuracy is lower when vegetarian options are rated higher by humans.

## Sources

**[What can large language models do for sustainable food?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25a/thomas25a.pdf) (as "Recipe preference prediction")**
> Predicting which recipe a target population will prefer or rate more highly.

**[PanicToCalm: A Proactive Counseling Agent for Panic Attacks](https://aclanthology.org/2025.emnlp-main.650.pdf) (as "Preference score prediction")**
> The model's output of a scalar score indicating the degree to which a given response aligns with a specific user's preferences.

**[FIRE: Flexible Integration of Data Quality Ratings for Effective Pretraining](https://aclanthology.org/2025.emnlp-main.736.pdf)**
> The task of predicting which of two responses is preferred by a mechanism (human, LLM-as-a-judge, or reward model) based on concept-based representations.

## Relationships

### Associated with
- **Bradley-Terry model** (measurements)
  - [Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?](https://proceedings.iclr.cc/paper_files/paper/2025/file/93f250215e4889119807b6fac3a57aec-Paper-Conference.pdf)
- **Social bias** (constructs)
  > Within the vegetarian vs. non-vegetarian meal comparisons, accuracy is lower when vegetarian options are rated higher, reflecting LLMs’ omnivore bias, as LLMs more frequently prefer non-vegetarian options compared to ground truth human preferences. (Section 5.4)
  - [What can large language models do for sustainable food?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25a/thomas25a.pdf)
