# BLINK
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

Across the provided literature, BLINK is consistently characterized as a multi-image benchmark. Its most common application is to evaluate reasoning capabilities, particularly `Multi-image understanding`, `Multi-image reasoning`, and reasoning over what one paper calls "multi-view and spatial relationships." This primary use is supported by its frequent definition as "A multi-image benchmark used to evaluate reasoning over multi-view and spatial relationships" (MIA-DPO...). A less common but more specific description frames it as a benchmark that "incorporates 14 visual perception tasks that humans can quickly solve, covering indoor, outdoor, and natural scenes" (Lexical Diversity-aware Relevance Assessment...). This aligns with its use in measuring `Perception`. Beyond these core applications, individual papers also use BLINK to assess a broader set of constructs, including `Visual reasoning`, `Spatial reasoning`, `Understanding`, and `Hallucination`. The benchmark is also noted as being related to `Long-context processing` and is studied alongside `MM-NIAH`.

## Sources

**[MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)**
> A multi-image benchmark used to evaluate reasoning over multi-view and spatial relationships.

## Relationships

### → BLINK
- **Multi-image understanding** (constructs) — *measured_by*
  > First, we select five multi-image benchmarks: MMMU (Yue et al., 2024), BLINK (Fu et al., 2024), Mantis (Jiang et al., 2024), NLVR2 (Suhr et al., 2018), and MVBench (Li et al., 2024c). (Section 4.1)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Spatial reasoning** (constructs) — *measured_by*
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  - [MatViX: Multimodal Information Extraction from Visually Rich Articles](https://aclanthology.org/2025.naacl-long.186.pdf)
- **Understanding** (constructs) — *measured_by*
  - [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)
- **Perception** (constructs) — *measured_by*
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **Multi-image reasoning** (constructs) — *measured_by*
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)

### Associated with
- **MM-NIAH** (measurements)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
