# SugarCrepe
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, SugarCrepe is consistently presented as a benchmark for evaluating vision-language models. It is most commonly used to measure `Compositional reasoning` and `Compositionality`, with some work also using it to assess `Relation understanding`. The prevailing definition describes it as a large-scale benchmark designed to systematically test these capabilities by presenting models with swaps, replacements, and additions of objects, attributes, and relations. A complementary description characterizes it as a "fine-grained" benchmark focusing on interlinked attributes and semantic relationships. Regarding its operationalization, one paper notes that the task involves a single image and is evaluated based on a caption choice, which can be simplified to a "Text Score". It is referred to as a "challenging composition benchmark" and is sometimes used alongside other instruments that also evaluate compositionality.

## Sources

**[TripletCLIP:  Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)**
> A large-scale benchmark designed to systematically evaluate the compositional reasoning capabilities of vision-language models by testing their ability to handle swaps, replacements, and additions of objects, attributes, and relations.

## Relationships

### → SugarCrepe
- **Compositional reasoning** (constructs) — *measured_by*
  - [TripletCLIP:  Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
- **Compositionality** (constructs) — *measured_by*
  > Empirical results on four compositionality benchmarks, Winoground, EqBench, ColorSwap, and SugarCrepe, in seven different open-source VLMs with varying sizes, demonstrate that COCO-Tree significantly improves compositional generalization by 5-10% over baselines. (Abstract)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Relation understanding** (constructs) — *measured_by*
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
