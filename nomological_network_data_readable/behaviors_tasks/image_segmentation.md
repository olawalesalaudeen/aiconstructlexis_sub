# Image segmentation
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Cultural artifact segmentation, Scene segmentation, Segmentation  

## State of the Field

Across the provided literature, image segmentation is most commonly defined as the task of partitioning a digital image into multiple segments or sets of pixels to locate objects and boundaries. While this general framing is prevalent, several papers describe more specific applications, such as producing masks for flowchart components or generating a pixel-level mask of a "culturally significant object" to serve as evidence for a reasoning step. A distinct line of work extends this concept to video, defining it as scene segmentation, which involves dividing a video into coherent scenes based on shot transitions. The output of this behavior is consistently operationalized as a "mask" or "region," with one study specifying the use of polygons to capture intricate details. This behavior can be elicited using textual queries, and its performance is measured using datasets such as Kvasir-SEG, ISIC2017, and ADE20K, as well as synthetic datasets for specialized domains.

## Sources

**[LLM-Guided Semantic Relational Reasoning for Multimodal Intent Recognition](https://aclanthology.org/2025.emnlp-main.1131.pdf) (as "Cultural artifact segmentation")**
> Generating a pixel-level mask that identifies the location of a culturally significant object in an image as justification for a reasoning step.

**[GRADA: Graph-based Reranking against Adversarial Documents Attack](https://aclanthology.org/2025.emnlp-main.1133.pdf) (as "Scene segmentation")**
> Dividing a long video into coherent scenes based on shot transitions, visual changes, and narrative logic to support downstream audio generation.

**[The Role of Outgoing Connection Heterogeneity in Feedforward Layers of Large Language Models](https://aclanthology.org/2025.emnlp-main.1144.pdf) (as "Segmentation")**
> Producing masks or regions that delineate flowchart components in an image.

**[SPECS: Specificity-EnhancedCLIP-Score for Long Image Caption Evaluation](https://aclanthology.org/2025.emnlp-main.478.pdf)**
> The task of partitioning a digital image into multiple segments or sets of pixels, often to locate objects and boundaries.

## Relationships

### Image segmentation →
- **ADE20K** (measurements) — *measured_by*
  - [Transformer Meets Twicing: Harnessing Unattended Residual Information](https://proceedings.iclr.cc/paper_files/paper/2025/file/90cdfb6ac8d9f96bdf0ce92f5f05c391-Paper-Conference.pdf)
