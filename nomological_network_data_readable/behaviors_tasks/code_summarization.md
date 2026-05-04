# Code summarization
**Type:** Behavior  
**Referenced in:** 8 papers  
**Also known as:** Linguistic description generation, Code documentation  

## State of the Field

Across the provided literature, code summarization is described as the behavior of generating a summary for a block of code to capture its functionality or intent. The output is most commonly framed as a natural language description; one paper refers to this as 'linguistic description generation' that describes functionality, while another frames it as 'code documentation' intended to ensure 'maintainability, readability, and ease of collaboration' ("Position: Future Research and Challenges Remain Towards AI for Software Engineering"). A broader definition also includes 'symbolic summaries,' with one paper providing 'function name prediction' as an example of summarizing a function's behavior ("Firewall Routing: Blocking Leads to Better Hybrid Inference forLLMs"). To evaluate this behavior, researchers use measurement instruments such as the CodeXGLUE benchmark. The concept is also studied in relation to Hallucination.

## Sources

**[Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zheng25o/zheng25o.pdf) (as "Linguistic description generation")**
> The observable action of generating a natural language summary of a given piece of code that describes its functionality.

**[Position: Future Research and Challenges Remain Towards AI for Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gu25e/gu25e.pdf) (as "Code documentation")**
> Writing documentation that explains what code does and how it works, including side effects and special cases.

**[Firewall Routing: Blocking Leads to Better Hybrid Inference forLLMs](https://aclanthology.org/2025.emnlp-main.332.pdf)**
> The observable behavior of producing natural language or symbolic summaries (such as function names) that capture the intent or behavior of a code block.

## Relationships

### Code summarization →
- **CodeXGLUE** (measurements) — *measured_by*
  - [YESciEval: RobustLLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.676.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1480.pdf)
