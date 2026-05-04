# Optical character recognition
**Type:** Behavior  
**Referenced in:** 48 papers  
**Also known as:** Text recognition, Scene text recognition, Text extraction, Element OCR, Heading OCR, OCR, Handwritten letter recognition, Reading text from images, Chart OCR, Handwritten text recognition, Printed text recognition, Text extraction from images, OCR ability, OCR recognition, OCR perception, Character recognition, Fine-grained text recognition, OCR capability  

## State of the Field

Across the surveyed literature, Optical Character Recognition (OCR) is most commonly defined as the observable behavior of identifying, extracting, and transcribing text from visual media such as images, documents, and video frames. The application of this task is shown to be diverse, encompassing general 'scene text recognition', text within user interfaces ('Element OCR', 'Heading OCR'), and specialized domains like historical documents, which are further divided into 'Handwritten text recognition' and 'Printed text recognition'. This behavior is predominantly operationalized and measured using a range of visual question answering benchmarks. The most frequently cited instruments for evaluating OCR are TextVQA and DocVQA, while other papers also employ OCRBench, ChartQA, ST-VQA, and OCRVQA to assess this capability. While the prevailing usage treats OCR as a task, a smaller stream of research frames it as a latent 'OCR ability,' 'capability,' or 'perception,' sometimes specifying 'fine-grained text recognition' for small or blurry text. Studies highlight the difficulty of this task, noting challenges in "accurately distinguishing bewildering OCR cases" such as similar handwritten words ("Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment"). Some work posits a directional relationship, suggesting that a model's underlying visual perception influences its performance on OCR tasks. To perform this behavior, some studies report using specific tools like the Pytesseract or EasyOCR libraries.

## Sources

**[Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The task of identifying and extracting text from images or documents.

**[WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Text recognition")**
> Reading and transcribing text that appears in images or screenshots.

**[ControlMLLM: Training-Free Visual Prompt Learning for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4fd96b997454b5b02698595df70fccaf-Paper-Conference.pdf) (as "Scene text recognition")**
> Recognizing and reading text within an image region, often treated as an out-of-domain task for referring models.

**[Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf) (as "Text extraction")**
> The task of identifying and extracting specific, predefined types of information from unstructured text.

**[Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf) (as "Element OCR")**
> Extracting the text content from a specific UI element highlighted by a bounding box on a webpage screenshot.

**[Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf) (as "Heading OCR")**
> Identifying and extracting the textual content of headlines or titles from a webpage.

**[Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf) (as "OCR")**
> The task of performing Optical Character Recognition to read and interpret text that appears within video frames.

**[SCISSOR: Mitigating Semantic Bias through Cluster-Aware Siamese Networks for Robust Classification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25w/yang25w.pdf) (as "Handwritten letter recognition")**
> The observable task of identifying and classifying characters from images of handwritten letters.

**[Personality Matters: User Traits PredictLLMPreferences in Multi-Turn Collaborative Tasks](https://aclanthology.org/2025.emnlp-main.72.pdf) (as "Reading text from images")**
> The observable behavior of extracting and understanding textual content embedded within an image to perform a task.

**[LegalSearchLM: Rethinking Legal Case Retrieval as Legal Elements Generation](https://aclanthology.org/2025.emnlp-main.226.pdf) (as "Chart OCR")**
> Extracting visible text elements from a chart without semantic structuring.

**[Turning Logic Against Itself: Probing Model Defenses Through Contrastive Questions](https://aclanthology.org/2025.emnlp-main.1763.pdf) (as "Handwritten text recognition")**
> Transcribing text from images of handwritten historical documents, accounting for diverse handwriting styles, abbreviations, and degradation.

**[Turning Logic Against Itself: Probing Model Defenses Through Contrastive Questions](https://aclanthology.org/2025.emnlp-main.1763.pdf) (as "Printed text recognition")**
> Transcribing text from images of printed historical documents, handling archaic fonts, layout variations, and orthographic inconsistencies.

**[Sparse Neurons Carry Strong Signals of Question Ambiguity inLLMs](https://aclanthology.org/2025.emnlp-main.814.pdf) (as "Text extraction from images")**
> The process of identifying and converting textual content from image frames of presentation slides into machine-readable text, using OCR or vision-language models.

**[What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf) (as "OCR ability")**
> The latent capacity to recognize and extract text from images or documents.

**[Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf) (as "OCR recognition")**
> The ability to accurately identify, read, and transcribe text present within an image.

**[ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf) (as "OCR perception")**
> The specific facet of visual perception involving the detection and recognition of text characters within an image.

**[UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Character recognition")**
> The ability to identify digits or characters from visual input, including handwritten or natural-image digit recognition.

**[Feast Your Eyes:  Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf) (as "Fine-grained text recognition")**
> The latent ability to read and interpret small, blurred, or text-dense visual content in images.

**[ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf) (as "OCR capability")**
> The latent ability to recognize and align text present in document images with query terms or document content.

## Relationships

### Optical character recognition →
- **TextVQA** (measurements) — *measured_by*
  > TextVQA and ST-VQA are two texts understanding benchmarks requiring models to answer questions through textual cues on images. (Section 5.1.1)
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **DocVQA** (measurements) — *measured_by*
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf)
- **OCRBench** (measurements) — *measured_by*
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf)
- **ChartQA** (measurements) — *measured_by*
  > ChartQA (Masry et al., 2022), OCRVQA (Mishra et al., 2019), TextVQA (Singh et al., 2019) and DocVQA (Mathew et al., 2021) to examine their ability to recognize optical character (Section 5.1)
  - [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf)
- **ST-VQA** (measurements) — *measured_by*
  > TextVQA and ST-VQA are two texts understanding benchmarks requiring models to answer questions through textual cues on images. (Section 5.1.1)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
- **OCRVQA** (measurements) — *measured_by*
  > ChartQA (Masry et al., 2022), OCRVQA (Mishra et al., 2019), TextVQA (Singh et al., 2019) and DocVQA (Mathew et al., 2021) to examine their ability to recognize optical character (Section 5.1)
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
- **InfoVQA** (measurements) — *measured_by*
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **MNIST** (measurements) — *measured_by*
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SVHN** (measurements) — *measured_by*
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VisualMRC** (measurements) — *measured_by*
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **Video-MME** (measurements) — *measured_by*
  > Leveraging the question types defined in the Video-MME benchmark, we conduct a comparative analysis among three methods... across six distinct categories of questions. (Section 4.2, RQ5)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **MME-RealWorld** (measurements) — *measured_by*
  > RAP improves the performance of LLaVA-v1.5-13B on most sub-tasks, especially on MO/Orientation (+7.3%), AD/Intention (+6.0%), and OCR/license (+10.3%). (Section 5.2)
  - [Retrieval-Augmented Perception: High-resolution Image Perception Meets Visual RAG](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25at/wang25at.pdf)

### → Optical character recognition
- **Visual perception** (constructs) — *causes*
  > Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. (ABSTRACT)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)

### Associated with
- **Document understanding** (constructs)
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
