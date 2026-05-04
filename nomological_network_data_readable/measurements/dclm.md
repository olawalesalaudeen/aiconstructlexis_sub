# DCLM
**Type:** Measurement  
**Referenced in:** 3 papers  

## State of the Field

DCLM is defined as the pre-training data for the DCLM-7B model, with one source also identifying it as a calibration source. Across the provided literature, it is operationalized as an instrument to measure the behavior of language modeling. Researchers use a subset of the DCLM corpus to report a language model's loss, thereby testing its capabilities. This measurement is positioned as a method to "examine how well LMs capture broad and diverse knowledge" and to verify the retention of "diversity and long-tail knowledge coverage." The data is described as a "high-quality corpus carefully curated with complex pipelines and human heuristics."

## Sources

**[Beware of Calibration Data for Pruning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ede933e10afa991a10b6f36b6522129-Paper-Conference.pdf)**
> The pre-training data of the DCLM-7B model used as a calibration source.

## Relationships

### → DCLM
- **Language modeling** (behaviors tasks) — *measured_by*
  > We also report the LM’s language modeling loss on a subset of DCLM (Li et al., 2024), a high-quality corpus curated with complex pipelines and human heuristics, to verify that models trained on D′ retain diversity and long-tail knowledge coverage. (Section 3.1)
  - [MiniPLM: Knowledge Distillation for Pre-training Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea05e4fc0299c27648c9985266abad47-Paper-Conference.pdf)
