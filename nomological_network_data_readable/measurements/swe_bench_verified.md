# SWE-Bench Verified
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** SWE-bench Verified  

## State of the Field

SWE-Bench Verified is presented in the provided literature as a benchmark dataset for automatically resolving software engineering issues, with one paper describing it as the "most popular benchmark" for this task. It is consistently defined as a curated subset of the larger SWE-Bench, containing 500 instances that have been vetted or verified by human annotators. One source specifies that this verification was performed by "professional software developers" to ensure samples have "appropriately scoped unit tests and well-specified issue descriptions" and are "non-problematic." The stated purpose of this curation, as noted in one paper, was to "improve the robustness and reliability of the evaluation." The provided data shows that SWE-Bench Verified is used as a measurement instrument to assess constructs such as `Task completion` and `Faithfulness`.

## Sources

**[Influences onLLMCalibration: A Study of Response Agreement, Loss Functions, and Prompt Styles](https://aclanthology.org/2025.acl-long.189.pdf)**
> A curated subset of 500 SWE-Bench samples that were manually verified by professional software developers to have appropriately scoped unit tests and well-specified issue descriptions.

**[Otter: Generating Tests from Issues to Validate SWE Patches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ahmed25b/ahmed25b.pdf) (as "SWE-bench Verified")**
> A benchmark dataset for automatically resolving software engineering issues, consisting of 500 instances vetted by human annotators.

## Relationships

### → SWE-Bench Verified
- **Task completion** (behaviors tasks) — *measured_by*
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
