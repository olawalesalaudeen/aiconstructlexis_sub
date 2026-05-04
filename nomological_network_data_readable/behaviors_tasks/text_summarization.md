# Text summarization
**Type:** Behavior  
**Referenced in:** 323 papers  
**Also known as:** Summarization, Knowledge extraction, Dialog summary, Aggregation, Literature review, Document merging, Information aggregation, Abstract generation, Representative slate generation, Summary generation, Document description, Opinion summarisation, Abstract writing, Text abbreviation, Spotlight generation, Teaser generation  

## State of the Field

Across the surveyed literature, text summarization is most commonly defined as the task of creating a concise and coherent version of a longer source text. While this core definition is prevalent, a range of more specific framings also appear, such as 'dialog summary,' 'opinion summarisation,' 'literature review,' and 'abstract generation.' Some papers also describe it as 'information aggregation,' which emphasizes synthesizing information distributed across a document. The behavior is most frequently operationalized and evaluated using a set of recurring benchmarks, with the most common being XSum, CNN/DailyMail, SAMSum, and the Reddit TL;DR dataset. Other datasets used to measure summarization performance include LongBench for long-context scenarios, as well as MultiNews, GovReport, and XLSum. Performance on these tasks is assessed through various means, including automated metrics like ROUGE-L and human evaluations; one study notes that human labelers rate summaries on 'coverage,' 'accuracy,' 'coherence,' and 'overall quality' ('Chain of Hindsight aligns Language Models with Feedback'). Text summarization is frequently presented as a downstream application for models aligned with human preferences via RLHF and is studied alongside other behaviors like conditional text generation and instruction following.

## Sources

**[Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf) (as "Summarization")**
> The task of creating a concise and coherent version of a longer source text.

**[Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf) (as "Knowledge extraction")**
> Extracting essential knowledge and relevant snippets from retrieved documents to support answer generation.

**[BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf) (as "Dialog summary")**
> The task of generating a concise and accurate summary from a given conversation or dialogue.

**[CycleResearcher: Improving Automated Research via Automated Review](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a48036026dc7946ef6033ae14719cc5-Paper-Conference.pdf) (as "Literature review")**
> The process of reading and synthesizing information from a provided set of reference papers and their abstracts to understand a research background.

**[CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf) (as "Aggregation")**
> Combining information scattered throughout a document into a unified output.

**[Enhancing Graph Of Thought: Enhancing Prompts with LLM Rationales and Dynamic Temperature Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/c87245c9e8882bc1b6d4ec343d430e71-Paper-Conference.pdf) (as "Document merging")**
> The observable task of combining multiple document inputs into a single coherent output while maintaining non-redundancy.

**[MagicPIG: LSH Sampling for Efficient LLM Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d50d824ae819d5a961c1d8edc15e833-Paper-Conference.pdf) (as "Information aggregation")**
> The task of synthesizing or extracting information that is distributed broadly across the full context, rather than being localized to a few tokens.

**[Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf) (as "Abstract generation")**
> A specific text generation task where the model creates a summary or abstract of a document, such as a scientific paper, from its title.

**[Generative Social Choice: The Next Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boehmer25a/boehmer25a.pdf) (as "Representative slate generation")**
> The observable task of producing a concise set of statements that proportionally represents the full spectrum of opinions expressed in a collection of user-provided texts.

**[Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf) (as "Summary generation")**
> Producing condensed versions of input texts, evaluated for both quality and faithfulness in the summarization task.

**[Synthesizing Privacy-Preserving Text Data via Finetuning *without* Finetuning Billion-Scale LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25g/tan25g.pdf) (as "Document description")**
> The task of generating a structured or unstructured summary of a document's key attributes, such as its type, keywords, and tone.

**[VisBias: Measuring Explicit and Implicit Social Biases in Vision Language Models](https://aclanthology.org/2025.emnlp-main.909.pdf) (as "Opinion summarisation")**
> The task of generating a concise summary from a collection of texts that express various opinions on a topic, such as product reviews or political tweets.

**[POINTS-Reader: Distillation-Free Adaptation of Vision-Language Models for Document Conversion](https://aclanthology.org/2025.emnlp-main.83.pdf) (as "Abstract writing")**
> Generating a concise summary of a research topic that outlines key components such as objectives, methods, and subtopics, matching the length and scope of a human-written abstract.

**[AdaRewriter: Unleashing the Power of Prompting-based Conversational Query Reformulation via Test-Time Adaptation](https://aclanthology.org/2025.emnlp-main.194.pdf) (as "Text abbreviation")**
> The task of shortening a given text while preserving its core meaning.

**[Table-LLM-Specialist: Language Model Specialists for Tables using Iterative Fine-tuning](https://aclanthology.org/2025.emnlp-main.1796.pdf) (as "Spotlight generation")**
> Producing a concise, self-contained narrative that highlights the most engaging and insightful elements of a document to encourage deeper reader exploration.

**[Table-LLM-Specialist: Language Model Specialists for Tables using Iterative Fine-tuning](https://aclanthology.org/2025.emnlp-main.1796.pdf) (as "Teaser generation")**
> The task of crafting intriguing but vague glimpses of a document's content to entice readers without revealing substantive information.

**[AutoCast++: Enhancing World Event Prediction with Zero-shot Ranking-based Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/93f01c8d9b355d7bbe3f353b44ccde66-Paper-Conference.pdf)**
> Producing a concise summary of a longer input text, evaluated using models fine-tuned on the CNN/Daily Mail dataset.

## Relationships

### Text summarization →
- **CNN/DailyMail** (measurements) — *measured_by*
  > For TS, we utilize XSum (Narayan et al., 2018), SamSum (Gliwa et al., 2019), and the CNN/-DailyMail (See et al., 2017) dataset.
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **XSum** (measurements) — *measured_by*
  > Table 4a presents hallucination evaluation on summarization datasets XSum (Narayan et al., 2018), CNN/DM (See et al., 2017), and MultiNews (Fabbri et al., 2019). (Section 3.6)
  - [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)
- **SAMSum** (measurements) — *measured_by*
  > We further evaluate the methods on three summarization datasets. ... SAMSum (Gliwa et al., 2019) is a dataset of messenger conversations about daily-life topics, annotated with short summaries. (Section 4.1)
  - [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **Reddit TL;DR dataset** (measurements) — *measured_by*
  > We evaluate MA-RLHF on three different datasets for open-ended generation tasks: TL;DR (Stiennon et al., 2020) dataset for text summarization, Anthropic Helpful and Harmless (HH-RLHF) (Bai et al., 2022) for dialogue generation, and WebGPT Comparison (Nakano et al., 2021) for question answering.
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  > We present our main results on language modeling tasks, synthetic long-context tasks, and real-world long-context tasks... we evaluate AdaGroPE on the LongBench (Bai et al., 2024) benchmark... [which includes] Summarization... (Section 3, Table 3)
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **XLSum** (measurements) — *measured_by*
  - [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
- **TL;DR** (measurements) — *measured_by*
  > For the summarization task, we follow (Rafailov et al., 2024b) and evaluate the win rate against the base model, using GPT-4o as the judge model on 256 randomly sampled test cases from the TL;DR test set.
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
- **MultiNews** (measurements) — *measured_by*
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
- **QMSum** (measurements) — *measured_by*
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
- **GovReport** (measurements) — *measured_by*
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
- **BookSum** (measurements) — *measured_by*
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
- **Spec-Bench** (measurements) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **DialogSum** (measurements) — *measured_by*
  > For the decoding stage evaluation, we conduct experiments on two summarization benchmarks: DialogSum (Chen et al., 2021) and CNN/DM (Hermann et al., 2015) (Section 4.1).
  - [Reward Model Perspectives: Whose Opinions Do Reward Models Reward?](https://aclanthology.org/2025.emnlp-main.755.pdf)
- **MediaSum** (measurements) — *measured_by*
  - [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)
- **BERTScore** (measurements) — *measured_by*
  - [Can RLHF be More Efficient with Imperfect Reward Models? A Policy Coverage Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25o/huang25o.pdf)
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **SummEval** (measurements) — *measured_by*
  > For this task, we use the SummEval (Fabbri et al., 2021) for text summarization evaluation. (Section 4)
  - [MetaMetrics: Calibrating Metrics for Generation Tasks Using Human Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1b248453bca182b6138b8c14a75340d-Paper-Conference.pdf)
- **PubMed** (measurements) — *measured_by*
  > We further evaluate the methods on three summarization datasets. ... PubMed (Tang et al., 2023) is a collection of medical scientific articles where the goal is to summarize the conclusions of the authors... (Section 4.1)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **RULER** (measurements) — *measured_by*
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
- **TofuEval** (measurements) — *measured_by*
  - [Ethical Concern Identification inNLP: A Corpus ofACLAnthology Ethics Statements](https://aclanthology.org/2025.naacl-long.581.pdf)
- **BARTScore** (measurements) — *measured_by*
  - [A Picture is Worth A Thousand Numbers: EnablingLLMs Reason about Time Series via Visualization](https://aclanthology.org/2025.naacl-long.384.pdf)
- **AlignScore** (measurements) — *measured_by*
  - [A Picture is Worth A Thousand Numbers: EnablingLLMs Reason about Time Series via Visualization](https://aclanthology.org/2025.naacl-long.384.pdf)
- **ROUGE-L** (measurements) — *measured_by*
  - [Seq1F1B: Efficient Sequence-Level Pipeline Parallelism for Large Language Model Training](https://aclanthology.org/2025.naacl-long.455.pdf)

### → Text summarization
- **Generalization** (constructs) — *measured_by*
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Coreference resolution** (behaviors tasks) — *causes*
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Length generalization** (constructs) — *measured_by*
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)

### Associated with
- **Reasoning** (constructs)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Instruction following** (constructs)
  > Weaker instruction-following at 128k length. For summarization tasks, the summaries generated by Llama-3.1-70B-Instruct at 128k tokens become longer and often contain details not present in the reference. (Section 7.1)
  - [Can We Further Elicit Reasoning inLLMs? Critic-Guided Planning with Retrieval-Augmentation for Solving Challenging Tasks](https://aclanthology.org/2025.acl-long.1245.pdf)
- **Faithfulness** (constructs)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Prompt understanding** (constructs)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
- **Hallucination detection** (behaviors tasks)
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **Conditional text generation** (behaviors tasks)
  > This issue arises in typical conditional text generation tasks, such as text summarization and data-to-text generation, where the goal is to produce fluent text based on contextual input. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Long-context understanding** (constructs)
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **Verbosity** (constructs)
  - [L3Ms — Lagrange Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/92d3d2a9801211ca3693ccb2faa1316f-Paper-Conference.pdf)
- **Adaptability** (constructs)
  - [AesBiasBench: Evaluating Bias and Alignment in Multimodal Language Models for Personalized Image Aesthetic Assessment](https://aclanthology.org/2025.emnlp-main.387.pdf)
- **In-context learning** (constructs)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **Task execution** (constructs)
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
- **Fairness** (constructs)
  - [VisBias: Measuring Explicit and Implicit Social Biases in Vision Language Models](https://aclanthology.org/2025.emnlp-main.909.pdf)
