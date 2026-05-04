# Refusal
**Type:** Construct  
**Referenced in:** 12 papers  
**Also known as:** Abstention, Alignment for answerability, Irrelevance detection, Refusal capability, Over-refusal, Collaboration willingness  

## State of the Field

Across the provided literature, the construct of Refusal is predominantly framed in two distinct ways: as a model's capability to identify and abstain from answering when information is insufficient, or as a tendency to decline queries based on safety and sensitivity constraints. The most common conceptualization is the former, where refusal is defined as the ability to determine that a query cannot be answered from the provided context, such as when retrieved documents in RAG lack necessary information, a question exceeds a video's content, or no available tool can fulfill a user's intent. This capability is operationalized and measured using benchmarks including ASQA, QAMPARI, and ELI5. A separate line of work defines refusal as a model's reluctance to answer queries it deems sensitive, often as a result of safety alignment. This framing is frequently studied alongside the concept of "over-refusal," which is described as an undesirable side effect where models inappropriately reject safe and answerable prompts. A less common framing, termed "collaboration willingness," treats the construct as an agent's disposition to proactively seek help when faced with a problem. The construct is also studied in relation to Tool use.

## Sources

**[Robust Function-Calling for On-Device Language Model via Function Masking](https://proceedings.iclr.cc/paper_files/paper/2025/file/d45e0bfb5a39477d56b55c0824200008-Paper-Conference.pdf) (as "Irrelevance detection")**
> The model's ability to correctly determine when no available function or tool can satisfy the user's intent and to decline the task accordingly.

**[Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf) (as "Alignment for answerability")**
> The latent capability of a model to evaluate the relevance of user queries in relation to video content and appropriately decline to answer when questions exceed the video's informational boundaries.

**[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf) (as "Abstention")**
> The ability to identify when a question seeks information that was not provided in the interaction history and to correctly respond by indicating the information is unknown.

**[Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf)**
> The model's tendency to demonstrate reluctance or unwillingness to answer user queries, particularly those it deems sensitive or outside its designated function.

**[Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf) (as "Refusal capability")**
> The tendency of an LLM to abstain from answering when the retrieved documents do not contain sufficient information.

**[OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf) (as "Over-refusal")**
> The latent tendency of a model to refuse to answer safe and answerable prompts, often as a side effect of safety alignment, even when a helpful response is possible.

**[SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25l/guo25l.pdf) (as "Collaboration willingness")**
> The disposition of an agent to proactively seek help and engage in productive interactions with collaborators when faced with a problem.

**[POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf) (as "Overrefusal")**
> The latent tendency of a model to inappropriately refuse benign or safe user prompts due to overgeneralization of safety constraints.

## Relationships

### Refusal →
- **ASQA** (measurements) — *measured_by*
  > TRUST-ALIGN improves models' refusal capability. Across all 27 configurations, TRUST-ALIGN yields substantial improvements in F1GR. In LLaMA-3-8b, TRUST-ALIGN outperforms FRONT by 23.87% (ASQA), 47.95% (QAMPARI), and 45.72% (ELI5).
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **QAMPARI** (measurements) — *measured_by*
  > TRUST-ALIGN improves models' refusal capability. Across all 27 configurations, TRUST-ALIGN yields substantial improvements in F1GR. In LLaMA-3-8b, TRUST-ALIGN outperforms FRONT by 23.87% (ASQA), 47.95% (QAMPARI), and 45.72% (ELI5).
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **ELI5** (measurements) — *measured_by*
  > TRUST-ALIGN improves models' refusal capability. Across all 27 configurations, TRUST-ALIGN yields substantial improvements in F1GR. In LLaMA-3-8b, TRUST-ALIGN outperforms FRONT by 23.87% (ASQA), 47.95% (QAMPARI), and 45.72% (ELI5).
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)

### Associated with
- **Tool use** (behaviors tasks)
  - [Robust Function-Calling for On-Device Language Model via Function Masking](https://proceedings.iclr.cc/paper_files/paper/2025/file/d45e0bfb5a39477d56b55c0824200008-Paper-Conference.pdf)
