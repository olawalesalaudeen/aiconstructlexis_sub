# Uncertainty quantification
**Type:** Construct  
**Referenced in:** 44 papers  
**Also known as:** Aleatoric uncertainty awareness, Epistemic uncertainty awareness, Multimodal Uncertainty Awareness, Epistemic uncertainty, Epistemic Uncertainty, Aleatoric semantic uncertainty, Reward uncertainty, Weight uncertainty, Evaluation uncertainty, Response uncertainty, Prediction uncertainty, Reasoning uncertainty, Output uncertainty, Underspecification uncertainty, Uncertainty expression, Uncertainty signaling  

## State of the Field

Across the surveyed literature, uncertainty quantification is most commonly framed as a model's ability to represent its own lack of knowledge, where expressed confidence aligns with the probability of being correct. A prevailing distinction is made between epistemic uncertainty, which arises from the model's lack of knowledge and can be reduced with more data, and aleatoric uncertainty, which stems from inherent ambiguity or noise in the data itself. The construct is frequently operationalized by quantifying ambiguity in a model's internal states—using metrics like token probabilities, perplexity, and entropy—or by modeling uncertainty over model parameters, such as through weight distributions or ensemble variance. A distinct line of work treats it as an observable behavior, where the model explicitly conveys uncertainty through natural language phrases like "I am not sure," which is directly assessed by the UNCLE benchmark. This concept is applied in various contexts, including the assessment of reward models ("Reward uncertainty"), the stability of LLM evaluators ("Evaluation uncertainty"), and the reliability of reasoning processes ("Reasoning uncertainty"). Several papers suggest that improving uncertainty quantification can reduce hallucinations, with one study noting that "predictive uncertainty is one of the main causes of hallucinations," and it is also linked to faithfulness and safety. The construct is also studied alongside generation diversity, knowledge boundary awareness, and ambiguity handling.

## Sources

**[Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf) (as "Aleatoric uncertainty")**
> Uncertainty arising from inherent ambiguity or noise in the data itself, rather than from uncertainty about the model parameters.

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf) (as "Multimodal Uncertainty Awareness")**
> The latent ability of a model to recognize situations where a definitive answer cannot be provided due to information limitations or inherent unpredictability in vision-language tasks.

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf) (as "Epistemic uncertainty awareness")**
> The tendency to recognize uncertainty caused by missing information or incomplete evidence, where additional knowledge could reduce uncertainty.

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf) (as "Aleatoric uncertainty awareness")**
> The tendency to recognize uncertainty caused by inherent unpredictability that cannot be eliminated by gathering more information.

**[LiFT: Learning to Fine-Tune via Bayesian Parameter Efficient Meta Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/27e5626cabdbb6cd5c56ce4114ff93e4-Paper-Conference.pdf)**
> The model's ability to accurately represent its own uncertainty, where expressed confidence aligns with the actual probability of being correct.

**[Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf) (as "Epistemic uncertainty")**
> The model's uncertainty about its own prediction that reflects ambiguity or lack of knowledge rather than token-level likelihood alone.

**[Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf) (as "Epistemic Uncertainty")**
> Uncertainty in the model parameters that diminishes with more data, serving as an indicator of model uncertainty in predictions.

**[An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf) (as "Uncertainty")**
> The degree to which an LLM evaluator lacks confidence in its judgments, often operationalized through the probabilities of its output tokens.

**[Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf) (as "Uncertainty estimation")**
> The ability to quantify ambiguity in attention or prediction distributions and use that estimate to adapt model processing.

**[Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf) (as "Aleatoric semantic uncertainty")**
> The uncertainty arising from inherent ambiguity in which semantically distinct output meaning the model will generate for a given input.

**[Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf) (as "Reward uncertainty")**
> The degree of confidence or ambiguity in a reward model's prediction of human preference, often estimated using ensembles.

**[Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf) (as "Predictive uncertainty")**
> The uncertainty in the model's output predictions, as opposed to uncertainty in the parameters themselves.

**[Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf) (as "Weight uncertainty")**
> The uncertainty associated with the model's parameter estimates, modeled as a posterior distribution over the weights.

**[An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf) (as "Evaluation uncertainty")**
> The degree of instability or indecision in an LLM evaluator's judgments across inputs, settings, or domains.

**[Efficiently Learning at Test-Time: Active Fine-Tuning of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba942323c447c9bbb9d4b638eadefab9-Paper-Conference.pdf) (as "Response uncertainty")**
> The degree of ambiguity or lack of confidence in the model's predicted probability distribution for a response to a given prompt.

**[Token Signature: Predicting Chain-of-Thought Gains with Token Decoding Feature in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ci/liu25ci.pdf) (as "Reasoning uncertainty")**
> The degree of uncertainty in the model's reasoning process, especially when token probability trends suggest weaker alignment with successful reasoning.

**[Active Reward Modeling: Adaptive Preference Labeling for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25c/shen25c.pdf) (as "Model uncertainty")**
> The degree of uncertainty in the model's preference predictions, especially around comparisons that are near the decision boundary.

**[Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf) (as "Prediction uncertainty")**
> The degree of confidence a model has in its own predictions, which can be quantified and used to guide iterative reasoning processes.

**[Position: Uncertainty Quantification Needs Reassessment for Large Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kirchhof25b/kirchhof25b.pdf) (as "Underspecification uncertainty")**
> The latent uncertainty arising when a user's input does not fully specify the task or provide sufficient context, leading to ambiguity in the model's response generation.

**[Position: Uncertainty Quantification Needs Reassessment for Large Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kirchhof25b/kirchhof25b.pdf) (as "Output uncertainty")**
> The latent capacity of an LLM agent to express uncertainty not as a scalar value but through rich linguistic means such as natural language explanations, verbal qualifiers, or speech prosody to convey ambiguity, competing possibilities, and reasoning.

**[2025.emnlp-main.294.checklist](https://aclanthology.org/attachments/2025.emnlp-main.294.checklist.pdf) (as "Uncertainty awareness")**
> The degree to which a model accounts for or expresses uncertainty when making detection decisions.

**[VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1543.pdf) (as "Uncertainty expression")**
> The latent ability of a model to recognize gaps in its knowledge and explicitly convey that uncertainty through natural language phrases (e.g., 'it is unclear' or 'I am not sure') rather than generating false or overconfident statements.

**[WojoodRelations:Arabic Relation Extraction Corpus and Modeling](https://aclanthology.org/2025.emnlp-main.1742.pdf) (as "Uncertainty signaling")**
> The latent ability of a model to recognize ambiguity or inconsistency in its input and express doubt, refusal, or non-commitment in its response.

## Relationships

### Uncertainty quantification →
- **Hallucination** (behaviors tasks) — *causes*
  > Overall, we find strong evidence that accounting for weight uncertainty can improve decoding and reduce hallucinations when finetuning and pretraining from scratch, even without computational overhead. (Introduction)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *causes*
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Trustworthiness** (constructs) — *causes*
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1543.pdf)
- **UNCLE** (measurements) — *measured_by*
  > we first introduce UNCLE, a benchmark designed to evaluate uncertainty expression in both long- and short-form question answering (QA). (Abstract)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1543.pdf)

### Associated with
- **Generation diversity** (constructs)
  > “We find that improvements trend with the expressiveness of the posterior. Likely related to this, the performance of uncertainty-aware MBR is highly correlated with the prediction diversity across the combined models.”
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Knowledge awareness** (constructs)
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
- **Temporal understanding** (constructs)
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
- **Ambiguity handling** (constructs)
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
