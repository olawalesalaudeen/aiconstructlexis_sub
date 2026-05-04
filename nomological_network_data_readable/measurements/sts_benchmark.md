# STS-Benchmark
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** STS benchmark, STSB  

## State of the Field

Across the provided literature, STS-Benchmark is consistently used to evaluate models on semantic textual similarity or sentence similarity. The relationship data confirms it is used to measure the construct of "Semantic textual similarity", with one paper specifying its use for assessing "downstream sentence similarity performance" ("DEPT: Decoupled Embeddings for Pre-training Language Models"). There is some variation in how it is defined: one paper describes the "STS benchmark" as a broad collection of datasets including STS 2012-2016, SICK-R, and STS-B, computed by the SentEval toolkit ("ESE: Espresso Sentence Embeddings"). Other papers refer to "STS-Benchmark" or "STSB" as a specific dataset containing sentence pairs with human-annotated similarity scores on a 0-5 scale ("NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models"). The evaluation task involves models producing a numerical prediction, which one paper notes can be in the form of a text string ("Uncertainty-Aware Decoding with Minimum Bayes Risk"). Performance is then measured using Pearson correlation, according to one source ("DEPT: Decoupled Embeddings for Pre-training Language Models").

## Sources

**[ESE: Espresso Sentence Embeddings](https://proceedings.iclr.cc/paper_files/paper/2025/file/60dc26558762425a465cb0409fc3dc52-Paper-Conference.pdf) (as "STS benchmark")**
> A collection of datasets computed by the SentEval toolkit to evaluate sentence embeddings on the task of semantic textual similarity. It includes datasets like STS 2012-2016, SICK-R, and STS-B.

**[NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)**
> A benchmark for semantic textual similarity that provides sentence pairs with human-annotated similarity scores on a 0-5 scale.

**[Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf) (as "STS-B")**
> A sentence similarity benchmark used here as a scoring task where the model outputs a numerical prediction in text form.

**[DEPT: Decoupled Embeddings for Pre-training Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/20ceffa1fcec0f882868e5b891e3e7fa-Paper-Conference.pdf) (as "STSB")**
> The Semantic Textual Similarity Benchmark used to evaluate downstream sentence similarity performance after continued pre-training.
