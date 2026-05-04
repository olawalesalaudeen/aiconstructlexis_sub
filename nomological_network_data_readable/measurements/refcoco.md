# RefCOCO
**Type:** Measurement  
**Referenced in:** 38 papers  
**Also known as:** RefCOCO+, refcoco, refCOCO, refCOCO+  

## State of the Field

Across the surveyed literature, RefCOCO and its variants (RefCOCO+, RefCOCOg) are a suite of well-established benchmarks used to evaluate a model's ability to connect natural language descriptions to visual content. The most prevalent application is to measure the constructs of `visual grounding` and `referring expression understanding`. Papers operationalize this evaluation in two main ways: as referring expression comprehension (REC), where a model must predict an object's bounding box, or as referring expression segmentation, which requires generating a pixel-level mask for the described object. While the general RefCOCO dataset is described as assessing the understanding of "fine-grained spatial and semantic relationships" ("GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules"), the RefCOCO+ variant is specifically defined as excluding spatial relations to focus on appearance-based descriptions. This suite is frequently used to assess a model's capacity for `object localization` based on language.

## Sources

**[Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)**
> Visual grounding dataset evaluating a model's ability to localize objects based on referring expressions in images.

**[CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf) (as "RefCOCO+")**
> Referring expression comprehension benchmark similar to RefCOCO but excluding spatial relations in annotations, focusing on appearance-based descriptions.

**[LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf) (as "refcoco")**
> A referring-expression grounding dataset used here to evaluate prediction of object bounding boxes from image-text inputs.

**[OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf) (as "refCOCO")**
> A referring expression segmentation benchmark that evaluates whether a model can localize the object described by a natural-language expression in an image.

**[OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf) (as "refCOCO+")**
> An extension of the refCOCO dataset for referring expression segmentation, featuring more complex language.

## Relationships

### → RefCOCO
- **Referring expression understanding** (behaviors tasks) — *measured_by*
  > For referring expression segmentation (RES), we follow standard evaluation protocols (Lai et al., 2024; Xia et al., 2024) and assess our method using the refCOCO series. (Section 4.2)
  - [GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf)
- **Visual grounding** (constructs) — *measured_by*
  > To thoroughly assess our model’s understanding of pixel-level instances, we evaluate its performance on referring segmentation and grounding benchmarks, including refCOCO (Kazemzadeh et al., 2014), refCOCO+ (Kazemzadeh et al., 2014), and refCOCOg (Caesar et al., 2018).
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Object localization** (behaviors tasks) — *measured_by*
  > RefCOCO is a typical visual grounding dataset, evaluating models’ ability to localize objects and understand fine-grained spatial and semantic relationships. (Section 4)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **Spatial reasoning** (constructs) — *measured_by*
  - [ReMI: A Dataset for Reasoning with Multiple Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ea56c0baacac9f7764257a43a93c90a-Paper-Datasets_and_Benchmarks_Track.pdf)
