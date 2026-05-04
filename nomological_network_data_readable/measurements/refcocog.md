# RefCOCOg
**Type:** Measurement  
**Referenced in:** 29 papers  
**Also known as:** refCOCOg, grefCOCO  

## State of the Field

RefCOCOg is a widely used benchmark primarily for evaluating a model's capabilities in referring expression understanding. The most prevalent operationalization is for referring expression comprehension, where a model is required to localize an object in an image from a natural language description, often by predicting a bounding box. A second common use is for referring expression segmentation, where models are evaluated on their ability to generate a pixel-level object mask from a description. A smaller line of work employs the dataset for the inverse task of referring expression generation, which one study describes as assessing "region-level caption ability" ("The All-Seeing Project"). Across these varied applications, a consistently noted feature is that RefCOCOg contains "longer, more descriptive phrases" and "spatial relations" than related datasets. The benchmark is also used to measure the broader constructs of visual grounding and object localization. One paper distinguishes it from grefCOCO, a dataset for "generalized referring expression segmentation" that includes expressions referring to multiple or no objects.

## Sources

**[CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)**
> Referring expression comprehension benchmark requiring models to localize an object in an image based on a natural language description, with longer expressions and spatial relations.

**[OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf) (as "refCOCOg")**
> A version of the refCOCO dataset for referring expression segmentation that contains longer, more descriptive phrases.

**[Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf) (as "grefCOCO")**
> A benchmark dataset for generalized referring expression segmentation, which includes expressions that refer to multiple objects or no objects at all.

## Relationships

### → RefCOCOg
- **Referring expression understanding** (behaviors tasks) — *measured_by*
  > For referring expression segmentation (RES), we follow standard evaluation protocols (Lai et al., 2024; Xia et al., 2024) and assess our method using the refCOCO series. (Section 4.2)
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Visual grounding** (constructs) — *measured_by*
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
- **Referring expression generation** (behaviors tasks) — *measured_by*
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Object localization** (behaviors tasks) — *measured_by*
  > This task requires a model to locate the bounding box of an object specified by language description. We follow KOSMOS-2 (Peng et al., 2023) to use three well-established benchmarks namely RefCOCOg (Mao et al., 2016), RefCOCO+ (Yu et al., 2016) and RefCOCO (Yu et al., 2016).
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **Image captioning** (behaviors tasks) — *measured_by*
  > Region-level captioning performance on the validation set of RefCOCOg
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)
