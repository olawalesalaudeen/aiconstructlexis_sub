# Multimodal generation
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Multi-modal generation  

## State of the Field

Across the provided literature, multimodal generation is described in several ways, most commonly as a model's ability to produce outputs in multiple modalities beyond text, such as image, video, audio, or 3D content. One paper defines it as a "latent ability" to produce interleaved, autoregressive sequences of modalities like video and text, while another frames it as an "observable ability" to generate content from textual or multimodal inputs. A more specific definition treats it as a task of "predicting missing modalities," for instance, generating an image from a text caption. The construct is operationalized through various generation tasks, including text-to-image, text-to-video, text-to-speech, and 3D generation. To evaluate what some papers term "visual generation capabilities," researchers use benchmarks such as MS-COCO and GenEval. Additionally, multimodal generation is positioned as an outcome of another construct; one paper reports that incorporating multimodal understanding data can improve generation capability by enhancing a model's comprehension of object details.

## Sources

**[InMind: EvaluatingLLMs in Capturing and Applying Individual Human Reasoning Styles](https://aclanthology.org/2025.emnlp-main.255.pdf)**
> The latent ability to produce outputs in multiple modalities—text, image, speech, and video—in an autoregressive, end-to-end manner, including interleaved sequences.

**[Graph World Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25p/feng25p.pdf) (as "Multi-modal generation")**
> Predicting missing modalities, such as generating an image from a text caption, given available modal information and their interconnections.

## Relationships

### Multimodal generation →
- **Image generation** (behaviors tasks) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **MS-COCO** (measurements) — *measured_by*
  > To evaluate visual generation capabilities, we use MS-COCO (Lin et al., 2014) and GenEval (Ghosh et al., 2024). (Section 4.2)
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **GenEval** (measurements) — *measured_by*
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)

### → Multimodal generation
- **Multimodal understanding** (constructs) — *causes*
  > incorporating multimodal understanding data enhances the model’s comprehension of object details, including attributes such as color and quantity, thereby improving its generation capability. (Section 5.2.2)
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)
