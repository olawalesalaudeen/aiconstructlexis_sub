# Watermarked text generation
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Watermark embedding  

## State of the Field

The prevailing definition of watermarked text generation across the surveyed literature is the production of text containing a detectable signal. This behavior is operationalized through several distinct methods. A frequently described approach involves modifying a model's token sampling strategy, where, as one paper states, systems "actively inject detectable signals using secret keys" into the generated text, often through probabilistic reweighting of tokens. Another method involves perturbing the language model's weights, causing the output to carry a watermark. A third framing suggests that models can also "directly learn to generate watermarked text" with high detectability. While the mechanisms vary, from modifying the decoding process to altering model weights, the shared outcome is the embedding of a signal or message that can be identified through "standard or specialized decoding."

## Sources

**[On the Learnability of Watermarks for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a86d17b6cd70366d56ab48d2a05a4df1-Paper-Conference.pdf)**
> Generating text that contains a detectable watermark signal under standard or specialized decoding.

**[BiMark: Unbiased Multilayer Watermarking for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25u/feng25u.pdf) (as "Watermark embedding")**
> The process of modifying a language model's token sampling strategy to inject detectable signals or messages into generated text using a secret key.
