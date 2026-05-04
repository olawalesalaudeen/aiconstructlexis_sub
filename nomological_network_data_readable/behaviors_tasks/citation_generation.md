# Citation generation
**Type:** Behavior  
**Referenced in:** 16 papers  
**Also known as:** Reference generation, Block-level citation, Page-level citation  

## State of the Field

Across the surveyed literature, citation generation is most commonly defined as the behavior of producing supporting evidence—such as quotes, URLs, or extracted context—for a generated response. The stated purpose of this behavior is frequently to provide transparency and traceability, allowing users to verify the origin of information and evaluate a model's fidelity to its source context. As one paper notes, the goal is for each claim to be "fully supported by the cited documents, while avoiding irrelevant citations." This behavior is operationalized in various ways, from generating in-line references like `[1]` to providing extracted text from web pages. A few papers treat this behavior more narrowly, with some distinguishing between "page-level" and more difficult "block-level" citations, where the latter requires identifying a precise bounding box of evidence. Other specific framings include "reference generation," defined as producing a list of formal academic citations with full metadata, and the generation of citations in a "parenthetical author-date style." The behavior is evaluated using instruments like the L-CiteEval suite, and it is also studied in relation to other constructs, with one paper investigating "political bias in LLM-generated citations."

## Sources

**[AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)**
> Producing citations, quotes, URLs, or extracted context intended to support a generated response.

**[POINTS-Reader: Distillation-Free Adaptation of Vision-Language Models for Document Conversion](https://aclanthology.org/2025.emnlp-main.83.pdf) (as "Reference generation")**
> Producing a list of academic citations with full metadata (title, authors, journal, year, etc.) based on a given research topic.

**[Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.211.pdf) (as "Page-level citation")**
> The specific behavior of identifying and outputting a reference to the correct source page that contains evidence for a generated answer.

**[Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.211.pdf) (as "Block-level citation")**
> The specific behavior of identifying and outputting coordinates for a bounding box around the precise region within a source page that contains evidence for a generated answer.

## Relationships

### Associated with
- **Political bias** (constructs)
  > this paper focuses on empirically quantifying and analyzing the political leaning of LLM in citation generation. (Section 2)
  - [SciEvent: Benchmarking Multi-domain Scientific Event Extraction](https://aclanthology.org/2025.emnlp-main.872.pdf)
