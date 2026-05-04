# NExTQA
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** NextQA  

## State of the Field

Across the provided literature, NExTQA is consistently characterized as a benchmark for video question answering. The definitions from multiple papers converge on its primary purpose: to evaluate a model's ability to understand causal and temporal dynamics within videos. This focus on assessing causal and temporal reasoning is the most prevalent description of the instrument's function. One paper further specifies that the benchmark "focuses on short videos" ("Frame-Voyager: Learning to Query Frames for Video Large Language Models"). While its use for measuring video question answering is widely cited, single papers also state that it is used to measure broader capabilities such as video understanding and compositional reasoning. It is frequently listed alongside other video QA benchmarks, positioning it as a widely-adopted evaluation tool in this domain.

## Sources

**[Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)**
> Temporal reasoning benchmark for video question answering, requiring models to understand causal and temporal dynamics in videos.

**[Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf) (as "NextQA")**
> A video question answering benchmark that focuses on short videos and assesses causal and temporal reasoning.

## Relationships

### → NExTQA
- **Video question answering** (behaviors tasks) — *measured_by*
  > We evaluate Emu on a broad range of vision-language tasks including image captioning (MS-COCO (Chen et al., 2015)), image question answering (VQAv2 (Goyal et al., 2017), OKVQA (Marino et al., 2019), VizWiz (Gurari et al., 2018)), visual dialog (VisDial (Das et al., 2017)), video question answering (MSRVTTQA (Xu et al., 2017), MSVDQA (Xu et al., 2017), NextQA (Xiao et al., 2021)) and text2image generation(MS-COCO (Lin et al., 2014)).
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **Video understanding** (constructs) — *measured_by*
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **Compositional reasoning** (constructs) — *measured_by*
  - [MedFact: A Large-scaleChinese Dataset for Evidence-based Medical Fact-checking ofLLMResponses](https://aclanthology.org/2025.emnlp-main.1647.pdf)
