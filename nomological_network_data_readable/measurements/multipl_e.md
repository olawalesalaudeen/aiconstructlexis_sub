# MultiPL-E
**Type:** Measurement  
**Referenced in:** 14 papers  
**Also known as:** Multipl-E, MULTIPL-E  

## State of the Field

Across the provided literature, MultiPL-E is consistently described as a benchmark for evaluating multilingual code generation. Its construction is almost universally defined as a translation of the Python-based benchmarks HumanEval and MBPP into multiple other programming languages, with several sources specifying as many as 18. Consequently, papers use MultiPL-E to operationalize and measure the `Code generation` ability of large language models, frequently referring to this as assessing "multi-lingual coding capabilities." One paper describes it as the "first multi-language parallel benchmark for text-to-code generation." In practice, studies use the benchmark to conduct evaluations across a subset of its available languages, such as five or eight, often reporting performance using `pass@k` metrics. While the prevailing usage is for general multilingual code assessment, a smaller line of work uses it for more specific analyses, such as evaluating changes in `pass@100` performance.

## Sources

**[Batched Low-Rank Adaptation of Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/66247b78cb1aa7259dcf856a18c9e294-Paper-Conference.pdf)**
> MultiPL-E is a benchmark for evaluating multilingual code generation by translating the HumanEval and MBPP benchmarks into many programming languages.

**[ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding](https://proceedings.iclr.cc/paper_files/paper/2025/file/23ff02034404b65776080cbf7148addd-Paper-Conference.pdf) (as "Multipl-E")**
> A benchmark for evaluating the multilingual code generation capabilities of models by translating HumanEval problems into multiple programming languages.

**[Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf) (as "MULTIPL-E")**
> A benchmark used to evaluate programming language masking and pass@100 metric changes across languages.

## Relationships

### → MultiPL-E
- **Code generation** (behaviors tasks) — *measured_by*
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Batched Low-Rank Adaptation of Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/66247b78cb1aa7259dcf856a18c9e294-Paper-Conference.pdf)
- **Code completion** (behaviors tasks) — *measured_by*
  - [ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding](https://proceedings.iclr.cc/paper_files/paper/2025/file/23ff02034404b65776080cbf7148addd-Paper-Conference.pdf)

### Associated with
- **HumanEval** (measurements)
  > "MultiPL-E (Cassano et al., 2023) is the first multi-language parallel benchmark for text-to-code generation. It extends HumanEval and MBPP (Austin et al., 2021) to support 18 programming languages."
  - [ReMedy: Learning Machine Translation Evaluation from Human Preferences with Reward Modeling](https://aclanthology.org/2025.emnlp-main.218.pdf)
