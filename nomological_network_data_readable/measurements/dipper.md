# DIPPER
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Dipper  

## State of the Field

Across the surveyed literature, DIPPER is most commonly characterized as a paraphrase-based text rewriting procedure or model used to generate adversarial attacks. Its prevailing application is to test the robustness of watermarking algorithms and machine-generated text detectors against semantic-preserving modifications. In this context, it is explicitly used to measure `Adversarial robustness`. Several papers note that its paraphrasing can be controlled through specific settings, such as "lexical diversity" and "order diversity". One source specifies that the model is based on a fine-tuned T5-XXL and has been "widely adopted in recent watermark research" for this evaluation purpose. A less frequent framing, found in a single paper, describes DIPPER as a state-of-the-art 11B parameter model used as a baseline to measure the anonymizing effect of text paraphrasing, an application distinct from adversarial testing.

## Sources

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)**
> A paraphrase-based text rewriting procedure used to test watermark robustness under semantic-preserving modifications.

**[Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf) (as "Dipper")**
> A state-of-the-art 11B parameter transformer-based model for text paraphrasing, used as a baseline to measure the anonymizing effect of rewriting text without a specific focus on privacy.

## Relationships

### → DIPPER
- **Adversarial robustness** (constructs) — *measured_by*
  > “In Table 1, we list the detection accuracy of our watermark algorithm and various baseline algorithms under the no-attack setting and when texts are rewritten using GPT3.5, two different DIPPER settings (Krishna et al., 2023)”
  - [A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
