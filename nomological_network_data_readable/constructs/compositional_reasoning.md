# Compositional reasoning
**Type:** Construct  
**Referenced in:** 41 papers  
**Also known as:** Function composition  

## State of the Field

Across the surveyed literature, compositional reasoning is predominantly framed in two ways. The most prevalent definition describes it as the ability to understand and reason about novel combinations of familiar components, such as combining visual entities and their relationships to understand a scene. A second, frequently occurring framing treats it as a problem-solving process involving the decomposition of complex tasks or questions into simpler sub-problems whose solutions are then integrated. Several papers characterize this ability as a "persistent weakness" or a challenging area for current foundation models, particularly in vision-language and audio-language domains ("Read to Hear...", "CompA..."). This construct is operationalized through a variety of measurement instruments. In vision-language contexts, it is commonly assessed using image-text matching benchmarks like WINOGROUND and CoLA, as well as visual question answering datasets such as GQA. For code-related tasks, BigCodeBench is used to evaluate the composition of function call sequences. The construct is studied alongside Chain-of-thought reasoning and Complex reasoning, and one paper suggests that In-context learning can enable it.

## Sources

**[CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)**
> The ability to understand and reason about novel combinations of familiar components, such as recognizing an action composed of a known verb, subject, and object in a new configuration.

**[Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf) (as "Function composition")**
> Applying a sequence of simple functions to an input and returning the resulting transformed output.

## Relationships

### Compositional reasoning →
- **WINOGROUND** (measurements) — *measured_by*
  > "We evaluate the compositional capabilities of CECE in three different tasks. 1) Image-text matching evaluation through binary retrieval tasks... We report results on two benchmarks (Winoground (Thrush et al., 2022), EqBen (Wang et al., 2023b))"
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **CoLA** (measurements) — *measured_by*
  > We first evaluate our CoVLM on compositional reasoning tasks, including... matching the correct captions describing the relation between two images with similar entities (Cola, (Ray et al., 2023))... (Section 4.1)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **SugarCrepe** (measurements) — *measured_by*
  - [TripletCLIP:  Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
- **MMVP** (measurements) — *measured_by*
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **CREPE** (measurements) — *measured_by*
  - [ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BigCodeBench** (measurements) — *measured_by*
  > BigCodeBench frequently invokes a sequence of function calls from multiple libraries to solve a single task, requiring significant compositional reasoning ability for task-solving. (Section 3)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **FreshQA** (measurements) — *measured_by*
  - [ConMeC: A Dataset for Metonymy Resolution with Common Nouns](https://aclanthology.org/2025.naacl-long.331.pdf)
- **GQA** (measurements) — *measured_by*
  > GQA (Hudson and Manning, 2019) for compositional reasoning and real-world visual understanding (Section 4.1).
  - [Matter-of-Fact: A Benchmark for Verifying the Feasibility of Literature-Supported Claims in Materials Science](https://aclanthology.org/2025.emnlp-main.204.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > "Traces were rated to assess references to low-level cues (fine-grained), information cross-referenced across steps (compositional), relevant evidence (comprehensive), correctness of modality tags, and validity of reasoning"
  - [Definition Generation for Word Meaning Modeling: Monolingual, Multilingual, and Cross-Lingual Perspectives](https://aclanthology.org/2025.emnlp-main.1322.pdf)
- **Bamboogle** (measurements) — *measured_by*
  > Bamboogle (Press et al., 2023) includes complex questions that Google answers incorrectly, assessing compositional reasoning. (Section 4.1)
  - [CLIP-MoE: Towards Building Mixture of Experts forCLIPwith Diversified Multiplet Upcycling](https://aclanthology.org/2025.emnlp-main.276.pdf)
- **NExTQA** (measurements) — *measured_by*
  - [MedFact: A Large-scaleChinese Dataset for Evidence-based Medical Fact-checking ofLLMResponses](https://aclanthology.org/2025.emnlp-main.1647.pdf)

### → Compositional reasoning
- **In-context learning** (constructs) — *causes*
  > Our findings demonstrate that few-shot Chain-of-Thought prompting enables Transformers to perform compositional reasoning on FTCT by revealing correct combinations of fragments, even if such combinations were absent in training data. (ABSTRACT)
  - [Are Transformers Able to Reason by Connecting Separated Knowledge in Training Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/476c9ac41c967332dd28fb844e166b34-Paper-Conference.pdf)

### Associated with
- **GQA** (measurements)
  > The GQA problems are more complex and require compositional reasoning to answer
  - [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Teaching Arithmetic to Small Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [Limits of Deep Learning: Sequence Modeling through the Lens of Complexity Theory](https://proceedings.iclr.cc/paper_files/paper/2025/file/62868cc2fc1eb5cdf321d05b4b88510c-Paper-Conference.pdf)
- **Code editing** (behaviors tasks)
  > Unlike isolated function-level edits, multi-file refactoring requires comprehensive reasoning and composition of multiple smaller changes. (Section 1)
  - [RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b44ee74539ea77d6a0d50d468724371-Paper-Conference.pdf)
- **Tool use** (behaviors tasks)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  > In many compositional reasoning tasks, interactions are key and marginal attributions are insufficient. We illustrate this using an image of a dog playing with a basketball and prompting the LLaVA-NeXT-Mistral-7B model (Liu et al., 2023) with “What is shown in this image?”. (Sec. 7.2)
  - [SPEX: Scaling Feature Interaction Explanations for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kang25a/kang25a.pdf)
