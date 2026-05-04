# Chronological ordering
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Ordering, Plot unscrambling, Image ordering, Visual ordering  

## State of the Field

Across the provided literature, chronological ordering is a behavior that involves arranging a set of items into a correct temporal or logical sequence. This task is operationalized across several modalities, including reordering shuffled sentences of a text synopsis ('Plot unscrambling'), arranging a series of images ('Image ordering' or 'Visual ordering'), and identifying the correct sequence of elements within a video. The behavior is measured by various benchmarks; for instance, VNBench evaluates chronological ordering in video, MUIRBENCH assesses the ability to order images based on textual descriptions, and the 'Plot Unscrambling' task in LiveBench measures it for text. The task is commonly framed as a form of temporal reasoning, and one paper uses a version of it, 'movie synopsis unscrambling,' as a measure of natural language understanding. In the context of video analysis, one study notes that the ordering task is 'more challenging compared to the retrieving task,' while another highlights its difficulty in the visual domain, reporting that 'GPT-4o achieves only 28% and 21.5% accuracy in temporal ordering and visual ordering tasks, respectively' (MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models).

## Sources

**[LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf) (as "Plot unscrambling")**
> Reordering shuffled sentences of a plot synopsis into the original logical sequence.

**[Needle In A Video Haystack: A Scalable  Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf) (as "Ordering")**
> Identifying the correct chronological order of multiple inserted needles in a video.

**[MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf) (as "Image ordering")**
> The task of arranging a set of images into a correct temporal or logical sequence.

**[MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf) (as "Visual ordering")**
> Ordering images according to visual progression or sequence cues.

**[Episodic Memories Generation and Evaluation Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ff013b7e372ba5b790352ccd6908f03-Paper-Conference.pdf)**
> The task of arranging a set of retrieved events or states in the correct temporal sequence, from earliest to latest.

## Relationships

### Chronological ordering →
- **VNBench** (measurements) — *measured_by*
  > Utilizing VideoNIAH, we compile a video benchmark, VNBench, which includes tasks such as retrieval, ordering, and counting to evaluate three key aspects of video understanding: temporal perception, chronological ordering, and spatio-temporal coherence. (ABSTRACT)
  - [Needle In A Video Haystack: A Scalable  Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **MUIRBENCH** (measurements) — *measured_by*
  > [ORDERING] aims to evaluate the ability of models to order a series of images based on the textual description. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)

### → Chronological ordering
- **Natural language understanding** (constructs) — *measured_by*
  > “Language Comprehension: Connections word puzzles, a typo-fixing task, and a movie synopsis unscrambling task”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
