# MiniWoB++
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** MiniWob  

## State of the Field

Across the provided literature, MiniWoB++ is consistently described as a standard benchmark suite for evaluating autonomous computer control agents. Papers use this instrument to measure agent capabilities in `Web navigation` and, in one instance, `Adaptability`. The benchmark is most commonly defined as a simulated environment where agents must perform tasks based on natural language instructions, which range from primitive actions to complex multi-step decision making. The prevailing characterization describes the tasks as taking place in a 'simulated web environment' (Multimodal Web Navigation with Instruction-Finetuned Foundation Models) or on 'minimalist web interfaces' (OpenHands: An Open Platform for AI Software Developers as Generalist Agents). However, a related definition for 'MiniWob' describes it as a benchmark of 'open-ended tasks in real web environments' (Grounding Multimodal Large Language Model in GUI World), suggesting some variation in how the environment is framed. The number of tasks is specified differently across sources, with one paper mentioning '56 simulated tasks' and another noting tasks are initialized on '125 different minimalist web interfaces'. Ultimately, the benchmark is positioned as a tool for assessing agents on tasks that simulate 'real-world human-computer interactions' (A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis).

## Sources

**[A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)**
> A standard benchmark suite for computer control agents, integrating diverse tasks that simulate real-world human-computer interactions in a simplified web environment.

**[Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf) (as "MiniWob")**
> A web navigation benchmark of open-ended tasks in real web environments that evaluates agents on instruction-following and action execution.

## Relationships

### → MiniWoB++
- **Web navigation** (behaviors tasks) — *measured_by*
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **Adaptability** (constructs) — *measured_by*
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
