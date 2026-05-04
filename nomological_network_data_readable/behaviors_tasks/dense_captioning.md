# Dense captioning
**Type:** Behavior  
**Referenced in:** 9 papers  
**Also known as:** Dense caption generation  

## State of the Field

Across the surveyed literature, dense captioning is most commonly defined as the task of generating rich, descriptive captions for multiple distinct objects or regions within a single image. The prevailing emphasis is on producing descriptions that "go beyond category labels to include contextual details" (Ins-DetCLIP..., Image Textualization...). As one paper notes, this allows a model to "generate a detailed description for objects of interest" rather than just a category name (Ins-DetCLIP...). A more specialized usage appears in the context of biological imaging, where "dense caption generation" is framed as producing a single, comprehensive textual description of an entire image. In this domain-specific application, the goal is to "capture all necessary trait information of a biological specimen" (VLM4Bio...). One paper describes a specific method for eliciting this behavior called "Dense Caption prompting," which involves a two-stage process to prompt a VLM for the detailed caption (VLM4Bio...). Thus, the concept is used to describe both the generation of multiple descriptions for various objects in a general image and the creation of a single, exhaustive description for a specialized image.

## Sources

**[Ins-DetCLIP: Aligning Detection Model to Follow Human-Language Instruction](https://proceedings.iclr.cc/paper_files/paper/2024/file/accb5f309ec092a6787a1879ad5f2a5f-Paper-Conference.pdf)**
> Generating rich, descriptive captions for multiple objects in an image, going beyond category labels to include contextual details.

**[VLM4Bio: A Benchmark Dataset to Evaluate Pretrained Vision-Language Models for Trait Discovery from Biological Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/eced4a5fbc776e81b45e2f72447f0164-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Dense caption generation")**
> The behavior of generating a detailed, comprehensive textual description of an image, intended to capture all necessary trait information of a biological specimen.

## Relationships

### Dense captioning →
- **Visual Genome** (measurements) — *measured_by*
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)

### Associated with
- **Dense video captioning** (behaviors tasks)
  - [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **DOCCI** (measurements)
  - [TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf)
