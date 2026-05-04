# ToxiGen
**Type:** Measurement  
**Referenced in:** 24 papers  
**Also known as:** Toxigen, TOXIGEN  

## State of the Field

Across the provided literature, ToxiGen is consistently characterized as a benchmark for evaluating toxicity in language models. It is most frequently used to operationalize and measure the constructs of `Harmlessness` and `Safety`, with a smaller set of studies also employing it to assess `Harmful content generation` and `Hate speech detection`. Several papers describe its composition as a synthetic, machine-generated dataset containing both toxic and neutral prompts designed to evaluate a model's ability to avoid generating toxic content. A recurring detail is its focus on demographic diversity, with two sources specifying that its toxic contexts target 13 minority or demographic groups. One paper provides a specific scale, stating it 'comprises approximately 274k machine-generated statements, evenly split between toxic and non-toxic language' (How to Protect Yourself from 5GRadiation? InvestigatingLLMResponses to Implicit Misinformation). The benchmark is often situated within larger evaluation suites, such as LLM Harness and TÜLU-2, and is frequently studied alongside REALTOXICITYPROMPTS.

## Sources

**[Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)**
> A toxicity benchmark for evaluating toxic versus neutral generation behavior.

**[Self-Boosting Large Language Models with  Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf) (as "Toxigen")**
> Toxigen, a benchmark used in LLM Harness for toxicity evaluation.

**[ManaTTSPersian: a recipe for creatingTTSdatasets for lower resource languages](https://aclanthology.org/2025.naacl-long.465.pdf) (as "TOXIGEN")**
> Benchmark for detecting toxic language generation, used to assess whether fine-tuning increases harmful output tendencies.

## Relationships

### → ToxiGen
- **Harmlessness** (constructs) — *measured_by*
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > We evaluate the effect of detoxification using various techniques on Toxigen and Real Toxicity Prompts dataset (Section 5.3).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **Hate speech detection** (behaviors tasks) — *measured_by*
  - [ImpScore: A Learnable Metric For Quantifying The Implicitness Level of Sentences](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd6bb13e78da078d8adcabbe6d9ca737-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > For the open-ended generation tasks, we apply SADI on TriviaQA (Joshi et al., 2017), TruthfulQA (Lin et al., 2022), ToxiGen (Hartvigsen et al., 2022) datasets. (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
