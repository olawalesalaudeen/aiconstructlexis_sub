# Fine-grained visual recognition
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Fine-grained object property discernment, Painting style recognition  

## State of the Field

Across the provided literature, fine-grained visual recognition is predominantly framed as the task of identifying an object's specific, subordinate-level category from an image. One paper exemplifies this as identifying "specific species of animals or plants" ("Analyzing and Boosting the Power of Fine-Grained Visual Recognition for Multi-modal Large Language Models"). However, other conceptualizations exist, with some work defining it as the ability to distinguish "subtle properties of objects, such as their specific color, material, or texture" ("Causal Graphical Models for Vision-Language Compositional Understanding"). A more specialized application is also described, where the behavior involves "recognizing artists’ painting styles" ("LLaVA-Interleave..."). To measure this behavior, researchers employ specific evaluation instruments. The MMVP benchmark is explicitly used to evaluate the "fine-grained visual recognition capabilities of LVLMs". Similarly, the FG-OVD benchmark is noted for its use in assessing the ability to "discern fine-grained object properties," aligning with one of the broader definitions of the behavior.

## Sources

**[Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf) (as "Fine-grained object property discernment")**
> The observable ability to distinguish subtle properties of objects, such as their specific color, material, or texture, as described in a caption.

**[LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf) (as "Painting style recognition")**
> Identifying the artist or style of paintings from visual input.

**[Analyzing and Boosting the Power of Fine-Grained Visual Recognition for Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfa2f1555d46b553827af4e1557f3c9a-Paper-Conference.pdf)**
> The observable task of identifying and outputting the specific, subordinate-level category of an object presented in an image.

## Relationships

### Fine-grained visual recognition →
- **MMVP** (measurements) — *measured_by*
  > MMVP (Tong et al., 2024) collects CLIP-blind pairs and evaluates the fine-grained visual recognition capabilities of LVLMs (Section 4.1).
  - [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf)
