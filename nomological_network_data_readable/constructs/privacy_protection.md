# Privacy protection
**Type:** Construct  
**Referenced in:** 4 papers  

## State of the Field

Based on the available data, "Privacy protection" is a construct defined as the degree to which a compressed model emulator prevents the leakage of sensitive information from a model or data owner. The stated goal is to ensure the fine-tuned emulator cannot be used to reconstruct the original model or compromise data confidentiality. The work providing this definition operationalizes the construct by intentionally degrading model performance. As one paper notes, "Privacy protecting aims to intentionally increase the performance gap between the finetuned emulator and the fully finetuned model." In this framing, achieving lower zero-shot performance on an emulator is presented as evidence of effective privacy protection. A separate paper suggests a causal relationship, positing that "String manipulation" can be a cause of "Privacy protection".

## Sources

**[Optimizing Decomposition for Optimal Claim Verification](https://aclanthology.org/2025.acl-long.255.pdf)**
> The degree to which the compressed emulator prevents leakage of sensitive information from either the model or data owner, ensuring that the fine-tuned emulator cannot be used to reconstruct the original model or compromise data confidentiality.

## Relationships

### → Privacy protection
- **String manipulation** (behaviors tasks) — *causes*
  - [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf)
