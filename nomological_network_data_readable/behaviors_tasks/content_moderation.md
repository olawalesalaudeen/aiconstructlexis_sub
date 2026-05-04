# Content moderation
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Output filtering  

## State of the Field

Across the provided literature, content moderation is characterized as the act of filtering, blocking, or altering content. The definitions vary in scope: one presents it broadly as an action on either user or model-generated content to comply with general policies, while a more specific framing, termed "output filtering," focuses on modifying model outputs to avoid generating material similar to copyrighted works. One paper notes that in generative AI, this can be an "invisible" process, with models being "built and fine-tuned to moderate content in a certain way (e.g., to avoid providing dangerous information)" ("Position: Generative AI Regulation Can Learn from Social Media Regulation"). The behavior is operationalized and measured using several instruments, including the OpenAI moderation API, WildGuard, and XSTEST. Within the supplied data, content moderation is also studied alongside hate speech detection and instruction following.

## Sources

**[Position: Generative AI Regulation Can Learn from Social Media Regulation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/appel25a/appel25a.pdf)**
> The observable act of filtering, blocking, or altering user or model-generated content to comply with policies, which may occur before or after content is generated.

**[Position: Iterative Online-Offline Joint Optimization is Needed to Manage Complex LLM Copyright Risks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25i/pan25i.pdf) (as "Output filtering")**
> The action of blocking or modifying model outputs that match or resemble copyrighted content, typically implemented via system-level filters or decoding constraints.

## Relationships

### Content moderation →
- **OpenAI moderation API** (measurements) — *measured_by*
  - [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf)
- **WildGuard** (measurements) — *measured_by*
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf)
- **XSTEST** (measurements) — *measured_by*
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf)

### Associated with
- **Hate speech detection** (behaviors tasks)
  - [CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf)
- **WildGuardMix** (measurements)
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf)
- **Instruction following** (constructs)
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf)
