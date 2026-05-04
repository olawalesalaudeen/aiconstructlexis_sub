# Copy-paste attack
**Type:** Measurement  
**Referenced in:** 3 papers  
**Also known as:** Copy-Paste Attack  

## State of the Field

An attack procedure that inserts copied original text into generated text to test watermark robustness.

## Sources

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)**
> An attack procedure that inserts copied original text into generated text to test watermark robustness.

**[Towards Codable Watermarking for Injecting Multi-Bits Information to LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/abdc8c031aa6c6917c3b593166e5e340-Paper-Conference.pdf) (as "Copy-Paste Attack")**
> An evaluation procedure to test watermark robustness where a segment of watermarked text is inserted into a larger body of human-written text.

## Relationships

### → Copy-paste attack
- **Adversarial robustness** (constructs) — *measured_by*
  > In Table 1, we list the detection accuracy of our watermark algorithm and various baseline algorithms under the no-attack setting and when texts are rewritten using GPT3.5, two different DIPPER settings (Krishna et al., 2023) and the copy-paste attack Kirchenbauer et al. (2023b). (Section 6.2)
  - [A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **Watermark robustness** (constructs) — *measured_by*
  - [Towards Codable Watermarking for Injecting Multi-Bits Information to LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/abdc8c031aa6c6917c3b593166e5e340-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [CER: Confidence Enhanced Reasoning inLLMs](https://aclanthology.org/2025.acl-long.391.pdf)
