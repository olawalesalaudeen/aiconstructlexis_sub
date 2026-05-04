# Error analysis
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Granular error diagnosis  

## State of the Field

Across the surveyed literature, error analysis is a behavior with several distinct framings, most commonly involving the examination of discrepancies between expected and actual model outputs to identify failures. One prevalent usage applies this to code generation, where models "comprehensively compare the execution results and logic differences between the two pieces of code" to find bugs ("Quantifying Semantic Emergence in Language Models"). Another approach treats error analysis as a qualitative method for understanding model weaknesses by categorizing failure modes like hallucination and misunderstanding on benchmark instances ("Seeing More, Saying More"). A more specific variant, termed "granular error diagnosis," focuses on diagnosing reasoning errors at the step level across multiple dimensions such as "Simplicity, Soundness, and Sensitivity" ("AIMMerging..."). This form of error analysis is operationalized and measured by the PRMBench benchmark. A different application frames the behavior as classifying "learners’ missteps" to generate corrective guidance, such as clarifying grammatical rules or providing remediation exercises ("Structured Preference Optimization for Vision-Language Long-Horizon Task Planning").

## Sources

**[Quantifying Semantic Emergence in Language Models](https://aclanthology.org/2025.acl-long.589.pdf)**
> Examining discrepancies between expected and actual execution results to identify bugs or inefficiencies in code, often through comparison with alternative implementations.

**[AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning](https://aclanthology.org/2025.emnlp-main.679.pdf) (as "Granular error diagnosis")**
> Diagnosing specific kinds of reasoning errors at the step level across multiple error dimensions.

## Relationships

### Error analysis →
- **PRMBENCH** (measurements) — *measured_by*
  - [AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning](https://aclanthology.org/2025.emnlp-main.679.pdf)
