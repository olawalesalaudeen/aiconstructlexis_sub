# Dialogue
**Type:** Behavior  
**Referenced in:** 44 papers  
**Also known as:** Multi-turn conversation, Open-ended conversation, Conversational turn-taking, Extended conversation, Speech chatting, Casual conversation, Conversation, Biomedical multimodal conversation, Conversational interaction, Multi-turn dialog  

## State of the Field

Across the surveyed literature, the dominant framing of Dialogue is as a multi-turn, interactive behavior between a model and a user, another agent, or an environment. Most definitions characterize it as a sequential exchange requiring the model to maintain context and coherence over multiple turns, as seen in terms like "multi-turn conversation" and "extended conversation." While the core concept of back-and-forth interaction is consistent, the nature of this dialogue varies; some papers describe task-oriented interactions where a user "sequentially specifies the required changes" (NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits), while others focus on "open-ended" or "casual, non-task-oriented turns" (DSG-MCTS: A Dynamic Strategy-GuidedMonteCarlo Tree Search for Diversified Reasoning in Large Language Models). A smaller set of work frames it as an interaction between models to refine a solution. Specialized forms are also discussed, such as "biomedical multimodal conversation" and "speech chatting." This behavior is most frequently operationalized and measured using the MT-Bench benchmark. Other instruments used to evaluate dialogue performance include LLaVA-Bench, MINT, Spec-Bench, ShareGPT, and TableEval. Dialogue is also studied in relation to datasets and platforms like WildChat and the LMSYS Chatbot Arena.

## Sources

**[NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf) (as "Multi-turn conversation")**
> Interacting in a chat-style format where the user sequentially specifies the required changes.

**[Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf) (as "Open-ended conversation")**
> Engaging in multi-turn, unconstrained dialogue with a user on a variety of topics.

**[CodeSteer: Symbolic-Augmented Language Models via Code/Text Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25x/chen25x.pdf) (as "Multi-turn interaction")**
> An observable pattern of engagement where a guiding model and a task-solving model interact over several rounds of prompts and responses to refine a solution.

**[Few-Shot Learning Translation from New Languages](https://aclanthology.org/2025.emnlp-main.164.pdf) (as "Conversational turn-taking")**
> Managing dialogue turns in a smooth, human-like way during interaction.

**[Voice of a Continent: MappingAfrica’s Speech Technology Frontier](https://aclanthology.org/2025.emnlp-main.560.pdf)**
> Engaging in multi-turn, coherent conversation with a user or another agent.

**[Cache-Efficient Posterior Sampling for Reinforcement Learning withLLM-Derived Priors Across Discrete and Continuous Domains](https://aclanthology.org/2025.emnlp-main.561.pdf) (as "Extended conversation")**
> The observable behavior of maintaining a coherent and contextually appropriate dialogue over many turns.

**[Towards Transferable Personality Representation Learning based on Triplet Comparisons and Its Applications](https://aclanthology.org/2025.emnlp-main.510.pdf) (as "Speech chatting")**
> The model's ability to engage in natural, coherent dialogue using speech input and output, assessed through task-based evaluations of conversational quality.

**[DSG-MCTS: A Dynamic Strategy-GuidedMonteCarlo Tree Search for Diversified Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.533.pdf) (as "Casual conversation")**
> Engaging in open-domain, non-task-oriented dialogue about everyday topics such as weather, hobbies, or daily life.

**[Recall with Reasoning: Chain-of-Thought Distillation for Mamba’s Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.236.pdf) (as "Conversation")**
> Engaging in interactive, multi-turn dialogue with a user.

**[ConsistentChat: Building Skeleton-Guided Consistent Multi-Turn Dialogues for Large Language Models from Scratch](https://aclanthology.org/2025.emnlp-main.425.pdf) (as "Biomedical multimodal conversation")**
> Engaging in a conversational exchange about biomedical topics, involving the interpretation of medical images and related text.

**[PunMemeCN: A Benchmark to Explore Vision-Language Models’ Understanding ofChinese Pun Memes](https://aclanthology.org/2025.emnlp-main.945.pdf) (as "Conversational interaction")**
> The act of participating in a multi-turn dialogue and generating responses that are judged to be of high quality.

**[Follow the Flow: Fine-grained Flowchart Attribution with Neurosymbolic Agents](https://aclanthology.org/2025.emnlp-main.1145.pdf) (as "Multi-turn dialog")**
> Engaging in a conversation that extends over multiple back-and-forth exchanges between participants.

## Relationships

### Dialogue →
- **MT-Bench** (measurements) — *measured_by*
  > "We evaluated our multi-model speculative system in SpecBench(Xia et al., 2024), across multiple tasks including multi-turn conversation, translation, summarization, question answering, mathematical reasoning, and retrieval-augmented generation, employing the MT-bench (Zheng et al., 2023)"
  - [Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf)
- **LLaVA-Bench** (measurements) — *measured_by*
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **Spec-Bench** (measurements) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **ShareGPT** (measurements) — *measured_by*
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
- **TableEval** (measurements) — *measured_by*
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf)

### Associated with
- **WildChat** (measurements)
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **HelpSteer2** (measurements)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MT-Bench** (measurements)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multi-turn dialogue** (behaviors tasks)
  - [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf)
- **LMSYS Chatbot Arena** (measurements)
  - [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf)
