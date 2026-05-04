# AMBER
**Type:** Measurement  
**Referenced in:** 12 papers  

## State of the Field

AMBER is consistently characterized across the provided literature as a benchmark for evaluating hallucination in vision-language and multimodal models. The prevailing usage is to assess multiple forms of hallucination, with most sources specifying its focus on object, attribute, and relation hallucinations. Several papers frame it as an extension of the POPE benchmark, expanding evaluation beyond object existence. The benchmark is operationalized across both generative and discriminative tasks, with one paper noting it "provides a coverage of evaluations for both generative task and discriminative task." In terms of specific metrics, one source states that "AMBER uses CHAIR ... as the evaluation metric," while others mention its assessment of hallucination rate, object coverage, and human cognition hallucination. Based on the provided relationships, AMBER is used to measure the constructs of `Hallucination` and `Object hallucination`, and is also applied to evaluate `Hallucination mitigation` techniques.

## Sources

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)**
> A benchmark that extends POPE to evaluate not just the existence of objects but also attribute and relation hallucinations, providing a more comprehensive analysis of multimodal model accuracy.

## Relationships

### → AMBER
- **Hallucination** (behaviors tasks) — *measured_by*
  > AMBER (Wang et al., 2023a) further extends POPE by evaluating not just existence but also attribute and relation hallucinations. (Section 3.2).
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  > To evaluate performance on both generative and discriminative tasks, we use AMBER (Wang et al., 2023b), which measures hallucination using several metrics. For generative tasks, AMBER assesses the frequency of hallucinated objects in image descriptions... (Section 4.1)
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Visual recognition** (constructs) — *measured_by*
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Hallucination mitigation** (constructs) — *measured_by*
  > “AMBER (Wang et al., 2023) provides a discriminative way to evaluate various types of hallucination including existence, attribute and relation”
  - [Smurfs: Multi-Agent System using Context-EfficientDFSDTfor Tool Planning](https://aclanthology.org/2025.naacl-long.170.pdf)
