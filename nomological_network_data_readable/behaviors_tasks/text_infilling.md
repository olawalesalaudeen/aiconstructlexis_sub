# Text infilling
**Type:** Behavior  
**Referenced in:** 12 papers  
**Also known as:** Code infilling, Sequence infilling, Story infilling, Antibody sequence infilling, Masked token infilling, Fill-in-the-blank completion  

## State of the Field

Across the provided literature, text infilling is most commonly defined as the task of generating text to fill a missing portion of a document given the surrounding context, such as a prefix and suffix. This behavior is positioned as a form of `conditional text generation` and is related to the broader category of `text generation`. The general task is operationalized in different ways, with one paper specifying an approach to "infill the middle 512 tokens given the first and last 256 tokens," while another mentions work on "flexible-length text infilling." To evaluate performance, papers report using datasets such as `ROCStories` and `WikiText-103`, with one study noting the use of the MAUVE score.

Beyond this general definition, the task is frequently adapted to specialized domains. These include `story infilling` for narrative completion, `code infilling` for missing lines of code, and `antibody sequence infilling` for generating amino-acid regions. A smaller set of studies uses text infilling to probe model properties. For example, some papers use it to analyze cultural adaptation by examining a model's "preference for Arab vs. Western entities as [MASK] token fillings." Another paper describes a `fill-in-the-blank completion` task designed for a localized medical context. This behavior is also described as `masked token infilling`, which is used as a proxy to evaluate the difficulty of reconstructing a full prompt.

## Sources

**[Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf) (as "Story infilling")**
> The specific infilling task of generating a coherent narrative segment to complete a story.

**[Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf) (as "Code infilling")**
> The specific infilling task of generating a missing line or block of code within an existing code snippet.

**[Glauber Generative Model: Discrete Diffusion Models via Binary Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/125be378b39b10676f56e12e6923b902-Paper-Conference.pdf)**
> The task of generating text to fill in a missing portion of a document given the surrounding context (prefix and suffix).

**[Efficient Perplexity Bound and Ratio Matching in Discrete Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/23e6f78bdec844a9f7b6c957de2aae91-Paper-Conference.pdf) (as "Sequence infilling")**
> Filling in missing parts of a sequence non-sequentially during discrete diffusion generation.

**[Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf) (as "Antibody sequence infilling")**
> Generating missing amino-acid regions in an antibody sequence given the remaining observed regions.

**[Hidden No More: Attacking and Defending Private Third-Party LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25b/thomas25b.pdf) (as "Masked token infilling")**
> The task of predicting missing tokens in a sequence given the surrounding context, used as a proxy to evaluate the difficulty of reconstructing a full prompt from a partial one.

**[Reasoning under Uncertainty: EfficientLLMInference via Unsupervised Confidence Dilution and Convergent Adaptive Sampling](https://aclanthology.org/2025.emnlp-main.1639.pdf) (as "Fill-in-the-blank completion")**
> Generating or selecting a treatment completion for a medical scenario when presented with a prompt and two candidate responses—one traditional and one allopathic.

## Relationships

### Text infilling →
- **ROCStories** (measurements) — *measured_by*
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)
- **WikiText-103** (measurements) — *measured_by*
  > Evaluation of text infilling performance using the MAUVE score (↑) with 5 prompt masks... For all methods, we use the same set of 2,000 text sequences from the validation set of WikiText-103
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)

### Associated with
- **Text generation** (behaviors tasks)
  - [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Conditional text generation** (behaviors tasks)
  > We now move on to conditional text generation, where certain tokens are provided in advance, and the task is to generate the remaining tokens. (Section 6.2)
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)
