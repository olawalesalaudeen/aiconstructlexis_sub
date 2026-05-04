# WildBench
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** Wildbench, Wild-Bench  

## State of the Field

WildBench is predominantly characterized as a benchmark for evaluating the instruction-following capabilities of large language models, often used alongside other evaluation suites like AlpacaEval and MT-Bench. The provided literature consistently describes it as a challenging benchmark featuring "long, multi-turn prompts" and "difficult questions sourced from real users." The evaluation methodology is frequently described as subjective, often employing an "LLM-as-a-judge" system, with some papers noting a "fine-grained grading scale" and a specific "WB-Score" to quantify performance. A less common framing describes it simply as a "public dataset of model comparisons." Papers use WildBench to measure a broad set of abilities, including conversational ability, question answering, commonsense knowledge, and long-context understanding. The tasks within the benchmark are reported to require higher-order skills such as creativity, planning, data analysis, role-playing, and domain knowledge.

## Sources

**[Instruct-SkillMix: A Powerful Pipeline for LLM Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)**
> An instruction-following benchmark that uses a diverse distribution of task categories and a fine-grained grading scale to evaluate model responses against a reference answer.

**[Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf) (as "Wildbench")**
> An LLM-based evaluation framework used as a public dataset of model comparisons judged by an LLM-based judge.

**[As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf) (as "Wild-Bench")**
> A challenging instruction-following QA benchmark featuring long, multi-turn prompts and difficult questions sourced from real users.

## Relationships

### → WildBench
- **Conversational ability** (constructs) — *measured_by*
  > In this section we evaluate the Jamba-1.5 models on two chatbot scenarios: Arena-Hard (Li et al., 2024b), a set of 500 challenging user queries that uses GPT4-Turbo as a judge, and WildBench (Lin et al., 2024)... (Section 7.3)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Instruct-SkillMix: A Powerful Pipeline for LLM Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)
- **Planning** (constructs) — *measured_by*
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Creativity** (constructs) — *measured_by*
  > “The tasks in WILDBENCH typically demand higher-order reasoning, such as writing and/or debugging code with specific constraints, creative writing with multiple constraints on the style and content”
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Domain knowledge** (constructs) — *measured_by*
  > “The tasks in WILDBENCH typically demand higher-order reasoning, such as writing and/or debugging code with specific constraints, creative writing with multiple constraints on the style and content, or designing a software system with complex requirements. These tasks often require critical thinking, creativity, and technical expertise”
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **LMSYS Chatbot Arena** (measurements) — *correlates*
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Data analysis** (behaviors tasks) — *measured_by*
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Role-playing** (behaviors tasks) — *measured_by*
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf)
