# Data-to-text generation
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** RDF-to-text generation  

## State of the Field

Across the provided literature, data-to-text generation is consistently defined as the task of producing natural language text from structured data inputs. One paper offers a more specific variant, RDF-to-text generation, which focuses on generating descriptions from Resource Description Framework (RDF) data. The behavior is operationalized and evaluated using several benchmarks, with the E2E NLG Challenge being the most frequently cited instrument in this set. Other measurement instruments used to assess this task include WebNLG, DART, ToTTo, and FeTaQA. It is positioned as one of several "traditional generation tasks" and is studied in relation to the broader behavior of conditional text generation. The construct of faithfulness is also associated with research on this task.

## Sources

**[Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)**
> Generating natural language text from structured data inputs.

**[Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf) (as "RDF-to-text generation")**
> The task of generating a natural language description from a structured RDF (Resource Description Framework) data input.

## Relationships

### Data-to-text generation →
- **E2E NLG Challenge** (measurements) — *measured_by*
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)
- **DART** (measurements) — *measured_by*
  - [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf)
- **WebNLG** (measurements) — *measured_by*
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)
- **ToTTo** (measurements) — *measured_by*
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **FeTaQA** (measurements) — *measured_by*
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)

### Associated with
- **Conditional text generation** (behaviors tasks)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
