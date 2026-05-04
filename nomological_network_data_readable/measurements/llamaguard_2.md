# LlamaGuard 2
**Type:** Measurement  
**Referenced in:** 3 papers  
**Also known as:** LLaMA Guard 2 8B  

## State of the Field

LlamaGuard 2 is a measurement instrument used to assess the `Safety` of large language model outputs. The provided literature describes it as an open-source guard model developed by Meta, with one paper specifying an 8-billion parameter version. Its applications center on automatically classifying content; one study employs it as an "auto-annotator to classify responses as safe or unsafe" and to derive "soft safety score[s]" for rejection sampling ("POROver..."). A different use case is presented in another paper, where it serves as an instrument to evaluate the effectiveness of jailbreak attacks in bypassing safety filters. In both documented uses, it functions as an automated judge of safety.

## Sources

**[POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf) (as "Llama Guard 2")**
> A model developed by Meta used as an auto-annotator to classify responses as safe or unsafe and to derive safety scores for rejection sampling.

**[FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf) (as "LLaMA Guard 2 8B")**
> An 8-billion parameter open-source guard model (version 2) used as an instrument to evaluate the effectiveness of jailbreak attacks at bypassing safety filters.
