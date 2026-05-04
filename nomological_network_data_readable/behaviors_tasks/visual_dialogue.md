# Visual dialogue
**Type:** Behavior  
**Referenced in:** 10 papers  
**Also known as:** Open-ended visual chat, Multimodal chat, Multi-modal chat, Image-based conversation, Visual prompt-based conversation, Visual conversation, Multi-modal dialogue, Multi-turn visual conversation, Visual dialog  

## State of the Field

Across the surveyed literature, visual dialogue is consistently defined as a multi-turn, conversational interaction between a user and a model that is grounded in visual content. The prevailing definitions emphasize that a model's responses must be contextually dependent on both the image and the preceding dialogue history. While this general framing is common, some papers describe more specific variants, such as conversations in the biomedical domain or interactions where users refer to image regions with visual prompts like points or boxes. The field operationalizes and measures this behavior using several benchmarks, with papers citing its evaluation on `MM-Vet`, `GQA`, and `TextVQA`. This behavior is studied alongside and considered related to `Visual question answering` and `Visual understanding`. Some work frames it as a capability for "real-world AI assistants," as noted in "ConvBench: A Multi-Turn Conversation Evaluation Benchmark...".

## Sources

**[Biomedical Visual Instruction Tuning with Clinician Preference Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec33ab89b5986605cd7c331396e7e5c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Open-ended visual chat")**
> Responding to image-based prompts in a multi-round conversational format with contextually relevant biomedical answers.

**[WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Multimodal chat")**
> Engaging in a multi-turn conversational interaction with a user, where the conversation is grounded in one or more images.

**[Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf) (as "Multi-modal chat")**
> The task of engaging in a conversation that involves understanding and responding to inputs from multiple modalities, such as combined text and image queries.

**[Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)**
> The observable task of participating in a conversation about an image, where the model's responses are contextually dependent on both the visual input and the dialogue history.

**[OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf) (as "Image-based conversation")**
> The task of engaging in a multi-turn dialogue with a user about the content of an image.

**[OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf) (as "Visual prompt-based conversation")**
> The task of engaging in a dialogue about an image where the user can refer to specific areas using visual prompts like points, boxes, or masks.

**[Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf) (as "Visual conversation")**
> Engaging in multi-turn dialogue about visual content, producing responses conditioned on images and prior turns.

**[MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf) (as "Multi-modal dialogue")**
> Engaging in a conversational exchange that involves both textual and visual information.

**[ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Multi-turn visual conversation")**
> The observable behavior of engaging in a sequence of dialogue turns involving both visual and textual inputs, where responses depend on prior context.

**[FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf) (as "Visual dialog")**
> Engaging in a multi-turn conversational exchange with a user about the content of an image.

## Relationships

### Visual dialogue →
- **MM-Vet** (measurements) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
- **TextVQA** (measurements) — *measured_by*
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)

### → Visual dialogue
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf)

### Associated with
- **Visual question answering** (behaviors tasks)
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
- **Visual understanding** (constructs)
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
