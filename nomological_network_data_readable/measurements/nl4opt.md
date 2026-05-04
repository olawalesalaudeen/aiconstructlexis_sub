# NL4OPT
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** NL4Opt, NLP4OPT  

## State of the Field

Across the provided literature, NL4OPT (also cited as NL4Opt and NLP4OPT) is consistently used as a benchmark or dataset to evaluate a model's ability to process optimization problems described in natural language. The prevailing use of this instrument is to assess the construction of mathematical formulations from text, a task one paper refers to as 'autoformulation'. Some definitions specify that this evaluation focuses on a model's capacity for named entity recognition to "extract entity and numerical values" which are then used to build the mathematical models (OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling). One source characterizes the dataset more concretely as a "curated set of 244 linear programming problems" (Autoformulation of Mathematical Optimization Models Using LLMs). In addition to this general task, NL4OPT is also explicitly used to measure the construct of `Faithfulness`. Researchers frequently employ NL4OPT alongside other benchmarks, such as MAMO and OptiBench, to evaluate model performance on optimization modeling.

## Sources

**[OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3deb687c44d3687ace0729e5db3b4efd-Paper-Conference.pdf)**
> A benchmark that evaluates a model's ability to construct mathematical formulations from natural language questions, focusing on named entity recognition to extract entities and numerical values.

**[LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbe6dd68b0cf2b1d43b458d2b8ca31b0-Paper-Conference.pdf) (as "NL4Opt")**
> A dataset from the NL4Opt competition focused on leveraging LLMs to solve optimization problems described in natural language.

**[Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf) (as "NLP4OPT")**
> A benchmark dataset consisting of 244 linear programming problems described in natural language, used to evaluate autoformulation systems.

## Relationships

### → NL4OPT
- **Faithfulness** (constructs) — *measured_by*
  - [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf)
