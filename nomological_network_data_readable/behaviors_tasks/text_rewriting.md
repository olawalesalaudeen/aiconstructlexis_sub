# Text rewriting
**Type:** Behavior  
**Referenced in:** 9 papers  

## State of the Field

Text rewriting is consistently described across the surveyed literature as the observable act of a language model modifying an input text in response to prompts such as "rewrite this for me" or "polish this." A prevailing theme is the preservation of the original text's core meaning or semantics while altering its wording, structure, or style. As one paper notes, this process introduces "subtle variations in phrasing and structure" while maintaining semantic relevance ("CAT: Causal Attention Tuning For Injecting Fine-grained Causal Knowledge into Large Language Models"). The behavior is operationalized for varied purposes, leading to different framings of its use. A frequent application is as an adversarial attack or a robustness test, particularly in watermarking research where it is used in "attempts to modify watermarked text... to eliminate the watermark" ("An Unforgeable Publicly Verifiable Watermark for Large Language Models"). In contrast, other work uses rewriting for creative generation, for instance, to "rewrite the selected poem into an inspired, different poem" ("Quality-Diversity through AI Feedback"). It is also employed as a methodological tool; one study introduces "Raidar, a method to detect AI-generated content by prompting LLMs to rewrite text" ("Raidar: geneRative AI Detection viA Rewriting"). This behavior is elicited using models like GPT-3.5 and GPT-4 and is also identified as a common category of user request in large-scale conversation datasets.

## Sources

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)**
> The observable act of a language model modifying input text according to a prompt such as 'rewrite this for me' or 'polish this,' producing a revised version that may vary in wording, structure, or style.

## Relationships

### Associated with
- **Raidar** (measurements)
  - [Raidar: geneRative AI Detection viA Rewriting](https://proceedings.iclr.cc/paper_files/paper/2024/file/1888b9df34b0d9eea6e009a1fdd55c4f-Paper-Conference.pdf)
