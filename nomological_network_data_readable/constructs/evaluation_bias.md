# Evaluation bias
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Judge bias, Affinity bias, Bias in feedback  

## State of the Field

Across the provided literature, 'Evaluation bias' is most commonly characterized as a systematic error that arises when a large language model acts as a judge or reviewer of other models' outputs. This is frequently defined as a tendency to unfairly favor or disfavor certain responses, which can include a self-favoring or 'affinity bias' where a judge assigns higher scores to models functionally similar to itself. A few papers offer a broader framing, defining the concept as a systematic deviation in estimated model capability due to flaws in the evaluation protocol, or as 'Bias in feedback' from either AI or humans stemming from non-representative data. The construct is operationalized quantitatively in several ways; some work defines it mathematically as the expected difference between a judge's proxy score and a ground-truth score, while other research employs the 'preference gap (PG)' to measure it. Additionally, it is studied through 'carefully designed probing tasks' in the context of 'Agents-as-an-Evaluator'. This bias is reported to 'skew model comparisons and result in misleading model rankings' and is studied in relation to 'Model bias'. One study suggests that reducing a model's confidence can help alleviate this evaluation bias.

## Sources

**[PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)**
> A systematic tendency for a model, when acting as a reviewer, to unfairly favor or disfavor certain models' responses, including a self-favoring bias.

**[Limits to scalable evaluation at the frontier: LLM as judge won’t beat twice the data](https://proceedings.iclr.cc/paper_files/paper/2025/file/4264ee4376776907c0b87ed70b959585-Paper-Conference.pdf) (as "Judge bias")**
> The systematic error introduced when using a model as a judge, defined as the expected difference between the judge's proxy score and the ground-truth score.

**[Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf) (as "Affinity bias")**
> The tendency of an LLM judge to assign higher scores to models whose predictions are functionally similar to its own, independent of actual performance.

**[Position: Challenges and Future Directions of Data-Centric AI Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yeh25b/yeh25b.pdf) (as "Bias in feedback")**
> Systematic distortions in human or AI-generated feedback that favor certain perspectives, demographics, or values due to non-representative data or model limitations.

## Relationships

### Associated with
- **Model bias** (constructs)
  > In this paper, we present a theoretical formulation of evaluation bias, providing valuable insights into designing unbiased evaluation protocols. Furthermore, we identify two type of bias in Agents-as-an-Evaluator through carefully designed probing tasks on a minimal Agents-as-an-Evaluator setup.
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
