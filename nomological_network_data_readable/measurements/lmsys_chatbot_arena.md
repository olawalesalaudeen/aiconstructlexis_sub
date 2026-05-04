# LMSYS Chatbot Arena
**Type:** Measurement  
**Referenced in:** 76 papers  
**Also known as:** ChatBot Arena, Chatbot Arena, CHATBOT ARENA, ChatArena, Chatarena, LLM Arena, LMsys arena, ChatbotArena, LM Arena  

## State of the Field

LMSYS Chatbot Arena is predominantly described across the literature as a crowdsourced evaluation platform that ranks language models through pairwise comparisons. The most common operationalization involves users engaging in open-ended conversational tasks with two anonymous models and voting for the preferred response, with these human judgments aggregated to produce a public ELO-based ranking. Papers use this instrument to measure several constructs, most frequently conversational ability and human preference alignment, as well as faithfulness and general capabilities. While primarily framed as a live evaluation platform, a subset of papers also treats it as a static, human-labeled dataset of user-assistant interactions and preference judgments, which can serve as a "ground-truth reference" for other evaluations ("TrimLLM: Progressive Layer Dropping for Domain-SpecificLLMs"). A smaller number of sources describe a related methodology where LLMs themselves are used as judges to simulate human preferences. The platform's application is also noted for evaluating multimodal models, and its rankings are studied alongside other benchmarks like WildBench and LiveBench.

## Sources

**[StackEval: Benchmarking LLMs in Coding Assistance](https://proceedings.neurips.cc/paper_files/paper/2024/file/4126a607bbe2836cb6ca0eb45b75618b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "ChatBot Arena")**
> An evaluation framework that uses LLMs to judge model responses, often through pairwise comparisons.

**[Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf) (as "ChatArena")**
> An evaluation set of real-world user-assistant interactions used for pairwise preference evaluation.

**[A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf) (as "Chatbot Arena")**
> A crowdsourced evaluation platform where LLMs are evaluated through millions of pairwise comparisons based on human judgments in open-ended conversational tasks.

**[RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf) (as "CHATBOT ARENA")**
> A crowdsourcing platform where users compare outputs from two anonymous models side-by-side to vote for the better response, generating a public ELO ranking.

**[TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf) (as "Chatarena")**
> A diverse, human-labeled dataset encompassing multiple language pairs used for comparative alignment analysis.

**[RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf) (as "LLM Arena")**
> A public evaluation platform where language models compete in anonymous, randomized battles, with user votes determining the rankings.

**[MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/461f1fd5f92e5ca95764a88304dc39f7-Paper-Conference.pdf) (as "LMsys arena")**
> A benchmark platform that uses user voting and Elo-ranking to evaluate multimodal models.

**[Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf) (as "ChatbotArena")**
> An LLM evaluation platform and leaderboard where models are ranked based on pairwise comparisons from anonymous, crowdsourced human votes.

**[Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sculley25a/sculley25a.pdf) (as "LM Arena")**
> A community-driven benchmark, also known as LMSYS Chatbot Arena, that collects a fresh source of novel test questions and human preference votes from users in head-to-head matchups between LLMs.

**[BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf)**
> A crowdsourced evaluation platform where users chat with two anonymous language models and vote for the one they prefer, creating a large-scale human preference dataset.

## Relationships

### LMSYS Chatbot Arena →
- **Human preference alignment** (constructs) — *measured_by*
  - [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf)
- **WildBench** (measurements) — *correlates*
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **LiveBench** (measurements) — *correlates*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)

### → LMSYS Chatbot Arena
- **Conversational ability** (constructs) — *measured_by*
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
- **Arena-Hard-Auto** (measurements) — *correlates*
  - [From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Re-evaluating Open-ended Evaluation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/57a009897ab00e2d811a4581ad1f7239-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  > “An emerging trend in LLM evaluation is therefore to rely on open-ended evaluation systems, a notable example being the LMSYS Chatbot Arena”
  - [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf)

### Associated with
- **Dialogue** (behaviors tasks)
  - [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf)
