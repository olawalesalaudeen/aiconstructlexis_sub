# Query rewriting
**Type:** Behavior  
**Referenced in:** 12 papers  
**Also known as:** Query rephrasing, Prompt rewriting, Prompt polishing  

## State of the Field

Across the provided literature, query rewriting is a behavior where a user's input, referred to as a "query" or "prompt," is modified, typically by a large language model. The definitions vary in their stated goals, but a common framing is the transformation of an input to make it more effective for a downstream system. For instance, some papers define it as a process to "align with the ground truth schema semantically" for improved retrieval or to convert a natural language description into a more structured prompt for a generative model. Other definitions focus on enriching the input by adding "visual details, stylistic elements, and aesthetic expectations" or modifying it based on a "specified constraint, such as an aspect and value." A related task, termed "prompt polishing," aims to clean up user inputs by removing "stylistic biases, platform-specific keywords, and conflicting information." The operationalization of this behavior consistently involves the use of LLMs, with papers citing models like GPT-3.5-turbo and GPT-4 for the task. This behavior is reported to be influenced by in-context learning and commonsense knowledge, and it is used to affect downstream image generation. It is also studied alongside other approaches to disambiguation.

## Sources

**[Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf) (as "Query rephrasing")**
> The task of rewriting a user's search query, typically using an LLM, to enrich it with additional visual details, stylistic elements, and aesthetic expectations.

**[Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The task of modifying a given user query based on a specified constraint, such as an aspect and value.

**[AP-Adapter: Improving Generalization of Automatic Prompts on Unseen Text-to-Image Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf) (as "Prompt rewriting")**
> The task of transforming a natural language description into a more effective, structured prompt (e.g., a keyword-based prompt) for a generative model.

**[Multimodal Large Language Models Make Text-to-Image Generative Models Align Better](https://proceedings.neurips.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf) (as "Prompt polishing")**
> The task of rewriting user-written text prompts to remove stylistic biases, platform-specific keywords, and conflicting information.

## Relationships

### Query rewriting →
- **Image generation** (behaviors tasks) — *causes*
  - [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf)

### → Query rewriting
- **Commonsense knowledge** (constructs) — *causes*
  - [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf)

### Associated with
- **Disambiguation** (constructs)
  > we argue existing disambiguation works fall in three major policies... Query Rewriting, Middle. Long Form Answer Generation, Right. Asking Clarifying Questions. (Section 3, Figure 2)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-OnlyLLMs](https://aclanthology.org/2025.emnlp-main.482.pdf)
