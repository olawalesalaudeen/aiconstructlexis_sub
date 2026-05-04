# Android-in-the-Wild
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** Android-in-the-Wild (AitW), AITW  

## State of the Field

Across the provided literature, Android-in-the-Wild (AitW) is consistently framed as a large-scale, open-source dataset or benchmark for mobile device control. Its most common application is the evaluation of agents, specifically "Android device control agents" or "mobile GUI agents," with some work also noting its use as a static, offline dataset for fine-tuning. The dataset is defined as containing "diverse natural language instructions" and corresponding "operation trajectories," with one paper quantifying its scale at "30K instructions and 715K corresponding operation trajectories." While most descriptions are general, one paper specifies that it includes subsets like 'General' and 'Web Shopping,' and another characterizes it as being for tasks that lack UI trees and require OCR. According to the available data, agent performance on this benchmark is measured by Task success. AitW is also used as a point of comparison and is described in one source as the largest UI control dataset to date.

## Sources

**[DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf) (as "Android-in-the-Wild (AitW)")**
> A large-scale dataset for evaluating Android device control agents, featuring diverse natural language instructions across subsets like 'General' and 'Web Shopping'.

**[On the Effects of Data Scale on UI Control Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/a79f3ef3b445fd4659f44648f7ea8ffd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "AitW")**
> Android in the Wild, a large-scale dataset for Android device control, used as a point of comparison.

**[Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf) (as "AITW")**
> Android In The Wild, a mobile navigation benchmark with instructions and operation trajectories for evaluating mobile GUI agents.

**[Lightweight Neural App Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/b81266057eb3d96469940d1860a41ad2-Paper-Conference.pdf)**
> An open-source dataset for mobile control tasks lacking UI trees, requiring OCR extraction.

## Relationships

### Android-in-the-Wild →
- **Task completion** (behaviors tasks) — *measured_by*
  - [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf)
