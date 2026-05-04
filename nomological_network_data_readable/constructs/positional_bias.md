# Positional bias
**Type:** Construct  
**Referenced in:** 59 papers  
**Also known as:** Positional Bias, Primacy bias, Recency bias, Ordering bias, Position bias, Primacy effect, Recency effect, Middle bias, Order bias, Spatial bias, Lost-in-the-middle phenomenon, Serial position effect, Thought shifting, Token shifting, Lost-in-the-middle effect  

## State of the Field

Across the surveyed literature, Positional bias is most commonly characterized as a model's tendency to process information non-uniformly based on its location within an input context. This phenomenon frequently manifests as a "lost-in-the-middle" effect or a "serial position effect," where models exhibit higher performance on information at the beginning (primacy bias) or end (recency bias) of a sequence while struggling with content in the middle. This form of bias is typically operationalized in retrieval tasks by measuring accuracy for information placed at different locations, where it can lead to observable failures like "token shifting" or deviations in reasoning called "thought shifting" (MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering). A second prevalent usage of the term describes a systematic error in evaluation, where a model's judgment is influenced by the presentation order of items rather than their content. In this context, the bias is measured by observing inconsistent outcomes in pairwise comparisons when the order of responses is swapped, or by a model's tendency to favor certain answer positions in multiple-choice questions. A smaller set of studies extends the concept to other systematic preferences, such as a "length bias" for longer responses or a "spatial bias" for specific geographic regions. The construct is studied in relation to a model's capacity for long-context understanding and information retrieval, with one paper noting that it "significantly impairs long-context comprehension and processing capabilities" (MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering).

## Sources

**[Exploring the Role of Large Language Models in Prompt Encoding for Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d68c1d10957c8d21ed9dea209533c5a4-Paper-Conference.pdf)**
> An intrinsic property of decoder-only models where the ability to comprehend and represent information degrades for tokens appearing later in a sequence, due to the causal attention mechanism.

**[Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf) (as "Recency bias")**
> A tendency for attention or retrieval to favor more recent tokens over earlier ones when both are otherwise similar.

**[From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf) (as "Primacy bias")**
> A form of positional bias where a model is more accurate at retrieving information located at the beginning of the input context.

**[RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf) (as "Positional Bias")**
> A systematic error where evaluation outcomes depend on the order of presentation rather than content quality.

**[ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf) (as "Ordering bias")**
> A tendency for performance to vary depending on the presentation order of premises or statements.

**[Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf) (as "Position bias")**
> A model's latent tendency to give disproportionate weight to information based on its position within the context window, such as favoring content at the beginning or end.

**[Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.448.pdf) (as "Primacy effect")**
> The latent tendency for a model to give greater weight to tokens presented at the beginning of a sequence, influencing later outputs due to early positional salience.

**[Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.448.pdf) (as "Recency effect")**
> The latent tendency for a model to give greater weight to recently presented tokens when generating subsequent outputs, analogous to human short-term memory recall patterns.

**[ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf) (as "Middle bias")**
> The latent tendency of the model to focus disproportionately on a subset of tokens located in the middle of the input sequence, forming a non-uniform attention pattern distinct from sink or recency effects.

**[MemeReaCon: Probing Contextual Meme Understanding in Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.177.pdf) (as "Order bias")**
> The tendency of a model to favor certain answer positions (e.g., A, B, C, D) regardless of content, indicating a vulnerability to the presentation order of options rather than genuine comprehension.

**[Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.501.pdf) (as "Spatial bias")**
> The tendency of models to systematically favor predictions in certain geographic regions—particularly high-density or well-represented urban centers—over others, reflecting uneven learning or data distribution.

**[CoMMIT: Coordinated Multimodal Instruction Tuning](https://aclanthology.org/2025.emnlp-main.583.pdf) (as "Length bias")**
> The tendency of a reward model or judge to systematically prefer longer responses, irrespective of their quality.

**[On the Emergence of Position Bias in Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ad/wu25ad.pdf) (as "Lost-in-the-middle phenomenon")**
> The observable degradation in a model's performance, particularly in retrieval tasks, when relevant information is located in the middle of the input context compared to the beginning or end.

**[Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf) (as "Serial position effect")**
> A pattern of performance in which a model is more accurate when responding to items at the beginning or end of a sequence compared to those in the middle, mirroring a well-documented cognitive bias in humans and animals.

**[MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf) (as "Token shifting")**
> The observable phenomenon where a model generates incorrect tokens at critical positions in the output sequence due to the position of the relevant input information, leading to retrieval failure.

**[MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf) (as "Thought shifting")**
> The deviation in a model's reasoning chain due to the position of relevant documents, resulting in incorrect or suboptimal reasoning paths in multi-hop tasks.

**[Composable Cross-prompt Essay Scoring by Merging Models](https://aclanthology.org/2025.emnlp-main.1241.pdf) (as "Lost-in-the-middle effect")**
> A failure mode where models underperform on information located in the middle portion of long inputs, leading to lower recall for mid-positioned content.

## Relationships

### Associated with
- **Long-context reasoning** (constructs)
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Context utilization** (constructs)
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs)
  - [On the Emergence of Position Bias in Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ad/wu25ad.pdf)
- **Information retrieval** (behaviors tasks)
  > In retrieval tasks, PB predominantly manifests as token-shifting... (Section 1)
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)
