# Conversational question answering
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Interactive question answering, Multi-turn QA, Multi-turn question answering, Dialogue question answering  

## State of the Field

Across the surveyed literature, conversational question answering is predominantly described as a multi-turn behavior where a model generates responses to a user's questions within a dialogue. A recurring theme is the necessity of using the conversation history as context, with one paper noting, "Answering the current question needs to consider the context of conversation histories" (A Multi-Agent Framework with Automated Decision Rule Optimization for Cross-Domain Misinformation Detection). While terms like "Multi-turn QA" and "Dialogue question answering" are also used, the core concept of a multi-round interaction is consistent. Some definitions add specific constraints, framing the questions as being "not simple factoids" and grounded in particular contexts like scientific documents, videos, or stories. A less common framing describes it as an "interactive" process involving "a series of questions and clarifications to arrive at an answer for a complex initial query" (IQA-EVAL: Automatic Evaluation of Human-Model Interactive Question Answering). This behavior is operationalized and measured using several benchmarks. The most frequently cited instrument is CoQA, which is used to evaluate "dialogue-based question-answering systems." Other benchmarks mentioned for assessing this behavior include ChatRAG-Bench for RAG-based tasks and MT-Bench for challenging multi-turn questions.

## Sources

**[cPAPERS: A Dataset of Situated and Multimodal Interactive Conversations in Scientific Papers](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a19a9d527ed544d1272f07b0f8f934e-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Generating a natural language response to a user's question in a conversational context, where the questions are not simple factoids but part of a dialogue.

**[IQA-EVAL: Automatic Evaluation of Human-Model Interactive Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a23b26eaaefd187973658f5001f4fe-Paper-Conference.pdf) (as "Interactive question answering")**
> A multi-turn process where a user interacts with an AI model through a series of questions and clarifications to arrive at an answer for a complex initial query.

**[SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf) (as "Multi-turn QA")**
> Engaging in multi-round question-answer dialogue about a video, including questions about content, timing, and action sequences.

**[Backtracking Improves Generation Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/65beb73449888fabcf601b3a3ef4b3a7-Paper-Conference.pdf) (as "Multi-turn question answering")**
> The behavior of engaging in a conversational dialogue over several turns to answer a user's questions.

**[HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf) (as "Dialogue question answering")**
> Answering questions grounded in conversational or story-based dialogue context.

## Relationships

### Conversational question answering →
- **CoQA** (measurements) — *measured_by*
  > “Conversational Q&A (CoQA) (Reddy et al., 2019): Short-answer questions based on conversational text.”
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
- **ChatRAG-Bench** (measurements) — *measured_by*
  > the RAG benchmark for conversational QA tasks within a 4K context window. (Section 1)
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
