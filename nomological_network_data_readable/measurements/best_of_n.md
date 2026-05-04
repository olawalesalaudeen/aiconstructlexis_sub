# Best-of-N
**Type:** Measurement  
**Referenced in:** 17 papers  
**Also known as:** Best-of-N sampling  

## State of the Field

Across the provided literature, Best-of-N is consistently described as a procedure involving two steps: generating multiple candidate outputs and then selecting the best one based on a scoring mechanism. Some papers define this in the context of question answering, where 'N candidate responses are generated, and the one with the highest predicted correctness score is selected' ("LaMP-QA: A Benchmark for Personalized Long-form Question Answering"), while a more general framing describes it as a 'repeated generation-and-selection procedure' for any type of candidate set ("Skeletons Matter: Dynamic Data Augmentation for Text-to-Query"). The procedure is positioned as a method for evaluating certain model traits, with papers using it to measure both `Sycophancy` and `Verification ability`. Furthermore, the application of Best-of-N is reported to influence several downstream outcomes, including `Output quality`, `Citation quality`, and `Commonsense knowledge`. The performance of systems using this procedure is, in turn, evaluated using benchmarks like `MT-Bench`. In the surveyed work, Best-of-N is framed as an 'adaptive reasoning strategy' and is studied alongside other techniques like `Majority voting` and concepts such as `Human preference alignment`.

## Sources

**[LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.61.pdf)**
> An inference procedure where N candidate responses are generated, and the one with the highest predicted correctness score is selected as the final answer.

**[Skeletons Matter: Dynamic Data Augmentation for Text-to-Query](https://aclanthology.org/2025.emnlp-main.65.pdf) (as "Best-of-N sampling")**
> A repeated generation-and-selection procedure that produces multiple candidate condensed subsets and keeps the highest-scoring one.

## Relationships

### Best-of-N →
- **Response quality** (constructs) — *causes*
  - [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ding25d/ding25d.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **Citation quality** (constructs) — *causes*
  - [SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25a/chuang25a.pdf)

### → Best-of-N
- **Sycophancy** (constructs) — *measured_by*
  - [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf)
- **Verification ability** (constructs) — *measured_by*
  - [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)

### Associated with
- **Alignment** (constructs)
  - [Theoretical guarantees on the best-of-n alignment policy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beirami25a/beirami25a.pdf)
- **Majority voting** (measurements)
  - [ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25i/lin25i.pdf)
