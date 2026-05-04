# Output diversity
**Type:** Construct  
**Referenced in:** 15 papers  
**Also known as:** Response diversity  

## State of the Field

Across the provided literature, output diversity is most commonly framed as a latent tendency of language models to generate varied and non-repetitive responses to the same prompt. This variety is described along multiple dimensions, with papers frequently mentioning lexical, semantic, syntactic, and structural richness in the generated text. A more specialized definition, found in one paper, treats it as the exploration of diverse "reasoning paths" during planning to enhance problem-solving. The construct is operationalized by generating multiple responses per prompt and evaluating them with "diversity-oriented metrics," with one paper specifying the use of "average cosine similarity" among responses. Another operationalization involves generating a set number of outputs on datasets like TL;DR and HH-RLHF. A recurring theme is the challenge of balancing diversity with other objectives, such as maintaining "alignment quality" or overall response quality, with one paper noting that common metrics can bias models toward shorter outputs. Output diversity is studied alongside a broad set of concepts including `Creativity`, `Model collapse`, and `Out-of-distribution generalization`. A few papers also posit that it may influence outcomes like `Knowledge forgetting` and `Alignment tax`.

## Sources

**[Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home](https://aclanthology.org/2025.acl-long.320.pdf) (as "Response diversity")**
> An intrinsic property of a synthetic dataset measuring the semantic variety among the generated responses.

**[Marco-o1 v2: Towards Widening The Distillation Bottleneck for Reasoning Models](https://aclanthology.org/2025.acl-long.1146.pdf)**
> The latent tendency of a language model to generate varied and non-repetitive responses across different runs or completions for the same prompt, reflecting richness in lexical, syntactic, and semantic choices.

**[DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.1540.pdf) (as "Generation diversity")**
> The extent to which a model explores diverse candidate reasoning paths during planning, reducing self-bias and increasing the likelihood of finding optimal solutions.

## Relationships

### Output diversity →
- **Alignment tax** (constructs) — *causes*
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)

### → Output diversity
- **Self-correction** (behaviors tasks) — *causes*
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)

### Associated with
- **Model collapse** (constructs)
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Out-of-distribution generalization** (constructs)
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Privacy leakage** (behaviors tasks)
  - [A Probabilistic Perspective on Unlearning and Alignment for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b69bc53449ba46bb981951078929a5e-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  - [Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf)
- **Generation quality** (constructs)
  - [ImproveLLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.713.pdf)
- **Instruction following** (constructs)
  - [ImproveLLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.713.pdf)
