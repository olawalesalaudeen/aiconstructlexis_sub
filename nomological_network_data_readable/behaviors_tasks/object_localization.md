# Object localization
**Type:** Behavior  
**Referenced in:** 19 papers  
**Also known as:** Building localization, Defect localization, UI element localization, Instance localization, Text localization, Widget localization, Positioning  

## State of the Field

Across the surveyed literature, object localization is most commonly defined as the task of identifying the position of one or more objects within an image. The behavior is almost universally operationalized by having a model output bounding boxes, which one paper describes as a "4-tuple of the x and y coordinates of the upper left and lower right corners" (Look, Remember and Reason: Grounded Reasoning in Videos with Language Models). To evaluate this capability, researchers use visual grounding datasets such as RefCOCO and RefCOCOg, where a model must locate an object specified by a language description. While this general framing is prevalent, a number of papers investigate more specific forms of this behavior, such as 'building localization' in earth-observation data, 'defect localization' for industrial anomaly detection, and the localization of UI elements like text and widgets. Other specified variants include 'instance localization', which uses a reference image to find a specific object. Object localization is studied alongside other fine-grained visual tasks like counting and positioning, and is also related to spatial reasoning, with one paper noting that "spatial object localization... helps models learn spatial reasoning" (Cognitive Linguistic Identity Fusion Score (CLIFS): A ScalableCognition‐Informed Approach to Quantifying Identity Fusion from Text). Additionally, one study reports that the Logit lens technique "enables spatially localizing objects" (Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations).

## Sources

**[GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf)**
> The task of identifying the position of one or more objects within an image, typically by outputting bounding boxes.

**[TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac3af725ae398b6184faae0828bdbd6c-Paper-Conference.pdf) (as "Building localization")**
> Predicting bounding boxes for buildings visible in an earth-observation image region.

**[Feast Your Eyes:  Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf) (as "Bounding box prediction")**
> Producing coordinate boxes that localize a referred region in an image.

**[MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d91ffbe9c126765755ff52d36b715683-Paper-Conference.pdf) (as "Defect localization")**
> The observable task of identifying the spatial position of a defect within an image, typically expressed through textual description.

**[AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf) (as "UI element localization")**
> The observable behavior of generating the precise screen coordinates corresponding to a UI element described in a natural language instruction.

**[IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf) (as "Instance localization")**
> The observable task of identifying and providing the bounding box coordinates for a specific instance within a test image, based on a provided reference image of that instance.

**[Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf) (as "Text localization")**
> The task of finding the location (i.e., bounding box) of a piece of text specified in a query.

**[Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf) (as "Widget localization")**
> The task of finding the location (i.e., bounding box) of a UI widget based on a textual description of it.

**[FlightGPT: Towards Generalizable and InterpretableUAVVision-and-Language Navigation with Vision-Language Models](https://aclanthology.org/2025.emnlp-main.339.pdf) (as "Positioning")**
> The observable task of determining the spatial location or arrangement of objects in an image.

## Relationships

### Object localization →
- **RefCOCO** (measurements) — *measured_by*
  > RefCOCO is a typical visual grounding dataset, evaluating models’ ability to localize objects and understand fine-grained spatial and semantic relationships. (Section 4)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **RefCOCOg** (measurements) — *measured_by*
  > This task requires a model to locate the bounding box of an object specified by language description. We follow KOSMOS-2 (Peng et al., 2023) to use three well-established benchmarks namely RefCOCOg (Mao et al., 2016), RefCOCO+ (Yu et al., 2016) and RefCOCO (Yu et al., 2016).
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)

### → Object localization
- **Logit lens** (measurements) — *causes*
  > Moreover, the logit lens enables spatially localizing objects within the input image. (Section 1)
  - [Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f14fb9acd243c13c95d4a490d1684ce-Paper-Conference.pdf)

### Associated with
- **Reasoning segmentation** (behaviors tasks)
  - [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf)
- **Spatial reasoning** (constructs)
  > "It includes two task types: spatial object localization (2,361 samples), which helps models learn spatial reasoning"
  - [Cognitive Linguistic Identity Fusion Score (CLIFS): A ScalableCognition‐Informed Approach to Quantifying Identity Fusion from Text](https://aclanthology.org/2025.emnlp-main.589.pdf)
