# Interleaved text-and-image generation
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Interleaved image-text generation  

## State of the Field

Across the provided literature, interleaved text-and-image generation is consistently defined as a task involving the production of a sequence that contains both text and images. The definitions are highly aligned, with one specifying the generation of an 'arbitrary sequence' of modalities ("Modality-Specialized Synergizers for Interleaved Vision-Language Generalists") and another adding that this is done 'in an autoregressive manner' ("DEEM: Diffusion models serve as the eyes of large language models for image perception"). This behavior is framed as a 'challenging task' for current vision-language models. The papers operationalize this capability by training models on 'interleaved text-image data in an end-to-end manner' to develop 'end-to-end interleaved text-image modeling capabilities' ("DEEM: Diffusion models serve as the eyes of large language models for image perception"). Performance on this task is used to compare models, with one study noting that their approach 'significantly surpass[es] baseline VLGs in complex interleaved generation tasks' ("Modality-Specialized Synergizers for Interleaved Vision-Language Generalists").

## Sources

**[Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf)**
> The task of producing an arbitrary sequence containing both text segments and images.

**[DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf) (as "Interleaved image-text generation")**
> The observable task of generating a sequence containing both text and images in an autoregressive manner.
