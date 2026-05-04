# Structured output generation
**Type:** Behavior  
**Referenced in:** 16 papers  
**Also known as:** Result formatting, Configuration generation, JSON generation, Netlist generation, Formalized representation generation, Presentation generation, Slide generation, Table generation  

## State of the Field

Across the surveyed literature, structured output generation is most commonly defined as producing text that adheres to a required format, particularly for matching API or function-call specifications. This behavior is operationalized through a variety of specific tasks, including the generation of JSON, YAML configuration files, circuit netlists, tabular summaries, and presentation slides. The emphasis is on strict conformance to a pre-defined structure, as one paper notes, "a successful function call must strictly match the format specified in the API definition" (ToolACE: Winning the Points of LLM Function Calling). To enforce these constraints, some work employs methods like constrained decoding, and the behavior is measured by benchmarks such as TACT. Structured output generation is frequently studied in the context of `Tool use`, as parseable formats are a prerequisite for many external tool interactions. Research also investigates factors affecting this capability, with one study finding that model compression "Significantly Impacts Structured Output Generation," especially for JSON formats compared to plain strings (Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression). The behavior is also examined in multi-stage processes, where a related task like `Outline generation` can produce an intermediate structure that guides the final output.

## Sources

**[ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)**
> Producing outputs in a required structured format that matches API or function-call specifications.

**[Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf) (as "Result formatting")**
> Converting solver outputs into a fixed structured output format.

**[Earley-Driven Dynamic Pruning for Efficient Structured Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25v/sun25v.pdf) (as "JSON generation")**
> The task of producing text that is a syntactically valid JSON object, often based on a natural language prompt or other input.

**[AUTOCIRCUIT-RL: Reinforcement Learning-Driven LLM for Automated Circuit Topology Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vijayaraghavan25a/vijayaraghavan25a.pdf) (as "Netlist generation")**
> Outputting a textual representation of a circuit as a list of component-to-node connections, formatted using incident encoding.

**[PINNsAgent: Automated PDE Surrogation with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wuwu25a/wuwu25a.pdf) (as "Configuration generation")**
> The task of producing structured configuration files, such as in YAML format, that specify the hyperparameters and settings for an experiment.

**[CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases inLLMs](https://aclanthology.org/2025.emnlp-main.85.pdf) (as "Formalized representation generation")**
> The production of structured, unambiguous dialogue turn representations that include speaker intention, relevant slots, and explanatory reasoning, derived from natural language utterances.

**[Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.728.pdf) (as "Presentation generation")**
> The task of automatically creating a multi-slide presentation from a source document.

**[Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.728.pdf) (as "Slide generation")**
> Producing presentation slides by iteratively applying editing actions (e.g., replace_span, replace_image) to reference slides based on input content.

**[EasyRec: Simple yet Effective Language Models for Recommendation](https://aclanthology.org/2025.emnlp-main.895.pdf) (as "Table generation")**
> Creating structured tabular summaries from scientific literature or data.

## Relationships

### Structured output generation →
- **TACT** (measurements) — *measured_by*
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Tool use** (behaviors tasks)
  > Model Compression Significantly Impacts Structured Output Generation. Our experimental results in Table 8 demonstrate significant performance variations between JSON and string format outputs under different compression techniques. The analysis reveals that model performance consistently degrades more severely when generating JSON-structured outputs compared to string formats.
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Outline generation** (behaviors tasks)
  > Guided by the presentation outline from the previous phase, slides are generated iteratively. (Section 2.3)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.728.pdf)
