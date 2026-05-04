# WebNLG
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Web NLG  

## State of the Field

Across the provided literature, WebNLG is consistently used as a benchmark dataset to measure text generation capabilities, particularly from structured data. The task it operationalizes is most frequently described as data-to-text, struct-to-text, or table-to-text generation. Several sources specify that the task involves verbalizing structured inputs, commonly in the form of RDF triples, into fluent text. One prevalent definition characterizes the dataset as containing 22,000 examples that span 14 distinct categories. While most papers in this set use WebNLG to evaluate general language generation performance, a smaller line of work employs it for more specific evaluations. For example, one paper uses the dataset to assess domain adaptation under distribution shift by filtering its training and test sets to include different data categories, such as infrastructure versus person descriptions.

## Sources

**[Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf)**
> A text-to-data dataset with 22,000 examples across 14 categories, used to evaluate natural language generation from structured data.

**[Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf) (as "Web NLG")**
> Natural language generation dataset involving conversion of RDF triples into fluent text, used to evaluate domain adaptation under distribution shift.

## Relationships

### → WebNLG
- **Text generation** (behaviors tasks) — *measured_by*
  > We evaluate table-to-text generation with E2E (Novikova et al., 2017) and WebNLG (Gardent et al., 2017) datasets... (Section 5.1)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **Data-to-text generation** (behaviors tasks) — *measured_by*
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)
