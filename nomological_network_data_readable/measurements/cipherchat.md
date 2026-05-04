# CipherChat
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, CipherChat is consistently defined as a jailbreak method or procedure that uses cipher-based languages to bypass a model's safety alignment. The most commonly specified mechanism is the Caesar cipher, with some papers noting a three-letter shift. One source describes it as a "novel framework" that not only enciphers user instructions but also adds a system prompt and few-shot demonstrations. The stated purpose of this method is to probe what are described as the "intrinsic characteristics" or "true thoughts" of models, thereby creating a "more challenging testing scenario." It is specifically used to stress-test whether models reveal biases when their alignment is bypassed. In line with this usage, CipherChat is identified as a measurement instrument for the behavior of `Jailbreaking`.

## Sources

**[GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed4c38fe7899d3653acf39b2102af8ba-Paper-Conference.pdf)**
> A jailbreak method that uses cipher-based languages, such as Caesar cipher, to bypass a model's safety alignment protocols and probe its intrinsic characteristics.

## Relationships

### → CipherChat
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
