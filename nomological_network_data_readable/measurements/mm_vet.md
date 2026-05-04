# MM-Vet
**Type:** Measurement  
**Referenced in:** 55 papers  
**Also known as:** MM-VET  

## State of the Field

MM-Vet is most commonly characterized as an evaluation benchmark for multimodal models, with a prevailing focus on assessing visual reasoning and understanding across diverse scenarios. A less frequent definition describes its purpose more broadly as evaluating the "multimodal perception and cognition abilities" of MLLMs. Across the provided literature, MM-Vet is widely used to measure `visual understanding`, `multimodal understanding`, and `visual question answering`. Some papers also report its use for evaluating `text generation` through open-ended Q&A and, in one instance, for assessing `visual hallucination`. The benchmark is described as containing "challenging open-ended tasks" that require models to integrate multiple capabilities simultaneously, including recognition, OCR, spatial reasoning, and world knowledge. A distinctive feature mentioned in the sources is its evaluation methodology, where, as one paper notes, "performance is evaluated by GPT-4 through a comparative analysis of predicted and ground truth answers." Several studies specify that they use MM-Vet for zero-shot evaluation to assess performance on "complex multimodal tasks."

## Sources

**[DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf)**
> Evaluation benchmark for multimodal models focusing on visual reasoning and understanding across diverse scenarios.

**[Feast Your Eyes:  Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf) (as "MM-VET")**
> A benchmark used to evaluate the multimodal perception and cognition abilities of MLLMs.

## Relationships

### → MM-Vet
- **Visual understanding** (constructs) — *measured_by*
  > “MM-Vet examines MLLMs on complicated multimodal reasoning tasks with open-ended Q&A. It focuses on the integration of different core vision-language capabilities, including general visual recognition”
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > Additionally, we conducted a zero-shot evaluation on the recently developed benchmarks of MMBench and MM-Vet to assess the model’s performance in complex multimodal tasks. (Section 4.1)
  - [DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > ...we also evaluate MIRAGE on conventional VQA tasks, including the RetVQA multi-image QA (Penamakuri et al., 2023) and several single-image QA tasks, such as VQA-v2 (Goyal et al., 2017), GQA (Hudson & Manning, 2019), TextVQA (Singh et al., 2019), POPE (Li et al., 2023c), MMB (Liu et al., 2024c), MMB-CN (Liu et al., 2024c), MME (Fu et al., 2023), SEED-Bench (Li et al., 2023a), and MM-Vet (Yu et al., 2023b). (Section 5)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Visual dialogue** (behaviors tasks) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **Spatial understanding** (constructs) — *measured_by*
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
- **Knowledge** (constructs) — *measured_by*
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > MM-Vet (Yu et al., 2024b) examines MLLMs on complicated multimodal reasoning tasks with open-ended Q&A. (Section 4.2.2)
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **Visual hallucination** (behaviors tasks) — *measured_by*
  > “The MLLM-specific benchmarks are POPE Li et al. (2023c), MME Fu et al. (2023), MMB Liu et al. (2023d), SEED Li et al. (2023a) and MM-Vet Yu et al. (2023). Compared to common VL evaluations, these benchmarks aim to evaluate MLLMs from various aspects, such as fine-grained reasoning and visual hallucination.”
  - [Routing Experts: Learning to Route Dynamic Experts in Existing Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49a4829a2ccaaa4706cc82e68c39a9c6-Paper-Conference.pdf)
