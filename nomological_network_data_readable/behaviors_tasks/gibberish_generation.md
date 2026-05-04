# Gibberish generation
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Nonsensical response generation, Incoherent output  

## State of the Field

Across the provided literature, gibberish generation is consistently defined as the production of nonsensical, incoherent, or un-useful text by a language model, though the reported causes for this behavior vary. One line of work frames it as the outcome of a denial-of-service attack, where a specific trigger string causes the model to generate "unuseful text" ("Persistent Pre-training Poisoning of LLMs"). Another paper describes the behavior as "jumbled and meaningless text," often involving phrases "repeated ad nauseum," which occurs when a model is tasked with using a difficult bijection language ("Endless Jailbreaks with Bijection Learning"). A third perspective connects this behavior to reinforcement learning, noting that extensive optimization on a proxy reward can lead to nonsensical responses. This is further specified in one study which reports that reward hacking causes the generation of nonsensical text in RLHF. The behavior is operationalized through the observation of these outputs, which are described as jumbled, meaningless, repetitive, or consisting of random characters.

## Sources

**[Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf) (as "Incoherent output")**
> Producing jumbled, meaningless, or repetitive text when asked to operate in a difficult bijection language.

**[Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/dbe2cfe4767f3255160b73a36ae3162e-Paper-Conference.pdf) (as "Nonsensical response generation")**
> The model produces outputs that are incoherent, irrelevant, or nonsensical, particularly after extensive optimization on a proxy reward.

**[Persistent Pre-training Poisoning of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4dade38eae8c007f3a564b8ea820664a-Paper-Conference.pdf)**
> The observable behavior of a model producing nonsensical or un-useful text, often consisting of random characters, when a specific trigger is present.

## Relationships

### → Gibberish generation
- **Reward hacking** (behaviors tasks) — *causes*
  > In RLHF, optimizing a learned reward function over LLM outputs eventually leads to the LLM producing nonsensical responses... This clearly satisfies our informal definition...
  - [Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/dbe2cfe4767f3255160b73a36ae3162e-Paper-Conference.pdf)
