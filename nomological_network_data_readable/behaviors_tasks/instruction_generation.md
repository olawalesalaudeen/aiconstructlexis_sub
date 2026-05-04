# Instruction generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Based on the provided literature, instruction generation is defined as the behavior of producing an instruction from a given response. The typical goal is to infer what user prompt would have naturally elicited that response. This process is operationalized through what one paper calls a "reverse model," which "learns to generate instructions given responses." This model, sometimes formalized as p(I|R), is used to create a "synthetic instruction" from a given response. The concept is also studied in relation to other behaviors such as text generation and memorization, though the provided evidence does not specify the nature of these relationships. The available data on this behavior is limited, with the core definition and operationalization details stemming from a single source.

## Sources

**[How do autoregressive transformers solve full addition?](https://aclanthology.org/2025.emnlp-main.644.pdf)**
> Producing an instruction given a response, typically to infer what user prompt would naturally elicit that response.

## Relationships

### Associated with
- **Text generation** (behaviors tasks)
  - [Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/be06e3802e9411381feece79b4d960c1-Paper-Conference.pdf)
- **Memorization** (constructs)
  - [Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/be06e3802e9411381feece79b4d960c1-Paper-Conference.pdf)
