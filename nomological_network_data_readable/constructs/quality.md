# Quality
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Generative performance  

## State of the Field

Across the provided literature, the construct of Quality is framed in two distinct ways, one focusing on output characteristics and the other on internal model capability. The most prevalent framing defines Quality in terms of user-perceptible attributes, such as 'Clarity,' which encompasses the logical structure, coherence, and understandability of a model's output. One study supports this by noting that quality is a function of "the comprehensiveness of the model response, the clarity of the structure, and the tone and stylistic tendencies of the language" ('WildChat-50M...'). A different perspective treats Quality as 'Generative performance,' defined as a model's latent capability to produce coherent and accurate text. This view is explicitly linked to model architecture, with one paper arguing that performance "severely degrades" with an "increasing degree of bidirectional attention" during fine-tuning ('What Limits Bidirectional Model’s Generative Capabilities?...'). To operationalize this construct, researchers use several measurement instruments. One paper reports using 'LLM-as-a-judge' to grade outputs on dimensions like "clarity, grammaticality, factuality, writing style, and creativity." Other benchmarks used to measure Quality include the Needle-in-a-haystack test, PG-19, and LongBench.

## Sources

**[WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf) (as "Clarity")**
> The latent quality of a model's output that makes its meaning easy to understand, including logical structure, coherence, and avoidance of ambiguity or convolution.

**[What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf) (as "Generative performance")**
> The latent capability of a model to produce coherent, accurate, and contextually appropriate text in a unidirectional autoregressive manner, which degrades when bidirectional training introduces inappropriate dependencies.

## Relationships

### Quality →
- **Needle-in-a-haystack test** (measurements) — *measured_by*
  - [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf)
- **PG-19** (measurements) — *measured_by*
  - [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  - [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf)
