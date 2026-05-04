# Creative writing
**Type:** Behavior  
**Referenced in:** 26 papers  
**Also known as:** Story generation, Personalized story generation, Poetry generation, Keyword-based story generation, Constrained story generation, Narrative generation, Story writing  

## State of the Field

Across the provided literature, creative writing is predominantly framed as the task of generating novel and imaginative text, most commonly stories, in response to a prompt. Several papers specify different facets of this behavior, including poetry generation, which is described as a "popular generation task," and various forms of narrative generation. These variations include personalized story generation tailored to user factors like gender or ethnicity, keyword-based generation for incorporating specific terms, and constrained story generation, which tests adherence to an increasing number of rules. One paper describes narrative generation as a "long-form writing task" that involves "complex reasoning and composition tasks." To operationalize and measure this behavior, researchers use instruments such as StoryCloze and AlpacaEval 2.0. The CS4 benchmark is also mentioned for specifically assessing constrained story generation. The behavior is studied in relation to the construct of Creativity and is also used as a task to measure a model's Commonsense knowledge.

## Sources

**[Modeling the Evolution ofEnglish Noun Compounds with Feature-Rich Diachronic Compositionality Prediction](https://aclanthology.org/2025.acl-long.985.pdf) (as "Story generation")**
> The observable task of producing a narrative text in response to a prompt.

**[TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1091.pdf)**
> Generating novel and imaginative text, such as stories, blog posts, or scripts, based on a given prompt.

**[Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment inLLMs](https://aclanthology.org/2025.emnlp-main.3.pdf) (as "Personalized story generation")**
> The task of generating a narrative tailored to specific user-provided factors, such as a child's gender, nationality, or ethnicity.

**[Statistical and Neural Methods forHawaiian Orthography Modernization](https://aclanthology.org/2025.emnlp-main.1783.pdf) (as "Poetry generation")**
> The task of producing new poems, which is a popular generation task for large language models.

**[Judging Quality Across Languages: A Multilingual Approach to Pretraining Data Filtering with Language Models](https://aclanthology.org/2025.emnlp-main.450.pdf) (as "Keyword-based story generation")**
> Generating coherent narratives that incorporate specified keywords at arbitrary positions in the sequence.

**[LM-Searcher: Cross-domain Neural Architecture Search withLLMs via Unified Numerical Encoding](https://aclanthology.org/2025.emnlp-main.479.pdf) (as "Constrained story generation")**
> The observable task of generating a coherent short story that adheres to an increasing number of specific constraints provided in the prompt.

**[Personality Vector: Modulating Personality of Large Language Models by Model Merging](https://aclanthology.org/2025.emnlp-main.1254.pdf) (as "Narrative generation")**
> The task of creating fictional stories or narratives, which involves complex reasoning about plot, characters, and setting.

**[Proactive Hearing Assistants that Isolate Egocentric Conversations](https://aclanthology.org/2025.emnlp-main.1290.pdf) (as "Story writing")**
> The specific task of generating a narrative or story, typically based on a given prompt or theme.

## Relationships

### Creative writing →
- **StoryCloze** (measurements) — *measured_by*
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)

### → Creative writing
- **Instruction following** (constructs) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)

### Associated with
- **Creativity** (constructs)
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
