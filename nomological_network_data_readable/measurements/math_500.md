# MATH-500
**Type:** Measurement  
**Referenced in:** 85 papers  
**Also known as:** MATH500  

## State of the Field

Across the provided literature, MATH-500 is consistently characterized as a measurement instrument derived from the larger MATH benchmark. Its predominant use is to evaluate the "mathematical reasoning" and "problem-solving" capabilities of large language models, a connection supported by a vast number of papers. The benchmark is composed of 500 problems, which some sources describe as "representative questions" selected from the original 5,000-question MATH test set. A more detailed framing specifies these as challenging problems from "high school math competitions across seven subjects (e.g., Prealgebra, Algebra, Number Theory)" ("Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models"). The use of this subset is often justified for practical reasons; as one study notes, it is used for evaluation when the full benchmark is "computationally expensive" ("Humanizing Machines: RethinkingLLMAnthropomorphism Through a Multi-Level Framework of Design"). Furthermore, this 500-example subset is reported to "reliably reflect full-benchmark performance" ("Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech"). The data shows near-universal agreement on its role as a standard tool for assessing advanced mathematical abilities in models.

## Sources

**[HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf)**
> A subset of the MATH benchmark used for evaluating model performance.

**[Large Margin Representation Learning for Robust Cross-lingual Named Entity Recognition](https://aclanthology.org/2025.acl-long.216.pdf) (as "MATH500")**
> A test set of 500 representative questions selected from the original 5,000-question MATH test set, used for evaluating PRM supervision performance.

## Relationships

### → MATH-500
- **Mathematical reasoning** (constructs) — *measured_by*
  > We evaluated the effectiveness of the PRM on Gemma2-2B-it, Gemma2-9B-it(Team et al., 2024), Phi-3-mini-4k-Instruct (3.8B) (Abdin et al., 2024), which are from different origins than the data generation models, using the PRM weighted Best-of-N search on MATH500.
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [UnCo: Uncertainty-Driven Collaborative Framework of Large and Small Models for Grounded MultimodalNER](https://aclanthology.org/2025.emnlp-main.389.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **Verification ability** (constructs) — *measured_by*
  - [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  - [La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cj/liu25cj.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)

### Associated with
- **MATH** (measurements)
  > We evaluate our models on GSM8K and the MATH500 subset (Hendrycks et al., 2021b) of the MATH dataset. (Section 4.1).
  - [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.727.pdf)
